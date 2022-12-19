def permute_a_palindrome (input):
    convertido_en_cadena = list(input)
    num_items_uno = 0
    item = 0
    for item in convertido_en_cadena:
        if num_items_uno < 1 and (convertido_en_cadena.count(item)) == 1:
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