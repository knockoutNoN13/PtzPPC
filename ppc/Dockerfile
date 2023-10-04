FROM alpine:latest

RUN apk add --no-cache python3 \
    py3-pip \
    libdmtx \
    libdmtx-libs \
     && pip install asyncio Pillow pylibdmtx

EXPOSE 8080

COPY ./app /app

ENTRYPOINT [ "python3" ]

CMD [ "/app/server.py" ]
