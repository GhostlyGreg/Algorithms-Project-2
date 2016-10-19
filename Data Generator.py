## Random Number Generator Script
## Change the name of the .txt file
## Change the second variable of range
## to fit your needs

import random
import math 

f = open( "data.txt", "w" )
for x in range(1, 70000):
    Y = math.log(x)/math.log(10)
    Z = x * Y / 480000
    f.write( str(Z) )
    f.write( "\n" )
f.close()
