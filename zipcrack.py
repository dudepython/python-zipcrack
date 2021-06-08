import itertools
import time
import zipfile
start = time.time()

def permutation_with_repeats(seq, key):
    """ 
    generator that produces all permutations of length key 
    of the elements in  seq.
    seq = list('abc'); key = 4
    >>> aaaa aaab aaac aaba aabb aabc aaca aacb...
    seq = list('abcdefghijklmnopqrstuvwzyz'); key = 2
    >>> aa ab ac ad ae af ag ah ai aj ak al...
    """
    for _ in  itertools.product(seq, repeat=key):
        yield ''.join(_)

seq = list('abcdefghijklmnopqrstuvwxyz1234567890')
key = 1
zip_file = str(input("enter file name with extension (file must be in same location as code)"))
cnt=0 
f = open("passgen.txt", "w")
a = permutation_with_repeats(seq, key) # seq and key of arbitrary size > 0
pguess = str("")
obj = zipfile.ZipFile(zip_file)
while key<= 7:
    while True:
        try:
            pguess = (next(a))
            cnt+=1
            try:
                obj.extractall(pwd=pguess.encode())
                print (pguess)
                print("Password found at try ", cnt)
                print("Password is", pguess)
            except:
                continue
                

        except StopIteration:
            key+=1
            print("key is now",key,)
            end = time.time()
            print ("time took for generation =",end-start)
            a = permutation_with_repeats(seq, key)
            break


end = time.time()
print ("time took for generation =",end-start)
print(pguess)

print("no of permutaions generated =",cnt)
f.close() 
