def summation(num):
    i = 0
    sumador = 0
    while i <= num:
        sumador = sumador + i
        i = i + 1 
        
    return sumador




if __name__ == "__main__":
    assert summation(1) == 1
    assert summation(8) == 36
    assert summation(22) == 253
    assert summation(100) == 5050
    assert summation(213) == 22791