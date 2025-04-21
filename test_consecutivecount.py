from consecutivecount import longest_consecutive

numbers = [100, 4, 200, 1, 3, 2,  4, 5, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18]
print ("printing")

def test1():
    #numbers = [100, 4, 200, 1, 3, 2,  4, 5, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    assert longest_consecutive(numbers) == 9

def test2():
    #numbers = [100, 4, 200, 1, 3, 2,  4, 5, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    assert longest_consecutive(numbers) == 6

def test3():
    assert longest_consecutive(numbers) == 4
