import json

class Dispatcher:
    def __init__(self, skeleton):
        self.skeleton = skeleton

    def dispatch_request(self, payload):
        message = json.loads(payload)
        method_name = message["method_id"]
        arguments = [json.loads(arg) for arg in message["arguments"]]
        result = getattr(self.skeleton, method_name)(*arguments)
        return json.dumps(result)

