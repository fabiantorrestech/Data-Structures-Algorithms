package Java_Interfaces;

public class Cat implements Printable {

    public String name;             // attributes of Cat
    public int age;

    public Cat(){}
    public void print(){            // Cat's implementation of "print" method from "Printable" interface!
        System.out.println("Meow!");
    }

}
