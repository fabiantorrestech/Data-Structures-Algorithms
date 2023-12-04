// problem: https://leetcode.com/problems/valid-parentheses/ 
// - TIME: O(n)
// - SPACE: O(n)
// - 

class Solution {
  public boolean isValid(String s) {
      
      Stack<Character> stack = new Stack<Character>();
      
      for(int i=0; i<s.length(); i++){
          char c = s.charAt(i);
          
          // populate the stack if its empty or if we see an opening paren
          if(stack.empty() ||
             (c == '{' || c == '(' || c == '['))
              stack.push(c);
          
          // pop the stack if we find the appropriate paren vs current character.
          // -if its the wrong character, we don't have matching parens - return false.
          else{
              if(c == '}' && stack.peek() == '{'){  
                  stack.pop();
              }
              else if(c == ')' && stack.peek() == '('){
                  stack.pop();
              }
              else if(c == ']' && stack.peek() == '['){
                  stack.pop();
              }
              else{
                  return false;
              }
          }
      }
      
      // if any characters have been unmatched by the end, there is an unmatched paren - return false.
      if(!stack.empty())
          return false;
      
      return true;
      
  }
}