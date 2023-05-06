from backend_app.models.application.requests.create_text_request import CreateTextRequest
from backend_app.repository.text_repository import TextRepository

class TextService:
    def __init__(self, repository: TextRepository):
        self.__repository = repository
    
    def create_text(self, request: CreateTextRequest):
        return self.__repository.create_text(request)
    
    def get_texts(self):
        return self.__repository.get_texts()