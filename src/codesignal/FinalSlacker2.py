def finalSlacker2(weights, scores):
    grade = [0, 60, 70, 80, 90, 100]
    s1 = sum(scores[0]) / len(scores[0]) / 10 * weights[0]
    s2 = sum(scores[1]) / len(scores[1]) / 5 * weights[1]
    s3 = sum(scores[2]) / len(scores[2]) / 100 * weights[2]
    gradeIndex = 0
    while grade[gradeIndex + 1] < s1 + s2 + s3:
        gradeIndex += 1

    if gradeIndex == 4:
        r = 100
        while s1 + s2 + (sum(scores[2]) + r) / (len(scores[2]) + 1) / 100 * weights[2] >= 90:
            r -= 1
        return r + 1
    else:
        r = 0
        w = -1
        while r <= 100 and s1 + s2 + (sum(scores[2]) + r) / (len(scores[2]) + 1) / 100 * weights[2] < grade[gradeIndex + 1]:
            if s1 + s2 + (sum(scores[2]) + r) / (len(scores[2]) + 1) / 100 * weights[2] >= grade[gradeIndex]:
                gradeIndex += 1
                w = r
            r += 1
        if r > 100:
            return w
        else:
            return r

#weights = [25, 25, 50]
#scores = [[9,9,8,7,7,6,8,5,4,7,3], [3,3,2,3,1], [88,66,50]]
#weights = [10, 15, 75]
#scores = [[10,10,10,10,10,10,10,9,8,7], [5,5,5,5,5], [77,80,70,50]]
weights = [1, 1, 98]
scores = [[0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0], [69]]

print(finalSlacker2(weights, scores))