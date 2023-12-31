package cliente;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;

public class TCPClient {

	Socket socket = null;
	DataInputStream in = null;
	DataOutputStream out = null;

	public TCPClient(String serverIP, int port) {
		try {
			socket = new Socket(serverIP, port);
			in = new DataInputStream(socket.getInputStream());
			out = new DataOutputStream(socket.getOutputStream());
		} catch (UnknownHostException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public void sendRequest(byte[] requisicao) {
		// enviado via moodle
	}

	public byte[] getReply() {
		// enviado via moodle
	}

	public void finaliza() {
		try {
			socket.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}