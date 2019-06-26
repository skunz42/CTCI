# CTCI Chapter 1

def isUnique(str1):
    strset = set()
    for s in str1:
        strset.add(s)

    return len(str1) == len(strset)

def checkPermutation(str1, str2):
    return False

def URLify(str, strLen):
    retStr = ""
    for i in range(0, strLen):
        if str[i] == " ":
            retStr += "%20"
        else:
            retStr += str[i]
    return retStr

def main():
    # IsUnique Test
    print(isUnique("yuh"))
    print(isUnique("cat"))
    print(isUnique("wow"))

    # URLify Test
    print(URLify("Mr John Smith  ", 13))
main()
