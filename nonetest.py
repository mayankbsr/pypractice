xs = [()]                          # This initialises a list of empty tuples
print (type(xs))                   # list

res = [False] * 2                  # list of [False, False]
if xs:                             # list itself is not None
    print ("xs is not None")
    res[0] = True                  # so this gets set

if xs[0]:                          # but the first tuple is still None
    print (type(xs[0]), xs[0])     # tuple, ()
    res[1] = True                  # so this does not get set
else:
    print ("xs[0] is None")
    print (type(xs[0]), xs[0])

print (res)                        # [True, False]
