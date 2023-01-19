import java.util.HashMap;

class IntializeAHashMap{

    public static void main(String[] args){
        
        // hashmaps can only contain Object-types, not primitives.
        HashMap<String, Integer> hm = new HashMap<String, Integer>();
        
        
        // ADD - add into a HashMap
        hm.put("key1", 1);
        hm.put("key2", 2);
        hm.put("key3", 3);
        System.out.println(hm.toString());
        
        
        // ACCESS - access an item in HashMap -- null if it doesn't exist.
        Integer value1 = hm.get("key1");
        System.out.println(value1);
        
        
        // check if a key exists/DNE in a HashMap
        boolean keyExists = hm.containsKey("key1");
        System.out.println(keyExists);
        
        boolean keyNotInMap = hm.containsKey("eggs");
        System.out.println(keyNotInMap);
        
        
        // loop through a hashmap - keys and values
        for(String key: hm.keySet()){
            System.out.println(key);    // keys
        }
        
        for(Integer value: hm.values()){
            System.out.println(value);  // values
        }
        
        for(String key: hm.keySet()){
            System.out.println("key: " + key + " = " + hm.get(key));    // keys and values
        }
        
        
        // REMOVE - remove a key from a hashmap.
        hm.remove("key1");
        System.out.println(hm.toString());
        
        
        // clear out the whole hashmap
        hm.clear();
        System.out.println(hm.toString());
        
        
    }

}