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
new_data.sort()
if N % 2 == 0 : 
    median1 = float(new_data[N // 2 ])
    median2 = float(new_data[N //2 -1 ])
    median = (median1 + median2)/2
else :
    median = new_data[N // 2 ]
print(str(median))        