#!/usr/bin/env python
# -*- coding: utf-8 -*-


def nwd(x, y):

    if x == y:
        return x

    if x > y:
        x, y = y, x

    while x != 0:
        x, y = y % x, x
    return y

    print(nwd(654188429 * 17, 17))  # 17 - 654188429 jest pierwsza
    print(nwd(654188429, 17))  # 1 - obydwie pierwsze


def main(args):
    a = int(input("Podaj liczbę: "))
    b = int(input("Podaj liczbę: "))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
