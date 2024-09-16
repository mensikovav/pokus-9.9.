def prumer(s):
    "vrací aritmetický průměr"
    if (len(s)==0): 
        return None
    suma = 0
    for i in s:
        suma+=i
    return (suma/len(s))

print(prumer([1,2,6]))