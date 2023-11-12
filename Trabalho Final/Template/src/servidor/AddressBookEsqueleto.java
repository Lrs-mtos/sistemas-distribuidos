package servidor;

public class AddressBookEsqueleto {

	AddressBookServente servente;

	public AddressBookEsqueleto() {
		servente = new AddressBookServente();
	}

	public byte[] addPerson(ByteString args) {
		// (1) Desempacota argumento de entrada
		// (2) chama o metodo do servente
		// (3) empacota resposta do método servente e retorna
	}

	public byte[] list(ByteString args) {
		// (1) Desempacota argumento de entrada
		// (2) chama o metodo do servente
		// (3) empacota resposta do método servente e retorna
	}

	public byte[] remove(ByteString args) {
		// (1) Desempacota argumento de entrada
		// (2) chama o metodo do servente
		// (3) empacota resposta do método servente e retorna
	}
}
