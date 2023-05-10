import matplotlib.pyplot as plt

Year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
Temp_index = [0.72, 0.61, 0.65, 0.68, 0.75, 0.90, 1.02, 0.93, 0.85, 0.99, 1.02]

plt.plot(Year, Temp_index)
plt.xlabel('Year')
plt.ylabel('Temp_index')
plt.title('Yearwise Global Temperature Index', {'fontsize':12,'horizontalalignment':'center'})
plt.show()
