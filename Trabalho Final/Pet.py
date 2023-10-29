class Pet:
    def __init__(self, energy=0, hungry=0, clean=0):
        self.alive = True
        self.energyMax = energy
        self.hungryMax = hungry
        self.cleanMax = clean
        self.clean = clean
        self.energy = energy
        self.hungry = hungry
        self.age = 0
        self.diamonds = 0

    def test_alive(self):
        if self.alive:
            return True
        print("fail: pet esta morto")
        return False

    def set_clean(self, value):
        if value <= 0:
            self.clean = 0
            print("fail: pet morreu de sujeira")
            self.alive = False
        elif value > self.cleanMax:
            self.clean = self.cleanMax
        else:
            self.clean = value

    def set_energy(self, value):
        if value <= 0:
            self.energy = 0
            print("fail: pet morreu de fraqueza")
            self.alive = False
        elif value > self.energyMax:
            self.energy = self.energyMax
        else:
            self.energy = value

    def set_hungry(self, value):
        if value <= 0:
            self.hungry = 0
            print("fail: pet morreu de fome")
            self.alive = False
        elif value > self.hungryMax:
            self.hungry = self.hungryMax
        else:
            self.hungry = value

    def play(self):
        if not self.test_alive():
            return
        self.set_energy(self.energy - 2)
        self.set_hungry(self.hungry - 1)
        self.set_clean(self.clean - 3)
        self.diamonds += 1
        self.age += 1

    def eat(self):
        if not self.test_alive():
            return
        self.set_energy(self.energy - 1)
        self.set_hungry(self.hungry + 4)
        self.set_clean(self.clean - 2)
        self.age += 1

    def shower(self):
        if not self.test_alive():
            return
        self.set_energy(self.energy - 3)
        self.set_hungry(self.hungry - 1)
        self.set_clean(self.cleanMax)
        self.age += 2

    def sleep(self):
        if not self.test_alive():
            return
        if self.energy == self.energyMax:
            print("fail: nao esta com sono")
            return
        self.set_energy(self.energyMax)
        self.set_hungry(self.hungry - 1)
        self.age += 5

    def get_clean_max(self):
        return self.cleanMax

    def get_hungry_max(self):
        return self.hungryMax

    def get_energy_max(self):
        return self.energyMax

    def __str__(self):
        return f"E:{self.energy}/{self.energyMax}, S:{self.hungry}/{self.hungryMax}, L:{self.clean}/{self.cleanMax}, D:{self.diamonds}, I:{self.age}"


if __name__ == "__main__":
    pet = Pet(0, 0, 0)

    while True:
        line = input()
        args = line.split(' ')

        if args[0] == "show":
            print(pet)

        elif args[0] == "init":
            pet = Pet(int(args[1]), int(args[2]), int(args[3]))

        elif args[0] == "play":
            pet.play()

        elif args[0] == "shower":
            pet.shower()

        elif args[0] == "eat":
            pet.eat()

        elif args[0] == "sleep":
            pet.sleep()

        elif args[0] == "end":
            break

        else:
            print("fail: comando invalido")
