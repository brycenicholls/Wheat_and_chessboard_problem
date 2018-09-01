#!/usr/bin/env python3

# second version
# need to workout the maths behind the variable assignments.

# define functions below


def add(x, y):
    """add"""
    return x + y


def sub(x, y):
    """subtract"""
    return x - y


def div(x, y):
    """divide"""
    return x / y


def mult(x, y):
    """multiply"""
    return x * y


def mod(x, y):
    """remainder"""
    return x % y


def power(x, y):
    """exponentiation"""
    return x ** y


# assign variables


a = 0
b = 16


while b <= 16:
    tile = add(b, 1)
    grain = power(2, b)
    kg = 50000
    ton = add(kg, 1000)
    titanic = add(ton, 52000)
    empire = add(ton, 365000)
    hoover = add(ton, 6600000)
    cubic = add(ton, 1000000000)
    coal = add(ton, 1730000000)
    message_1 = f'Tile {tile} has {grain} grain.'
    message_2 = f'Tile {tile} has {kg} Kilograms {message_1[11:]}'
    message_3 = f'Tile {tile} has {ton} Ton {message_2[11:]}'
    message_4 = f'Tile {tile} has {titanic} Size of the Titanic {message_3[11:]}'
    message_5 = f'Tile {tile} has {empire} Size of the Empire State Building {message_4[11:]}'
    message_6 = f'Tile {tile} has {hoover} Size of Hoover Dam {message_5[11:]}'
    message_7 = f'Tile {tile} has {cubic} Cubic Kilometers {message_6[11:]}'
    message_8 = f'Tile {tile} has {coal} times the Coal Reserves of China in 2009 {message_7[11:]}'
    if grain > coal:
        print(message_8)
    else:
        print(message_1)
    if grain > cubic:
        print(message_7)
    else:
        print(message_1)
    if grain > hoover:
        print(message_6)
    else:
        print(message_1)
    if grain > empire:
        print(message_5)
    else:
        print(message_1)
    if grain > titanic:
        print(message_4)
    else:
        print(message_1)
    if grain > ton:
        print(message_3)
    else:
        print(message_1)
    if grain > kg:
        kg = grain / kg
        grain = grain % kg
        print(message_2)
    else:
        print(message_1)
    b += 1
