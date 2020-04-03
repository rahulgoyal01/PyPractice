
def isPhoneNumber(text):
    if len(text) != 12:
        return False        #not a phone number
    for i in range(0,3):
        if not text[i].isdecimal():
            return False    #don't have an area code
    if text[3] != '-':
        return False        #missing dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False    #no first 3 digits
    if text[3] != '-':
        return False        #missing dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False    #missing last 4 digits
    return True

print(isPhoneNumber('999-345-7865'))

msg = "Call me on 426-847-9898 or my personal cell 222-909-9999"
foundNumber = False
for i in range(len(msg)):
    chunk = msg[i:i + 12]
    if isPhoneNumber(chunk):
        print("Phone number found: " + chunk)
        foundNumber = True
if not foundNumber:
    print("Counld not find the number.")
