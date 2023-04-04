mydict = {
    "happy" : "ख़ुश",
    "sad" : "उदास",
    "eyes" : "नेत्र",
    "dark" : "अंधेरा",
    "bright" : "उज्ज्वल"
}

print("Options are as follows\n", mydict.keys())
a = input("Enter any word from the given options :\n")

print("The meaning of the word you entered is :\n", mydict.get(a))