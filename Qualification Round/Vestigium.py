a= int(input("Enter Number of Tests: "))
for thing in range (0,a):
    b= int(input("Enter Matrix Order: "))
    d=[]
    for j in range(0,b):
        c= eval(input("Enter the row: "))
        d.append(c)
    for l in range(0, b):
        for m in range(0, b):
            if d[l][m]>= 1 and d[l][m]<= b:
                pass
            else:
                print("Not Latin Matrix")

    sum= 0
    for l in range(0,b):
        sum= sum+ d[l][l]

    for i in d:
        count1 = 0
        var = 0
        if var != 1:
            for bod in i:
                if i.count(bod)>1:
                    count1= count1+1
                    var= 1
                else:
                    pass
    count = 0
    for m in range(0, b):
        top=[]
        for l in range(0, b):
            top.append(d[l][m])
        var = 0
        for q in top:
            if var != 1:
                if top.count(q) > 1:
                    count = count + 1
                    var = 1
                else:
                    pass
            else:
                pass

    str1 = "Case#" + str(thing+1) + ":"
    print(str1, sum, end=" ")
    print(count1, end=" ")
    print(count)



