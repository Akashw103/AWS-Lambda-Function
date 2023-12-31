import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('This is my first Lamda Function using Ci-Cd')
    }
