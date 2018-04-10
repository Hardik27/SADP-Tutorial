
interface Expression {

    double calculate();
}

class Constant implements Expression {

    double value;

    public Constant(double value) {
        this.value = value;
    }

    @Override
    public double calculate() {
        return value;
    }
}


abstract class BinaryExpression implements Expression {

    protected Expression left;
    protected Expression right;

    public BinaryExpression(Expression left, Expression right) {

        this.left = left;
        this.right = right;
    }
}


class Add extends BinaryExpression {

    public Add(Expression left, Expression right) {
        super(left, right);
    }

    @Override
    public double calculate() {
        return left.calculate() + right.calculate();
    }
}


class Subtract extends BinaryExpression {

    public Subtract(Expression left, Expression right) {
        super(left, right);
    }

    @Override
    public double calculate() {
        return left.calculate() - right.calculate();
    }
}



class Multiply extends BinaryExpression {

    public Multiply(Expression left, Expression right) {
        super(left, right);
    }

    @Override
    public double calculate() {
        return left.calculate() * right.calculate();
    }
}



class Divide extends BinaryExpression {

    public Divide(Expression left, Expression right) {
        super(left, right);
    }

    @Override
    public double calculate() {
        return left.calculate() / right.calculate();
    }
}



public class Tut6 {
	
	public static void main(String ar[]) {
	
	Expression cons1 = new Constant(5.0);
	Expression cons2 = new Constant(2.0);
	Expression e = new Divide(cons1,cons2);
	Expression f = new Multiply(cons1,cons2);
	Expression a = new Add(e,f);
	System.out.println("Hello"+" "+e.calculate());
	System.out.println("Hello"+" "+f.calculate());
	System.out.println("Hello"+" "+a.calculate());
}
}