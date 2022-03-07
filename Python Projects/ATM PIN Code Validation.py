def validate_atm_pin_code(pin):
    # Complete this function
    is_valid=True
    is_having_four_or_six_characters=(len(pin)==4) or (len(pin)==6)
    
    if is_having_four_or_six_characters:
        is_all_digits=pin.isdigit()
        if not is_all_digits:
            is_valid=False
    else:
         is_valid=False
            
    if is_valid:
         print("Valid PIN Code")
    else:
         print("Invalid PIN Code")
pin = input()
# Call the validate_atm_pin_code function
validate_atm_pin_code(pin)
