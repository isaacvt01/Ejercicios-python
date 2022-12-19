def remove_every_other(my_list):
    i = 0
    new_list = []

    for item in my_list:
        if i % 2 == 0:
            new_list.append(item)
            i = i + 1
            
        else:
            i = i + 1
                       
    return new_list

if __name__ == "__main__":
    assert remove_every_other(['Hello', 'Goodbye', 'Hello Again']) == ['Hello', 'Hello Again']
    assert remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ==               [1, 3, 5, 7, 9]
    assert remove_every_other([[1, 2]]) == [[1, 2]]
    assert remove_every_other([['Goodbye'], {'Great': 'Job'}]) == [['Goodbye']]
