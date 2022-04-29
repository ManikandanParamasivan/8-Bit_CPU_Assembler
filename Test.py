name = str(input("Enter the reading asm file"))
file = open(name, "r")
name2 = str(input("Enter the writing hex file"))
read = file.readlines()
file.close()


l2 =[]
for i in read:
    l1 = i.split()
    for each in l1:
        l2.append(each)

def hexano(n):
    conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    decimal = n
    hexadecimal = ''

    while (decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16

    return hexadecimal

hexcode = {
    "LDA":"1",
    "ADD":"2",
    "SUB":"3",
    "STA":"4",
    "LDI":"5",
    "JMP":"6",
    "JC":"7",
    "JZ":"8",
    "OUT":"e",
    "HLT":"f",
}
l3 = []
l4 = [] # For LDI indices
l5 = [] # For LDA indices
l6 = [] # For STA indices
l7 = []
for i,j in enumerate(l2):
    if j == "LDI":
        l4.append(i)
for i, j in enumerate(l2):
    if j == "LDA":
        l5.append(i)
for i, j in enumerate(l2):
    if j == "STA":
        l6.append(i)
for each in l2:
    if each == "LOOP:":
        n2 = l2.index("LOOP:")
for each in l2:
    if(each == "LDA"):
        for k in l5:
            n = int(l2[k + 1])
            if n > 9:
                hexi = hexano(n)
            else:
                hexi = n
            wrt = hexcode["LDA"] + str(hexi)
            l3.append(wrt)
            for j in l3:
                if j not in l7:
                    l7.append(j)

    elif(each == "ADD"):
        n = int(l2[l2.index("ADD") + 1])
        if n > 9:
            hexi = hexano(n)
        else:
            hexi = n
        wrt = hexcode["ADD"] + str(hexi)
        l3.append(wrt)
        l7.append(wrt)

    elif(each == "SUB"):
        n = int(l2[l2.index("SUB") + 1])
        if n > 9:
            hexi = hexano(n)
        else:
            hexi = n
        wrt = hexcode["SUB"] + str(hexi)
        l3.append(wrt)
        l7.append(wrt)

    elif(each == "STA"):
        for k in l6:
            n = int(l2[k + 1])
            if n > 9:
                hexi = hexano(n)
            else:
                hexi = n
            wrt = hexcode["STA"] + str(hexi)
            l3.append(wrt)
            for j in l3:
                if j not in l7:
                    l7.append(j)

    #elif(each == "LOOP"):
        #n2 = l2[l2.index("LOOP:")]
    elif (each == "LDI"):
        for k in l4:
            n = int(l2[k + 1])
            if n > 9:
                hexi = hexano(n)
            else:
                hexi = n
            wrt = hexcode["LDI"] + str(hexi)
            l3.append(wrt)
            for j in l3:
                if j not in l7:
                    l7.append(j)
    elif(each == "JMP"):
        if n2 % 2:
            n2 = int(n2/2)
            wrt = hexcode["JMP"] + str(n2)
            l3.append(wrt)
            l7.append(wrt)
        else:
            n2 = int(n2/2)
            wrt = hexcode["JMP"] + str(n2)
            l3.append(wrt)
            l7.append(wrt)

    elif(each == "JC"):
        wrt = hexcode["JC"] + "0"
        l3.append(wrt)
        l7.append(wrt)
    elif(each == "JZ"):
        wrt = hexcode["JZ"] + "0"
        l3.append(wrt)
        l7.append(wrt)
    elif(each == "OUT"):
        wrt = hexcode["OUT"] + "0"
        l3.append(wrt)
        l7.append(wrt)
    elif(each == "HLT"):
        wrt = hexcode["HLT"] + "0"
        l3.append(wrt)
        l7.append(wrt)

cnt = 0
cnt2 = 0
for each in l2:
    if each == "LDI":
        cnt += 1
    elif each == "STA":
        cnt2 += 1
if cnt > 1:
    temp = l7[1]
    l7[1] = l7[2]
    l7[2] = temp
    print(l7)
if cnt2 > 1:
    temp = l7[1]
    l7.insert(6,temp)

    print(l7)

# Writing the file in hex
c = open(name2, "a")
for rn in l7:
    c.write(rn + " ")

