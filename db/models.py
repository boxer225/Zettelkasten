from pydantic import BaseModel

class NoteIn(BaseModel):
    tag: str
    description: str
    addiction_id: int


class Note(BaseModel):
    id: int
    tag: str
    description: str
    addiction_id: int
