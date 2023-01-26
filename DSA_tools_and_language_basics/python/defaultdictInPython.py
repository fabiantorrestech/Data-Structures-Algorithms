from collections import defaultdict

defDict = defaultdict(list) # ~ default-(value) dictionary ~
                            #   - default dicts do NOT give "KeyError" when asked to access a non-existing key. 
                            #     They give whatever value is specified at creation, so in THIS CASE: it will populate it with a list


defDict["one"] = 1          # assigning a dictionary key a value (normal dict behavior)
print(defDict["one"])

print(defDict["two"])       # in a regular dict(), this would give keyError, since we didn't create it.
                            # ... but in defaultdict, it is automatically generated and given a value of an empty list [].
                            # so it now exists in defDict!

defDict["three"].append(4) # we don't need for a key to be created ALREADY to start editing its value in a defaultdict.
print(defDict["three"])