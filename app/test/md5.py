"""
# Python 3 code to demonstrate the
# working of MD5 (string - hexadecimal)

import hashlib

# initializing string
str2hash = "GeeksforGeeks"

#encoding GeeksforGeeks using encode()
#then sending to md5()
result = hashlib.md5(str2hash.encode()).hexdigest()

#printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end="")
print(result)
A = result.hexdigest()
print(A, ": A")
"""
"""
import hashlib
str2hash = "GeeksforGeeks"
result = hashlib.md5(str2hash.encode()).hexdigest()
print(result)
"""
import hashlib

class Md5():
    @staticmethod
    def md5sum_file(filepath):
        return hashlib.md5(open(filepath, 'rb').read()).hexdigest()

