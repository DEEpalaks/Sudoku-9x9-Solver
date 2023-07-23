a=[]
def list_generation(p): # argument as user question    using p=user()
    High_Row=[]
    High_Column=[]
    row=[]  # inside nested list
    column=[]
    for i in [0,9,18,27,36,45,54,63,72]:
        for j in range(9):
            if j==0:
                m=i
                row.append(p[m])
            else:
                m+=1
                row.append(p[m])
        High_Row.append(row)
        row=[]
    for i in range(9):
        for j in range(9):
            column.append(High_Row[j][i])
        High_Column.append(column)
        column=[]
    #print(High_Row,High_Column)
    return (High_Row,High_Column)
def  checking(High_Row,High_Column):                                
    a="box1"
    box_row=[]
    big_box=[]
    for i in range(9):
        if i in [0,3,6]:
            for j in range(i,i+3):
                for t in range(3):
                    box_row.append(High_Row[j][t])
            big_box.append(box_row)
            box_row=[]
        elif i in [1,4,7]:
            for j in range(i-1,i+2):
                for t in range(3,6):
                    box_row.append(High_Row[j][t])
            big_box.append(box_row)
            box_row=[]
        elif i in [2,5,8]:
            for j in range(i-2,i+1):
                for t in range(6,9):
                    box_row.append(High_Row[j][t])
            big_box.append(box_row)
            box_row=[]
    #print("big_box=  in checking   ",big_box)
    #print("High_Row= in checking   ",High_Row,"High_Column=  in checking  ",High_Column)
    for i in range(9): 
        for j in range(9):
            if High_Row[i][j]==0 and (High_Row[i].count(0)==1):
                 for t in range(1,10):
                    if  t not in High_Row[i]:
                        High_Row[i][j]=t
                        High_Column[j][i]=t
            elif High_Row[i][j]==0 and (High_Column[j].count(0)==1):
                for t in range(1,10):
                    if t not in High_Column[j]:
                        High_Row[i][j]=t
                        High_Column[j][i]=t
            elif High_Row[i][j]==0:
                if i in [0,1,2]:
                    y=0
                    for u in [3,6,9]:
                        if j<u:
                            break
                        else:
                            y+=1
                    #print(y)
                    #print(big_box)
                    if big_box[y].count(0)==1:
                        d=big_box[y].index(0)
                        for t in range(1,10):
                            if t not in big_box[y]:
                                big_box[y][d]=t
                                break
                        High_Row[i][j]=t
                        High_Column[j][i]=t
                elif i in [3,4,5]:
                    y=3
                    for u in [3,6,9]:
                        if j<u:
                            break
                        else:
                            y+=1
                    #print(y)
                    #print(big_box)
                    if big_box[y].count(0)==1:
                        d=big_box[y].index(0)
                        for t in range(1,10):
                            if t not in big_box[y]:
                                big_box[y][d]=t
                                break
                        High_Row[i][j]=t
                        High_Column[j][i]=t
                elif i in [6,7,8]:
                    y=6
                    for u in [3,6,9]:
                        if j<u:
                            break
                        else:
                            y+=1
                    #print(y)
                    #print(big_box)
                    if big_box[y].count(0)==1:
                        d=big_box[y].index(0)
                        for t in range(1,10):
                            if t not in big_box[y]:
                                big_box[y][d]=t
                                break
                        High_Row[i][j]=t
                        High_Column[j][i]=t
    box_row=[]
    big_box=[]
    for i in range(9):
        if i in [0,3,6]:
            for j in range(i,i+3):
                for t in range(3):
                    box_row.append(High_Row[j][t])  # big_box creation
            big_box.append(box_row)
            box_row=[]
        elif i in [1,4,7]:
            for j in range(i-1,i+2):
                for t in range(3,6):
                    box_row.append(High_Row[j][t])
            big_box.append(box_row)
            box_row=[]
        elif i in [2,5,8]:
            for j in range(i-2,i+1):
                for t in range(6,9):
                    box_row.append(High_Row[j][t])
            big_box.append(box_row)
            box_row=[]
    return (High_Row,High_Column,big_box)        
