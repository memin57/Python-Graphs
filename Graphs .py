import matplotlib.pyplot as plt
import random


def main():

    x = [0,1,2,3,4]
    y = [2,1,7,3,5]

    plt.title("Sales by Year")
    plt.xlabel("X cor")
    plt.ylabel("Y cor")

    plt.xticks([0,1,2,3,4],["2016","2017","2018","2019","2020"])
    plt.yticks([0,1,2,3,4,5,6,7],["0m$","1m$","2m$","3m$","4m$","5m$","6m$","7m$"])
    plt.plot(x,y)
    plt.show()


main()  


# PIE CHART

"""
def main():
    values = [10,20,70,40,80]
    adlar = ["1.","2.","3.","4.","5."]
    plt.title("Pie Chart")
    plt.pie(values,labels = values)
    plt.show()

main()    
"""

#BAR CHART 


"""
liste = []

for i in range(0,10):
    liste.append(random.randint(0,10))

x = [1,2,3,4,5,6,7,8,9,10]
plt.xlabel("Random Numbers")
plt.title("Bar Chart Of Random Numbers")
plt.bar(x,liste,color = ("g","b","y","r","k"))
plt.show()
"""
