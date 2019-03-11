# AWS Parameter Store generator
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/taherbs/aws-arameter-store-generator/master/LICENSE)

This script will help creating/delete [parameter store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-paramstore.html) params by simply listing them in a [yaml file](params.yaml.template). <br>
This become handy when you have multiple parameters to create/update/delete.

## Prerequisites
* Install prerequisites by running the below command:
```bash
pip3 install -r requirements.txt
```

## Usage:
* Create your params.yaml file, use [params.yaml.template](./params.yaml.template) as a template
* Run the below command:
```bash
# Read the params prefixed with the specifued value
python3 parameter_store_cli.py read --prefix=/PARAM_PREFIX/ | python -m json.tool

# Create the params listed in the params.yaml file
python3 parameter_store_cli.py create

# Delete the params listed in the params.yaml file
python3 parameter_store_cli.py delete
```
