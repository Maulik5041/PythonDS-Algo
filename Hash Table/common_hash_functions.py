"""Common hash functions in modern programming"""


# Arithmetic Modular: key MOD size of list
def hash_modular(key, size):
    return key % size


lst = [None] * 10
key = 35
index = hash_modular(key, len(lst))
print(f"The index for key {str(key)} is {str(index)}")


# Truncation: key MOD 1000
def hash_truncation(key):
    return key % 1000


key = 123456
index = hash_truncation(key)
print(f"The index for key {str(key)} is {str(index)}")


# Folding: Dividing a key in smaller chunks and then adding those chunks
def hash_fold(key, chunck_size):
    str_key = str(key)
    print(f"Key: {str_key}")
    hash_val = 0
    print("Chunks: ")

    for i in range(0, len(str_key), chunck_size):
        if (i + chunck_size < len(str_key)):
            print(str_key[i: i + chunck_size])
            hash_val += int(str_key[i: i + chunck_size])
        else:
            print(str_key[i:len(str_key)])
            hash_val += int(str_key[i:len(str_key)])
    return hash_val


key = 34567989
chunck_size = 2
print(f"Hash Key: {str(hash_fold(key, chunck_size))}")
