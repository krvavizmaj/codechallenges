def pinPadDiscovery(logins):
    
    result = ""
    for j in range(0, 4):
        o = [0 for _ in range(10)]
        digit = ""
        for i in range(len(logins)):
            o[int(logins[i][j][0])] += 1
            o[int(logins[i][j][1])] += 1
        
        numberOf4 = 0
        for i,d in enumerate(o):
            if d == len(logins):
                numberOf4 += 1
                digit += str(i)
        if numberOf4 == 1:
            result += digit
        else:
            result += "?"


    return result

logins = [
    ["18","18","24","09"], 
    ["18","18","02","69"], 
    ["18","18","26","59"], 
    ["18","18","25","39"], 
    ["18","18","24","69"]
]
print(pinPadDiscovery(logins))