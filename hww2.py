import csv
from collections import Counter
from typing import Text
from matplotlib import pyplot as plt
import pandas as pd

#Top 5 arabica coffee producing countries
with open('Coffee-modified.csv') as csv_file:
    read=csv.DictReader(csv_file)
    country=Counter()
    for row in read:
        country.update([row['Country.of.Origin']])
print("country=", country)

origin = []
count = []
for i in country.most_common(5):
    origin.append(i[0])
    count.append(i[1])
print(origin)
print(count)

plt.suptitle("Top 5 Most Common Coffee Origins")
plt.title("The dataset is made up of Arabica coffee beans reviewed by the Coffee Quality Institute", fontsize=8)
slices = count
labels = origin
colors=['#A8FF33', '#33FFDA','#FFE633','#337AFF', '#A833FF']
plt.pie(slices, labels=labels, startangle=90, colors=colors, autopct='%1.1f%%', wedgeprops={'edgecolor':'black'})
plt.show()
#Stacked bar chart of coffee exports vs product in top 5 producing countries 
x = []
y = []
y1 = []
with open('total-production.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
            x.append(row[0])
            y.append(row[1])
            y1.append(row[2])
labels = ['Brazil', 'Vietnam', 'Colombia', 'Indonesia', 'Honduras', 'Ethiopia']
exports_2018 = [35382, 27888, 13824, 4539, 3122, 3589]
production_2018 = [62925, 31174, 13858, 9418, 7560, 7475]
fig, ax = plt.subplots()
ax.bar(labels, exports_2018, width = 0.3, color = '#7D3C98', label='Exports')
ax.bar(labels, production_2018, width = 0.3, color = '#D35400', bottom=exports_2018,
       label='Production')
plt.xlabel('Exporting Country', fontsize = 9)
plt.ylabel('Coffee Exports in thousands of 60-kg bags', fontsize = 9)
plt.title("The dataset is made up of top the top 5 coffee producing countries worldwide", fontsize=8)
plt.suptitle('Coffee Production vs Exports in 2018')
plt.grid()
plt.legend()
plt.xticks(rotation = 45, fontsize = 5)
plt.show()

#extra graphs I didn't use

# x = []
# y = []
# y1 = []
# with open('total-production.csv','r') as csvfile:
#     lines = csv.reader(csvfile, delimiter=',')
#     for row in lines:
#             x.append(row[0])
#             y.append(row[1])
#             y1.append(row[2])

# ax1 = plt.gca()
# ax1.scatter(x, y, color = '#7D3C98', marker = 'o',label = "Exports")
# ax1.scatter(x, y1, color = '#D35400', marker = 'o',label = "Total Production")
# plt.xticks(rotation = 90, fontsize = 5)
# plt.yticks(fontsize = 5)
# plt.xlabel('Exporting Country')
# plt.ylabel('Coffee Exports in thousands of 60-kg bags')
# plt.title('Coffee Production vs Exports in 2018', fontsize = 22)
# plt.grid()
# plt.legend()
# plt.show()
'''
with open('netflix_titles.csv') as csv_file:
    read=csv.DictReader(csv_file)
    duration=Counter()
    for row in read:
        duration.update([row['duration']])
print("duration=", duration)

time = []
count = []
for i in duration.most_common(10):
    time.append(i[0])
    count.append(i[1])
print(time)
print(count)

plt.bar(time, count, color='green')
plt.xlabel("Duration/Runtimes")
plt.ylabel("Count")
plt.title("Most Frequent Runtimes for Netflix Shows")
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
plt.show()
'''
'''
x = []
y = []
y1 = []

with open('total-production.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
            x.append(row[0])
            y.append(row[1])
            y1.append(row[2])

print(x)
print (y)
print(y1)

plt.plot(x, y)
plt.plot(y1)

plt.show()
'''

# ax1 = plt.gca()
# ax1.scatter(x, y, color = '#7D3C98', marker = 'o',label = "Exports")
# ax1.scatter(x, y1, color = '#D35400', marker = 'o',label = "Total Production")
# plt.xticks(rotation = 90, fontsize = 5)
# plt.yticks(fontsize = 5)
# plt.xlabel('Exporting Country')
# plt.ylabel('Coffee Exports in thousands of 60-kg bags')
# plt.title('Coffee Production vs Exports in 2018', fontsize = 22)
# plt.grid()
# plt.legend()
# plt.show()


# x = []
# y = []
# with open('total_exports2018.csv','r') as csvfile:
#     lines = csv.reader(csvfile, delimiter=',')
#     for row in lines:
#             x.append(row[0])
#             y.append(row[1])
# print(x)
# print(y)

# x1 = []
# y1 = []
# with open('total_production2018.csv','r') as csvfile:
#     lines = csv.reader(csvfile, delimiter=',')
#     for row in lines:
#             x1.append(row[0])
#             y1.append(row[1])
# print(x1)
# print(y1)

# ax1 = plt.gca()
# ax1.scatter(x, y, color = '#7D3C98', marker = 'o',label = "Exports")
# ax1.scatter(x1, y1, color = '#D35400', marker = 'o',label = "Total Production")
# plt.xticks(rotation = 90, fontsize = 5)
# plt.yticks(fontsize = 5)
# plt.xlabel('Exporting Country')
# plt.ylabel('Coffee Exports in thousands of 60-kg bags')
# plt.title('Coffee Production vs Exports in 2018', fontsize = 22)
# plt.grid()
# plt.legend()
# plt.show()

'''
exports=[]
with open('exports-calendar-year.csv') as csv_file:
    read=csv.DictReader(csv_file)
print("exports=", exports)

time = []
count = []
for i in exports:
    time.append(i[0])
    count.append(i[1])
print(time)
print(count)
'''


