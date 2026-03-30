dict2={"Alice":80,"Bob":79,"charlie":85,"Bob":100}
print(dict2)
dict2["Daniel"]=87
print(dict2)

dict2["Charlie"]=95
print(dict2)

dict2["charlie"]=95
print(dict2)

del dict2["Charlie"]
print(dict2)
dict2.up