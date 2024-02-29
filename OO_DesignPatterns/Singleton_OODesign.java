package OO_DesignPatterns;

static class Singleton {

  private static Singleton s = null; // must be private static because only Singleton class can access these.
  private String value = null;

  private Singleton() {} // empty contructor, only declared to make it private.

  public static Singleton getInstance() { // how outside interacts with singleton.
      if(s == null){
          s = new Singleton();
      }
      return s;
  }

  public String getValue() {
      return this.value;
  }

  public void setValue(String value) {
      this.value = value;
  } 
}

public class Singleton_OODesign {

  public static void main(String[] args) {
    Singleton s = Singleton.getInstance();

    s.getValue(); // null

    s.setValue("a value string");
    s.getValue(); // "a value string"

    Singleton s2 = Singleton.getInstance();

    s2.getValue(); // "a value string"
  }
  
}
