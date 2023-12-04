import java.util.Stack;

public class Main {
    public static void main(String[] args) {

        // declare a stack (needs 'import java.util.Stack')
        // - LIFO = Last In (last index), First out
        Stack<String> stack = new Stack<String>();

        // add to stack
        stack.push("hello");
        stack.push("hi");
        stack.push("hey");

        // find stack size
        System.out.println("stack size: " + stack.size() + '\n');

        // get element at i'th index
        System.out.println(stack.get(2) + '\n');

        // 1) print a stack (for-each loop)
        for(String str : stack){
            System.out.println(str);
        }
        System.out.println();

        // 2) print stack (for loop)
        for(int i=0; i<stack.size(); i++){
            System.out.println(stack.get(i));
        }
        System.out.println();

        // remove from top of stack
        stack.pop();
        for(String str : stack){
            System.out.println(str);
        }
        System.out.println();

        // see top stack element (but do not pop it)
        System.out.println(stack.peek() + '\n');

        // see if element exists in Stack
        if(stack.contains("hello")){
            System.out.println("hello is in stack! (:");
        }

        // give index where a stack element is located
        // - 1-index based.
        // - will return -1 if not present.
        System.out.println("hello is at " + Integer.toString(stack.search("hello")));
        System.out.println("hey isn't present, so it gives us " + Integer.toString(stack.search("hey")));

    }
}