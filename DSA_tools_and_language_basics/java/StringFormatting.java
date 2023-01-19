import java.text.MessageFormat;

public class StringFormatting {
    public static void main(String[] args) {

        String name = "Fabian";
        int age = 23;
        String country = "USA";
        String sport = "running";
        int hours = 2;
        String game = "Apex Legends";
        String subject = "English";
        char grade = 'A';
        
        // 1) MessageFormat.format()
        System.out.println(MessageFormat.format("My name is {0} . I''m {1} years old, and I''m from {2}.", name, age, country));
        // 2) String.format()
        System.out.println(String.format("My favourite sport is %s. I play for %d hours a day.", sport, hours));
        // 3) static string + var + string...
        System.out.println("When I'm tired, I like to play " + game + ".");
        System.out.println("In school, my favourite subject was " + subject + ", I scored an " + grade + ".");

    }
}