# ctci 16.8

from collections import OrderedDict

def english_int(n):
    d = OrderedDict()
    d[0] = 'zero'
    d[1] = 'one'
    d[2] = 'two'
    d[3] = 'three'
    d[4] = 'four'
    d[5] = 'five'
    d[6] = 'six'
    d[7] = 'seven'
    d[8] = 'eight'
    d[9] = 'nine'
    d[10] = 'ten'
    d[11] = 'eleven'
    d[12] = 'twelve'
    d[13] = 'thirteen'
    d[14] = 'fourteen'
    d[15] = 'fifteen'
    d[16] = 'sixteen'
    d[17] = 'seventeen'
    d[18] = 'eighteen'
    d[19] = 'nineteen'
    d[20] = 'twenty'
    d[30] = 'thirty'
    d[40] = 'forty'
    d[50] = 'fifty'
    d[60] = 'sixty'
    d[70] = 'seventy'
    d[80] = 'eighty'
    d[90] = 'ninety'

    if n in d:
        return d[n]

    tens = OrderedDict()
    tens[100] = 'hundred'
    tens[1000] = 'thousand'
    tens[100000] = 'million'

    for k, v in reversed(tens.items()):
        if n >= k:
            return english_int(n/k) + ' ' + v + ' ' + english_int(n - (n/k) * k)

    result = []
    for k, v in reversed(d.items()):
        if n == 0:
            break
        if k <= n:
            n = n - k
            result.append(v)

    return ' '.join(result)

print english_int(1001)
print english_int(567)
print english_int(69)
