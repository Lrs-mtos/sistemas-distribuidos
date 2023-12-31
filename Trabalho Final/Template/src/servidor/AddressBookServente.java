package servidor;


public class AddressBookServente {

	// Essa é classe que REALMENTE implementa o serviço.
	// Neste exemplo, os métdos devem adicionar, listar e remover contatos de
	// uma
	// agenda.
	// Os dados são armazenados em arquivo

	public AddressBook list(String agenda) {

		// Lê o arquivo que armazena a agenda e retorna um objeto
		// AddressBook preenchido com esses dados
	}

	public String addPerson(Person person, String nomeAgenda) {

		// Adiciona uma pessoa ao arquivo que mantem os dados da agenda.
		// O path do arquivo é indicado por "nomeAgenda"
		// Retorna uma mensagem de sucesso ou de erro
	}

	public String remove(int id, String nomeAgenda) {

		// Remove uma pessoa do arquivo que mantem os dados da agenda.
		// A pessoa que deve ser removida é indica po "id"
		// O path do arquivo é indicado por "nomeAgenda"
		// Retorna uma mensagem de sucesso ou de erro
	}
}