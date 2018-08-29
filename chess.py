#!/usr/bin/env python3
#

#
a = 0
b = 1

print('Tile 1 has 1 grain')
while b <= 64:
    n = b+1
    x = 2 ** b
    KG = 50000
    TON = KG * 1000
    TIT = TON * 52000
    ESB = TON * 365000
    HOOVER = TON * 6600000
    CK = TON * 1000000000
    COAL = TON * 1730000000


    if x > TON:
        whole = x-KG/TON
        remainder = x%KG/TON
        print ("Tile " , n , " has " , whole , 'Tons,' , remainder , 'KG')

    elif x > KG:
        kg = int(x/KG)
        grain = x%KG
        print ('Tile' , n ,'has', kg , 'KG and ' , grain , 'grain')
    else: print ('Tile',n,'has', x, 'grain')
    b = b + 1
