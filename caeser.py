FIRST_CHAR_CODE = ord ('A')
LAST_UPPERCASE_CHAR_CODE = ord ('Z')
CHAR_CODE_RANGE = LAST_UPPERCASE_CHAR_CODE - FIRST_CHAR_CODE + 1

def caeser_encryption(message, shift):
    result = ""
    for i in message.upper():    
        if i.isalpha() :
            unicode = ord(i)
            new = unicode + shift
            if new > LAST_UPPERCASE_CHAR_CODE:
                new -= CHAR_CODE_RANGE 
            
            if new < FIRST_CHAR_CODE:
                new += CHAR_CODE_RANGE
            reverse = chr(new)
            result = result + reverse
        else:
            result += i    
    print(result)          

    
user_msg = input("Enter your message: ")
user_shift_key = int(input("Enter your shift key: "))

caeser_encryption(user_msg, user_shift_key)