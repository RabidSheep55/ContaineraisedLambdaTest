# READ THIS https://docs.aws.amazon.com/lambda/latest/dg/applications-tutorial.html
# this too https://aws.amazon.com/blogs/compute/using-container-image-support-for-aws-lambda-with-aws-sam/

import json

info = {
    "name": "isExactEqual",
    "version": "0.2",
    "valid_commands": ["get_function_info", "grade"],
    "grade_schema": {
        "response": {"type": ["string", "number"]},
        "answer": {"type": ["string", "number"]}
    }
}

# Grading function
def grade(event):
    return {
        "isCorrect": event["response"] == event["answer"],
        "response_interp_type": str(type(event["response"])),
        "answer_interp_type": str(type(event["answer"]))
    }

# Event handler - redirect to the grade function if request is valid
def handler(event, context):
    # If the event comes from the API gateway, the info we need is in the body, as a string
    if "body" in event:
        event = event["body"]
        event = json.loads(event)

    if "command" not in event:
        return {"error": f"Invalid request, 'command' key required (valid options are {info['valid_commands']})"}

    if event['command'] == "get_function_info":
        return info

    elif event['command'] == "grade":
        return grade(event)

    else:
        return {'error': f"Invalid request, command needs to be from {info['valid_commands']}"}
