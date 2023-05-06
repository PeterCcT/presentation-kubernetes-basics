FROM localstack/localstack

EXPOSE 4566
EXPOSE 4510-4559:4510-4559

ENV SERVICES=dynamodb
ENV AWS_ACCESS_KEY=test
ENV AWS_SECRET_ACCESS_KEY=test
ENV AWS_DEFAULT_REGION=us-east-1
ENV DEBUG=1
ENV INIT_SCRIPTS_PATH=/docker-entrypoint-initaws.d

RUN mkdir /root/.aws

COPY ./aws_credentials/ /root/.aws/

RUN mkdir /docker-entrypoint-initaws.d

COPY create_database.sh /docker-entrypoint-initaws.d

RUN chmod +x /docker-entrypoint-initaws.d/create_database.sh
