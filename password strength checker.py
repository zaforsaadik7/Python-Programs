import re


def strongPass(password):
    lengthError = len(password) < 8
    digitError = re.search(r"\d", password) is None
    uppercaseError = re.search(r"[A-Z]", password) is None
    lowercaseError = re.search(r"[a-z]", password) is None
    symbleError = re.search(r"\W", password) is None

    if lengthError:
        print("Password must be atleast 8 character long.")
    elif digitError:
        print("Password must contain digits.")
    elif uppercaseError:
        print("Password must have uppercase character.")
    elif lowercaseError:
        print("Password must contain lowercase character.")
    elif symbleError:
        print("password must contain symbolic character.")
    else:
        print("Password is strong.")


password = input("enter your password: ")
strongPass(password)
