from pydantic import BaseModel, Field, field_validator
from typing import List, Optional

class Question(BaseModel):
    question: str
    question_slug: str = Field(..., description="Unique slugified version of the question.")  # Use Field for descriptions
    reference_id: Optional[str] = Field(None, description="Optional reference ID.")
    hint: Optional[str] = Field(None, description="Optional hint for the question.")

class Section(BaseModel):
    marks_per_question: int = Field(default=1)  # Default value
    type: str
    questions: List[Question]

class Params(BaseModel):
    board: str
    grade: int
    subject: str

    @field_validator('board', 'subject')
    def not_empty(cls, v, field):
        if not v or not v.strip():
            raise ValueError(f'{field.name} cannot be empty')
        return v

    @field_validator('grade')
    def grade_valid(cls, v):
        if v <= 0:
            raise ValueError('grade must be a positive integer')
        return v


