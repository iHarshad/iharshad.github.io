#!/usr/bin/env python3

import os


# Get the value of the GITHUB_RUN_ID environment variable
print(f"GITHUB_RUN_ID = {os.environ.get('GITHUB_RUN_ID')}")

print(f"Message: { os.environ.get('GITHUB_EVENT_INPUTS_MESSAGE1') }")
print(f"Tags: {os.environ.get('INPUT_MESSAGE')}")
