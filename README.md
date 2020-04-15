# Password Creation
    Helps create random passwords
    
# randomPasswdMix(length)
    This is the creation of a password with lowercase, uppercase, numbers, select punctuation.
    length defines the total length of the password created.
    for example if you put in 20 might get something like: 5z.5#4idi)vy2EDEZy01
    
# randomPasswd(length)
    Does the same as randomPasswdMix but doesn't add in the select punctuation within the password.
    for example if you put in 20
    might get something like: 9tLaQNNA4abV8CVU53F3
    
# randomWordPasswd(mix, leet)
    What this creates is a password with a random word from the word_alpha wordlist.
    mix defines the total amount of words from the wordlist to pick
    leet defines weather or not to use leet speak rather than normal text. Takes a True or False
    Returns something like : [2 words and leet enabled] : b13ns34nc3m3rcur13s
    Returns something like : [2 words and leet disabled] : ranchconspiratress
    
# twoFactor(mix)
    Takes a mix which takes a True or False statement
    Creates a 6 long characters
    For example twoFactor(True) returns: 0pkGfz
    For example twoFactor(False) returns: 038781
    
