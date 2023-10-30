import json

class Shop:
    def __init__(self):
        self.products = []

    def create_product(self, name, price, product_id):
        product = {
            "name": name,
            "price": price,
            "id": product_id
        }
        self.products.append(product)
        print(f"Produto '{name}' criado com sucesso!")

    def list_products(self):
        print("\nLista de Produtos:")
        for product in self.products:
            print(f"ID: {product['id']} - Nome: {product['name']} - Preço: ${product['price']}")

    def save_to_json(self):
        with open("products.json", "w") as file:
            json.dump(self.products, file)
        print("Produtos salvos em products.json")

    def load_from_json(self):
        try:
            with open("products.json", "r") as file:
                self.products = json.load(file)
            print("Produtos carregados de products.json")
        except FileNotFoundError:
            print("Nenhum arquivo de produtos encontrado.")

def main():
    shop = None
    while True:
        print("\nEscolha uma ação:")
        print("1 - Iniciar a loja")
        print("2 - Criar produto")
        print("3 - Listar produtos")
        print("4 - Salvar produtos")
        print("5 - Sair")

        choice = input("Opção: ")

        if choice == "1":
            shop = Shop()
            print("Loja iniciada.")
        elif choice == "2":
            if shop:
                name = input("Nome do produto: ")
                price = float(input("Preço do produto: "))
                product_id = input("ID do produto: ")
                shop.create_product(name, price, product_id)
            else:
                print("A loja não foi iniciada. Escolha a opção 1 para iniciar.")
        elif choice == "3":
            if shop:
                shop.list_products()
            else:
                print("A loja não foi iniciada. Escolha a opção 1 para iniciar.")
        elif choice == "4":
            if shop:
                shop.save_to_json()
            else:
                print("A loja não foi iniciada. Escolha a opção 1 para iniciar.")
        elif choice == "5":
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")

if __name__ == "__main__":
    main()
