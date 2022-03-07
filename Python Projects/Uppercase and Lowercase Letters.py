def get_lower_and_upper_case_letters(word):
    # Complete this function
    uppercase=""
    lower=""
    
    for letter in word:
        if letter.upper()==letter:
            uppercase+=letter
        else:
            lower+=letter
    print(uppercase)
    print(lower)
word = input()
# Call the get_lower_and_upper_case_letters function
get_lower_and_upper_case_letters(word)
