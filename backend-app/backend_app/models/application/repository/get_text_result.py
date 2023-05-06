from typing import Optional
from pydantic import BaseModel

from backend_app.models.domain.text import Text


class GetTextResult(BaseModel):
    values: list[Text]
    cursor: Optional[dict] = None
