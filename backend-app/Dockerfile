FROM python:3.11

ENV AWS_ACCESS_KEY=test
ENV AWS_SECRET_ACCESS_KEY=test
ENV AWS_DEFAULT_REGION=us-east-1

RUN mkdir /root/.aws

COPY ./aws_credentials /root/.aws/

WORKDIR /usr/src/application

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "python", "-m", "backend_app" ]