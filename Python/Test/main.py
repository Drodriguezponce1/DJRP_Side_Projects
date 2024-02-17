import os

def main():
    print(sum(3))
    stry = "RANDOMSTRING"
    print(stry[3:-2:2])

    path = r"C:\Users\Daniel\Documents\Side_Projects\DJRP_Side_Projects\Python\Test\tester.txt";
    path2 = r"C:\Users\Daniel\Documents\Side_Projects\DJRP_Side_Projects\OSRS\BarrowsText.txt"
    d = readText(path2)
    print(type(d))
    print(d)


def sum(x):
    return x * 2;


def readText(f):

    di = {}
    text = open(f,"r")
    counter = 0
    for x in text:
        temp = x.split(",")
        di.update({temp[0]: temp[1][0:-1]})

    text.close();
    return di;








if __name__ == "__main__":
    main()