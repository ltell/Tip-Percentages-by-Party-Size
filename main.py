import csv
import numpy as np
import matplotlib.pyplot as plt

with open("tips.csv", "r") as file:
  data = csv.reader(file,delimiter=",")
  headers = next(data)
  data_list = list(data)
  data_numpy = np.array(data_list)

size = data_numpy[:,6]
# select every row (:), and grabbing index position 1. CSV file is string so convert to float in order to perform calculations.
tips = np.array(data_numpy[:,1], dtype=float)

# select every row (:), and grab the 0 position index, which will pull the "total_bill" values from the dataset.
bills = np.array(data_numpy[:,0], dtype=float)
tip_percentages = (tips/bills)
# print(tips_percentage)

print(f"The average bill amount is ${round(np.mean(bills), 2)}")
print(f"The median bill amount is ${round(np.median(bills), 2)}")
print(f"The smallest bill is ${round(np.min(bills), 2) }")
print(f"The largest bill is ${round(np.max(bills), 2)}")

plt.scatter(size, tip_percentages, color="orange")
plt.xlabel("Dinner Party Size")
plt.ylabel("Tip Percentage")
plt.title("Tip Percentages by Party Size")
plt.savefig("tip_percentages.png")