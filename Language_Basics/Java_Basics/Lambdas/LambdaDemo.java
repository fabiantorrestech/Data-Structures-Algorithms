package Lambdas;

import Interfaces.Cat;
import Interfaces.Printable;

public class LambdaDemo {
    public static void main(String[] args){
        Interfaces.Cat myCat = new Cat();       // create a new Cat object
                                                // lambda function example!
        printThing(() -> {                      // - () = params ...(still needs to be Printable implemented)
                                                // - {} = function
            System.out.println("Meow!");
        });
    }

    static void printThing(Printable thing){ // takes in any object that implements the "Printable" interface (Cat object does!)
        thing.print(); // calls the object's print method (which falls back to the Cat's print() implementation)
    }
}