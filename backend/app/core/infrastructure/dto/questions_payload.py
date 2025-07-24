from pydantic import BaseModel

class QuestionPayload(BaseModel):
    question_text: str