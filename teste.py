import matplotlib.pyplot as plt

year = [1998, 2000, 2002]
gdp = [1.0, 2.0, 3.0]

plt.plot(year, gdp, color = 'red')
plt.scatter(year, gdp, color = 'green')

plt.xticks([1998, 1999, 2000, 2001, 2002])
plt.yticks([1.0, 1.5, 2.0, 2.5, 3.0],
           ['1.0$', '1.5$', '2.0$', '2.5$', '3.0$'])
plt.xlabel('Year')
plt.ylabel('GDP')
plt.title('GDP x Yea')
plt.show()
