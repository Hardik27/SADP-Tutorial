import java.io.*;
import java.net.*;
public class Clientcalc2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try{
		    Socket socket=new Socket("127.0.0.1",8885);
		    DataInputStream inStream=new DataInputStream(socket.getInputStream());
		    DataOutputStream outStream=new DataOutputStream(socket.getOutputStream());
		    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		    String clientMessage="",serverMessage="";
		    while(!clientMessage.equals("bye")){
		      System.out.println("Enter number :");
		      clientMessage=br.readLine();
		      outStream.writeUTF(clientMessage);
		      outStream.flush();
		      serverMessage=inStream.readUTF();
		      System.out.print(serverMessage);
		    }
		    while(true)
		    {
		    	serverMessage=inStream.readUTF();
		    	if(serverMessage.equals("done"))
		    	{
		    		break;
		    	}
		    	System.out.println(serverMessage);
		    }
		    outStream.close();
		    outStream.close();
		    socket.close();
		  }catch(Exception e){
		    System.out.println(e);
		  }
	}

}
