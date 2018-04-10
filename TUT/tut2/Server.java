import java.net.*;
import java.io.*;
public class Server {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Server Started!!");
		try {
			//server open socket
			ServerSocket ss=new ServerSocket(8885);
			int counter=0;
			while(true)
			{
				Socket s=ss.accept();
				counter++;
				System.out.println("Client: "+String.valueOf(counter)+" is connected to the server");
				ClientServerThread cst=new ClientServerThread(counter,s);
				cst.start();
			}
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
	}
}
