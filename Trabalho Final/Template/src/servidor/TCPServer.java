package servidor;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class TCPServer {
	public static void main(String args[]) {
		try {
			int serverPort = 7896;
			ServerSocket listenSocket = new ServerSocket(serverPort);
			while (true) {
				Socket clientSocket = listenSocket.accept();
				Connection c = new Connection(clientSocket);
			}
		} catch (IOException e) {
			System.out.println("Listen :" + e.getMessage());
		}
	}
}

class Connection extends Thread {
	DataInputStream in;
	DataOutputStream out;
	Socket clientSocket;
	AddressBookDespachante despachante;

	public Connection(Socket aClientSocket) {
		try {
			despachante = new AddressBookDespachante();
			clientSocket = aClientSocket;
			System.out.println("conectado a " + clientSocket.getInetAddress()
					+ ":" + clientSocket.getPort());
			in = new DataInputStream(clientSocket.getInputStream());
			out = new DataOutputStream(clientSocket.getOutputStream());
			this.start();
		} catch (IOException e) {
			System.out.println("Connection:" + e.getMessage());
		}
	}

	public byte[] getRequest() {
		// enviado via moodle
	}

	public Message desempacotaRequisicao(byte[] array) {
		// Desempacota mensagem de requisicao
	}

	public byte[] empacotaResposta(byte[] resultado, int requestId) {
		// Empacota mensagem de resposta
	}

	public void sendReply(byte[] resposta) {
		// enviado via moodle
	}

	public void run() {
		// Loop para intergair com socket client - TCP Permanente
		while (clientSocket.isConnected()) {
			Message requisicao = desempacotaRequisicao(getRequest());
			byte[] resultado = despachante.selecionaEqueleto(requisicao);
			sendReply(empacotaResposta(resultado, requisicao.getRequestId()));
		}
		try {
			clientSocket.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}