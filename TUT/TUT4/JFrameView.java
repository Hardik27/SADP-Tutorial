package view;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Scanner;
import javax.swing.*;
import controller.*;
public class JFrameView implements ActionListener{
	public String expression;

	JFrame f;

    public JTextField t=new JTextField();
    public boolean isExpressionReady=false;
    JButton bclear,bresult,b1,b2,b3,b4,b5,b6,b7,b8,b9,b0,bplus,bminus,bdiv,bmul;

    //double result;
    JPanel panel; 
    public JFrameView() {
    	f=new JFrame("Calculator");
    	bclear=new JButton("clear");

        bresult=new JButton("result");
        b1=new JButton("1 ");
        b2=new JButton("2 ");
        b3=new JButton("3 ");
        b4=new JButton("4 ");
        b5=new JButton("5 ");
        b6=new JButton("6 ");
        b7=new JButton("7 ");
        b8=new JButton("8 ");
        b9=new JButton("9 ");
        b0=new JButton("0 ");
        bplus=new JButton("+ ");
        bminus=new JButton("- ");
        bdiv=new JButton("/ ");
        bmul=new JButton("* ");
        f.setLayout(null);

        f.setVisible(true);

        f.setSize(1000,500);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setResizable(true);
        t.setBounds(40,30,500,40);
        b1.setBounds(40,100, 50,20);
        b2.setBounds(140,100, 50, 20);
        b3.setBounds(240,100, 50, 20);
        b4.setBounds(40,130, 50,20);
        b5.setBounds(140,130, 50, 20);
        b6.setBounds(240,130, 50, 20);
        b7.setBounds(40,160, 50,20);
        b8.setBounds(140,160, 50, 20);
        b9.setBounds(240,160, 50, 20);
        b0.setBounds(140,190, 50, 20);
        bplus.setBounds(40,220, 50, 20);
        bminus.setBounds(100,220, 50, 20);
        bdiv.setBounds(160,220, 50, 20);
        bmul.setBounds(220,220, 50, 20);
        bclear.setBounds(40,250,100,40);
        bresult.setBounds(170,250,100,40);
        f.add(b1);
        f.add(b2);
        f.add(b3);
        f.add(b4);
        f.add(b5);
        f.add(b6);
        f.add(b7);
        f.add(b8);
        f.add(b9);
        f.add(b0);
        f.add(bplus);
        f.add(bminus);
        f.add(bdiv);
        f.add(bmul);
        f.add(t);

        f.add(bclear);

        f.add(bresult);
    }
    public void getUserInput() {
    	
        
        b1.addActionListener(this);
        b2.addActionListener(this);
        b3.addActionListener(this);
        b4.addActionListener(this);
        b5.addActionListener(this);
        b6.addActionListener(this);
        b7.addActionListener(this);
        b8.addActionListener(this);
        b9.addActionListener(this);
        b0.addActionListener(this);
        bplus.addActionListener(this);
        bminus.addActionListener(this);
        bdiv.addActionListener(this);
        bmul.addActionListener(this);
        bclear.addActionListener(this);
        bresult.addActionListener(this);;
    }
    public void actionPerformed(ActionEvent e)

    {
    	System.out.println("Inside actionPerformed");
        if(e.getSource()==bclear)

        	t.setText("");

    if(e.getSource()==bresult)

        {
        	expression=t.getText();
        	this.isExpressionReady=true;
        	System.out.println(expression); 
        }
        if(e.getSource()==b1)
        {
           	t.setText(t.getText().concat("1 "));
        }
        if(e.getSource()==b2)
        {
           	
           	t.setText(t.getText().concat("2 "));
        }
        if(e.getSource()==b3)
        {
           	
           	t.setText(t.getText().concat("3 "));
        }
        if(e.getSource()==b4)
        {
           	
           	t.setText(t.getText().concat("4 "));
        }
        if(e.getSource()==b5)
        {
           
           	t.setText(t.getText().concat("5 "));
        }
        if(e.getSource()==b6)
        {
           	
           	t.setText(t.getText().concat("6 "));
        }
        if(e.getSource()==b7)
        {
           
           	t.setText(t.getText().concat("7 "));
        }
        if(e.getSource()==b8)
        {
           
           	t.setText(t.getText().concat("8 "));
        }
        if(e.getSource()==b9)
        {
           	
           	t.setText(t.getText().concat("9 "));
        }
        if(e.getSource()==b0)
        {
           	
           	t.setText(t.getText().concat("0 "));
        }
        if(e.getSource()==bplus)
        {
           	
           	t.setText(t.getText().concat("+ "));
        }
        if(e.getSource()==bminus)
        {
           	
           	t.setText(t.getText().concat("- "));
        }
        if(e.getSource()==bdiv)
        {
           	
           	t.setText(t.getText().concat("/ "));
        }
        if(e.getSource()==bmul)
        {
           	
           	t.setText(t.getText().concat("* "));
        }
    }
    
    public void setResult(double r) {
		t.setText(String.valueOf(r));
	}
}
