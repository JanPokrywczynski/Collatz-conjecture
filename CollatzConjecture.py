import matplotlib.pyplot as plt

def collatzConjecture(number):
    result=[]
    number=int(number)
    while(number!=1):
        if number%2==0:
            number//=2
        else:
            number=3*number+1
        result.append(number)
    return result

def showBarPlot(number): #shows how many steps it takes to reach 1 in range 1 to number in Bar chart
    number=int(number)
    names=[str(i) for i in range(1,number+1)]
    values=[len(collatzConjecture(i)) for i in range(1,number+1)]
    plt.bar(names, values, width=0.5)
    plt.ylabel("length")
    plt.xlabel("number")
    plt.autoscale(enable=True)
    plt.suptitle(f"Collatz conjecture - length from 1 to {number}")
    x0, xmax = plt.xlim()
    y0, ymax = plt.ylim()
    data_width = xmax - x0
    data_height = ymax - y0
    text = f"max value:\n  {values.index(max(values))+1}"
    plt.text(x0 + data_width, y0 + data_height, text, fontsize=8)
    plt.show()

def showNormalPlot(number): #shows how many step it takes to reach 1 in range 1 to number in Line chart
    number=int(number)
    names = [str(i) for i in range(1, number + 1)]
    values = [len(collatzConjecture(i)) for i in range(1, number + 1)]
    plt.plot(names, values)
    plt.suptitle("Collatz conjecture")
    plt.ylabel("length")
    plt.xlabel("number")
    x0, xmax = plt.xlim()
    y0, ymax = plt.ylim()
    data_width = xmax - x0
    data_height = ymax - y0
    text = f"max value:\n  {values.index(max(values))+1}"
    plt.text(x0 + data_width, y0 + data_height, text, fontsize=8)
    plt.show()

def showPointPlot(number):
    number=int(number)
    names = [str(i) for i in range(1, number + 1)]
    values = [len(collatzConjecture(i)) for i in range(1, number + 1)]
    plt.plot(names,values, "ro", markersize=2)
    plt.show()

def showNumberPlot(number): #shows every value number reaches in Collatz conjecture until it reaches 1
    values=collatzConjecture(number)
    names=[str(i) for i in range(1, len(values)+1)]
    plt.plot(names, values, 'r-o')
    plt.suptitle(f"Collatz conjecture - number {number}")
    plt.ylabel("number")
    plt.xlabel("step")
    x0, xmax=plt.xlim()
    y0, ymax=plt.ylim()
    data_width=xmax-x0
    data_height=ymax-y0
    text=f"steps: {len(values)}\nmax value: {max(values)}"
    plt.text(x0+data_width,y0+data_height, text, fontsize=8)
    plt.show()

x=input()
# showBarPlot(x)
# showNormalPlot(x)
showPointPlot(x)
# showNumberPlot(x)

