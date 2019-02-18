def areSimilar(a, b):
    da = []
    db = []
    for i,n in enumerate(a):
        if a[i] != b[i]:
            da.append(a[i])
            db.append(b[i])
    
    return len(da) <= 2 and len(db) <= 2 and sorted(da) == sorted(db) 

a = [1, 1, 4]
b = [1, 2, 3]
print(areSimilar(a,b))