from math import sqrt

# prime function to check given number prime or not
def Prime(number, itr):  
    # base condition
    if itr == 1 or itr == 2:  
        return True
      # if given number divided by itr or not
    if number % itr == 0:  
        return False
      # Recursive function Call
    if Prime(number, itr - 1) == False:  
        return False

    return True

num = 13

itr = int(sqrt(num) + 1)

print(Prime(num, itr))