def logical(High_Row,High_Column,big_box):
    #print(big_box,"in logical")
    m=0
    for i in range(9):
        m=m+High_Row[i].count(0)
    number=[]
    big_number=[]
    for i in range(9):
        #print(i)
        for j in range(9):
            #print(j)               #position of missing  number
            if  big_box[i][j]==0:
                number.append(j)
        big_number.append(number)
        number=[]
    #print("big_number=",big_number)
    missing=[]
    big_missing=[]
    for i in range(9):
        for j in range(1,10):
            if j not in big_box[i]:
                missing.append(j)
        big_missing.append(missing)
        missing=[]
    #print("big_missing=",big_missing)
    form=[[0,1,2,0,1,2],[0,1,2,3,4,5],[0,1,2,6,7,8],[3,4,5,0,1,2],[3,4,5,3,4,5],[3,4,5,6,7,8],[6,7,8,0,1,2],[6,7,8,3,4,5],[6,7,8,6,7,8]]
    inf1=[]
    inf2=[]
    inf3=[]
    for i in range(9):
        for j in range(3):
            for t in range(3,6):
                inf3.append(form[i][j])
                inf3.append(form[i][t])
                inf2.append(inf3)
                inf3=[]
        inf1.append(inf2)
        inf2=[]
    #print("inf1=",inf1)
    great_inf1=[]
    great_inf2=[]
    for i in range(9):
        for j in big_number[i]:
            great_inf2.append(inf1[i][j])
        great_inf1.append(great_inf2)
        great_inf2=[]
    #print("great_inf1=",great_inf1)
    #for i in range(9):
        #print(len(great_inf1[i]))
    possibility1=[]
    possibility2=[]
    possibility3=[]
    for i in range(9):
        for j in range(len(big_number[i])):
            for t in big_missing[i]:
                if (t not in (High_Row[great_inf1[i][j][0]])) and (t not in (High_Column[great_inf1[i][j][1]])):
                    possibility3.append(t)
            possibility2.append(possibility3) 
            possibility3=[]
        possibility1.append(possibility2)
        possibility2=[]
    #print("possibility1=",possibility1)
    y=0
    for i in range(9):
        for j in big_missing[i]:
            for t in range(len(big_missing[i])):
                if j in possibility1[i][t]:
                    y+=1
            if y==1:
                for o in range(len(big_missing[i])):
                    if j in possibility1[i][o]:
                        big_box[i][big_number[i][o]]=j
                        High_Row[great_inf1[i][o][0]][great_inf1[i][o][1]]=j
                        High_Column[great_inf1[i][o][1]][great_inf1[i][o][0]]=j
            y=0
    c=0
    for i in range(9):
        c=c+High_Row[i].count(0)
    return(High_Row,High_Column,big_box,m,c)#,big_number,big_missing,great_inf1,possibility1
    #print(High_Row)



