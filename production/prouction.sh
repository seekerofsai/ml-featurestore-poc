#!/bin/sh
pip install feast --upgrade --no-cache-dir
pip install "feast[aws,redis,postgres,snowflake]" --upgrade --no-cache-dir
pip install cryptography==38.0.4 --no-cache-dir
pip install pyOpenSSL==22.1.0 --no-cache-dir
feast apply