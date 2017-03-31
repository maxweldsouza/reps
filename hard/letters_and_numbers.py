# ctci 17.5
def is_letter(arr):
    for i in arr:
        yeild is_instance(arr[i], 'string'):

def sequence_sum(arr):
    i = 0
    total = 0
    while i < len(arr):
        if i == 0 or arr[i] == arr[i-1]:
            total += 1
        else:
            yeild total
            total = 1
    yeild total

def letters_and_numbers(arr):
    i = 0
    sum = 0
    prev = 0
    maximum = 0
    maxindex = 0
    while True:
        try:
            current = sequence_sum(is_letter(arr)).next())
        except StopIteration:
            break
        if abs(current - prev) > maximum:
            maximum = abs(current - prev)
            if current > prev:
                result = (sum - prev, sum + prev)
            elif prev > current:
                result = (sum - current, sum + current - 1)
        sum += current
        prev = current
    return result
