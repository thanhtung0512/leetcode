// https://coderbyte.com/results/thanhtung05122003:Bracket%20Combinations:Java

import java.util.*;
import java.io.*;

class Main {

    static int res = 0;

    public static boolean checkValidParentheses(String paren) {
        Stack<Character> temp = new Stack<>();
        for (char c : paren.toCharArray()) {
            if (c == '(') {
                temp.push(new Character(c));
            } else {
                if (!temp.isEmpty()) {
                    Character lastChar = temp.pop();
                    if (lastChar.charValue() == ')')
                        return false;
                } else
                    return false;
            }
        }
        if (temp.isEmpty())
            return true;
        return false;
    }

    public static boolean checking(String a, int num) {
        int open = 0;
        int close = 0;
        for (char c : a.toCharArray()) {
            if (c == '(') {
                open++;
            } else
                close++;
        }
        return open == num && open == close;
    }

    public static void nextPermute(String a, int num) {
        if (a.length() == 2 * num) {
            if (checking(a, num)) {
                if (checkValidParentheses(a)) {
                    res++;
                }
            }
            return;
        }
        nextPermute(a + '(', num);
        nextPermute(a + ')', num);
    }

    public static int BracketCombinations(int num) {
        nextPermute("", num);
        return res;
    }

    public static void main(String[] args) {
        // keep this function call here
        Scanner s = new Scanner(System.in);
        System.out.print(BracketCombinations(s.nextLine()));
    }

}