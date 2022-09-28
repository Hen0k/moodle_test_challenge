FROM python:3.10.2

ADD . /scripts
WORKDIR /scripts

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /scripts
USER appuser

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["./run.sh"]