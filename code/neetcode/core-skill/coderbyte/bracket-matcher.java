// https://coderbyte.com/editor/Bracket%20Matcher:Java

import java.util.*;
import java.io.*;

class Main {

    public static String normalize(String s) {
        StringBuilder builder = new StringBuilder("");
        for (char x : s.toCharArray()) {
            if (x == '(' || x == ')') {
                builder.append(x);
            }
        }
        return builder.toString();
    }

    public static String BracketMatcher(String str) {
        if (str.contains(")(")) return "0";
        int counting = 0;
        for (char x : str.toCharArray()) {
            if (x == '(') {
                counting ++;
            }
            else if (x == ')') {
                counting--;
            }
        }
        if (counting == 0) return "1"; 
        else return "0";
    }

    public static void main(String[] args) {
        // keep this function call here
        Scanner s = new Scanner(System.in);
        System.out.print(BracketMatcher(s.nextLine()));
    }

}