import json
from jsonschema import validate, ValidationError

RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "answer": {"type": "string"},
        "confidence": {"type": "number"},
        "source_used": {"type": "boolean"}
    },
    "required": ["answer", "confidence", "source_used"]
}

def validate_json(response_text):
    try:
        data = json.loads(response_text)
        validate(instance=data, schema=RESPONSE_SCHEMA)
        return True, data
    except (json.JSONDecodeError, ValidationError):
        return False, None

def hallucination_check(answer, context):
    answer_words = set(answer.lower().split())
    context_words = set(context.lower().split())
    overlap = len(answer_words.intersection(context_words))
    return overlap >= 5

