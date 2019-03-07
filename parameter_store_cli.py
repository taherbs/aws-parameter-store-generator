import json
import argparse
import yaml
import boto3

def read_param(client, param_path_prefix):
    try:
        data = []
        paginator = client.get_paginator('get_parameters_by_path')
        for page in paginator.paginate(Path=param_path_prefix, WithDecryption=True, Recursive=True):
            for param in page['Parameters']:
                item = {}
                item['Name'] = param['Name']
                item['Type'] = param['Type']
                item['Value'] = param['Value']
                data.append(item)
        return json.dumps(data)

    except Exception as error_msg:
        raise Exception("{} - {}".format(param_path_prefix, error_msg))

def create_param(client, param, overwrite):
    try:
        response = client.put_parameter(
            Name=param['name'],
            Value=param['value'],
            Type=param['type'],
            Overwrite=overwrite
        )
        return response
    except Exception as error_msg:
        if type(error_msg).__name__ == 'ParameterAlreadyExists':
            message = '{} parameter already exists, please enable parameter overwrite if you want to update existing parameters'.format(param['name'])
            return json.dumps({'HTTPStatusCode':'200', 'message': message})
        raise Exception("{} - {}".format(param['name'], error_msg))

def delete_param(client, param):
    try:
        response = client.delete_parameter(
            Name=param['name']
        )
        return response
    except Exception as error_msg:
        if type(error_msg).__name__ == 'ParameterNotFound':
            message = '{} parameter not found, is your parameter name correct?'.format(param['name'])
            return json.dumps({'HTTPStatusCode':'200', 'message': message})
        raise Exception("{} - {}".format(param['name'], error_msg))

def main():
    try:

        parser = argparse.ArgumentParser()
        parser.add_argument("action", type=str, choices=['create', 'delete', 'read'], help="what action needs to be performed")
        parser.add_argument("--prefix", type=str, help="specify the prefix if you are attempting to retrieve parameters path path prefix (read operation)")
        args = parser.parse_args()

        if args.action == 'read':
        # verify that prefix variable is specified if action is read
            if args.prefix is None:
                raise Exception("Specify the --prefix arg with read action")

        # load yaml configuration if the action is different that read
        conf_file = open("params.yaml")
        config = yaml.safe_load(conf_file)
        conf_file.close()

        # Connect to AWS SSM
        client = boto3.client('ssm', region_name=config['aws']['region'])
        # Process parameters
        if args.action == 'read':
            response = read_param(client, args.prefix)
            print("{}".format(response))
        else:
            for param in config["parameters"]:
                if args.action == 'create':
                    response = create_param(client, param, config['aws']['overwrite_param'])
                    print("{}".format(response))
                elif args.action == 'delete':
                    response = delete_param(client, param)
                    print("{}".format(response))
                else:
                    raise Exception("Unsupported action - Supported actions are create/delete/read.")

    except Exception as error_msg:
        raise Exception("Error - Something bad happened - {}.".format(error_msg))

# main entry point
if __name__ == "__main__":
    main()
