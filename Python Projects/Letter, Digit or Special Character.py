
 
def charCheck(input_char):
     
    # CHECKING FOR ALPHABET
    if ((int(ord(input_char)) >= 65 and
        int(ord(input_char)) <= 90) or
        (int(ord(input_char)) >= 97 and
        int(ord(input_char)) <= 122)):
        print( "Uppercase Letter")
     
    # CHECKING FOR DIGITS
    elif (int(ord(input_char)) >= 48 and
            int(ord(input_char)) <= 57):
        print("Digit")
 
    # OTHERWISE SPECIAL CHARACTER
    else:
        print("Special Character")
 
input_char = input()
charCheck(input_char)
 
