import ollama
import json
from fastapi import HTTPException
from typing import List
from app.core.domain.product_model import RelatedProduct
from app.core.ports.related_products_port import RelatedProductsPort


class OllamaRelatedProductsAdapter(RelatedProductsPort):
    _PROMPT_TEMPLATE = """
    Generate a list of three cell phones with prices in {currency} that meet the following characteristics: {characteristics}.
    The response must only be an array of objects in JSON format. Each object must contain a "name" key for the cell phone name and a "value" key for its price only in integer format.
    IMPORTANT:Does not include additional explanatory text ONLY the response must be a JSON array of objects.
    """
    def __init__(self, db_path: str = "db.json", model: str = "codellama:7b-instruct", host: str = None):
        with open(db_path, 'r', encoding='utf-8') as f:
            self._data = json.load(f)
        self.model = model
        self.client = ollama.Client(host=host)

    def get_related_products(self, product_id: str) -> List[RelatedProduct]:
        product = next((p for p in self._data['products'] if p['id'] == product_id), None)
        
        if not product:
            return []
        
        characteristics = [f"{item['label']} {item['value']}" for item in product['characteristics']]
        currency = product['product_info']['price']['currency']
        
        final_prompt = self._PROMPT_TEMPLATE.format(
            currency=currency,
            characteristics=characteristics
        )

        try:
            response = self.client.generate(
                model=self.model,
                prompt=final_prompt,
                options=ollama.Options(temperature=0.2) 
            )
            
            raw_response_content = response['response']

            clean_json_str = raw_response_content.strip().replace("```json", "").replace("```", "").strip()
            related_products = [RelatedProduct(**item) for item in json.loads(clean_json_str)]
            self._data['products'][self._data['products'].index(product)]['related_products'] = related_products
            return related_products
        except json.JSONDecodeError as e:
            raise HTTPException(status_code=500, detail=f"Error decoding JSON response from Ollama: {e}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An unexpected error occurred when contacting Ollama. {e}")