FROM python:alpine3.19
WORKDIR /app
COPY requirement.txt . 
COPY src src
RUN apk update && apk upgrade && \
    apk add --no-cache --virtual build-dependencies gcc musl-dev && \
    adduser -D myuser && \
    rm -rf /var/cache/apk/* && \
    pip install --no-cache-dir -r requirement.txt && rm -f requirement.txt && \
    apk del build-dependencies && \
    chmod 500 . && chmod 500 src
USER myuser
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=3 \
                CMD curl -f http://localhost:5000/heath || exit 1
ENTRYPOINT [ "python", "-m", "./src/app.py" ]