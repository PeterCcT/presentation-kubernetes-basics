from pydantic import BaseModel


class CreateTextRequest(BaseModel):
    value: str