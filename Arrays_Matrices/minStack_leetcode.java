// problem: https://leetcode.com/problems/min-stack/
// TIME: push=O(1), pop=O(1), top=O(1), getMin=O(1)
// SPACE: O(2n) -> O(n)
// - optimal solution where we can get the minimum in constant time. however, we need 2 array to accomplish this in constant time.

class MinStack {

  public List<Integer> stack;     // holds all values of the stack. 
  public List<Integer> minimums;  // keeps track of the minimum at corresponding index for stack.


  public MinStack() {
      this.stack = new ArrayList<>();
      this.minimums = new ArrayList<>();
  }
  
  public void push(int val) {
      stack.add(val);
      minimums.add(val); 
      if(minimums.size()>=2 &&
      minimums.get(minimums.size()-2) < minimums.get(minimums.size()-1))
          minimums.set(minimums.size()-1, minimums.get(minimums.size()-2));
  }
  
  public void pop() {
      stack.remove(stack.size()-1);
      minimums.remove(minimums.size()-1);
  }
  
  public int top() {
      return stack.get(stack.size()-1);
  }
  
  public int getMin() {
      return minimums.get(minimums.size()-1);
  }
}

/**
* Your MinStack object will be instantiated and called as such:
* MinStack obj = new MinStack();
* obj.push(val);
* obj.pop();
* int param_3 = obj.top();
* int param_4 = obj.getMin();
*/