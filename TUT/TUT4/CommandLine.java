package view;

import java.util.Scanner;


public class CommandLine {
	 public String expression;
	 public boolean isExpressionReady=false;
     public void getUserInput() {
    	 Scanner sc=new Scanner(System.in);
    	
    		 System.out.println("Enter Expression to evaluate(Enter 'exit' to exit):");
    		 expression =sc.nextLine();
    		 if(expression.equals("exit"))
    			 {
    			 	System.exit(0);
    			 	sc.close();
    			 }
    		 isExpressionReady=true;
    		 System.out.println("expression set");
    	
    	 
     } 
     public void setResult(double r) {
    	 System.out.println(r);
     }
}
