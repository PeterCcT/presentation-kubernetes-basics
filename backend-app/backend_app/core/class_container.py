from backend_app.repository.text_repository import TextRepository
from backend_app.service.text_service import TextService


class ClassContainer:
    __instances = {}
    __TEXT_SERVICE = 'TEXT_SERVICE'
    __TEXT_REPOSITORY = 'TEXT_REPOSITORY'

    def get_text_service(self) -> TextService:
        text_service = self.__instances.get(self.__TEXT_SERVICE)
        if not text_service:
            text_service = TextService(repository=self.__get_text_repository())
            self.__instances[self.__TEXT_SERVICE] = text_service
        return text_service


    def __get_text_repository(self) -> TextRepository:
        text_repository = self.__instances.get(self.__TEXT_REPOSITORY)
        if not text_repository:
            text_repository = TextRepository()
            self.__instances[self.__TEXT_REPOSITORY] = text_repository
        return text_repository