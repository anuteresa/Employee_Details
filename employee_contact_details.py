from tkinter import*
window= Tk()
# Label formation
a1=Label(window,text="Contact List")
a1.grid(row=0, column=0,columnspan=2)
a2=Label(window,text= "New Contact")
a2.grid(row=0,column=4)

b1=Label(window,text="First Name:")
b1.grid(row=1,column=3)
b2=Label(window,text="Last Name:")
b2.grid(row=2,column=3)
b3=Label(window,text="Employee ID:")
b3.grid(row=3,column=3)
b4=Label(window,text="phone #")
b4.grid(row=4,column=3)
b5=Label(window,text="Department:")
b5.grid(row=5,column=3)
b6=Label(window,text="Last Name:")
b6.grid(row=10,column=0)

#Entry label formation

first_name=StringVar()
e1=Entry(window,textvariable=first_name)
e1.grid(row=1,column=4)

last_name=StringVar()
e2=Entry(window,textvariable=last_name)
e2.grid(row=2,column=4)

employee_id=StringVar()
e3=Entry(window,textvariable=employee_id)
e3.grid(row=3,column=4)

phone_no=StringVar()
e4=Entry(window,textvariable=phone_no)
e4.grid(row=4,column=4)

department_name=StringVar()
e4=Entry(window,textvariable=department_name)
e4.grid(row=5,column=4)

search_value=StringVar()
e4=Entry(window,textvariable=search_value)
e4.grid(row=10,column=1)

 # listbox formation
list1=Listbox(window,height=6,width=20)
list1.grid(row=1, column=0,rowspan=4,columnspan=2)


#Button formation
d1=Button(window,text="Add Contact",width=10)
d1.grid(row=6,column=4)
d2=Button(window,text="Search ",width=10)
d2.grid(row=12,column=1)
d3=Button(window,text="Display",width=10)
d3.grid(row=4, column=0,rowspan=4,columnspan=2)

window.mainloop()