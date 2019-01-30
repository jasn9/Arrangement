

#................ Problem NO 1 .......


'''

 A customer asked dev company JDC , \
 to develop warehouse and invertory mangaement system for buisness product .
 In the project it is required to create a softwar component to arrange
 on 'just in time basis '


'''



#-------------------------- Written by ken@localhost.in.................

dic = [['Levi-sh',123,4560,'Clothes'],['Parle',90,56,'Biscuit'],['SD-Card',8,890,'Computer'],['oreo',890,78,'Biscuit'],['LOR',8,550,'Books']]

#print(sorted(dic,key=lambda dic:dic[3]))



import tkinter as tk

#def write_slogan():
 #   print(" Tkinter starts... ")

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()
l1 = tk.Label(frame,text=" Welcome user,....... \n View your data is any order you desire \n ( Imp - Modification of data is not allowed , contact admin for further clarification... )")
l1.pack()

#defining first event

def press():
    arr = sorted(dic,key=lambda dic:dic[1])
    ans = ' Name       Quant.  Price       Category \n'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ans+="  "+str(arr[i][j])+"         "
        ans+='\n'
    print(ans)
    l1.config(text=ans)
#defining second event
def press1():
    arr = sorted(dic,key=lambda dic:dic[2])
    ans = ' Name       Quant.  Price       Category \n'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ans+="     "+str(arr[i][j])+"       "
        ans+='\n'
    print(ans)
    l1.config(text=ans)

#defining third event
def press2():
    arr = sorted(dic,key=lambda dic:dic[3])
    ans = ' Name       Quant.  Price       Category \n'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ans+="        "+str(arr[i][j])+"       "
        ans+='\n'
    print(ans)
    l1.config(text=ans)

#defining fourth event

def press3():
    arr = sorted(dic,key=lambda dic:dic[1],reverse=True)
    ans = ' Name       Quant.  Price       Category \n'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ans+="  "+str(arr[i][j])+"       "
        ans+='\n'
    print(ans)
    l1.config(text=ans)

def press4():
    arr = sorted(dic,key=lambda dic:dic[2],reverse=True)
    ans = ' Name       Quant.  Price       Category \n'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ans+="     "+str(arr[i][j])+"       "
        ans+='\n'
    print(ans)
    l1.config(text=ans)

def press5():
    arr = sorted(dic,key=lambda dic:dic[3],reverse=True)
    ans = ' Name       Quant.  Price       Category \n'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ans+="        "+str(arr[i][j])+"       "
        ans+='\n'
    print(ans)
    l1.config(text=ans)

def pressno():
    arr = dic
    ans = ' Name       Quant.  Price       Category \n'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ans+="        "+str(arr[i][j])+"       "
        ans+='\n'
    print(ans)
    l1.config(text=ans)
button = tk.Button(frame,text="Quit",fg="red",command=quit)
button.pack(side=tk.LEFT)
slogan6 = tk.Button(frame,text="View Data",fg="red",command=pressno)
slogan6.pack(side=tk.LEFT)
slogan = tk.Button(frame,text="Quantity",fg="red",command=press)
slogan.pack(side=tk.LEFT)

slogan1 = tk.Button(frame,text="Price",fg="red",command=press1)
slogan1.pack(side=tk.LEFT)

slogan2 = tk.Button(frame,text="Category",fg="red",command=press2)
slogan2.pack(side=tk.LEFT)

slogan3 = tk.Button(frame,text="Quantity DSC",fg="red",command=press3)
slogan3.pack(side=tk.LEFT)

slogan4 = tk.Button(frame,text="Price DSC",fg="red",command=press4)
slogan4.pack(side=tk.LEFT)

#slogan5 = tk.Button(frame,text="Category DSC",fg="red",command=press5)
#slogan5.pack(side=tk.LEFT)


root.mainloop()
