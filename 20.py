#bmi calculator engine
weight = int(input())
height = float(input())/100
bmi = weight/pow(height, 2)
print(round(bmi, 2))