import os

print(os.getcwd())
os.chdir("//Users/arun//")
print(os.getcwd())


def perm(l):
# Compute the list of all permutations of l
    if len(l) <= 1:
        return [l]
    r = []
    for i in range(len(l)):
        s = l[:i] + l[i + 1:]
        p = perm(s)
        for x in p:
            r.append(l[i:i + 1] + x)
    return r

print(perm("arun"))

