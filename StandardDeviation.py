import math
import csv

with open('data.csv', newline = '')as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

 #calculating the mean
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/n
    return mean

 #subtract each number with mean and then square each number
squared_list = []
for number in data:
    a = int(number)-mean(data)
    a = a**2
    squared_list.append(a)

 #calculate the sum of all the squared numbers
sum = 0
for i in squared_list:
    sum = sum + i

 #divide the result with n - 1
result = sum/(len(data)-1)

 #calculate the standard deviation by appplying the sqaure root to the result
standard_deviation = math.sqrt(result)
print(standard_deviation)