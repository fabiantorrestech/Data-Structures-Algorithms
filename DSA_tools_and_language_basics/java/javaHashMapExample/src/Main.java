import java.util.HashMap;

public class Main {

  public static void main(String[] args) {

    // creating a hashmap
    HashMap<String, String> countriesWithCapitols = new HashMap<String, String>();

    // print out a hashmap - sout
    System.out.println(countriesWithCapitols);

    // add keys & values - .put()
    countriesWithCapitols.put("USA", "Washington D.C.");
    countriesWithCapitols.put("India", "New Delhi");
    countriesWithCapitols.put("Russia", "Moscow");
    countriesWithCapitols.put("China", "Beijing");
    System.out.println(countriesWithCapitols);

    // remove a hashmap entry (by key) - .remove()
    countriesWithCapitols.remove("USA");
    System.out.println(countriesWithCapitols);

    // get hashmap value - .get()
    System.out.println(countriesWithCapitols.get("Russia"));

    // get size of hashmap - .size()
    System.out.println(countriesWithCapitols.size());

    // replace a hashmap entry's value - .replace()
    countriesWithCapitols.replace("Russia", "IDK!");
    System.out.println(countriesWithCapitols);

    // check if a hashmap contains a key (true or false) - .containsKey()
    System.out.println(countriesWithCapitols.containsKey("India"));

    // check if a hashmap contains a value (true or false) - .containsValue()
    System.out.println(countriesWithCapitols.containsValue("Bro"));

    // iterate over a hashmap with a for-each loop
    System.out.println("-- Iterating over the hashmap with a for-each loop! --");
    for(String country : countriesWithCapitols.keySet()){
      System.out.println(country +" = " + countriesWithCapitols.get(country));
    }
    System.out.println("-----");

    // clear out the entire hashmap of all entries - .clear()
    countriesWithCapitols.clear();
    System.out.println("clearing out all of a hashmap's entries: " + countriesWithCapitols);

  }
}