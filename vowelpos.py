def solution(s):
    print (s, len(s))
    vowelpos = []
    vowels = ["A", "E", "I", "O", "U"]
    for i in range(len(s)):
        print(i, s[i])
        if s[i].upper() in vowels:
            vowelpos.append(i)
    return vowelpos

print (solution("hello"))
