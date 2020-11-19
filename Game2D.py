# 1  1  1  X  X  X  X
# 1  1  X  X  X  X  X
# 1  X  X  X  X  X  X
# X  X  X  X  X  X  1
# 1  1  1  X  X  1  1
# 1  1  1  X  1  1  1

def numberOfUpperCases(word1, word2):
    sum = 0
    for n in range(len(word1)):
        if word1[n] == word1[n].upper():
            sum += 1
    for n in range(len(word2)):
        if word2[n] == word2[n].upper():
            sum += 1
    return sum
word1 = input()
word2 = input()
result = numberOfUpperCases(word1, word2)
print(result)