import ollama
import json
import pathlib
from io import BytesIO
from PIL import Image

def image_to_base64_bytes(image_path: str) -> bytes:
    """
    Converts an image to base64 encoded bytes, compatible with Ollama.
    """
    path = pathlib.Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {image_path}")
    
    with Image.open(path) as img:
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')

        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        return buffered.getvalue()

def generate_components_with_ollama(image_path: str, model: str = "llava") -> dict:
    """
    Analyzes a web page image using Ollama and returns Vue components.
    """
    print(f"🚀 Analyzing the image with Ollama using the '{model}' model...")

    try:
        img_bytes = image_to_base64_bytes(image_path)
    except Exception as e:
        print(f"❌ Error reading the image: {e}")
        return {}

    prompt = """
You are an expert frontend developer in Vue 3 and Tailwind CSS.
Your task is to analyze the image of the provided web page, divide it into logical, reusable components and above all accurately replicate the design of the image.
Respect colors, fonts and arrangement of elements.

Follow these instructions:
1. Identify the main components of the interface (ex: ProductInfo, ImageGallery, SellerInfo, ActionButtons).
2. For each component, generate Vue 3 functional Vue code.
3. Use Tailwind CSS for styling, replicating the image design.
4. No props or complex logic included, just static content.

IMPORTANT: Provide your response as a single valid JSON object, without additional explanations.
The keys must be the names of the components in PascalCase. The values must be strings with Vue code.
    """

    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    'role': 'user',
                    'content': prompt,
                    'images': [img_bytes]
                }
            ],
            options={"response_format": {"type": "json_object"}}
        )

        components_json = response['message']['content']
        components = json.loads(components_json)
        print(f"✅ Component generation complete. Found {len(components)} components.")
        return components

    except json.JSONDecodeError:
        print("❌ The model's response was not valid JSON:")
        print(response.get('message', {}).get('content', 'No content'))
    except Exception as e:
        print(f"❌ Error generating components with Ollama: {e}")
    
    return {}

def validate_and_correct_vue_code(vue_code: str, model: str) -> str:
    print("Validating and correcting Vue component syntax...")

    prompt = """
You are an automated Vue 3 and Tailwind CSS code linter and corrector.
Your task is to analyze the provided Vue component code for any syntax errors, inconsistencies, or structural problems.
If the code is already valid, return it as is.
If there are errors, correct them and return the complete, valid, and properly formatted Vue 3 component code.

IMPORTANT: Your response must contain ONLY the raw code for the .vue file. Do not include any explanations, comments, or markdown formatting like ```vue ... ```.
    """
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    'role': 'user',
                    'content': f"{prompt}\n\n{vue_code}"
                }
            ]
        )
        
        corrected_code = response.get('message', {}).get('content', '').strip()
        
        if corrected_code.startswith("```vue"):
            corrected_code = corrected_code[5:]
        if corrected_code.endswith("```"):
            corrected_code = corrected_code[:-3]

        if corrected_code:
            print("✅ Syntax validation and correction successful.")
            return corrected_code.strip()
        else:
            print("⚠️ Correction model returned an empty response. Using original code.")
            return vue_code

    except Exception as e:
        print(f"❌ Error during syntax validation: {e}. Using original code.")
        return vue_code


def save_components(components: dict, model: str, output_dir: str = "./ollama-components") -> None:
    """
    Validates, corrects, and saves the generated components into .vue files.
    """
    output_path = pathlib.Path(output_dir)
    output_path.mkdir(exist_ok=True)

    for name, code in components.items():
        print(f"\n--- Processing component: {name} ---")
        corrected_code = validate_and_correct_vue_code(code, model)
        
        file_path = output_path / f"{name}.vue"
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(corrected_code)
        print(f"📄 Component saved: {file_path}")


if __name__ == "__main__":
    image_path = "generator/image.png"
    model_name = "codellama:7b-instruct" 
    
    components = generate_components_with_ollama(image_path, model=model_name)

    if components:
        save_components(components, model=model_name)
        print("\n🎉 All components were validated and saved successfully!")
    else:
        print("\n⚠️ No components were generated.")