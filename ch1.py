# CTCI Chapter 1

# 1-1
def isUnique(str1):
    strset = set()
    for s in str1:
        strset.add(s)

    return len(str1) == len(strset)

# 1-2
def checkPermutation(str1, str2):
    return False

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
    count = {}
    retVal = ""
    newChar = str1[0]
    prevChar = str1[0]
    index = 0
    for s in str1:
        newChar = s
        if s in count:
            if newChar != prevChar:
                retVal += prevChar
                retVal += str(count[prevChar])
                prevChar = newChar
            else:
                count[newChar] += 1
        else:
            if newChar != prevChar:
                retVal += prevChar
                retVal += str(count[prevChar])
                prevChar = newChar
            count[newChar] = 1
            prevChar = newChar

        index += 1
        if index == len(str1)-1:
            last = str1[index]
            retVal += last
            counter = 0
            index2 = index
            char = last
            while (char == last):
                counter += 1
                index2 -= 1
                char = str1[index2]
            retVal += str(counter)
    return retVal

def main():
    # IsUnique Tests
    '''print(isUnique("yuh"))
    print(isUnique("cat"))
    print(isUnique("wow"))

    # URLify Tests
    print(URLify("Mr John Smith  ", 13))'''

    # One Away Tests
    '''print(oneAway('pale', 'ple'))
    print(oneAway('pales', 'pale'))
    print(oneAway('pale', 'bale'))
    print(oneAway('pale', 'bake'))
    print(oneAway('eee', 'ppp'))'''

    # String Compression Tests
    print(stringCompression('aabcccccaaa'))
main()
