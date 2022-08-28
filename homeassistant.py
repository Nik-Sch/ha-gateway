#!/bin/env python3
import argparse
from requests import post
from dotenv import load_dotenv
import os

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--domain', help='The domain (e.g. light)', required=True)
parser.add_argument('-s', '--service', help='The service to execute (e.g. turn_on)', required=True)
parser.add_argument('-e', '--entity', help='The entity id without domain (e.g. amplifier)', required=True)
args = parser.parse_args()

# load_dotenv doesn't handle symbol links correctly
load_dotenv(f"{os.path.dirname(os.path.realpath(__file__))}/.env")

url = f"http://homeassistant:8123/api/services/{args.domain}/{args.service}"
headers = {"Authorization": f"Bearer {os.environ['BEARER_TOKEN']}"}
data = {"entity_id": f"{args.domain}.{args.entity}"}
response = post(url, headers=headers, json=data)

print(response.json())