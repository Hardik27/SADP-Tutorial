import java.net.*;
import java.util.*;
import java.io.*;
public class Main {
	public static void main(String[] args)
	{
		try {
			InetAddress ip=InetAddress.getLocalHost();
			int port=9998;
			Socket s=new Socket(ip,port);
			DataInputStream dis=new DataInputStream(s.getInputStream());
			DataOutputStream dos=new DataOutputStream(s.getOutputStream());
			Scanner scan=new Scanner(System.in);
			while(true)
			{
				System.out.println("ENTER THE QUERY");
				String str=scan.nextLine();
				
				if(str.equals("over"))
				{
					s.close();
					break;
				}
				dos.writeUTF(str);
				String result=dis.readUTF();
				System.out.println("Result is "+ result);
			}
		}
		catch(Exception e)
		{
			System.err.println();
		}
	}
}
