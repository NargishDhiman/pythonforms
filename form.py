from tkinter import *
from tkinter import messagebox
import mysql.connector 
 
def Insert(): 
    Name=e1.get() 
    Email=e2.get() 
    Roll_no=e3.get() 
    Field=e4.get() 
    Department=e5.get() 
    University=e6.get()     
    if(Name=="" or Email=="" or Roll_no=="" or Field=="" or Department=="" or University==""): 
        messagebox.showinfo("insert status","please fill complete data") 
    else: 
        con=mysql.connector.connect(host="localhost", user="root",password="sakshi@1234567",database="gui1") 
        cur=con.cursor()         
        query="insert into guidata(Name,Email,Roll_no,Field,Department,University) values(%s,%s,%s,%s,%s,%s)"  
        values=[(Name,Email,Roll_no,Field,Department,University)]         
        cur.executemany(query,values)        
        con.commit() 
        messagebox.showinfo("insert status","Your data has been inserted successfully") 
        
def Update(): 
    Name=e1.get() 
    Email=e2.get() 
    Roll_no=e3.get() 
    Field=e4.get() 
    Department=e5.get()  
    University=e6.get()   
    if(Name=="" or Email=="" or Roll_no=="" or Field=="" or Department=="" or University==""): 
        messagebox.showinfo("update status","please fill complete data") 
    else: 
        con=mysql.connector.connect(host="localhost", user="root",password="sakshi@1234567",database="gui1") 
        cur=con.cursor() 
        query=f"update guidata set Name='{Name}',Email='{Email}',Roll_no='{Roll_no}',Field='{Field}',Department='{Department}',University='{University}' where Name='{Name}'" 
        cur.execute(query)       
        con.commit() 
        messagebox.showinfo("update status","Your data has been updated successfully") 
 
def Delete(): 
    Name=e1.get() 
    Email=e2.get() 
    Roll_no=e3.get() 
    Field=e4.get() 
    Department=e5.get()  
    University=e6.get()    
    if(Email==""): 
        messagebox.showinfo("delete status","please fill email data") 
    else: 
        con=mysql.connector.connect(host="localhost", user="root",password="sakshi@1234567",database="gui1") 
        cur=con.cursor()      
        query=f"delete from guidata where Email='{Email}'" 
        cur.execute(query)       
        con.commit() 
        messagebox.showinfo("delete status","Your data has been deleted successfully") 
 
root=Tk() 
 
#root.geometry("800*800") 
 
root.title("Form") 
 
#img=PhotoImage(file='tw.jpg') 
#ttk.Label(image=img).pack() 
 
l1=Label(root,text="Name",font=('Times',30))              # Courier, Times , Helvetica,Serif , Sans-serif, Script, and Display. 
l1.place(x=50,y=50,width=300)
e1=Entry(root,width=10,fg='black',bg='white',font=('Courier',30))
e1.place(x=350,y=50,width=400) 

l2=Label(root,text="Email",font=('Times',30))         
l2.place(x=50,y=100,width=300)
e2=Entry(root,width=10,fg='black',bg='white',font=('Courier',30))
e2.place(x=350,y=100,width=400) 

l3=Label(root,text="Roll_no",font=('Times',30))      
l3.place(x=50,y=150,width=300)
e3=Entry(root,width=10,fg='black',bg='white',font=('Courier',30))
e3.place(x=350,y=150,width=400) 

l4=Label(root,text="Field",font=('Times',30))      
l4.place(x=50,y=200,width=300)
e4=Entry(root,width=10,fg='black',bg='white',font=('Courier',30)) 
e4.place(x=350,y=200,width=400) 

l5=Label(root,text="Department",font=('Times',30))      
l5.place(x=50,y=250,width=300)
e5=Entry(root,width=10,fg='black',bg='white',font=('Courier',30))
e5.place(x=350,y=250,width=400) 

l6=Label(root,text="University",font=('Times',30))               
l6.place(x=50,y=300,width=300)
e6=Entry(root,width=10,fg='black',bg='white',font=('Courier',30)) 
e6.place(x=350,y=300,width=400)

b1=Button(root,text="Login",fg="white",bg="red",font=('Arial',20),command=Insert)
b1.place(x=100,y=400,width=150) 

b2=Button(root,text="Update",fg="black",bg="green",font=('Arial',20),command=Update) 
b2.place(x=300,y=400,width=150)

b3=Button(root,text="Delete",fg="white",bg="blue",font=('Arial',20),command=Delete)
b3.place(x=500,y=400,width=150) 

root.mainloop() 

