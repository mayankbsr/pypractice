mytpl = (1, 5, 12, 15, 6, 4, 3)
print (mytpl)

empty_tpl = ()

def replace_max(tpl):
    print (type(tpl))
    m = max(tpl)
    idx = tpl.index(m)
    return tpl[:idx] + (None,) + tpl[idx + 1:]   # (None,) creates another tuple so concatenation works

print(type(replace_max(mytpl)), replace_max(mytpl))
print(replace_max(empty_tpl))
