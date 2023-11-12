import json

class Skeleton:
    def __init__(self, servant):
        self.servant = servant

    def serve_method(self, method_name, *args):
        method = getattr(self.servant, method_name)
        result = method(*args)
        return json.dumps(result)

    def eat(self, food, drink):
        return self.serve_method("eat", food, drink)

    def play(self, game, join):
        return self.serve_method("play", game, join)
