package model;

public class CalculatorModel {
  private double result;
  private String expression;
  public void setResult(double r) {
	  this.result=r;
  }
  public void setExpression(String e) {
	  this.expression=e;
  }
  public double getResult() {
	return this.result;
}
  public String getExpression() {
	return this.expression;
}
  
}
