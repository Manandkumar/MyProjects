alpha =["a","n","a","n"]
alpha.append("d")
alpha=alpha+["d"," ", "K"]
print(alpha)
d_index =alpha.index("d")
del alpha[d_index]
print(alpha)


print(alpha.remove("a"))