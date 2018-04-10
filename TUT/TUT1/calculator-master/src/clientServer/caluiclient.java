package clientServer;
//Java program to illustrate Client Side Programming
//for Simple Calculator using TCP
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

public class caluiclient {
 public static void main(String[] args) throws IOException
 {
    // InetAddress ip = InetAddress.getLocalHost();
     Scanner sc = new Scanner(System.in);


     int portNum = 6666;
     // Step 1: Open the socket connection.
     Socket s = new Socket("127.0.0.1", portNum);

     // Step 2: Communication-get the input and output stream
     DataInputStream 	dis = new DataInputStream(s.getInputStream());
     DataOutputStream 	dos = new DataOutputStream(s.getOutputStream());

     while (true)
     {
         // Enter the equation in the form-
         // "operand1 operation operand2"
         System.out.print("Enter the expression :");
         

         String inp = sc.nextLine();

         if (inp.equals("bye")) {
        	// tell server to close connection
             dos.writeUTF("bye");
             dos.flush();
             break;
         }

         // send the equation to server
         dos.writeUTF(inp);
         dos.flush();

         // wait till request is processed and sent back to client
         String ans = (String)dis.readUTF();
         System.out.println("Answer=" + ans);
     }
     
     dis.close();
     dos.close();
     sc.close();
     s.close();
 }
 
}