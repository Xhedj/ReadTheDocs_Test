'''
m = "See you later in the city center"
c = "QSldSTQ7HkpIJj9cQBY3VUhbQ01HXD9VRBVYSkE6UWRQS0NHRVE3VUQrTDE="
'''
import string
"""
This here is an attempt to use Meet in the Middle attack to a cypher
"""
# E(k1 , m) = D(k2 , C)
alphabet = string.ascii_lowercase
print(len(alphabet))
lk1 = []
lk2 = []
for i in alphabet[0:25:]:
    for j in alphabet[1::]:
        for k in alphabet[2::]:
            for l in alphabet[3::]:
                key:str = i+j+k+l
                lk1.append(key)
                lk2 = lk1



