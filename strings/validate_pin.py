'''
Description:
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot 
contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
'''


def validate_pin(pin):
    return len(pin) in [4, 6] and pin.isdigit()


pin = "1234"
print(validate_pin(pin))


def validate_pin_alt(pin):
    if not pin.isdigit():
        return False

    if len(pin) in [4, 6]:
        return True
    return False


print(validate_pin_alt(pin))