from tkinter import *
def click():
    def result(row2):
            root2= Tk()
            root2.title("sudoku")
            root2.configure(background="white")
            w2 = Frame(root2)# width=500, height=450, padx=20, pady=20)
            w2.pack()
            bb1=Button(w2,text="close",width=25,command=root2.destroy,padx=25,bd=1,font=("forte",20,),relief=RIDGE,bg='grey',fg='black')
            bb1.pack()
            w = Frame(root2,bg='teal', width=500, height=450)#, padx=20, pady=20)
            w.pack()


            a0=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a0.grid(row=0,column=0)

            a1=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a1.grid(row=0,column=1)

            a2=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a2.grid(row=0,column=2)

            a3=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a3.grid(row=0,column=3)

            a4=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a4.grid(row=0,column=4)

            a5=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a5.grid(row=0,column=5)

            a6=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a6.grid(row=0,column=6)

            a7=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a7.grid(row=0,column=7)

            a8=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a8.grid(row=0,column=8)




            a9=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a9.grid(row=1,column=0)

            a10=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a10.grid(row=1,column=1)

            a11=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a11.grid(row=1,column=2)

            a12=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a12.grid(row=1,column=3)

            a13=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a13.grid(row=1,column=4)

            a14=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a14.grid(row=1,column=5)

            a15=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a15.grid(row=1,column=6)

            a16=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a16.grid(row=1,column=7)

            a17=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a17.grid(row=1,column=8)



            a18=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a18.grid(row=2,column=0)

            a19=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a19.grid(row=2,column=1)

            a20=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a20.grid(row=2,column=2)

            a21=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a21.grid(row=2,column=3)

            a22=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a22.grid(row=2,column=4)

            a23=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a23.grid(row=2,column=5)

            a24=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a24.grid(row=2,column=6)

            a25=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a25.grid(row=2,column=7)

            a26=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a26.grid(row=2,column=8)



            a27=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a27.grid(row=3,column=0)

            a28=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a28.grid(row=3,column=1)

            a29=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a29.grid(row=3,column=2)

            a30=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a30.grid(row=3,column=3)

            a31=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a31.grid(row=3,column=4)

            a32=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a32.grid(row=3,column=5)

            a33=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a33.grid(row=3,column=6)

            a34=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a34.grid(row=3,column=7)

            a35=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a35.grid(row=3,column=8)



            a36=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a36.grid(row=4,column=0)

            a37=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a37.grid(row=4,column=1)

            a38=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a38.grid(row=4,column=2)

            a39=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a39.grid(row=4,column=3)

            a40=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a40.grid(row=4,column=4)

            a41=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a41.grid(row=4,column=5)

            a42=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a42.grid(row=4,column=6)

            a43=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a43.grid(row=4,column=7)

            a44=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a44.grid(row=4,column=8)



            a45=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a45.grid(row=5,column=0)

            a46=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a46.grid(row=5,column=1)

            a47=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a47.grid(row=5,column=2)

            a48=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a48.grid(row=5,column=3)

            a49=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a49.grid(row=5,column=4)

            a50=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a50.grid(row=5,column=5)

            a51=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a51.grid(row=5,column=6)

            a52=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a52.grid(row=5,column=7)

            a53=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a53.grid(row=5,column=8)



            a54=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a54.grid(row=6,column=0)

            a55=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a55.grid(row=6,column=1)

            a56=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a56.grid(row=6,column=2)

            a57=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a57.grid(row=6,column=3)

            a58=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a58.grid(row=6,column=4)

            a59=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a59.grid(row=6,column=5)

            a60=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a60.grid(row=6,column=6)

            a61=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a61.grid(row=6,column=7)

            a62=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a62.grid(row=6,column=8)




            a63=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a63.grid(row=7,column=0)

            a64=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a64.grid(row=7,column=1)

            a65=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a65.grid(row=7,column=2)

            a66=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a66.grid(row=7,column=3)

            a67=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a67.grid(row=7,column=4)

            a68=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a68.grid(row=7,column=5)

            a69=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a69.grid(row=7,column=6)

            a70=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a70.grid(row=7,column=7)

            a71=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a71.grid(row=7,column=8)




            a72=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a72.grid(row=8,column=0)

            a73=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a73.grid(row=8,column=1)

            a74=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a74.grid(row=8,column=2)

            a75=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a75.grid(row=8,column=3)

            a76=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a76.grid(row=8,column=4)

            a77=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
            a77.grid(row=8,column=5)

            a78=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a78.grid(row=8,column=6)

            a79=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a79.grid(row=8,column=7)

            a80=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
            a80.grid(row=8,column=8)

            a0.insert(END,row2[0][0])
            a1.insert(END,row2[0][1])
            a2.insert(END,row2[0][2])
            a3.insert(END,row2[0][3])
            a4.insert(END,row2[0][4])
            a5.insert(END,row2[0][5])
            a6.insert(END,row2[0][6])
            a7.insert(END,row2[0][7])
            a8.insert(END,row2[0][8])

            a9.insert(END,row2[1][0])
            a10.insert(END,row2[1][1])
            a11.insert(END,row2[1][2])
            a12.insert(END,row2[1][3])
            a13.insert(END,row2[1][4])
            a14.insert(END,row2[1][5])
            a15.insert(END,row2[1][6])
            a16.insert(END,row2[1][7])
            a17.insert(END,row2[1][8])

            a18.insert(END,row2[2][0])
            a19.insert(END,row2[2][1])
            a20.insert(END,row2[2][2])
            a21.insert(END,row2[2][3])
            a22.insert(END,row2[2][4])
            a23.insert(END,row2[2][5])
            a24.insert(END,row2[2][6])
            a25.insert(END,row2[2][7])
            a26.insert(END,row2[2][8])

            a27.insert(END,row2[3][0])
            a28.insert(END,row2[3][1])
            a29.insert(END,row2[3][2])
            a30.insert(END,row2[3][3])
            a31.insert(END,row2[3][4])
            a32.insert(END,row2[3][5])
            a33.insert(END,row2[3][6])
            a34.insert(END,row2[3][7])
            a35.insert(END,row2[3][8])

            a36.insert(END,row2[4][0])
            a37.insert(END,row2[4][1])
            a38.insert(END,row2[4][2])
            a39.insert(END,row2[4][3])
            a40.insert(END,row2[4][4])
            a41.insert(END,row2[4][5])
            a42.insert(END,row2[4][6])
            a43.insert(END,row2[4][7])
            a44.insert(END,row2[4][8])

            a45.insert(END,row2[5][0])
            a46.insert(END,row2[5][1])
            a47.insert(END,row2[5][2])
            a48.insert(END,row2[5][3])
            a49.insert(END,row2[5][4])
            a50.insert(END,row2[5][5])
            a51.insert(END,row2[5][6])
            a53.insert(END,row2[5][8])
            a52.insert(END,row2[5][7])

            a54.insert(END,row2[6][0])
            a55.insert(END,row2[6][1])
            a56.insert(END,row2[6][2])
            a57.insert(END,row2[6][3])
            a58.insert(END,row2[6][4])
            a59.insert(END,row2[6][5])
            a60.insert(END,row2[6][6])
            a61.insert(END,row2[6][7])
            a62.insert(END,row2[6][8])

            a63.insert(END,row2[7][0])
            a64.insert(END,row2[7][1])
            a65.insert(END,row2[7][2])
            a66.insert(END,row2[7][3])
            a67.insert(END,row2[7][4])
            a68.insert(END,row2[7][5])
            a69.insert(END,row2[7][6])
            a70.insert(END,row2[7][7])
            a71.insert(END,row2[7][8])

            a72.insert(END,row2[8][0])
            a73.insert(END,row2[8][1])
            a74.insert(END,row2[8][2])
            a75.insert(END,row2[8][3])
            a76.insert(END,row2[8][4])
            a77.insert(END,row2[8][5])
            a78.insert(END,row2[8][6])
            a79.insert(END,row2[8][7])
            a80.insert(END,row2[8][8])
            
    
    zero=a0.get()
    one=a1.get()
    two=a2.get()
    three=a3.get()
    four=a4.get()
    five=a5.get()
    six=a6.get()
    seven=a7.get()
    eight=a8.get()
    nine=a9.get()
    ten=a10.get()
    eleven=a11.get()
    twelve=a12.get()
    thirteen=a13.get()
    fourteen=a14.get()
    fifteen=a15.get()
    sixteen=a16.get()
    seventeen=a17.get()
    eighteen=a18.get()
    nineteen=a19.get()
    twenty=a20.get()
    twenty1=a21.get()
    twenty2=a22.get()
    twenty3=a23.get()
    twenty4=a24.get()
    twenty5=a25.get()
    twenty6=a26.get()
    twenty7=a27.get()
    twenty8=a28.get()
    twenty9=a29.get()
    thirty=a30.get()
    thirty1=a31.get()
    thirty2=a32.get()
    thirty3=a33.get()
    thirty4=a34.get()
    thirty5=a35.get()
    thirty6=a36.get()
    thirty7=a37.get()
    thirty8=a38.get()
    thirty9=a39.get()
    fourty=a40.get()
    fourty1=a41.get()
    fourty2=a42.get()
    fourty3=a43.get()
    fourty4=a44.get()
    fourty5=a45.get()
    fourty6=a46.get()
    fourty7=a47.get()
    fourty8=a48.get()
    fourty9=a49.get()
    fifty=a50.get()
    fifty1=a51.get()
    fifty2=a52.get()
    fifty3=a53.get()
    fifty4=a54.get()
    fifty5=a55.get()
    fifty6=a56.get()
    fifty7=a57.get()
    fifty8=a58.get()
    fifty9=a59.get()
    sixty=a60.get()
    sixty1=a61.get()
    sixty2=a62.get()
    sixty3=a63.get()
    sixty4=a64.get()
    sixty5=a65.get()
    sixty6=a66.get()
    sixty7=a67.get()
    sixty8=a68.get()
    sixty9=a69.get()
    seventy=a70.get()
    seventy1=a71.get()
    seventy2=a72.get()
    seventy3=a73.get()
    seventy4=a74.get()
    seventy5=a75.get()
    seventy6=a76.get()
    seventy7=a77.get()
    seventy8=a78.get()
    seventy9=a79.get()
    eighty=a80.get()
    #eighty1=a81.get()
    global a
        

    su=[zero,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twenty1,twenty2,twenty3,twenty4,twenty5,twenty6,twenty7,twenty8,twenty9,thirty,thirty1,thirty2,thirty3,thirty4,thirty5,thirty6,thirty7,thirty8,thirty9,fourty,fourty1,fourty2,fourty3,fourty4,fourty5,fourty6,fourty7,fourty8,fourty9,fifty,fifty1,fifty2,fifty3,fifty4,fifty5,fifty6,fifty7,fifty8,fifty9,sixty,sixty1,sixty2,sixty3,sixty4,sixty5,sixty6,sixty7,sixty8,sixty9,seventy,seventy1,seventy2,seventy3,seventy4,seventy5,seventy6,seventy7,seventy8,seventy9,eighty]
    for y in su:
        if y!="":
            a.append(int(y))
        else:
            a.append(0)
    row,column=list_generation(a)
    v=0
    for i in range(9):
        v=v+row[i].count(0)
        row1,column1,box=checking(row,column)
        #print(box,"!!!!!!!")
        row2,column2,big_box2,m,c=logical(row1,column1,box)
    b=1
    while c<m:
        #print("b=",b)
        row3,column3,big_box3=checking(row2,column2)
        row2,column2,big_box2,m,c=logical(row3,column3,big_box3)
        b=b+1
    #print(row2)
    #for i in row2:
    #    print(i)
    #print(big_box2)
    root.destroy()    
    result(row2)
