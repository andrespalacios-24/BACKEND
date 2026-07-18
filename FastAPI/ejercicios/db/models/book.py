# donde se crea la clase del usuario 
from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: Optional[str] = None
    title: str
    author: str
    year: int
    available: bool
