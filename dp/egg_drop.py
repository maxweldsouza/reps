# http://www.geeksforgeeks.org/dynamic-programming-set-11-egg-dropping-puzzle/
# done

cache = {}

def egg_drop(eggs, floors):
    if (eggs, floors) in cache:
        return cache[(eggs, floors)]

    if eggs == 0:
        result = 0
    elif eggs == 1:
        return floors
    elif floors == 0:
        result = 0
    elif floors == 1:
        result = 1
    else:
        result = min([1 + max(egg_drop(eggs - 1, i-1), egg_drop(eggs, floors - i)) for i in range(1, floors)])
    cache[(eggs, floors)] = result
    return result

print egg_drop(2, 10)
print egg_drop(2, 36)
