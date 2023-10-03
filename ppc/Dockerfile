FROM alpine:latest

RUN apk add --no-cache python3 && apk add --no-cache py3-pip && pip install asyncio

EXPOSE 8080

COPY ./app /app

ENTRYPOINT [ "python3", "/app/server.py" ]
