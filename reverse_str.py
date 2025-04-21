s = bytes("my dog has fleas", encoding="utf8")
for n in range(len(s)):
    s[n] = chr(s[n])
print (s)
