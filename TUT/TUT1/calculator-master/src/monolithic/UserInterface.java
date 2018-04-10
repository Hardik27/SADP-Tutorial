package monolithic;

import java.util.Scanner;
import monolithic.BusinessLogic;

public class UserInterface {
	public static void main(String[] args) {	    
		Scanner sc = new Scanner(System.in);

	    while (true) {
	    	// Enter the equation in the form-
	        // "operand1 operation operand2"
	        System.out.print("Enter the expression :");
	        
	        String inp = sc.nextLine();

	        if (inp.equals("bye")) {
	        	System.out.println("Thanks for using calculator!\nBye!");
	        	break;
	        }
            
	        BusinessLogic c = new BusinessLogic();
	        
	        System.out.println("Answer =\t" + c.solve(inp));
	    }
	    sc.close();
	}
}