from uuid import uuid4
from backend_app.models.application.repository.get_text_result import GetTextResult
from backend_app.models.application.requests.create_text_request import CreateTextRequest
from backend_app.models.domain.text import Text
import boto3


class TextRepository:
    def __init__(self):
        self.__table = boto3.resource(
            'dynamodb',
            region_name='us-east-1',
            endpoint_url='http://database:4566'
        ).Table('texts')

    def create_text(self, request: CreateTextRequest):
        text = Text(
            id=str(uuid4()),
            value=request.value
        )
        self.__table.put_item(
            Item=text.to_dict()
        )
        return text
    
    def get_texts(self):
        data = self.__table.scan()
        return GetTextResult(
            values=self.__texts_from_db(data.get('Items')),
            cursor=data.get('LastEvaluatedKey')
        )
    

    def __texts_from_db(self, values: list[dict]):
        result: list[Text] = []
        for value in values:
            result.append(
                Text(
                    id=value.get('id'),
                    value=value.get('value')
                )
            )
        return result