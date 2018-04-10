
#include <cmath>
#include <iostream>
#include <stack>
#include <string>

using namespace std;

class Calculator
{
    string expr;
public:
    void init(string str)
    {
        expr= str;
    }
int evalInfix()
{
  return evalPostfix(infixToPostfix());
}
int evalPostfix(string expr);
bool isOperator(char letter);
int precedence(char op);
string infixToPostfix()
{
  string postfix;
  stack<char> stack;
  char previous;
  int openParens = 0;

  for (string::iterator it = expr.begin(); it != expr.end(); it++) {
    char letter = *it;
    if (isspace(letter)) {
      continue;
    }
    if (isdigit(letter)) {
      postfix.append(1, letter);
    } else if (letter == '(') {
      openParens++;
      stack.push(letter);
    } else if (isOperator(letter)) {
      if (stack.empty()) {
        stack.push(letter);
      } else {
        char op = stack.top();
        while (precedence(op) > precedence(letter)) {
          stack.pop();
          postfix.append(1, op);
        }
        stack.push(letter);
      }
    } else if (letter == ')') {
      openParens--;
      while (!stack.empty() && stack.top() != '(') {
        postfix.append(1, stack.top());
        stack.pop();
      }
      if (!stack.empty()) {
        stack.pop();
      }
    } else {
      if (isOperator(previous) || previous == '(' || previous == ')') {
        throw "operand error";
      } else {
        throw "operator error";
      }
    }
    previous = letter;
  }

  // Check paranthesis
  if (openParens > 0) {
    throw "imbalanced paranthesis error";
  }
  while (!stack.empty()) {
    postfix.append(1, stack.top());
    stack.pop();
  }

  return postfix;
}
};
// Eval function implementation
int Calculator:: evalPostfix(string expr)
{
  // stack is holding input numbers
  stack<int> stack;

  for (string::iterator it = expr.begin(); it != expr.end(); it++) {
    char letter = *it;
    if (isdigit(letter)) {
      // char -> int conversion
      stack.push(letter - '0');
    } else {
      int a = stack.top();
      stack.pop();
      int b = stack.top();
      stack.pop();
      int result;
      switch (letter) {
        case '+': result = b + a; break;
        case '-': result = b - a; break;
        case '*': result = b * a; break;
        case '/': result = b / a; break;
        case '^': result = (int) pow((double) b, a); break;
      }
      stack.push(result);
    }
  }
  return stack.top();
}

bool Calculator::  isOperator(char letter)
{
  return letter == '+' || letter == '-' || letter == '*' || letter == '^'|| letter == '/';
}

int Calculator:: precedence(char op)
{
  switch (op) {
    case '+': return 1;
    case '-': return 2;
    case '*': return 3;
    case '/': return 3;
    case '^': return 4;
  }
  return 0;
}

int main(int argc, char const *argv[])
{
  string line;
  Calculator c1;
    getline(cin, line);
    c1.init(line);
    //try {
      cout << c1.evalInfix() << endl;
    //} catch (char const* e) {
      //cerr << e << endl;
    //}
  return 0;
}
