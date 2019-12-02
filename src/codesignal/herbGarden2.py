import bisect
import math

def herbGarden(plants, days):
    identy = tuple(sorted(plants)+[days])
    return H(identy)

D = {}    
def H(identy):
    if identy in D:
        return D[identy]
    
    days = identy[-1]
    if days == 1:
        D[identy] =  math.floor(max(identy[:-1])/2)
    else:
        ls = []
        run = set(i for i in sorted(set(identy[:-1]))[:-2])
        
        for n,i in enumerate(identy[:-1]):
            if i not in run:
                run.add(i)
                plantsNew = list(identy)
                plantsNew.pop()
                i = plantsNew.pop(n)
                l = math.floor(i/2)
                bisect.insort(plantsNew,i-l)
                plantsNew = [m+2 for m in plantsNew]
                ls += l + H(tuple(plantsNew+[days-1])),
        D[identy] = max(ls)
    return D[identy]

plants = [8, 7, 99]
days = 16
print(herbGarden(plants, days))