from reverseint import Solution
s = Solution()

def test1():
    assert s.reverse(123) == 321

def test2():
    assert s.reverse(-123) == -321

def test3():
    assert s.reverse(320) == 23
