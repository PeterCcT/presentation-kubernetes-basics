from fastapi import APIRouter
from pydantic import ValidationError
from backend_app.core.class_container import ClassContainer

from backend_app.models.application.requests.create_text_request import CreateTextRequest

router = APIRouter(prefix='/text')

@router.post('')
def create_text(body: CreateTextRequest):
    try:
        text_service = ClassContainer().get_text_service()
        return text_service.create_text(body)
    except ValidationError as e:
        raise e
    except Exception as e:
        print(e)
        ...

@router.get('')
def get_texts():
    try:
        text_service = ClassContainer().get_text_service()
        return text_service.get_texts()
    except Exception as e:
        print(e)
        ...