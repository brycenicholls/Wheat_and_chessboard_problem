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


    if x > COAL:
        W_CO = x / COAL
        REM_CO = x % COAL
        W_CK = REM_CO / CK
        REM_CK = REM_CO % CK
        W_HOV = REM_CK / HOOVER
        REM_HOV = REM_CK % HOOVER
        W_ESB = REM_HOV / ESB
        REM_ESB = REM_HOV % ESB
        W_TIT = REM_ESB / TIT
        REM_TIT = REM_ESB % TIT
        W_TON  = REM_TIT / TON
        REM_TON = REM_TIT % TON
        W_KG = REM_TON / KG
        grain = REM_TON % KG
        print ("Tile ", n, " has ", int(W_CO), 'times the Coal Reserves of China in 2009,', int(W_CK),'Cubic Kilometer(s)',int(W_HOV), 'times Hoover Dam', int(W_ESB), 'times the weight of the Empire state building,', int(W_TIT), 'times the weight of the Titanic,', int(W_TON), 'Ton,', int(W_KG), 'KG and', grain, "grains")

    elif x > CK:
        W_CK = x / CK
        REM_CK = x % CK
        W_HOV = REM_CK / HOOVER
        REM_HOV = REM_CK % HOOVER
        W_ESB = REM_HOV / ESB
        REM_ESB = REM_HOV % ESB
        W_TIT = REM_ESB / TIT
        REM_TIT = REM_ESB % TIT
        W_TON  = REM_TIT / TON
        REM_TON = REM_TIT % TON
        W_KG = REM_TON / KG
        grain = REM_TON % KG
        print ("Tile ", n, " has ", int(W_CK),'Cubic Kilometer(s)',int(W_HOV), 'times Hoover Dam', int(W_ESB), 'times the weight of the Empire state building,', int(W_TIT), 'times the weight of the Titanic,', int(W_TON), 'Ton,', int(W_KG), 'KG and', grain, "grains")

    elif x > HOOVER:
        W_HOV = x / HOOVER
        REM_HOV = x % HOOVER
        W_ESB = REM_HOV / ESB
        REM_ESB = REM_HOV % ESB
        W_TIT = REM_ESB / TIT
        REM_TIT = REM_ESB % TIT
        W_TON  = REM_TIT / TON
        REM_TON = REM_TIT % TON
        W_KG = REM_TON / KG
        grain = REM_TON % KG
        print ("Tile ", n, " has ", int(W_HOV), 'times Hoover Dam', int(W_ESB), 'times the weight of the Empire state building,', int(W_TIT), 'times the weight of the Titanic,', int(W_TON), 'Ton,', int(W_KG), 'KG and', grain, "grains")
    elif x > ESB:
        W_ESB = x / ESB
        REM_ESB = x % ESB
        W_TIT = REM_ESB / TIT
        REM_TIT = REM_ESB % TIT
        W_TON  = REM_TIT / TON
        REM_TON = REM_TIT % TON
        W_KG = REM_TON / KG
        grain = REM_TON % KG
        print ("Tile ", n, " has ", int(W_ESB), 'times the weight of the Empire state building,', int(W_TIT), 'times the weight of the Titanic,', int(W_TON), 'Ton,', int(W_KG), 'KG and', grain, "grains")

    elif x > TIT:
        W_TIT = x / TIT
        REM_TIT = x % TIT
        W_TON  = REM_TIT / TON
        REM_TON = REM_TIT % TON
        W_KG = REM_TON / KG
        grain = REM_TON % KG
        print ("Tile ", n, " has ", int(W_TIT), 'times the weight of the Titanic,', int(W_TON), 'Ton,', int(W_KG), 'KG and', grain, "grains")
    elif x > TON:
        W_TON  = x / TON
        REM_TON = x % TON
        W_KG = REM_TON / KG
        grain = REM_TON % KG
        print ("Tile ", n, " has ", int(W_TON), 'Ton,', int(W_KG), 'KG and', grain, "grains")

    elif x > KG:
        kg = int(x/KG)
        grain = x%KG
        print ('Tile' , n ,'has', kg , 'KG and ' , grain , 'grains')
    else: print ('Tile',n,'has', x, 'grain')
    b = b + 1


