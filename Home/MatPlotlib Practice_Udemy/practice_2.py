import matplotlib.pyplot as plt

Month = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
Customer1 = [12, 13, 9, 8, 7, 8, 8, 7, 6, 5, 8, 10]
Customer2 = [14, 16, 11, 7, 6, 6, 7, 6, 5, 8, 9, 12]


# Line graph
# plt.plot(Month, Customer1, color='red', label='Customer1', marker='o')
# plt.plot(Month, Customer2, color='blue', label='Customer2', marker='^')
# plt.xlabel('Month')
# plt.ylabel('Electricity Consumption')
# plt.title('Power Consumption for this Year')
# plt.legend(loc='upper center')
# plt.show()


# Multiple graphs separately in the same window
# plt.subplot(1, 2, 1)    #row no., col no., no. of graphs
# plt.plot(Month, Customer1, color='red', label='Customer1', marker='o')
# plt.xlabel('Month')
# plt.ylabel('Electricity Consumption')
# plt.title('Power Consumption of building-1 for this Year')

# plt.subplot(1, 2, 2)    #row no., col no., no. of graphs
# plt.plot(Month, Customer2, color='blue', label='Customer2', marker='^')
# plt.xlabel('Month')
# plt.ylabel('Electricity Consumption')
# plt.title('Power Consumption of building-2 for this Year')

# plt.show()


# Scatter plot
# plt.scatter(Month, Customer1, color='orange', label='Customer-1')
# plt.scatter(Month, Customer2, color='blue', label='Customer-2')
# plt.xlabel('Month')
# plt.ylabel('Electricity Consumption')
# plt.title('Scatter Plots of Power Consumption')
# plt.grid()
# plt.legend(loc='upper center')
# plt.show()


# Histogram
# plt.hist(Customer1, bins=40, color='green')
# plt.xlabel('Month')
# plt.ylabel('Electricity Consumption')
# plt.title('Histogram of Power Consumption')
# plt.show()


# Bar charts
plt.bar(Month, Customer1, width=0.3, color='red')
plt.show()

