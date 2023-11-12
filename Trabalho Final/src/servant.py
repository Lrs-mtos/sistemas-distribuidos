# todo -> adicionar novas classes

import json

class Pet:
    def __init__(self, energyMax, hungryMax, cleanMax):
        self.alive = True
        self.clean = cleanMax
        self.cleanMax = cleanMax
        self.energy = energyMax
        self.energyMax = energyMax
        self.hungry = hungryMax
        self.hungryMax = hungryMax

    def eat(self, food, drink):
        print(f"You fed your pet with {food} and {drink}.")
        # todo -> lógica para atualizar os atributos do pet
        return {"status": "success"}

    def play(self, game, join):
        print(f"You played {game} with your pet. Participation: {join}.")
        # todo -> lógica para atualizar os atributos do pet
        return {"status": "success"}

class Servant:
    def __init__(self):
        self.pet = Pet(50, 50, 50)

    def eat(self, food, drink):
        return self.pet.eat(food, drink)

    def play(self, game, join):
        return self.pet.play(game, join)
