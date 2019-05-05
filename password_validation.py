import re

def hasNumber(s):
    f = any([c for c in s if c.isdigit()])
    if f == False:
        print("Must have at least one digit")
    return f

def hasUpperCaseAlphabet(s):
    f = False
    for i in range(0,len(s)):
        if ord(s[i]) >= 65 and ord(s[i]) <= 92:
            f = True
            break
    if f == False:
        print("Must have at least one upper case alphabet")
    return f

def hasLowerCaseAlphabet(s):
    f = any([c for c in s if c.islower()])
    if f == False:
        print("Must have at least one lower case alphabet")
    return f

def hasSpecialCharacter(s):
    special_symbols = ['$','@','#','%']
    f = any([c for c in s if c in special_symbols])
    if f == False:
        print("Must have at least one special character")
    return f

def hasValidLength(s):
    f = True
    if len(s) < 6: 
        f = False
        print("Must be at least 6 characters long")
    if len(s) > 20:
        f = False
        print("Must be at most 20 characters long")
    return f

def isValidPassword(s):
    return hasNumber(s) and hasUpperCaseAlphabet(s) and hasLowerCaseAlphabet(s) and hasSpecialCharacter(s) and hasValidLength(s)

def isValidPasswordRegex(s):
    exp = r"^[\dA-Za-z$@#%.]([\dA-Za-z$@#%.]){5,19}$"
    pattern = re.compile(exp)
    match = re.search(pattern,s)
    print("match=",match)
    return match

password = input("Enter a password: ")
if isValidPassword(password):
    print(password, "is a valid password")
else:
    print(password, "is not a valid password")


if isValidPasswordRegex(password):
    print(password, "is a valid password")
else:
    print(password, "is not a valid password")
