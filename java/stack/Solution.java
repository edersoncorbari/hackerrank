import java.util.*;

public class Solution {

  public static void main(String []argh) {
    Scanner sc = new Scanner(System.in);
    while (sc.hasNext()) {
      String input = sc.next();
      System.out.println(checkIsStringBalanced(input));
    }
    sc.close();
  }

  static boolean checkIsStringBalanced(String values) {
    Stack<Character> stack = new Stack<Character>();
    for (int i = 0; i < values.length(); i++) {
      char a = values.charAt(i);
      if (a == '(' || a == '[' || a == '{') {
        stack.push(a);
      } else if (stack.empty()) {
        return false;
      } else {
        char b = stack.pop();
        if ((b == '(' && a != ')') || (b == '[' && a != ']') || (b == '{' && a != '}')) {
          return false;
        }
      }
    }
    return stack.empty();
  }
}

