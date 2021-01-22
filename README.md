# JWT examples in python

This is a sample application showing JWT creation and verification with python.

## Prerequisites

* python3
* pip3

## Installation

* `python3 -m venv venv`
* `. venv/bin/activate`
* `pip3 install -r requirements.txt`

## Running

* `python3 run.py hmac` # shared key
* `python3 run.py hmac_verify_claims` # shared key, confirm those claims!
* `python3 run.py rsa` # rsa 256
* `python3 run.py rsa_wrong_algo` # rsa key but specify hmac when creating jwt. This blows up, as it should. Shows the value of using a library.

