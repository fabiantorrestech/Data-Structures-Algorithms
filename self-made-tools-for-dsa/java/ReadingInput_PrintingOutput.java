import java.util.Scanner; // utilizing Java Scanner for input

public class ReadingInput_PrintingOutput
{
	public static void main(String[] args) {
		
	    Scanner scan = new Scanner(System.in); 

	    int a = scan.nextInt();
	    String b = scan.next();
	    
	    
	    System.out.println("a: " + a);
		System.out.println("b: " + b);
	}
}
