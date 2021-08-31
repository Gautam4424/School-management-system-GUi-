from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
import mysql.connector
#-------------------------------------------------------Database Connection --------------------------------------------
connection=mysql.connector.connect(host="localhost",user='root',passwd="Gautam@4424",database="students")
cur=connection.cursor()

#-----------------------------------------------------------Root window-------------------------------------------------
root=Tk()
root.geometry("1550x750")
root['bg']='black'

#----------------------------------------------------------All functions------------------------------------------------
def save():
    try:
        if Namevar.get()=="" or Addmvar.get()=="" or classvar.get()=="" or Phonevar.get()=="" or DOBvar.get()=="" or Gendervar.get()=="" or Addressvar.get()=="":
            msg.showerror("Empty Feild","Some feilds are empty plese fill")
        else:
            cur.execute("INSERT INTO DATA (Name,Addmission_number,class,phone_number,Date_of_birth,Gender,Address) values('{}','{}','{}','{}','{}','{}','{}')"
                        .format(Namevar.get(),int(Addmvar.get()),int(classvar.get()),Phonevar.get(),DOBvar.get(),Gendervar.get(),Addressvar.get()))
            connection.commit()
            cur.execute("Select * from data")
            treeview.delete(*treeview.get_children())
            for i in cur:
                treeview.insert("",END,values=i)
            msg.showinfo("Added","Add successfully")
            clear()
    except Exception as e:
        msg.showerror("Error","Not added")

def get_cursor(ev):
    cursor_row=treeview.focus()
    contents=treeview.item(cursor_row)
    row=contents['values']
    Namevar.set(row[0])
    Addmvar.set(row[1])
    classvar.set(row[2])
    Phonevar.set(row[3])
    DOBvar.set(row[4])
    Gendervar.set(row[5])
    Addressvar.set(row[6])


def update():
    try:
        cur.execute("Update data set name='{}',Class='{}',phone_number='{}',Date_of_birth='{}',Gender='{}', Address='{}' where addmission_number='{}'".format(Namevar.get(),int(classvar.get()),Phonevar.get(),DOBvar.get(),Gendervar.get(),Addressvar.get(),Addmvar.get()))
        connection.commit()
        cur.execute("Select * from data where addmission_number='{}'".format(Addmvar.get()))
        treeview.delete(*treeview.get_children())
        for i in cur:
            treeview.insert("", END, values=i)
        msg.showinfo("Updated","Update successfully")
        clear()
    except Exception as e:
        msg.showerror("Error", "Not update")

def delete():
    result=msg.askquestion("Delete","Are you sure?",icon='warning')
    if result=="yes":
        cur.execute("Delete from data where addmission_number='{}'".format(Addmvar.get()))
        connection.commit()
        cur.execute("Select * from data")
        treeview.delete(*treeview.get_children())
        for i in cur:
            treeview.insert("", END, values=i)
        clear()
        msg.showinfo("Deleted", "Successfully deleted")

    else:
        msg.showerror("Error","Not deleted")

def show_all():
    cur.execute("Select * from data")
    data=cur.fetchall()
    if data!=[]:
        treeview.delete(*treeview.get_children())
        for i in data:
            treeview.insert("", END, values=i)
    else:
        msg.showinfo("Emty","No Data available")
def clear():
    Namevar.set("")
    Addmvar.set("")
    classvar.set("")
    Phonevar.set("")
    DOBvar.set("")
    Gendervar.set("")
    Addressvar.set("")
    searchvar.set("")
    search_by_var.set("")


def search():
    if search_by_var.get()=="Addmission number":
        cur.execute("Select * from data where Addmission_number='{}'".format(searchvar.get()))
        output=cur.fetchall()
        if output!=[]:
            treeview.delete(*treeview.get_children())
            for i in output:
                treeview.insert("",END,values=i)
        else:
              msg.showinfo("Not found","Entry not found")


    elif search_by_var.get()=="Name":
        cur.execute("Select * from data where Name='{}'".format(searchvar.get()))
        output2=cur.fetchall()
        if output2!=[]:
            treeview.delete(*treeview.get_children())
            for i in output2:
                treeview.insert("",END,values=i)
        else:
            msg.showinfo("Not found","Entry not found")


    elif search_by_var.get()=="Phone number":
        cur.execute("Select * from data where phone_number='{}'".format(searchvar.get()))
        output3=cur.fetchall()
        if output3!=[]:
            treeview.delete(*treeview.get_children())
            for i in output3:
                treeview.insert("",END,values=i)
        else:
            msg.showinfo("Not found","Entry not found")
    else:
        msg.showerror("error","Error occur Try again")


#----------------------------------------------------------Farames--------------------------------------------------
f1=Frame(root,bg="#355C7D",relief=SUNKEN)
f1.pack(side='top',fill=X)
f2=Frame(root,bg="#355C7D")
f2.place(x=10,y=70,width=400,height=620)
f3=Frame(root,bg="#355C7D")
f3.place(x=430,y=70,width=890,height=200)
f4=Frame(bg="#355C7D")
f4.place(x=430,y=280,width=890,height=400)


#---------------------------------------------------------Labels of f1-------------------------------------------------------
l1=Label(f1,text="School Management system",bg="#355C7D",fg="white",font="comicasansms 30 bold").pack()

