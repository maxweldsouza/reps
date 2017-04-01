# epi 17.2
# done http://practice.geeksforgeeks.org/problems/edit-distance/0

def initialize(width, height):
    result = []
    for i in xrange(width):
        result.append([0] * height)

    for i in xrange(width):
        result[i][0] = i
    for j in xrange(height):
        result[0][j] = j
    return result

def edit_distance(word1, word2):
    width = len(word1) + 1
    height = len(word2) + 1
    result = initialize(width, height)

    for i in xrange(1, width):
        for j in xrange(1, height):
            if word1[i-1] == word2[j-1]:
                result[i][j] = result[i-1][j-1]
            else:
                result[i][j] = min(result[i-1][j], result[i-1][j-1], result[i][j-1]) + 1
    return result[width-1][height-1]

print edit_distance('maxwell', 'kaxzell')
