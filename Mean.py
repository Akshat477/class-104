import csv

from cv2 import line
with open("SOCR-HeightWeight.csv",newline = "") as file : 
    data = csv.reader(file)
    file_data = list(data)
file_data.pop(0)
new_data = []    
for i in range(len(file_data)):
    Num = file_data[i][1] 
    new_data.append(float(Num))
N = len(new_data)
total = 0
for x in new_data : 
    total += x 
mean = total/N
print(str(mean))                
