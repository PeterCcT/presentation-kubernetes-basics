from dataclasses import asdict
from pydantic import BaseModel

class Text(BaseModel):
    id: str
    value: str

    def to_dict(self):
        return self.dict()