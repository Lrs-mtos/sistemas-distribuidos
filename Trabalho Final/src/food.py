#food.py

class Food:
    def __init__(self, name, calories, flavor):
        self.name = name
        self.calories = calories
        self.flavor = flavor

    def __str__(self):
        return f"{self.name} ({self.calories} kcal, {self.flavor})"

    def to_json(self):
        # transformar o objeto em um dicionário JSON
        return {
            "name": self.name,
            "calories": self.calories,
            "flavor": self.flavor
        }

    @staticmethod
    def from_json(json_dict):
        # transformar um dicionário JSON em um objeto
        return Food(
            json_dict["name"],
            json_dict["calories"],
            json_dict["flavor"]
        )
