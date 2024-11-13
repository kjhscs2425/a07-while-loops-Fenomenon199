# write a factorial function, given n, you return n!
def function(n): 
    counter=1 
    product=1 
    while counter < n:
        product=product*counter 
        counter=counter+1
    return product*counter 
print(function(5))
