FROM alpine:latest

WORKDIR /app

COPY *.txt *.py /app
COPY captcha_app /app/captcha_app

RUN set -eux \
&& apk add --no-cache --virtual .build-deps gcc libc-dev linux-headers python3-dev jpeg-dev zlib-dev \
&& apk add --no-cache tzdata jpeg zlib python3 \
&& python3 -m venv /app/venv \
&& /app/venv/bin/pip install -r /app/requirements.txt --no-cache-dir \
&& cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& apk del tzdata .build-deps \
&& mkdir -p /usr/share/zoneinfo/Asia \
&& cp /etc/localtime /usr/share/zoneinfo/Asia/Shanghai \
&& echo "Asia/Shanghai" > /etc/timezone \
&& rm -rf /app/requirements.txt

EXPOSE 5000

ENTRYPOINT ["/app/venv/bin/python3", "run.py"]
