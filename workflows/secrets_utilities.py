import boto3
from botocore.exceptions import ClientError
import datetime
import os
import re
import json
import logging
import awscli
import boto3
import sys
import argparse

parser = argparse.ArgumentParser(
    description="Secrets Utilities",
    prog=""
)

parser.add_argument(
    '-environment', type=str, help='environment to get secrets',
    dest="environment",
    default="staging"
)

parser.add_argument(
    '-prefix', type=str,
    help="Secrets namespace prefix",
    dest="prefix",
    default='/data_platform/dev/featurestore/'
)


class ssmParameterStore:
    def __init__(self, prefix=None, ssm_client=None):
        self._prefix = (prefix or '').rstrip('/') + '/'
        self._client = ssm_client or boto3.client("ssm")

    def get_secret(self, name, decryption=True):
        name = self._prefix + name
        parameter = self._client.get_parameter(Name=name, WithDecryption=True)['Parameter']
        value = parameter['Value']

        return value


def read_config(config_path="", env=""):
    with open(config_path) as json_conf:
        conf = json.load(json_conf)
        return conf


def load_secrets(environment: str, prefix:str):
    logger = get_logger(__name__)
    dir_path = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", 'configuration'))
    secret_config = None
    service_secrets = None
    json_conf = read_config(os.path.join(dir_path, "secrets_configuration.json"))
    secret_store = ssmParameterStore(prefix=prefix)
    if 'Secrets' in json_conf:
        secrets_config = json_conf['Secrets']
        for key in secrets_config:
            os.environ[key] = secret_store.get_secret(secrets_config[key])


def get_logger(name, level=logging.INFO):
    """Get logger
    :param name: name of module
    :param level: logging level, default is logging.INFO
    :return: logger object
    """
    logger = logging.getLogger(name)
    logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s', datefmt='%y/%m/%d %H:%M:%S')
    logger.setLevel(level)
    return logger


if __name__ == '__main__':
    args = parser.parse_args()
    logger.info(f"Reading secrets with env: {args.env} and prefix: {args.prefix}")

    try:
        load_secrets(environment=args.env, prefix=args.prefix)
        logger.info(f"Completed reading secrets with env: {args.env} and prefix: {args.prefix}")
    except Exception as e:
        logger.error(e)
        sys.exit(1)
