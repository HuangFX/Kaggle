import csv
from matplotlib import pyplot as plt

filename = 'train.csv'
surviveds=[]
age=[]
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)
    for index ,cloum_num in enumerate(header_row):
        print index,":",cloum_num
    for row in reader:
        if row[1]=="1":
            try:
                intage=int(row[5])
                age.append(intage)
            except ValueError:
                pass

    fig = plt.figure(dpi=128,figsize=(10,6))
    plt.plot(age,c="red")
    plt.title("surviveds age")
    plt.xlabel("",fontsize=16)
    plt.ylabel("age",fontsize=16)

    plt.show()