#---------------------------------------------------------Labels of f2--------------------------------------------------
l2=Label(f2,text="Entries",bg="#355C7D",fg='white',font="Arial 20 bold").pack()
l3=Label(f2,text="Name",font="Arial 20 ",fg="white",bg="#355C7D").place(x=10,y=50)
l4=Label(f2,text="Addm number",font="Arial 20 ",fg="white",bg="#355C7D").place(x=10,y=110)
l5=Label(f2,text="class",font="Arial 20 ",fg="white",bg="#355C7D").place(x=10,y=170)
l6=Label(f2,text="PH number",font="Arial 20 ",fg="white",bg="#355C7D").place(x=10,y=230)
l7=Label(f2,text="D-O-B",font="Arial 20 ",fg="white",bg="#355C7D").place(x=10,y=290)
l8=Label(f2,text="(DD-MM-YYYY)",font="Arial 10 ",fg="white",bg="#355C7D").place(x=100,y=298)
l9=Label(f2,text="Gender",font="Arial 20 ",fg="white",bg="#355C7D").place(x=10,y=350)
l10=Label(f2,text="Address",font="Arial 20 ",fg="white",bg="#355C7D").place(x=10,y=410)
#----------------------------------------------------------Labels of f3-------------------------------------------------
l11=Label(f3,text="Search By",font="Arial 20 ",bg="#355C7D",fg="white").place(x=20,y=95)
l12=Label(f3,text="Search ",font="Arial 20 ",bg="#355C7D",fg="white").place(x=330,y=95)
#----------------------------------------------------------scroll bars--------------------------------------------------
scroll_x=Scrollbar(f4,orient=HORIZONTAL)
scroll_y=Scrollbar(f4,orient=VERTICAL)
#----------------------------------------------------------Textvariable-------------------------------------------------
Namevar=StringVar()
Addmvar=StringVar()
classvar=StringVar()
Phonevar=StringVar()
Addressvar=StringVar()
Gendervar=StringVar()
DOBvar=StringVar()
search_by_var=StringVar()
searchvar=StringVar()
#-----------------------------------------------------------Entry widget------------------------------------------------
Name_entry=Entry(f2,font="Arial 12 ",textvariable=Namevar).place(x=210,y=55)
Addmn_entry=Entry(f2,font="Arial 12 ",textvariable=Addmvar).place(x=210,y=115)
Phone_entry=Entry(f2,font="Arial 12 ",textvariable=Phonevar).place(x=210,y=235)
DOB_entry=Entry(f2,font="Arial 12 ",textvariable=DOBvar).place(x=210,y=300)
Address_entry=Entry(f2,font="Arial 12 ",textvariable=Addressvar).place(x=210,y=415,height=100)

#------------------------------------------------------------f3 entries-------------------------------------------------

search_entry=Entry(f3,font="Arial 12",textvariable=searchvar).place(x=440,y=105)


#------------------------------------------------------------combobox---------------------------------------------------
combo_gender=ttk.Combobox(f2,values=["male","female","others"],state="readonly",textvariable=Gendervar).place(x=210,y=360,height=30)
combo_class=ttk.Combobox(f2,values=["1","2","3","4","5","6","7","8","9","10","11","12"],state="readonly"
                         ,textvariable=classvar).place(x=210,y=175,height=30)
combo_search=ttk.Combobox(f3,values=["Addmission number","Name","Phone number"],state="readonly"
                          ,textvariable=search_by_var).place(x=160,y=100,height=30)

#-----------------------------------------------------------Buttons-----------------------------------------------------
save_button=Button(f2,text="Save",command=save).place(x=20,y=550,width=80,height=50)
update_button=Button(f2,text="Update",command=update).place(x=120,y=550,width=80,height=50)
delete_button=Button(f2,text="Delete",command=delete).place(x=220,y=550,width=80,height=50)
clear_button=Button(f2,text="Reset",command=clear).place(x=320,y=550,width=70,height=50)
search_button=Button(f3,text="Search",command=search).place(x=650,y=100,width=100,height=50)
Show_all_button=Button(f3,text="Show All",command=show_all).place(x=780,y=100,width=100,height=50)

#----------------------------------------------------------Tree view----------------------------------------------------
treeview=ttk.Treeview(f4,columns=("Name","Addm number","Class","PH number","D-O-B","Gender","Address")
                      ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(fill=X,side=BOTTOM)
scroll_y.pack(fill=Y,side=RIGHT)
scroll_x.config(command=treeview.xview)
scroll_y.config(command=treeview.yview)
treeview.heading("Name",text="Name")
treeview.heading("Addm number",text="Addmission number")
treeview.heading("Class",text="class")
treeview.heading("PH number",text="Phone number")
treeview.heading("D-O-B",text="D-O-B")
treeview.heading("Gender",text="Gender")
treeview.heading("Address",text="Address")
treeview['show']='headings'
treeview.column("Name",width=200)
treeview.column("Addm number",width=200)
treeview.column("Class",width=200)
treeview.column("PH number",width=200)
treeview.column("D-O-B",width=200)
treeview.column("Gender",width=200)
treeview.column("Address",width=500)
treeview.bind("<ButtonRelease-1>",get_cursor)
treeview.pack(fill=BOTH,expand=1)




if __name__=='__main__':
    root.mainloop()