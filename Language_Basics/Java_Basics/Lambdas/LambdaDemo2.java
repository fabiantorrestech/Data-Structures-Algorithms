package Lambdas;

import Interfaces.Cat;
import Interfaces.Printable;

public class LambdaDemo2 {
    public static void main(String[] args){
        Cat myCat = new Cat();       // create a new Cat object

        Printable lambdaPrintable = () -> {System.out.println("Meow!");}; // we can save method implementations into objects!
        printThing(lambdaPrintable);
    }

    static void printThing(Printable thing){ // takes in any object that implements the "Printable" interface (Cat object does!)
        thing.print(); // calls the object's print method (which falls back to the Cat's print() implementation)
    }
}