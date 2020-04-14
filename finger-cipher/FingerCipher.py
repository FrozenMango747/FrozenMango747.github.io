deftable = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(48, 58)] + [i for i
                                                                                                                in
                                                                                                                '''.,’”!?/\ []{}()+-=_*~`><|$&@#^%∆√π~:;≠''']


# print(table)

def texor(a, b):
    return (a // 10 + b // 10) % 10 * 10 + (a + b) % 10  # all of the texor math in one line :)
    # adds the first digits together, mods by 10 --> x
    # adds second digits together, mods by 10 --> y
    # computes 10x+y


def texorSUB(a, b):
    return (a // 10 - b // 10) % 10 * 10 + (a - b) % 10  # all of the texor math in one line :)
    # adds the first digits together, mods by 10 --> x
    # adds second digits together, mods by 10 --> y
    # computes 10x+y


def nums(string,table):
    '''converts a string to numbers by referencing the encryption table'''
    return [table.index(i) for i in string]


def letters(numlist,table):
    '''converts a list of numbers to a list of chars by referencing table above'''
    return [table[num] for num in numlist]


def encrypt(pt, key,table):
    '''encrypts a string pt with a key of any length'''
    if len(pt) > len(key):  # if using keyword
        keyphrase = [key[i % len(key)] for i in range(len(pt))]  # repeat key as needed
    elif len(pt) < len(key):  # if using key
        keyphrase = key[:len(pt)]  # trim the key to length of plaintext
    else:
        keyphrase = key

    pt = nums(pt,table)  # convert to numbers that we can texor
    keyphrase = nums(keyphrase,table)
    ct = [texor(pt[i], keyphrase[i]) for i in range(len(pt))]  # zip up the two lists into one using texor

    return ''.join(letters(ct,table))  # we don't really want a list of numbers, so join it after converting to chars


def decrypt(pt, key,table):
    '''encrypts a string pt with a key of any length'''
    if len(pt) > len(key):  # if using keyword
        keyphrase = [key[i % len(key)] for i in range(len(pt))]  # repeat key as needed
    elif len(pt) < len(key):  # if using key
        keyphrase = key[:len(pt)]  # trim the key to length of plaintext
    else:
        keyphrase = key

    pt = nums(pt,table)  # convert to numbers that we can texor
    keyphrase = nums(keyphrase,table)
    ct = [texorSUB(pt[i], keyphrase[i]) for i in range(len(pt))]  # zip up the two lists into one using texor

    return ''.join(letters(ct,table))  # we don't really want a list of numbers, so join it after converting to chars

print(''.join(deftable))
