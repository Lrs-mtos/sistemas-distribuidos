# Classe Pet
class Pet:
    # Construtor
    def __init__(self, energyMax, hungryMax, cleanMax):
        # Atributos
        self.alive = True # se o pet está vivo
        self.clean = cleanMax # nível de limpeza
        self.cleanMax = cleanMax # nível máximo de limpeza
        self.energy = energyMax # nível de energia
        self.energyMax = energyMax # nível máximo de energia
        self.hungry = hungryMax # nível de fome
        self.hungryMax = hungryMax # nível máximo de fome
        self.age = 0 # idade do pet
        self.diamonds = 0 # diamantes que o pet possui

    # Método para verificar se o pet está vivo
    def testAlive(self):
        if not self.alive:
            print("Seu pet está morto. Você não pode mais interagir com ele.")
            return False
        return True

    # Método para mostrar os atributos do pet
    def toString(self):
        print("Seu pet tem os seguintes atributos:")
        print("Limpeza: " + str(self.clean) + "/" + str(self.cleanMax))
        print("Energia: " + str(self.energy) + "/" + str(self.energyMax))
        print("Fome: " + str(self.hungry) + "/" + str(self.hungryMax))
        print("Idade: " + str(self.age))
        print("Diamantes: " + str(self.diamonds))

    # Método para alimentar o pet
    def eat(self, food, drink):
        if not self.testAlive():
            return
        print("Você deu " + food + " e " + drink + " para o seu pet.")
        self.setHungry(self.hungryMax) # diminui a fome
        self.setClean(self.clean - 5) # diminui a limpeza
        self.setEnergy(self.energy - 2) # diminui a energia

    # Método para brincar com o pet
    def play(self, game, join):
        if not self.testAlive():
            return
        print("Você brincou de " + game + " com o seu pet.")
        if join:
            print("Você também se divertiu muito.")
        else:
            print("Você só observou o seu pet se divertir.")
        self.setHungry(self.hungry - 5) # diminui a fome
        self.setClean(self.clean - 10) # diminui a limpeza
        self.setEnergy(self.energy - 15) # diminui a energia
        self.diamonds += 1 # aumenta os diamantes

    # Método para dar banho no pet
    def shower(self):
        if not self.testAlive():
            return
        print("Você deu um banho no seu pet.")
        print("Ele ficou muito cheiroso e feliz.")
        self.setHungry(self.hungry - 2) # diminui a fome
        self.setClean(self.cleanMax) # aumenta a limpeza para o máximo
        self.setEnergy(self.energy - 5) # diminui a energia

    # Método para fazer o pet dormir
    def sleep(self, hours, dream):
        if not self.testAlive():
            return
        print("Você colocou o seu pet para dormir por " + str(hours) + " horas.")
        if dream:
            print("Ele teve sonhos muito bons e acordou bem disposto.")
            self.diamonds += 1 # aumenta os diamantes
        else:
            print("Ele dormiu tranquilamente e acordou bem descansado.")
        
        self.setHungry(self.hungry - hours * 2) # diminui a fome proporcionalmente às horas dormidas
        self.setClean(self.clean - hours * 3) # diminui a limpeza proporcionalmente às horas dormidas
        self.setEnergy(self.energyMax) # aumenta a energia para o máximo
        self.age += hours // 24 # aumenta a idade proporcionalmente às horas dormidas

    # Métodos get e set dos atributos

    def getClean(self):
        return self.clean
    
    def getCleanMax(self):
        return self.cleanMax
    
    def getEnergy(self):
        return self.energy
    
    def getEnergyMax(self):
        return self.energyMax
    
    def getHungry(self):
        return self.hungry
    
    def getHungryMax(self):
        return self.hungryMax
    
    def setClean(self, value):
        self.clean = value
        if self.clean <= 0:
            print("Seu pet morreu de sujeira.")
            self.alive = False
        elif self.clean > self.cleanMax:
            self.clean = self.cleanMax
    
    def setEnergy(self, value):
        self.energy = value
        if self.energy <= 0:
            print("Seu pet morreu de fraqueza.")
            self.alive = False
        elif self.energy > self.energyMax:
            self.energy = self.energyMax
    
    def setHungry(self, value):
        self.hungry = value
        if self.hungry <= 0:
            print("Seu pet morreu de fome.")
            self.alive = False
        elif self.hungry > self.hungryMax:
            self.hungry = self.hungryMax

# Programa principal
print("Bem-vindo ao jogo do Pet!")
print("Você pode interagir com o seu pet de várias formas:")
print("1 - Alimentar o seu pet. Você deve informar a comida e a bebida que deseja dar para ele.")
print("2 - Brincar com o seu pet. Você deve informar o jogo que deseja brincar e se vai participar ou não.")
print("3 - Dar banho no seu pet. Você não precisa informar nada, apenas deixá-lo limpo e cheiroso.")
print("4 - Fazer o seu pet dormir. Você deve informar a quantidade de horas que ele vai dormir e se ele vai sonhar ou não.")
print("5 - Mostrar os atributos do seu pet. Você pode ver como ele está se sentindo e quantos diamantes ele possui.")
print("6 - Sair do jogo. Você pode encerrar o jogo a qualquer momento.")

# Cria um pet com os valores máximos de energia, fome e limpeza
pet = Pet(50, 50, 50)

# Loop do jogo
while True:
    # Mostra o menu de opções
    print("\nEscolha uma opção:")
    option = input()
    # Verifica se a opção é válida
    if option not in ["1", "2", "3", "4", "5", "6"]:
        print("Opção inválida. Tente novamente.")
        continue
    # Executa a opção escolhida
    if option == "1":
        # Alimenta o pet
        print("O que você quer dar para o seu pet comer?")
        food = input()
        print("O que você quer dar para o seu pet beber?")
        drink = input()
        pet.eat(food, drink)
    elif option == "2":
        # Brinca com o pet
        print("Com qual jogo você quer brincar com o seu pet?")
        game = input()
        print("Você vai participar do jogo? (s/n)")
        join = input()
        if join == "s":
            join = True
        elif join == "n":
            join = False
        else:
            print("Resposta inválida. Digite s ou n.")
            continue
        pet.play(game, join)
    elif option == "3":
        # Dá banho no pet
        pet.shower()
    elif option == "4":
        # Faz o pet dormir
        print("Quantas horas você quer que o seu pet durma?")
        hours = int(input())
        print("Você quer que o seu pet sonhe? (s/n)")
        dream = input()
        if dream == "s":
            dream = True
        elif dream == "n":
            dream = False
        else:
            print("Resposta inválida. Digite s ou n.")
            continue
        pet.sleep(hours, dream)
    elif option == "5":
        # Mostra os atributos do pet
        pet.toString()
    elif option == "6":
        # Sai do jogo
        print("Obrigado por jogar. Até mais!")
        break

