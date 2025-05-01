from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None     # Optional field, can be None
    username: str
    email: str
    