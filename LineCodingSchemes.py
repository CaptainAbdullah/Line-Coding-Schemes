import matplotlib.pyplot as plt
# import numpy as np

# NRZ unipolar 
def NRZ_Unipolar():
    digitalData = list(input("Enter digital data elements: "))
    print(digitalData)
    y  = [int(i) for i in digitalData]
    print(y)
    x = []
    for i in range(len(y)):
        x.append(i) 
    print(x)
    plt.step(x,y, 'o-'  ,linewidth = '2')
    plt.ylim(-1.5, 1.5)
    plt.title('NRZ-Unipolar')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(0.2)
    plt.show()


# NRZ-L polar 
def NRZ_L():
    digitalData = list(input("Enter digital data elements: "))
    print(digitalData)
    y = []
    for i in digitalData:
        if int(i) == 0:
            y.append(-1)
        else:
            y.append(int(i))
    print(y)
    x = []
    for i in range(len(y)):
        x.append(i) 
    print(x)
    plt.step(x,y, 'o-'  ,linewidth = '2')
    plt.ylim(-1.5, 1.5)
    plt.title('NRZ-L')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(0.2)
    plt.show()

# NRZ-I (polar)
def NRZ_I():
    digitalData = list(input("Enter digital data elements: "))
    print(digitalData)
    temp = []
    for i in digitalData:
        temp.append(int(i))

    if temp[0] == 1:
        y = [-1]
    else:
        y = [1]
    z = 1
    for i in range(len(temp)-1):
        if temp[i]+temp[z] == temp[i]:
            y.append(y[z-1])
        else:  
            if y[z-1] == -1:
                y.append(1)
            else:
                y.append(-1)
        z = z + 1
    print(y)
    x = []
    for i in range(len(y)):
        x.append(i) 
    print(x)
    plt.step(x,y, 'o-'  ,linewidth = '2')
    plt.ylim(-1.5, 1.5)
    plt.title('NRZ-I')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(0.2)
    plt.show()


# Manchester 
def manchester():
    digitalData = list(input("Enter digital data elements: "))
    print(digitalData)
    temp  = [int(i) for i in digitalData]
    print(temp)

    y = []
    for i in range(len(temp)):
        if temp[i] == 1:
            y.append(-1)
            y.append(1)
        else: 
            y.append(1)
            y.append(-1)

    x = []
    for i in range(len(y)):
        x.append(i) 
    print(x)
    plt.step(x,y, 'o-', linewidth = '2')
    plt.ylim(-1.5, 1.5)
    plt.title('Manchester')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(0.2)
    plt.show()


# RZ 
def RZ():
    digitalData = list(input("Enter digital data elements: "))
    print(digitalData)
    temp  = [int(i) for i in digitalData]
    print(temp)

    y = []
    for i in range(len(temp)):
        if temp[i] == 1:
            y.append(1)
            y.append(0)
        else: 
            y.append(-1)
            y.append(0)

    x = []
    for i in range(len(y)):
        x.append(i) 
    print(x)
    plt.step(x,y, 'o-', linewidth = '2')
    plt.ylim(-1.5, 1.5)
    plt.title('RZ (Return-to-Zero)')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(0.2)
    plt.show()

# AMI 
def ami():
    digitalData = list(input("Enter digital data elements: "))
    print(digitalData)
    temp  = [int(i) for i in digitalData]
    print(temp)

    y = []
    # y = [1,0,-1,1,0,-1,0]
    # print(y)
    bList = [temp[0]]
    b = 0
    for i in temp:
        if int(i) == 0:
            y.append(0)
        else: 
            if bList[b] == 1:
                y.append(-1)
                bList.append(-1)
                b = b + 1   
            else:
                y.append(1)
                bList.append(1)
                b = b + 1   

    print(y)
    x = []
    for i in range(len(y)):
        x.append(i) 
    print(x)
    plt.step(x,y, 'o-', linewidth = '2')
    plt.ylim(-1.5, 1.5)
    plt.title('AMI')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(0.2)
    plt.show()


# Differential Manchester

def differentialManchester():
    digitalData = list(input("Enter digital data elements: "))
    print(digitalData)
    temp  = [int(i) for i in digitalData]
    print(temp)

    #y = [1,-1, 1,-1, -1,1, 1,-1, 1,-1, -1,1, -1,1]
    y = []

    for i in range(len(temp)):
        if temp[i] == 1:  
            if len(y) == 0:
                y.append(1)
                y.append(-1)
            elif y[i] == 1:
                y.append(-1)
                y.append(1)
            else:
                y.append(1)
                y.append(-1)   
        else:
            y.append(1)
            y.append(-1)
            
    print(y)
    x = []
    for i in range(len(y)):
        x.append(i) 
    print(x)
    plt.step(x,y, 'o-', linewidth = '2')
    plt.ylim(-1.5, 1.5)
    plt.title('Differential Manchester')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(0.2)
    plt.show()

def TwoB1Q():
    digitalData = list(input("Enter digital data elements: "))
    print(digitalData)
    temp  = [int(i) for i in digitalData]
    print(temp)
    y = []
    z = -1
    i = 0
    while i in range(len(temp)):
        if temp[i]+temp[i+1] == temp[i]:
            if temp[i] == 1:
                if len(y) == 0:
                    y.append(-1)
                    z = z + 1
                elif y[z] > 0:
                    y.append(-1)
                    z = z + 1
                else:
                    y.append(+1)
                    z = z + 1
            else:
                if len(y) == 0:
                    y.append(+1)
                    z = z +1
                elif y[z] > 0:
                    y.append(+1)
                    z = z +1
                else:
                    y.append(-1)
                    z = z +1
        else:
            if temp[i] == 1:
                if len(y) == 0:
                    y.append(-3)
                    z = z + 1
                elif y[z] > 0:
                    y.append(-3)
                    z = z+1
                else:
                    y.append(+3)
                    z = z + 1
            else:
                if len(y) == 0:
                    y.append(+3)
                    z = z +1
                elif y[z] > 0:
                    y.append(+3)
                    z = z +1
                else:
                    y.append(-3)
                    z = z +1
        i = i + 2
    print(y)
    y.insert(0,1)
    print(y)
    x = []
    for i in range(len(y)):
        x.append(i) 
    print(x)
    plt.step(x,y, 'o-', linewidth = '2')
    plt.ylim(-4, 4)
    plt.title('Differential Manchester')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(0.2)
    plt.show()

print("++++++++++++++ LINE CODING SCHEMES  +++++++++++++++++")
choice = -1
while choice != 0:
    print("Select Line Coding Scheme\n1.NRZ-Unipolar\n2.NRZ-L\n3.NRZ-I\n4.RZ\n5.Manchester\n6.Differential Manchester\n7.AMI\n8.2B1Q\nPress 0 to exit the program")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        NRZ_Unipolar()
    elif choice == 2:
        NRZ_L()
    elif choice == 3:
        NRZ_I()
    elif choice == 4:
        RZ()
    elif choice == 5:
        manchester()
    elif choice == 6:
        differentialManchester()
    elif choice == 7:
        ami()
    elif choice == 8:
        TwoB1Q()
    elif choice == 0:
        exit