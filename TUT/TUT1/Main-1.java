import java.util.*;
import java.io.*;
import java.net.*;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Server started");
		try {
			InetAddress ip=InetAddress.getLocalHost();
			int port=5048;
			ServerSocket ss=new ServerSocket(9998);
			Socket s=ss.accept();
			DataInputStream dis=new DataInputStream(s.getInputStream());
			DataOutputStream dos=new DataOutputStream(s.getOutputStream());
			Scanner scan=new Scanner(System.in);
			while(true)
			{
				String input=dis.readUTF();
				try
				{
				if(input.equals("over"))
				{
					ss.close();
					s.close();
					break;
				}
				
				System.out.println("Query received: " + input);
				
				StringTokenizer st = new StringTokenizer(input);
				int operand1=Integer.parseInt(st.nextToken());
				String operation = st.nextToken();
	            int operand2 = Integer.parseInt(st.nextToken());
				int result;
	            // perform the required operation.
				if (operation.equals("+"))
	            {
	                result = operand1 + operand2;
	            }
	            else if (operation.equals("-"))
	            {
	                result = operand1 - operand2;
	            }
	            else if (operation.equals("*"))
	            {
	                result = operand1 * operand2;
	            }
	            else
	            {
	                result = operand1 / operand2;
	            }
	            System.out.println("Sending the result: "+result);
	 
	            // send the result back to the client.
	            dos.writeUTF(Integer.toString(result));
				}
				catch(Exception e)
				{
					System.out.println(e);
				}
			}
	}
		catch(Exception e)
		{
			System.out.println(e);
		}
}
}
