f1 = open('Cash1.txt', 'r')
r1 = f1.read()
t1 = r1.split()
List1 = [float(item) for item in t1]

f2 = open('Cash2.txt', 'r')
r2 = f2.read()
t2 = r2.split()
List2 = [float(item) for item in t2]

f3 = open('Cash3.txt', 'r')
r3 = f3.read()
t3 = r3.split()
List3 = [float(item) for item in t3]

f4 = open('Cash4.txt', 'r')
r4 = f4.read()
t4 = r4.split()
List4 = [float(item) for item in t4]

f5 = open('Cash5.txt', 'r')
r5 = f5.read()
t5 = r5.split()
List5 = [float(item) for item in t5]

interval1 = List1[0] + List2[0] + List3[0] + List4[0] + List5[0]
interval2 = List1[1] + List2[1] + List3[1] + List4[1] + List5[1]
interval3 = List1[2] + List2[2] + List3[2] + List4[2] + List5[2]
interval4 = List1[3] + List2[3] + List3[3] + List4[3] + List5[3]
interval5 = List1[4] + List2[4] + List3[4] + List4[4] + List5[4]
interval6 = List1[5] + List2[5] + List3[5] + List4[5] + List5[5]
interval7 = List1[6] + List2[6] + List3[6] + List4[6] + List5[6]
interval8 = List1[7] + List2[7] + List3[7] + List4[7] + List5[7]
interval9 = List1[8] + List2[8] + List3[8] + List4[8] + List5[8]
interval10 = List1[9] + List2[9] + List3[9] + List4[9] + List5[9]
interval11 = List1[10] + List2[10] + List3[10] + List4[10] + List5[10]
interval12 = List1[11] + List2[11] + List3[11] + List4[11] + List5[11]
interval13 = List1[12] + List2[12] + List3[12] + List4[12] + List5[12]
interval14 = List1[13] + List2[13] + List3[13] + List4[13] + List5[13]
interval15 = List1[14] + List2[14] + List3[14] + List4[14] + List5[14]
interval16 = List1[15] + List2[15] + List3[15] + List4[15] + List5[15]

globallist = [interval1, interval2, interval3,interval4, interval5, interval6, interval7, interval8,
interval9, interval10, interval11,interval12,interval13,interval14,interval15,interval16]


def argmax(elements):
    winner = 1
    y = elements[0]
    for ind, x in enumerate(elements, start=1):
        if x > y:
            y = x
            winner = ind
    return winner
# print(argmax(globallist))