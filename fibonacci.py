fib = [0, 1]

for i in range(5):
    #print ('range {0}, fib[-1] = {1}, fib[-2] = {2}'.format(i, fib[-1], fib[-2]))
    fib.append(fib[-1] + fib[-2])

#for n in fib:
#    print (str(n))

print (', '.join(str(e) for e in fib))
