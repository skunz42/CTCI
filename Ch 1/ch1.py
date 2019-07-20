# CTCI Chapter 1

# 1-1
def isUnique(str1):
    strset = set()
    for s in str1:
        strset.add(s)

    return len(str1) == len(strset)

# 1-2
def checkPermutation(str1, str2):
    sortStr1 = sorted(str1)
    sortStr2 = sorted(str2)
    return sortStr1 == sortStr2

# 1-3
def URLify(str, strLen):
    retStr = ""
    for i in range(0, strLen):
        if str[i] == " ":
            retStr += "%20"
        else:
            retStr += str[i]
    return retStr

# 1-5
def oneAway(str1, str2):
    retVal = True
    difference = 0
    i = 0
    j = 0

    if abs(len(str1)-len(str2)) > 1:
        retVal = False
    else:
        while (difference < 2 and i < len(str1) and j < len(str2)):
            if str1[i] != str2[j]:
                difference += 1
                if str1[i+1] == str2[j]:
                    i+=1
                elif str1[i] == str2[j+1]:
                    j+=1
            i+=1
            j+=1

        if difference >= 2:
            retVal = False

    return retVal

# 1-6
def stringCompression(str1):
    retVal = ""
    newChar = str1[0]
    prevChar = str1[0]
    count = 0
    for idx, s in enumerate(str1):
        newChar = s
        if newChar != prevChar:
            retVal += prevChar
            retVal += str(count)
            count = 1
        else:
            count += 1

        if idx == len(str1)-1:
            retVal += newChar
            retVal += str(count)

        prevChar = newChar

    return retVal

#1-7
def rotateMatrix(n, mat):
    retMat = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            retMat[n-j-1][i] = mat[i][j]

    return retMat

#1-8
def zmHelper(m, n, s, t, mat):
    for i in range(m):
        for j in range(n):
            if i == s or j == t:
                mat[i][j] = 0

def zeroMatrix(m, n, mat):
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                zmHelper(m, n, i, j, mat)

    return mat

def swapInPlace(a, b):
    print(str(a) + " " + str(b))
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(str(a) + " " + str(b))

def main():
    # IsUnique Tests
    '''print(isUnique("yuh"))
    print(isUnique("cat"))
    print(isUnique("wow"))'''

    # checkPermutation Tests
    #print(checkPermutation('dog', 'god'))

    # URLify Tests
    #print(URLify("Mr John Smith  ", 13))'''

    # One Away Tests
    '''print(oneAway('pale', 'ple'))
    print(oneAway('pales', 'pale'))
    print(oneAway('pale', 'bale'))
    print(oneAway('pale', 'bake'))
    print(oneAway('eee', 'ppp'))'''

    # String Compression Tests
    # print(stringCompression('aabcccccaaa'))

    # rotateMatrix Tests
    # print(rotateMatrix(3, [[1, 3, 7], [5, 4, 2], [9, 8, 6]]))

    # zeroMatrix Tests
    # print(zeroMatrix(2, 3, [[1, 3, 5], [2, 4, 0]]))

    # Swap in Place
    swapInPlace(2, 7)
main()
