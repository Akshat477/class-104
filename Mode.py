import csv
from collections import Counter
from statistics import mode 

from cv2 import line
with open("SOCR-HeightWeight.csv",newline = "") as file : 
    data = csv.reader(file)
    file_data = list(data)
file_data.pop(0)
new_data = []    
for i in range(len(file_data)):
    Num = file_data[i][1] 
    new_data.append(float(Num))
N = Counter(new_data)
mode_range = {
    "50-60" : 0,
    "60-70" : 0,
    "70-80" : 0  
}
for h,o in N.items() : 
    if 50 < float(h)<60 : 
        mode_range["50-60"] += o
    elif 60 < float(h)<70 :
        mode_range["60-70"] += o
    elif 70 < float(h)<80 :
        mode_range["70-80"] += o       
mr,mo = 0,0
for r,o in mode_range.items() : 
    if o > mo : 
        mr,mo = [int(r.split("-")[0]),int(r.split("-")[1])],o 
mode = float((mr[0]+mr[1])/2) 
print(f"{mode:2f}")       