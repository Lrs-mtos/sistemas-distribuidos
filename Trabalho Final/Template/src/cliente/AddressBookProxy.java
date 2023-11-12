package cliente;


public class AddressBookProxy {
	int requestiId = 0;

	// O ideal seria solicitar os dados de conexao ao cliente
	// através de um nome de domínio (ex: www.ufc.br)
	TCPClient tcpClient = new TCPClient("localhost", 7896);

	public AddressBook list(String nomeAgenda) {
		// (1) Empacota argumentos de entrada (ex: nomeAgenda)
		// (2) Chama doOperation
		// (3) Desempacota argumento de resposta (retorno de doOperation)
		// (4) Retorna reposta desempacotada
		// ex:
		// addressBook = AddressBook.parseFrom(doOperation("AddressBook",
		// "list", listPessoa.build().toByteArray()));
	}

	public String addPerson(Person person) {
		// (1) Empacota argumentos de entrada
		// (2) Chama doOperation
		// (3) Desempacota argumento de resposta (retorno de doOperation)
		// (4) Retorna reposta desempacotada
	}

	public String remove(int id, String nomeAgenda) {
		// (1) Empacota argumentos de entrada
		// (2) Chama doOperation
		// (3) Desempacota argumento de resposta (retorno de doOperation)
		// (4) Retorna reposta desempacotada
	}

	public byte[] doOperation(String objectRef, String method, byte[] args) {

		byte[] data = empacotaMensagem(objectRef, method, args);

		// envio
		tcpClient.sendRequest(data);

		// recebimento
		Message resposta = desempacotaMensagem(tcpClient.getReply());

		return resposta.getArguments().toByteArray();

	}

	public void finaliza() {
		tcpClient.finaliza();
	}

	private byte[] empacotaMensagem(String objectRef, String method, byte[] args) {

		// empacota a Mensagem de requisicao

	}

	private Message desempacotaMensagem(byte[] resposta) {

		// desempacota a mensagem de resposta

	}

}