root= Tk()
root.title("sudoku")
root.configure(background="white")

w = Frame(root,bg='teal', width=500, height=450)#, padx=20, pady=20)
w.pack()


a0=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a0.grid(row=0,column=0)

a1=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a1.grid(row=0,column=1)

a2=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a2.grid(row=0,column=2)

a3=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a3.grid(row=0,column=3)

a4=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a4.grid(row=0,column=4)

a5=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a5.grid(row=0,column=5)

a6=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a6.grid(row=0,column=6)

a7=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a7.grid(row=0,column=7)

a8=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a8.grid(row=0,column=8)




a9=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a9.grid(row=1,column=0)

a10=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a10.grid(row=1,column=1)

a11=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a11.grid(row=1,column=2)

a12=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a12.grid(row=1,column=3)

a13=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a13.grid(row=1,column=4)

a14=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a14.grid(row=1,column=5)

a15=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a15.grid(row=1,column=6)

a16=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a16.grid(row=1,column=7)

a17=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a17.grid(row=1,column=8)



a18=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a18.grid(row=2,column=0)

a19=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a19.grid(row=2,column=1)

a20=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a20.grid(row=2,column=2)

a21=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a21.grid(row=2,column=3)

a22=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a22.grid(row=2,column=4)

a23=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a23.grid(row=2,column=5)

