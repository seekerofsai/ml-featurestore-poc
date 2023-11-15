#!/usr/bin/env bash

aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 910060188380.dkr.ecr.us-west-2.amazonaws.com
docker build -t feast-server .
docker tag feast-server:latest 910060188380.dkr.ecr.us-west-2.amazonaws.com/feast-server:latest
docker push 910060188380.dkr.ecr.us-west-2.amazonaws.com/feast-server:latest