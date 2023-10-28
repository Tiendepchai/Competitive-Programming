from decimal import Decimal
import decimal

from math import floor, fmod

def recurring_decimal(numerator, denominator, k):
    return str((numerator/denominator)*10**k).split('.')[0][-1]

while True:
	a, b, k = map(int, input().split())

	print(recurring_decimal(a,b,k))