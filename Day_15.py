# Day_15 : Check whether two string are isomorphic. Note : Two strings are isomorphic if one-to-one mapping is possible for every character of first 
# string to every character of second string while preserving the orders of the characters.

def checksIsomorphism(s1, s2):
    a = set()
    b = set()
    if len(s1) == len(s2):
        for i in range(len(s1)):
            a.add(s1[i])
            b.add(s2[i])
        if len(a) == len(b):
            return True
        else:
            return False
    else:
        return False
    
string1 = input("Enter the first string : ")
string2 = input("Enter the second string : ")
ans = checksIsomorphism(string1, string2)
print(ans)