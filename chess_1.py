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
b = 26

while b <= 64:
    tile = add(b, 1)
    grain = power(2, b)
    kg = 50000
    ton = mult(kg, 1000)
    titanic = mult(ton, 52000)
    empire = mult(ton, 365000)
    hoover = mult(ton, 6600000)
    cubic = mult(ton, 1000000000)
    coal = mult(ton, 1730000000)
    w_kg = int(div(grain, kg))
    r_kg_grain = int(mod(grain, kg))
    w_ton = div(grain, ton)
    r_ton_grain = mod(grain, ton)
    w_titanic = div(grain, titanic)
    r_titanic_grain = mod(grain, titanic)
    w_empire = div(grain, empire)
    r_empire_grain = mod(grain, empire)
    w_hoover = div(grain, hoover)
    r_hoover_grain = mod(grain, hoover)
    w_cubic = div(grain, cubic)
    r_cubic_grain = mod(grain, cubic)
    w_coal = div(grain, coal)
    r_coal_grain = mod(grain, coal)
    message_1 = f'Tile {tile} = {r_kg_grain} grain.'
    message_2 = f'Tile {tile} = {int(w_kg)} Kilograms and {r_kg_grain}'
    message_3 = f'Tile {tile} = {int(w_ton)} Ton, {message_2[10:]}'
    message_4 = f'Tile {tile} = {int(w_titanic)} Titanic, {message_3[10:]}'
    message_5 = f'Tile {tile} = {int(w_empire)} Empire State Building, {message_4[11:]}'
    message_6 = f'Tile {tile} = {int(w_hoover)} Hoover Dam, {message_5[11:]}'
    message_7 = f'Tile {tile} = {int(w_cubic)} Cubic Kilometers, {message_6[11:]}'
    message_8 = f'Tile {tile} = {int(w_coal)} Coal Reserves of China in 2009, {message_7[11:]}'
    if grain > coal:
        w_kg = int(div(grain, kg))
        r_kg_grain = int(mod(grain, kg))
        print(message_8)
    elif grain > cubic:
        print(message_7)
    elif grain > hoover:
        print(message_6)
    elif grain > empire:
        print(message_5)
    elif grain > titanic:
        print(message_4)
    elif grain > ton:
        print(message_3)
    elif grain > kg:
        print(message_2)
    else:
        print(message_1)
    b += 1