a24=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a24.grid(row=2,column=6)

a25=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a25.grid(row=2,column=7)

a26=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a26.grid(row=2,column=8)



a27=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a27.grid(row=3,column=0)

a28=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a28.grid(row=3,column=1)

a29=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a29.grid(row=3,column=2)

a30=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a30.grid(row=3,column=3)

a31=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a31.grid(row=3,column=4)

a32=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a32.grid(row=3,column=5)

a33=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a33.grid(row=3,column=6)

a34=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a34.grid(row=3,column=7)

a35=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a35.grid(row=3,column=8)



a36=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a36.grid(row=4,column=0)

a37=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a37.grid(row=4,column=1)

a38=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a38.grid(row=4,column=2)

a39=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a39.grid(row=4,column=3)

a40=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a40.grid(row=4,column=4)

a41=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a41.grid(row=4,column=5)

a42=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a42.grid(row=4,column=6)

a43=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a43.grid(row=4,column=7)

a44=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a44.grid(row=4,column=8)



a45=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a45.grid(row=5,column=0)

a46=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a46.grid(row=5,column=1)

a47=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a47.grid(row=5,column=2)

a48=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a48.grid(row=5,column=3)

a49=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a49.grid(row=5,column=4)

a50=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a50.grid(row=5,column=5)

