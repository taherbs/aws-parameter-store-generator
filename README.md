# AWS Parameter Store generator
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/taherbs/aws-arameter-store-generator/master/LICENSE)

This script will help creating [parameter store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-paramstore.html) params by simply listing them in a [yaml file](params.yaml.template). <br>
This become handy when you have multiple parameters to create/update.

## Prerequisites
* Install prerequisites by running the below command:
```bash
pip3 install -r requirements.txt
```

## Usage:
* Create your params.yaml file, use [params.yaml.template](./params.yaml.template) as a template
* Run the below command:
```bash
python3 generate.py
```
