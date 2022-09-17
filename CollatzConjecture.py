import matplotlib.pyplot as plt

def collatzConjecture(number):
    if number<=0:
        return []
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
    values = [len(collatzConjecture(i)) for i in range(0, number + 1)]
    #plt.plot(names, values)
    plt.plot(values,  "b-o", markersize=2, linewidth=0.5)
    plt.suptitle(f"Collatz conjecture\n0 - {number}")
    plt.ylabel("length")
    plt.xlabel("number")
    x0, xmax = plt.xlim()
    y0, ymax = plt.ylim()
    data_width = xmax - x0
    data_height = ymax - y0
    text = f"  longest sequence: {max(values)}\n  for number: {values.index(max(values))}"
    plt.text(x0 + data_width, y0 + data_height, text, fontsize=8)
    plt.show()

def showPointPlot(number):
    number=int(number)
    names = [str(i) for i in range(1, number + 1)]
    values = [len(collatzConjecture(i)) for i in range(0, number + 1)]
    #plt.plot(names,values, "ro", markersize=2)
    plt.plot(values, "ro", markersize=2)
    plt.suptitle(f"Collatz conjecture\n0 - {number}")
    plt.ylabel("length")
    plt.xlabel("number")
    x0, xmax = plt.xlim()
    y0, ymax = plt.ylim()
    data_width = xmax - x0
    data_height = ymax - y0
    text = f"  longest sequence: {max(values)}\n  for number: {values.index(max(values))}"
    plt.text(x0 + data_width, y0 + data_height, text, fontsize=8)
    plt.show()

def showNumberPlot(number): #shows every value number reaches in Collatz conjecture until it reaches 1
    values=collatzConjecture(number)
    names=[str(i) for i in range(1, len(values)+1)]
    #plt.plot(names, values, 'r-o')
    plt.plot(values, 'r-o', label="borek")
    plt.suptitle(f"Collatz conjecture - number {number}")
    plt.ylabel("number")
    plt.xlabel("step")
    x0, xmax=plt.xlim()
    y0, ymax=plt.ylim()
    data_width=xmax-x0
    data_height=ymax-y0
    text=f"steps: {len(values)}\nmax value: {max(values)}"
    plt.text(x0+data_width,y0+data_height, text, fontsize=8)
    plt.legend(bbox_to_anchor=(0.5,1.05))
    plt.show()

x=input()
# showBarPlot(x)
showNormalPlot(x)
showPointPlot(x)
# showNumberPlot(x)
