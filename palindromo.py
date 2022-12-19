#Write a function that will check whether ANY permutation of the characters of the input string is a palindrome. Bonus points for a solution that is efficient and/or that uses only built-in language functions. Deem yourself brilliant if you can come up with a version that does not use any function whatsoever.

#Crear dos for para, con el primero recorrer de izquierda a derecha y con el segundo de derecha a izquierda.

def permute_a_palindrome (input):
    convertido_en_cadena = list(input)
    num_items_uno = 0
    item = 0
    for item in convertido_en_cadena:
        if (convertido_en_cadena.count(item)) %2 == 0:
                num_items_uno += 1  
        elif (convertido_en_cadena.count(item)) == 1:
            return False                                
        else: 
            return False
    return True 





if __name__ == "__main__":
    print("Basic tests")
    assert permute_a_palindrome("a") == True
    assert permute_a_palindrome("aa") == True
    assert permute_a_palindrome("baa") == True
    assert permute_a_palindrome("aab") == True
    assert permute_a_palindrome("baabcd") == False
    assert permute_a_palindrome("racecars") == False

    assert permute_a_palindrome("abcdefghba") == False
    assert permute_a_palindrome("") == True