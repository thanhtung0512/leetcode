package code.neetcode.core

import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        
        Stack<Character> st = new Stack<>();
        
        for (char x : s.toCharArray()) {
            if (x == '(' || x == '{' || x == '[') {
                st.push(x);
                continue;
            }

            if (st.empty()) return false;
            if (x == ')') {
                char check = st.pop().charValue();
                if (check != '(') return false;
            }    
            else if ( x== '}') {
                char check = st.pop().charValue();
                if (check != '{') return false;
             }
             else if (x == ']') {
                char check == st.pop().charValue();
                if (check != '[') return false;
             }


        }

       
        return st.empty();
    }
}