import re

def validateLength(cardNumber):
    """"""
    if len(str(cardNumber)) == 16:
        return True
    else:
        return False

# y = '4444444444444' 
# print(validateLength(y))


def validateCardNo(ccardNumber):
    """Function that validates a 16 digit credit card """
    
    regex = re.compile('\d{4}-?\d{4}-?\d{4}-?\d{4}$')           # derive the regex

    if len(ccardNumber) == 0:
        return False
    
    p = regex.findall(ccardNumber)

    if p is None or len(p) == 0:
        return False
    else:
        return True
    

print(validateCardNo('4552536212128910'))