a51=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a51.grid(row=5,column=6)

a52=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a52.grid(row=5,column=7)

a53=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a53.grid(row=5,column=8)



a54=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a54.grid(row=6,column=0)

a55=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a55.grid(row=6,column=1)

a56=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a56.grid(row=6,column=2)

a57=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a57.grid(row=6,column=3)

a58=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a58.grid(row=6,column=4)

a59=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a59.grid(row=6,column=5)

a60=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a60.grid(row=6,column=6)

a61=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a61.grid(row=6,column=7)

a62=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a62.grid(row=6,column=8)




a63=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a63.grid(row=7,column=0)

a64=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a64.grid(row=7,column=1)

a65=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a65.grid(row=7,column=2)

a66=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a66.grid(row=7,column=3)

a67=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a67.grid(row=7,column=4)

a68=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a68.grid(row=7,column=5)

a69=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a69.grid(row=7,column=6)

a70=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a70.grid(row=7,column=7)

a71=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a71.grid(row=7,column=8)




a72=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a72.grid(row=8,column=0)

a73=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a73.grid(row=8,column=1)

a74=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a74.grid(row=8,column=2)

a75=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a75.grid(row=8,column=3)

a76=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a76.grid(row=8,column=4)

a77=Entry(w,width=2,bg='grey',fg='white',font=("Arial", 30))
a77.grid(row=8,column=5)

a78=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a78.grid(row=8,column=6)

a79=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a79.grid(row=8,column=7)

a80=Entry(w,width=2,bg='white',fg='black',font=("Arial", 30))
a80.grid(row=8,column=8)

w2 = Frame(root)# width=500, height=450, padx=20, pady=20)
w2.pack()
bb1=Button(w2,text="click me",width=25,command=click,padx=25,bd=1,font=("forte",20,),relief=RIDGE,bg='grey',fg='black')
bb1.pack()

