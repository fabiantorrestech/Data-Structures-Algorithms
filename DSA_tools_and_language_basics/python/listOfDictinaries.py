listOfDicts = [
                {1070: "I am the 1st key in 1st dict", 1071: "I am the 2nd key in 1st dict"},
                {1070: "I am the 1st key in 2nd dict", 1071: "I am the 2nd key in 2nd dict"},
                {1070: "I am the 1st key in 3rd dict", 1071: "I am the 2nd key in 3rd dict"}
              ]

# printing/retrieving individual items
print(listOfDicts[0][1070])
print(listOfDicts[1][1071])

# updating a value in 2nd dict
listOfDicts[1][1071] = "updated value"
print(listOfDicts)

# adding another value to 2nd dict
listOfDicts[1][1072] = "a 3rd key in the 2nd dict (: !!!"
print(listOfDicts)

# remove a value from a dict
listOfDicts[0].pop(1070)
print(listOfDicts)

