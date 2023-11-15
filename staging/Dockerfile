FROM python:3.10

RUN pip install feast --upgrade --no-cache-dir
RUN pip install "feast[redis,postgres,snowflake]" --upgrade --no-cache-dir
RUN pip install cryptography==38.0.4 --no-cache-dir
RUN pip install pyOpenSSL==22.1.0 --no-cache-dir
RUN pip install pyOpenSSL==22.1.0 --no-cache-dir
RUN pip install proto-plus==1.22.0 --no-cache-dir
RUN pip install protobuf==3.20.1 --no-cache-dir

COPY ./feature_store.yaml feature_store.yaml

ENV FEAST_USAGE=False

ENTRYPOINT feast feature-views list