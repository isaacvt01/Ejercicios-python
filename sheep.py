def count_sheeps(sheep):

    num_ovejas_true = 0
    item = 0
    for item in sheep:
        if item == True:
            num_ovejas_true += 1
        elif item == False:
            num_ovejas_true += 0            
    return num_ovejas_true 
        



array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]
              
assert count_sheeps(array1) == 17



















