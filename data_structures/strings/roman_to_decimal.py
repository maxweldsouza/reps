# done
# epi 7.9
# http://practice.geeksforgeeks.org/problems/roman-number-to-integer/0
# https://www.codewars.com/kata/51b6249c4612257ac0000005/solutions/python

def roman_to_decimal(roman):
    values = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    exceptions = { 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900 }
    result = 0

    i = 0
    while i < len(roman):
        if roman[i:i+2] in exceptions:
            result += exceptions[roman[i:i+2]]
            i += 2
        elif roman[i] in values:
            result += values[roman[i]]
            i += 1
    return result

print roman_to_decimal('DXXI')
print roman_to_decimal('CDXCIX')
print roman_to_decimal('XXIII')
