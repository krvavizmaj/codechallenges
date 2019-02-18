def boxBlur(image):
    newImage = [[0 for _ in range(len(image[0]) - 2)] for _ in range(len(image) - 2)]
    for i in range(1, len(image)-1):
        for j in range(1, len(image[0])-1):
            p = image[i-1][j-1] + image[i-1][j] + image[i-1][j+1] + image[i][j-1] + image[i][j] + image[i][j+1] + image[i+1][j-1] + image[i+1][j] + image[i+1][j+1]
            newImage[i-1][j-1] = p // 9

    return newImage

image = [[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]
print(boxBlur(image))