#!/usr/bin/env python3

import os
from dotenv import load_dotenv

load_dotenv()

# print(os.environ)

# Get the value of the GITHUB_RUN_ID environment variable
print(f"GITHUB_RUN_ID = {os.environ.get('GITHUB_RUN_ID')}")
print(f"GITHUB_SHA: {os.environ.get('GITHUB_SHA')}")
print(f"GITHUB_EVENT_NAME: {os.environ.get('GITHUB_EVENT_NAME')}")
print(f"GITHUB_JOB: {os.environ.get('GITHUB_JOB')}")

print(f"Message: { os.environ.get('GITHUB_EVENT_INPUTS_MESSAGE1') }")
print(f"Tags: {os.environ.get('INPUT_MESSAGE')}")
