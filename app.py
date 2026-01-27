import json
import os

def handler(event, context):
    """
    Sample Lambda handler
    """

    name = event.get("name", "World")

    response = {
        "message": f"Hello {name}",
        "lambda_function": context.function_name,
        "request_id": context.aws_request_id
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response)
    }
