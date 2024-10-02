from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
from tkinter import messagebox,ttk

mc=mysql.connector.connect(host="localhost",user="root",password="mrithula",database="online_shopping_management")
mr=mc.cursor()

rootmain = Tk()
rootmain.title("CSC project")
rootmain.geometry("1000x630")
rootmain.resizable(width=False, height=False)

bg =ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\Online-Shopping-System.png")
my_mcanvas=Canvas(rootmain,width=1000,height=630,bd=0,highlightthickness=0)
my_mcanvas.pack(fill="both", expand=True)
my_mcanvas.create_image(0,0, image=bg, anchor="nw")

tid=my_mcanvas.create_text(505,150, text="Welcome to", font=("lucida calligraphy italic", 34), fill="white")
tid=my_mcanvas.create_text(500,200, text="Halstons", font=("lucida calligraphy italic", 34), fill="white")

ei_entry1,pw_entry1="",""
ei_entry2,pw_entry2="",""
o1,o5=0,0
o2,o3,o4="","",""
cid=0

bgac=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\a1.png")
bgcart=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\cart1.png")
b4=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\elec1.png")
b5=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\ca1.png")
b5e=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\ca5.png")
b6=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\hf3.png")
b6e=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\hf2.png")

#ADMIN PORTAL
def admin():
    global bgac
    root1=Toplevel(rootmain)
    root1.title("ADMIN")
    my_canvas=Canvas(root1, width=1000, height=630)
    root1.resizable(width=False, height=False)
    my_canvas.pack(fill="both", expand=True)
    bgac=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\a1.png")
    my_canvas.create_image(0,0, image=bgac, anchor="nw")
    my_canvas.create_text(500,200, text="ADMINISTRATOR LOGIN", font=("ARIAL", 30), fill="black")
    global ei_entry1,pw_entry1
    
    #PROFILE WINDOW
    def newwin1():
        
        new1=Toplevel(new)
        new1.title("PROFILE DETAILS")
        n1canvas=Canvas(new1, width=1000, height=630)
        new1.resizable(width=False, height=False)
        n1canvas.pack(fill="both", expand=True)
        b1=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\a1.png")
        n1canvas.create_image(0,0, image=bgac, anchor="nw")
        n1canvas.create_text(500,50, text="PROFILE", font=("ARIAL", 30), fill="black")
        
        l1= Label(n1canvas, text='STAFF_ID', fg='black',font=26)
        l2= Label(n1canvas, text='NAME', fg='black',font=26)
        l3= Label(n1canvas, text='PHONE', fg='black',font=26)
        l4= Label(n1canvas, text='EMAIL', fg='black',font=26)
        l5= Label(n1canvas, text='PASSWORD', fg='black',font=26)
        l1.pack()
        l2.pack()
        l3.pack()
        l4.pack()
        l5.pack()
        n1canvas.create_window(70, 120, window=l1,anchor='w')
        n1canvas.create_window(70, 170, window=l2,anchor='w')
        n1canvas.create_window(70, 220, window=l3,anchor='w')
        n1canvas.create_window(70, 270, window=l4,anchor='w')
        n1canvas.create_window(70, 320, window=l5,anchor='w')

        def insertentry():
            global ei_entry1,pw_entry1
            a=ei_entry1.get()
            b=pw_entry1.get()
            mr.execute("select* from staff")
            rec=mr.fetchall()
            q=0
            for i in rec:
                if i[3]==a and i[4]==b:
                    c=i[1]
                    d=i[2]
                    e=i[0]
                    
            sid_entry.insert(0,e)
            nm_entry.insert(0,c)
            pn_entry.insert(0,d)
            em_entry.insert(0,a)
            pd_entry.insert(0,b) 
        
        def editprofile():
            sid=sid_entry.get()
            nm=nm_entry.get()
            pn=pn_entry.get()
            em=em_entry.get()
            pd=pd_entry.get()
            
            sql1="UPDATE staff SET name=%s,phone=%s,email_id=%s,password=%s WHERE staffid=%s"
            v1=(nm,pn,em,pd,int(sid))
            mr.execute(sql1,v1)
            mc.commit()
            messagebox.showinfo(title="SUCCESSFUL",message="YOUR PROFILE HAS BEEN UPDATED")
            
        sid_entry=Entry(new1,font=("Arial",16),width=14,fg="black",bd=0)
        nm_entry=Entry(new1,font=("Arial",16),width=14,fg="black",bd=0)
        pn_entry=Entry(new1,font=("Arial",16),width=14,fg="black",bd=0)
        em_entry=Entry(new1,font=("Arial",16),width=14,fg="black",bd=0)
        pd_entry=Entry(new1,font=("Arial",16),width=14,fg="black",bd=0)

        sid_window = n1canvas.create_window(280, 100, anchor="nw", window=sid_entry)
        nm_window = n1canvas.create_window(280, 150, anchor="nw", window=nm_entry)
        pn_window = n1canvas.create_window(280, 200, anchor="nw", window=pn_entry)
        em_window = n1canvas.create_window(280, 250, anchor="nw", window=em_entry)
        pd_window = n1canvas.create_window(280, 300, anchor="nw", window=pd_entry)

        insertentry()
        btnud=Button(new1,text="Update Profile", font=("Britannic Bold", 16), width=15, fg="black",command=editprofile)
        btnud_window=n1canvas.create_window(390,350,anchor="nw",window=btnud)

        
    #ORDERS WINDOW
    def newwin2():
        
        new2=Toplevel(new)
        new2.title("ORDERS")
        n2canvas=Canvas(new2, width=1000, height=350)
        new2.resizable(width=False, height=False)
        n2canvas.pack(fill="both", expand=True)
        b2=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\a1.png")
        n2canvas.create_image(0,0, image=bgac, anchor="nw")
        new2.configure(bg="lavender")
        n2canvas.create_text(500,50, text="ORDERS", font=("ARIAL", 30), fill="black")
        
        def Delete():
            selected = tv.focus()
            values=tv.item(selected,'values')
            x=values[0]
            y=values[1]
            tv.delete(selected)
            sql4="DELETE from orders_table  WHERE cid=%s and oid=%s"
            v4=(x,y)
            mr.execute(sql4,v4)
            mc.commit()
            
        btnD = Button(new2, text="REMOVE THE SELECTED ITEM WHICH HAS BEEN DELIVERED", font=("Arial", 12), width=55, fg="black",command=Delete)
        btnD_window = n2canvas.create_window(250, 100, anchor="nw", window=btnD)
        
        def insert_tree():
            mr.execute("select* from orders_table")
            rec=mr.fetchall()
            l=[]
            for i in rec:
                l.append(i)
            
            #global count
            count = 0
            for i in l:
                if count % 2 == 0:
                    tv.insert(parent='', index='end', iid=count, text='', values=(i[0],i[1],i[2],i[3]), tags=('evenrow',))
                else:
                    tv.insert(parent='', index='end', iid=count, text='', values=(i[0],i[1],i[2],i[3]), tags=('oddrow',))
                count+=1
        

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(new2)
        tree_scroll.pack(side=RIGHT, fill=Y)
        
        # Add Style
        style = ttk.Style()

        # Pick A Theme
        style.theme_use('default')

        # Configure the Treeview Colors
        style.configure("Treeview",background="lavender",foreground="black",rowheight=25,fieldbackground="lavender")
        style.map('Treeview',background=[('selected','plum')])
        
        tv = ttk.Treeview(new2,yscrollcommand=tree_scroll.set, selectmode="extended")
        tree_scroll.config(command=tv.yview)
        
        tv['columns']=('CID','OID', 'NAME','PRICE')
        tv.column('#0', width=0, stretch=NO)
        tv.column('CID', anchor=CENTER, width=150)
        tv.column('OID', anchor=CENTER, width=150)
        tv.column('NAME', anchor=CENTER, width=450)
        tv.column('PRICE', anchor=CENTER, width=240)
        
        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('CID', text='CID', anchor=CENTER)
        tv.heading('OID', text='OID', anchor=CENTER)
        tv.heading('NAME', text='NAME', anchor=CENTER)
        tv.heading('PRICE', text='PRICE', anchor=CENTER)

        tv.tag_configure('oddrow', background="white")
        tv.tag_configure('evenrow', background="lavender")

        tv.pack()
        insert_tree()
        
    #EDIT ELECTRONICS WINDOW
    def newwin4():
        global b4
        new4=Toplevel(new)
        new4.title("Edit ELECTRONICS")
        new4.resizable(width=False, height=False)
        new4.configure(bg="skyblue1")
        n4canvas=Canvas(new4, width=1000, height=350)
        n4canvas.pack(fill="both", expand=True)
        b4=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\elec1.png")
        n4canvas.create_image(0,0, image=b4, anchor="nw")
        n4canvas.create_text(500,50, text="EDIT ELECTRONICS MENU", font=("ARIAL", 30), fill="black")

        def insert_tree():
            mr.execute("select* from electronics")
            rec=mr.fetchall()
            l=[]
            for i in rec:
                l.append(i)
            
            #global count
            count = 0
            for i in l:
                if count % 2 == 0:
                    tv.insert(parent='', index='end', iid=count, text='', values=(i[0],i[1],i[2],i[3],i[4]), tags=('evenrow',))
                else:
                    tv.insert(parent='', index='end', iid=count, text='', values=(i[0],i[1],i[2],i[3],i[4]), tags=('oddrow',))
                count+=1
        

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(new4)
        tree_scroll.pack(side=RIGHT, fill=Y)
        # Add Style
        style = ttk.Style()

        # Pick A Theme
        style.theme_use('default')

        # Configure the Treeview Colors
        style.configure("Treeview",background="skyblue1",foreground="black",rowheight=28,fieldbackground="skyblue1")
        style.map('Treeview',background=[('selected','lightsalmon4')])
        
        tv = ttk.Treeview(new4,yscrollcommand=tree_scroll.set, selectmode="extended")
        tree_scroll.config(command=tv.yview)
        
        tv['columns']=('ID', 'NAME', 'STATUS','BRAND','PRICE')
        tv.column('#0', width=0, stretch=NO)
        tv.column('ID', anchor=CENTER, width=180)
        tv.column('NAME', anchor=CENTER, width=260)
        tv.column('STATUS', anchor=CENTER, width=180)
        tv.column('BRAND', anchor=CENTER, width=180)
        tv.column('PRICE', anchor=CENTER, width=180)
        
        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('ID', text='ID', anchor=CENTER)
        tv.heading('NAME', text='NAME', anchor=CENTER)
        tv.heading('STATUS', text='STATUS', anchor=CENTER)
        tv.heading('BRAND', text='BRAND', anchor=CENTER)
        tv.heading('PRICE', text='PRICE', anchor=CENTER)

        tv.tag_configure('oddrow', background="white")
        tv.tag_configure('evenrow', background="skyblue1")

        tv.pack()
        
        def edit():
            e1=eid_entry.get()
            e2=name_entry.get()
            e3=status_entry.get()
            e4=brand_entry.get()
            e5=price_entry.get()
            
            selected = tv.focus()
            tv.item(selected, text="", values=(eid_entry.get(),name_entry.get(),status_entry.get(),brand_entry.get(),price_entry.get()))
            sql1="UPDATE electronics SET name=%s,status=%s,brand=%s,price=%s WHERE eid=%s"
            v1=(e2,e3,e4,int(e5),int(e1))
            mr.execute(sql1,v1)
            mc.commit()

            # Clear entry boxes
            eid_entry.delete(0, END)
            name_entry.delete(0, END)
            status_entry.delete(0, END)
            brand_entry.delete(0, END)
            price_entry.delete(0, END)
                
        def add():
            e1=eid_entry.get()
            e2=name_entry.get()
            e3=status_entry.get()
            e4=brand_entry.get()
            e5=price_entry.get()
            selected = tv.focus()
            
            sql1="INSERT INTO electronics VALUES(%s,%s,%s,%s,%s)"
            v1=(int(e1),e2,e3,e4,int(e5))
            mr.execute(sql1,v1)
            mc.commit()
            tv.delete(*tv.get_children())
            insert_tree()
     
            
        def select_record(e):
            # Clear entry boxes
            eid_entry.delete(0, END)
            name_entry.delete(0, END)
            status_entry.delete(0, END)
            brand_entry.delete(0, END)
            price_entry.delete(0, END)

            # Grab record Number
            selected = tv.focus()
            # Grab record values
            values = tv.item(selected, 'values')

            # outpus to entry boxes
            eid_entry.insert(0, values[0])
            name_entry.insert(0, values[1])
            status_entry.insert(0, values[2])
            brand_entry.insert(0, values[3])
            price_entry.insert(0, values[4])
                
        tv.bind("<ButtonRelease-1>", select_record)
        insert_tree()
        l1= Label(n4canvas, text='EID', fg='black',font=26)
        l2= Label(n4canvas, text='NAME', fg='black',font=26)
        l3= Label(n4canvas, text='STATUS', fg='black',font=26)
        l4= Label(n4canvas, text='BRAND', fg='black',font=26)
        l5= Label(n4canvas, text='PRICE', fg='black',font=26)
        l1.pack()
        l2.pack()
        l3.pack()
        l4.pack()
        l5.pack()
        n4canvas.create_window(70, 140, window=l1,anchor='w')
        n4canvas.create_window(70, 180, window=l2,anchor='w')
        n4canvas.create_window(70, 220, window=l3,anchor='w')
        n4canvas.create_window(70, 260, window=l4,anchor='w')
        n4canvas.create_window(70, 300, window=l5,anchor='w')
            

        eid_entry = Entry(new4, font=("Arial", 18), width=15, fg="black", bd=0)
        name_entry = Entry(new4, font=("Arial", 18), width=15, fg="black", bd=0)
        status_entry = Entry(new4, font=("Arial", 18), width=15, fg="black", bd=0)
        brand_entry = Entry(new4, font=("Arial", 18), width=15, fg="black", bd=0)
        price_entry = Entry(new4, font=("Arial", 18), width=15, fg="black", bd=0)

        eid_window = n4canvas.create_window(200, 120, anchor="nw", window=eid_entry)
        name_window = n4canvas.create_window(200, 160, anchor="nw", window=name_entry)
        status_window = n4canvas.create_window(200, 200, anchor="nw", window=status_entry)
        brand_window = n4canvas.create_window(200, 240, anchor="nw", window=brand_entry)
        price_window = n4canvas.create_window(200, 280, anchor="nw", window=price_entry)
       
        
        # Add Buttons to Edit and add the items
        edit_btn = Button(new4, text="Update", font=("Arial", 12), width=25, fg="black", command=edit)
        edit_window = n4canvas.create_window(600, 200, anchor="nw", window=edit_btn)
        add_btn = Button(new4, text="Add record", font=("Arial", 12), width=25, fg="black",command=add)
        add_window = n4canvas.create_window(600, 300, anchor="nw", window=add_btn)
        
    #EDIT CLOTHING AND ACCESORIES
    def newwin5():
        global b5
        new5=Toplevel(new)
        new5.title("EDIT CLOTHING AND ACCESORIES")
        n5canvas=Canvas(new5, width=1000, height=350)
        new5.configure(bg="lavender")
        new5.resizable(width=False, height=False)
        n5canvas.pack(fill="both", expand=True)
        b5e=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\a1.png")
        n5canvas.create_image(0,0, image=b5, anchor="nw")
        n5canvas.create_text(500,50, text="EDIT CLOTHING AND ACCESORIES MENU", font=("ARIAL", 30), fill="black")
        
        def insert_tree():
            mr.execute("select* from clothingandaccessories")
            rec=mr.fetchall()
            l=[]
            for i in rec:
                l.append(i)
            
            count = 0
            for i in l:
                if count % 2 == 0:
                    tv.insert(parent='', index='end', iid=count, text='', values=(i[0],i[1],i[2],i[3],i[4]), tags=('evenrow',))
                else:
                    tv.insert(parent='', index='end', iid=count, text='', values=(i[0],i[1],i[2],i[3],i[4]), tags=('oddrow',))
                count+=1
        

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(new5)
        tree_scroll.pack(side=RIGHT, fill=Y)
        # Add Style
        style = ttk.Style()

        # Pick A Theme
        style.theme_use('default')

        # Configure the Treeview Colors
        style.configure("Treeview",background="lavender",foreground="black",rowheight=28,fieldbackground="lavender")
        style.map('Treeview',background=[('selected','plum')])
        
        tv = ttk.Treeview(new5,yscrollcommand=tree_scroll.set, selectmode="extended")
        tree_scroll.config(command=tv.yview)
        
        tv['columns']=('ID', 'NAME', 'STATUS','SIZE','PRICE')
        tv.column('#0', width=0, stretch=NO)
        tv.column('ID', anchor=CENTER, width=190)
        tv.column('NAME', anchor=CENTER, width=200)
        tv.column('STATUS', anchor=CENTER, width=200)
        tv.column('SIZE', anchor=CENTER, width=200)
        tv.column('PRICE', anchor=CENTER, width=200)
        
        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('ID', text='ID', anchor=CENTER)
        tv.heading('NAME', text='NAME', anchor=CENTER)
        tv.heading('STATUS', text='STATUS', anchor=CENTER)
        tv.heading('SIZE', text='SIZE', anchor=CENTER)
        tv.heading('PRICE', text='PRICE', anchor=CENTER)

        tv.tag_configure('oddrow', background="white")
        tv.tag_configure('evenrow', background="lavender")

        tv.pack()
        
        def edit():
            e1=eid_entry.get()
            e2=name_entry.get()
            e3=status_entry.get()
            e4=size_entry.get()
            e5=price_entry.get()
            selected = tv.focus()
            tv.item(selected, text="", values=(eid_entry.get(),name_entry.get(),status_entry.get(),size_entry.get(),price_entry.get()))
            sql1="UPDATE clothingandaccessories SET name=%s,status=%s,size=%s,price=%s WHERE caid=%s"
            v1=(e2,e3,e4,int(e5),int(e1))
            mr.execute(sql1,v1)
            mc.commit()

            # Clear entry boxes
            eid_entry.delete(0, END)
            name_entry.delete(0, END)
            status_entry.delete(0, END)
            size_entry.delete(0, END)
            price_entry.delete(0, END)
                
        def add():
            e1=eid_entry.get()
            e2=name_entry.get()
            e3=status_entry.get()
            e4=size_entry.get()
            e5=price_entry.get()
            
            selected = tv.focus()
            sql1="INSERT INTO clothingandaccessories  VALUES(%s,%s,%s,%s,%s)"
            v1=(int(e1),e2,e3,e4,int(e5))
            mr.execute(sql1,v1)
            mc.commit()
            tv.delete(*tv.get_children())
            insert_tree()
     
            
        def select_record(e):
            # Clear entry boxes
            eid_entry.delete(0, END)
            name_entry.delete(0, END)
            status_entry.delete(0, END)
            size_entry.delete(0, END)
            price_entry.delete(0, END)

            # Grab record Number
            selected = tv.focus()
            # Grab record values
            values = tv.item(selected, 'values')

            # outpus to entry boxes
            eid_entry.insert(0, values[0])
            name_entry.insert(0, values[1])
            status_entry.insert(0, values[2])
            size_entry.insert(0, values[3])
            price_entry.insert(0, values[4])
                
        tv.bind("<ButtonRelease-1>", select_record)
        insert_tree()
        
        l1= Label(n5canvas, text='C&A_ID', fg='black',font=26)
        l2= Label(n5canvas, text='NAME', fg='black',font=26)
        l3= Label(n5canvas, text='STATUS', fg='black',font=26)
        l4= Label(n5canvas, text='SIZE', fg='black',font=26)
        l5= Label(n5canvas, text='PRICE', fg='black',font=26)
        l1.pack()
        l2.pack()
        l3.pack()
        l4.pack()
        l5.pack()
        n5canvas.create_window(70, 140, window=l1,anchor='w')
        n5canvas.create_window(70, 180, window=l2,anchor='w')
        n5canvas.create_window(70, 220, window=l3,anchor='w')
        n5canvas.create_window(70, 260, window=l4,anchor='w')
        n5canvas.create_window(70, 300, window=l5,anchor='w')
            

        eid_entry = Entry(new5, font=("Arial", 18), width=15, fg="black", bd=0)
        name_entry = Entry(new5, font=("Arial", 18), width=15, fg="black", bd=0)
        status_entry = Entry(new5, font=("Arial", 18), width=15, fg="black", bd=0)
        size_entry = Entry(new5, font=("Arial", 18), width=15, fg="black", bd=0)
        price_entry = Entry(new5, font=("Arial", 18), width=15, fg="black", bd=0)

        eid_window = n5canvas.create_window(200, 120, anchor="nw", window=eid_entry)
        name_window = n5canvas.create_window(200, 160, anchor="nw", window=name_entry)
        status_window = n5canvas.create_window(200, 200, anchor="nw", window=status_entry)
        size_window = n5canvas.create_window(200, 240, anchor="nw", window=size_entry)
        price_window = n5canvas.create_window(200, 280, anchor="nw", window=price_entry)
       
        
        # Add Buttons to Edit and add the items
        edit_btn = Button(new5, text="Update", font=("Arial", 12), width=25, fg="black", command=edit)
        edit_window = n5canvas.create_window(600, 200, anchor="nw", window=edit_btn)
        add_btn = Button(new5, text="Add record", font=("Arial", 12), width=25, fg="black",command=add)
        add_window = n5canvas.create_window(600, 300, anchor="nw", window=add_btn)
        
    #EDIT HOMEAPPLAIANCE WINDOW
    def newwin6():
        global hf1
        new6=Toplevel(new)
        new6.title("EDIT HOMEAPPLIANCE AND FURNITURE")
        n6canvas=Canvas(new6, width=1000, height=360)
        new6.configure(bg="lavender")
        new6.resizable(width=False, height=False)
        n6canvas.pack(fill="both", expand=True)
        b6e=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\hf3.png")
        n6canvas.create_image(0,0, image=b6, anchor="nw")
        n6canvas.create_text(500,50, text="EDIT HOMEAPPLIANCE AND FURNITURE MENU", font=("ARIAL", 30), fill="black")

        def insert_tree():
            mr.execute("select* from homeappliance_and_furniture")
            rec=mr.fetchall()
            l=[]
            for i in rec:
                l.append(i)
            
            #global count
            count = 0
            for i in l:
                if count % 2 == 0:
                    tv.insert(parent='', index='end', iid=count, text='', values=(i[0],i[1],i[2],i[3],i[4]), tags=('evenrow',))
                else:
                    tv.insert(parent='', index='end', iid=count, text='', values=(i[0],i[1],i[2],i[3],i[4]), tags=('oddrow',))
                count+=1
        

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(new6)
        tree_scroll.pack(side=RIGHT, fill=Y)
        # Add Style
        style = ttk.Style()

        # Pick A Theme
        style.theme_use('default')

        # Configure the Treeview Colors
        style.configure("Treeview",background="lavender",foreground="black",rowheight=28,fieldbackground="lavender")
        style.map('Treeview',background=[('selected','plum')])
        
        tv = ttk.Treeview(new6,yscrollcommand=tree_scroll.set, selectmode="extended")
        tree_scroll.config(command=tv.yview)
        
        tv['columns']=('ID', 'NAME', 'STATUS','SPECIFICATION','PRICE')
        tv.column('#0', width=0, stretch=NO)
        tv.column('ID', anchor=CENTER, width=100)
        tv.column('NAME', anchor=CENTER, width=175)
        tv.column('STATUS', anchor=CENTER, width=175)
        tv.column('SPECIFICATION', anchor=CENTER, width=400)
        tv.column('PRICE', anchor=CENTER, width=150)
        
        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('ID', text='ID', anchor=CENTER)
        tv.heading('NAME', text='NAME', anchor=CENTER)
        tv.heading('STATUS', text='STATUS', anchor=CENTER)
        tv.heading('SPECIFICATION', text='SPECIFICATION', anchor=CENTER)
        tv.heading('PRICE', text='PRICE', anchor=CENTER)

        tv.tag_configure('oddrow', background="white")
        tv.tag_configure('evenrow', background="lavender")

        tv.pack()
        
        def edit():
            e1=eid_entry.get()
            e2=name_entry.get()
            e3=status_entry.get()
            e4=specification_entry.get()
            e5=price_entry.get()
            
            selected = tv.focus()
            tv.item(selected, text="", values=(eid_entry.get(),name_entry.get(),status_entry.get(),specification_entry.get(),price_entry.get()))
            sql1="UPDATE homeappliance_and_furniture SET name=%s,status=%s,specification=%s,price=%s WHERE hfid=%s"
            v1=(e2,e3,e4,int(e5),int(e1))
            mr.execute(sql1,v1)
            mc.commit()

            # Clear entry boxes
            eid_entry.delete(0, END)
            name_entry.delete(0, END)
            status_entry.delete(0, END)
            specification_entry.delete(0, END)
            price_entry.delete(0, END)
                
        def add():
            e1=eid_entry.get()
            e2=name_entry.get()
            e3=status_entry.get()
            e4=specification_entry.get()
            e5=price_entry.get()
            
            selected = tv.focus()
            sql1="INSERT INTO homeappliance_and_furniture VALUES(%s,%s,%s,%s,%s)"
            v1=(int(e1),e2,e3,e4,int(e5))
            mr.execute(sql1,v1)
            mc.commit()
            tv.delete(*tv.get_children())
            insert_tree()
     
            
        def select_record(e):
            # Clear entry boxes
            eid_entry.delete(0, END)
            name_entry.delete(0, END)
            status_entry.delete(0, END)
            specification_entry.delete(0, END)
            price_entry.delete(0, END)

            # Grab record Number
            selected = tv.focus()
            # Grab record values
            values = tv.item(selected, 'values')

            # outpus to entry boxes
            eid_entry.insert(0, values[0])
            name_entry.insert(0, values[1])
            status_entry.insert(0, values[2])
            specification_entry.insert(0, values[3])
            price_entry.insert(0, values[4])
                
        tv.bind("<ButtonRelease-1>", select_record)
        insert_tree()
        l1= Label(n6canvas, text='HFID', fg='black',font=26)
        l2= Label(n6canvas, text='NAME', fg='black',font=26)
        l3= Label(n6canvas, text='STATUS', fg='black',font=26)
        l4= Label(n6canvas, text='SPECIFICATION', fg='black',font=20)
        l5= Label(n6canvas, text='PRICE', fg='black',font=26)
        l1.pack()
        l2.pack()
        l3.pack()
        l4.pack()
        l5.pack()
        n6canvas.create_window(70, 140, window=l1,anchor='w')
        n6canvas.create_window(70, 180, window=l2,anchor='w')
        n6canvas.create_window(70, 220, window=l3,anchor='w')
        n6canvas.create_window(70, 260, window=l4,anchor='w')
        n6canvas.create_window(70, 300, window=l5,anchor='w')
            

        eid_entry = Entry(new6, font=("Arial", 18), width=15, fg="black", bd=0)
        name_entry = Entry(new6, font=("Arial", 18), width=15, fg="black", bd=0)
        status_entry = Entry(new6, font=("Arial", 18), width=15, fg="black", bd=0)
        specification_entry = Entry(new6, font=("Arial", 18), width=15, fg="black", bd=0)
        price_entry = Entry(new6, font=("Arial", 18), width=15, fg="black", bd=0)

        eid_window = n6canvas.create_window(250, 120, anchor="nw", window=eid_entry)
        name_window = n6canvas.create_window(250, 160, anchor="nw", window=name_entry)
        status_window = n6canvas.create_window(250, 200, anchor="nw", window=status_entry)
        specification_window = n6canvas.create_window(250, 240, anchor="nw", window=specification_entry)
        price_window = n6canvas.create_window(250, 280, anchor="nw", window=price_entry)
       
        
        # Add Buttons to Edit and add the items
        edit_btn = Button(new6, text="Update", font=("Arial", 12), width=25, fg="black", command=edit)
        edit_window = n6canvas.create_window(600, 200, anchor="nw", window=edit_btn)
        add_btn = Button(new6, text="Add record", font=("Arial", 12), width=25, fg="black",command=add)
        add_window = n6canvas.create_window(600, 300, anchor="nw", window=add_btn)

    #MAIN MENU FOR ADMIN
    def newwina():
        global new,bgac
        new=Toplevel(root1)
        new.title("ADMIN MENU")
        ncanvas=Canvas(new, width=1000, height=630)
        new.resizable(width=False, height=False)
        ncanvas.pack(fill="both", expand=True)
        bga=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\a1.png")
        ncanvas.create_image(0,0, image=bgac, anchor="nw")
        ncanvas.create_text(500,100, text="MAIN MENU", font=("Helvetica", 30), fill="black")

        btn1 = Button(new, text="Your profile", font=("Arial", 16), width=15, fg="black", command=newwin1)
        btn1_window = ncanvas.create_window(100, 200, anchor="nw", window=btn1)
        btn2 = Button(new, text="Orders", font=("Arial", 16), width=15, fg="black", command=newwin2)
        btn2_window = ncanvas.create_window(100, 300, anchor="nw", window=btn2)
        btn4 = Button(new, text=" Edit Electronics ", font=("Arial", 16), width=19, fg="black", command=newwin4)
        btn4_window = ncanvas.create_window(650, 150, anchor="nw", window=btn4)
        btn5 = Button(new, text="Edit Clothing & Accesories", font=("Arial", 12), width=25, fg="black", command=newwin5)
        btn5_window = ncanvas.create_window(650, 250, anchor="nw", window=btn5)
        btn6 = Button(new, text="Edit Homeappliance & furniture", font=("Arial", 12), width=25, fg="black", command=newwin6)
        btn6_window = ncanvas.create_window(650, 350, anchor="nw", window=btn6)


    label1= Label(my_canvas, text='Email Id', fg='black',font=26)
    label2= Label(my_canvas, text='Password', fg='black',font=26)
    label1.pack()
    label2.pack()
    
    my_canvas.create_window(400, 265, window=label1)
    my_canvas.create_window(400, 315, window=label2)

    ei_entry1 = Entry(root1, font=("Arial", 18), width=14, fg="black", bd=0)
    pw_entry1 = Entry(root1, font=("Arial", 18), width=14, fg="black", bd=0)

    ei_window = my_canvas.create_window(500, 250, anchor="nw", window=ei_entry1)
    pw_window = my_canvas.create_window(500, 300, anchor="nw", window=pw_entry1)

    mr.execute("select* from staff")
    rec=mr.fetchall()

    #LOGIN FUNCTION
    def loginchk():
        global ei_entry1,pw_entry1
        a=ei_entry1.get()
        b=pw_entry1.get()
        mr.execute("select* from staff")
        rec=mr.fetchall()
        q=0
        for i in rec:
            if i[3]==a and i[4]==b:
                newwina()
                q=1
            if q==0:    
                messagebox.showinfo(title="ACCESS DENIED",message="Wrong email_id or password...try again")
            
    login_btn = Button(root1, text="Login", font=("Arial", 16), width=13, fg="black", command=loginchk)

    login_btn_window = my_canvas.create_window(450, 350, anchor="nw", window=login_btn)
   
#CUSTOMER PORTAL  
def customer():
    global bgac
    root2=Toplevel(rootmain)
    root2.title("CUSTOMER")
    my_canvas=Canvas(root2, width=1000, height=630)
    root2.resizable(width=False, height=False)
    my_canvas.pack(fill="both", expand=True)
    bgac=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\a1.png")
    my_canvas.create_image(0,0, image=bgac, anchor="nw")
    my_canvas.create_text(510,180, text="CUSTOMER LOGIN", font=("ARIAL", 30), fill="black")
    global ei_entry2,pw_entry2,cid
    
    #CUSTOMER DETAILS WINDOW
    def newwin1():
        
        new1=Toplevel(new)
        new1.title("CUSTOMER DETAILS")
        n1canvas=Canvas(new1, width=1000, height=630)
        new1.resizable(width=False, height=False)
        n1canvas.pack(fill="both", expand=True)
        b1=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\a1.png")
        n1canvas.create_image(0,0, image=bgac, anchor="nw")
        n1canvas.create_text(500,50, text="PROFILE", font=("ARIAL", 30), fill="black")
        
        l1= Label(n1canvas, text='C_ID', fg='black',font=26)
        l2= Label(n1canvas, text='NAME', fg='black',font=26)
        l3= Label(n1canvas, text='PHONE', fg='black',font=26)
        l4= Label(n1canvas, text='EMAIL', fg='black',font=26)
        l5= Label(n1canvas, text='PASSWORD', fg='black',font=26)
        l6= Label(n1canvas, text='ADDRESS', fg='black',font=26)
        l1.pack()
        l2.pack()
        l3.pack()
        l4.pack()
        l5.pack()
        l6.pack()
        
        n1canvas.create_window(70, 120, window=l1,anchor='w')
        n1canvas.create_window(70, 170, window=l2,anchor='w')
        n1canvas.create_window(70, 220, window=l3,anchor='w')
        n1canvas.create_window(70, 270, window=l4,anchor='w')
        n1canvas.create_window(70, 320, window=l5,anchor='w')
        n1canvas.create_window(70, 370, window=l6,anchor='w')


        def insertentry():
            global ei_entry2,pw_entry2
            a=ei_entry2.get()
            b=pw_entry2.get()
            mr.execute("select* from login")
            rec=mr.fetchall()
            q=0
            for i in rec:
                if i[2]==a and i[3]==b:
                    c=i[1]
                    d=i[4]
                    e=i[0]
                    f=i[5]
                    
            cid_entry.insert(0,e)
            nm_entry.insert(0,c)
            pn_entry.insert(0,d)
            em_entry.insert(0,a)
            pd_entry.insert(0,b) 
            ad_entry.insert(0,f) 
        def editprofile():
            cid=cid_entry.get()
            nm=nm_entry.get()
            pn=pn_entry.get()
            em=em_entry.get()
            pd=pd_entry.get()
            ad=ad_entry.get()
            sql1="UPDATE login SET name=%s,phone=%s,email=%s,password=%s,address=%s WHERE cid=%s"
            v1=(nm,pn,em,pd,ad,int(cid))
            mr.execute(sql1,v1)
            mc.commit()
            messagebox.showinfo(title="SUCCESSFUL",message="YOUR PROFILE HAS BEEN UPDATED")
        cid_entry=Entry(new1,font=("Arial",16),width=25,fg="black",bd=0)
        nm_entry=Entry(new1,font=("Arial",16),width=25,fg="black",bd=0)
        pn_entry=Entry(new1,font=("Arial",16),width=25,fg="black",bd=0)
        em_entry=Entry(new1,font=("Arial",16),width=25,fg="black",bd=0)
        pd_entry=Entry(new1,font=("Arial",16),width=25,fg="black",bd=0)
        ad_entry=Entry(new1,font=("Arial",16),width=25,fg="black",bd=0)
        
        cid_window = n1canvas.create_window(280, 100, anchor="nw", window=cid_entry)
        nm_window = n1canvas.create_window(280, 150, anchor="nw", window=nm_entry)
        pn_window = n1canvas.create_window(280, 200, anchor="nw", window=pn_entry)
        em_window = n1canvas.create_window(280, 250, anchor="nw", window=em_entry)
        pd_window = n1canvas.create_window(280, 300, anchor="nw", window=pd_entry)
        ad_window = n1canvas.create_window(280, 350, anchor="nw", window=ad_entry)
        
        insertentry()
        btnud=Button(new1,text="Update Profile", font=("Britannic Bold", 16), width=15, fg="black",command=editprofile)
        btnud_window=n1canvas.create_window(390,420,anchor="nw",window=btnud)

                    
    #CART WINDOW
    def newwin2():
        
        new2=Toplevel(new)
        new2.title("YOUR CART")
        n2canvas=Canvas(new2, width=1000, height=250)
        new2.configure(bg="lavender")
        new2.resizable(width=False, height=False)
        n2canvas.pack(fill="both", expand=True)
        bgcarte=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\cart1.png")
        n2canvas.create_image(0,0, image=bgac, anchor="nw")
        n2canvas.create_text(500,50, text="YOUR CART", font=("ARIAL", 30), fill="black")
        global cid
        
        def Delete():
            global cid
            selected = tv.focus()
            values=tv.item(selected,'values')
            x=cid
            y=values[0]
            tv.delete(selected)
            sql4="DELETE from orders_table  WHERE cid=%s and oid=%s"
            v4=(x,y)
            mr.execute(sql4,v4)
            mc.commit()
            messagebox.showinfo(title="ITEM REMOVED",message="THE ITEM HAS BEEN REMOVED FROM YOUR CART")
            
        def bill():
            
            def confirm():
                messagebox.showinfo(title="ORDER SUCCESSFUL",message="YOUR ORDER HAS BEEN PLACED SUCCESSFULLY!!! THANKYOU FOR SHOPPING WITH US!!")  
            s='SELECT SUM(price) FROM orders_table where cid=%s'
            v=(cid,)
            mr.execute(s,v)
            record = mr.fetchone()
            a="your total bill amount is: Rs"+str(record[0])
            n2canvas.create_text(325,200, text=a, font=("ARIAL", 30), fill="black")
            con = Button(new2, text=" CONFIRM BILLING", font=("Arial", 12), width=16, fg="black",command=confirm)
            con_window = n2canvas.create_window(700, 175, anchor="nw", window=con)
        
        btnD = Button(new2, text=" DELETE THE SELECTED ITEM FROM THE CART", font=("Arial", 14), width=40, fg="black",command=Delete)
        btnD_window = n2canvas.create_window(100, 100, anchor="nw", window=btnD)
        bill_btn = Button(new2, text="BILL", font=("Arial", 14), width=12, fg="black",command=bill)
        bill_btn_window = n2canvas.create_window(700, 100, anchor="nw", window=bill_btn)
        
        def insert_tree():
            global cid
            sql3="select* from orders_table WHERE cid=%s"
            v3=(cid,)
            mr.execute(sql3,v3)
            rec=mr.fetchall()
            l=[]
            for i in rec:
                l.append(i)
            
            #global count
            count = 0
            for i in l:
                if count % 2 == 0:
                    tv.insert(parent='', index='end', iid=count, text='', values=(i[1],i[2],i[3]), tags=('evenrow',))
                else:
                    tv.insert(parent='', index='end', iid=count, text='', values=(i[1],i[2],i[3]), tags=('oddrow',))
                count+=1
                
        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(new2)
        tree_scroll.pack(side=RIGHT, fill=Y)
        
        # Add Style
        style = ttk.Style()

        # Pick A Theme
        style.theme_use('default')

        # Configure the Treeview Colors
        style.configure("Treeview",background="lavender",foreground="black",rowheight=34,fieldbackground="lavender")
        style.map('Treeview',background=[('selected','plum')])
        
        tv = ttk.Treeview(new2,yscrollcommand=tree_scroll.set, selectmode="extended")
        tree_scroll.config(command=tv.yview)
        
        tv['columns']=('OID', 'NAME','PRICE')
        tv.column('#0', width=0, stretch=NO)
        tv.column('OID', anchor=CENTER, width=225)
        tv.column('NAME', anchor=CENTER, width=300)
        tv.column('PRICE', anchor=CENTER, width=275)
        
        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('OID', text='PRODUCT ID', anchor=CENTER)
        tv.heading('NAME', text='NAME', anchor=CENTER)
        tv.heading('PRICE', text='PRICE', anchor=CENTER)

        tv.tag_configure('oddrow', background="white")
        tv.tag_configure('evenrow', background="lavender")

        tv.pack()
        insert_tree()  

    #ELECTRONICS WINDOW    
    def newwin4():
        global b4
        new4=Toplevel(new)
        new4.title(" ELECTRONICS")
        n4canvas=Canvas(new4, width=1000, height=250)
        new4.configure(bg="skyblue1")
        new4.resizable(width=False, height=False)
        n4canvas.pack(fill="both", expand=True)
        b4=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\elec1.png")
        n4canvas.create_image(0,0, image=b4, anchor="nw")
        n4canvas.create_text(500,50, text=" ELECTRONICS MENU", font=("ARIAL", 30), fill="black")
        n4canvas.create_text(500,100, text=" CLICK TO VIEW ITEM DETAILS", font=("ARIAL", 30), fill="black")
        
        def insert_tree():
            mr.execute("select* from electronics")
            rec=mr.fetchall()
            l=[]
            for i in rec:
                l.append(i)
            
            #global count
            count = 0
            for i in l:
                if count % 2 == 0:
                    tv.insert(parent='', index='end', iid=count, text='', values=(i[0],i[1],i[2],i[3],i[4]), tags=('evenrow',))
                else:
                    tv.insert(parent='', index='end', iid=count, text='', values=(i[0],i[1],i[2],i[3],i[4]), tags=('oddrow',))
                count+=1
        

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(new4)
        tree_scroll.pack(side=RIGHT, fill=Y)
        
        # Add Style
        style = ttk.Style()

        # Pick A Theme
        style.theme_use('default')

        # Configure the Treeview Colors
        style.configure("Treeview",background="skyblue1",foreground="black",rowheight=35,fieldbackground="skyblue1")
        style.map('Treeview',background=[('selected','lightsalmon4')])
        
        tv = ttk.Treeview(new4,yscrollcommand=tree_scroll.set, selectmode="extended")
        tree_scroll.config(command=tv.yview)
        
        tv['columns']=('ID', 'NAME', 'STATUS','BRAND','PRICE')
        tv.column('#0', width=0, stretch=NO)
        tv.column('ID', anchor=CENTER, width=100)
        tv.column('NAME', anchor=CENTER, width=250)
        tv.column('STATUS', anchor=CENTER, width=240)
        tv.column('BRAND', anchor=CENTER, width=200)
        tv.column('PRICE', anchor=CENTER, width=200)
        
        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('ID', text='ID', anchor=CENTER)
        tv.heading('NAME', text='NAME', anchor=CENTER)
        tv.heading('STATUS', text='STATUS', anchor=CENTER)
        tv.heading('BRAND', text='BRAND', anchor=CENTER)
        tv.heading('PRICE', text='PRICE', anchor=CENTER)

        tv.tag_configure('oddrow', background="white")
        tv.tag_configure('evenrow', background="skyblue1")

        tv.pack()
        
        def select_record(e):
            
            global o1,o2,o3,o4,o5
            new41=Toplevel(new4)
            new41.title("ITEM")
            new41c=Canvas(new41, width=700, height=500)
            new41.resizable(width=False, height=False)
            new41c.pack(fill="both", expand=True)
            b4e=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\elec1.png")
            new41c.create_image(0,0, image=b4, anchor="nw")
            new41c.create_text(350,50, text=" ITEM DETAILS", font=("ARIAL", 30), fill="black")
            # Grab record Number
            selected = tv.focus()
            # Grab record values
            values = tv.item(selected, 'values')

            #ORDER FUNCTION
            def orders():
                messagebox.showinfo(title="CART",message="YOUR ITEM HAS BEEN ADDED TO THE CART")
                global cid,o1,o2,o5
                sql2="INSERT INTO orders_table(cid,oid,name,price)VALUES(%s,%s,%s,%s)"
                v2=(int(cid),int(o1),o2,int(o5))
                mr.execute(sql2,v2)
                mc.commit()

            o1=values[0]
            o2=values[1]
            o3=values[2]
            o4=values[3]
            o5=values[4]
            
            l1= Label(new41, text='EID', fg='black',font=26)
            l2= Label(new41, text='NAME', fg='black',font=26)
            l3= Label(new41, text='STATUS', fg='black',font=26)
            l4= Label(new41, text='BRAND', fg='black',font=26)
            l5= Label(new41, text='PRICE', fg='black',font=26)
            l1.pack()
            l2.pack()
            l3.pack()
            l4.pack()
            l5.pack()
            
            new41c.create_window(70, 140, window=l1,anchor='w')
            new41c.create_window(70, 180, window=l2,anchor='w')
            new41c.create_window(70, 220, window=l3,anchor='w')
            new41c.create_window(70, 260, window=l4,anchor='w')
            new41c.create_window(70, 300, window=l5,anchor='w')
            new41c.create_text(300,150, text=o1, font=("ARIAL", 26), fill="black")
            new41c.create_text(300,190, text=o2, font=("ARIAL", 26), fill="black")
            new41c.create_text(300,230, text=o3, font=("ARIAL", 26), fill="black")
            new41c.create_text(300,270, text=o4, font=("ARIAL", 26), fill="black")
            new41c.create_text(300,310, text=o5, font=("ARIAL", 26), fill="black")
            cart_btn = Button(new41, text="Add to cart", font=("Arial", 12), width=25, fg="black",command=orders)
            cart_window = new41c.create_window(450, 250, anchor="nw", window=cart_btn)

        tv.bind("<ButtonRelease-1>", select_record)
        insert_tree()

    #CLOTHING AND ACCESORIES WINDOW
    def newwin5():
        global b5
        new5=Toplevel(new)
        new5.title("CLOTHING AND ACCESORIES")
        n5canvas=Canvas(new5, width=1000, height=250)
        new5.configure(bg="lavender")
        new5.resizable(width=False, height=False)
        n5canvas.pack(fill="both", expand=True)
        b5e=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\ca1.png")
        n5canvas.create_image(0,0, image=b5, anchor="nw")
        n5canvas.create_text(500,50, text="CLOTHING AND ACCESORIES MENU", font=("ARIAL", 30), fill="white")
        n5canvas.create_text(500,100, text=" CLICK TO VIEW ITEM DETAILS", font=("ARIAL", 30), fill="white")
        
        def insert_tree():
            mr.execute("select* from clothingandaccessories ")
            rec=mr.fetchall()
            l=[]
            for i in rec:
                l.append(i)
            
            #global count
            count = 0
            for i in l:
                if count % 2 == 0:
                    tv.insert(parent='', index='end', iid=count, text='', values=(i[0],i[1],i[2],i[3],i[4]), tags=('evenrow',))
                else:
                    tv.insert(parent='', index='end', iid=count, text='', values=(i[0],i[1],i[2],i[3],i[4]), tags=('oddrow',))
                count+=1
        

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(new5)
        tree_scroll.pack(side=RIGHT, fill=Y)
        # Add Style
        style = ttk.Style()

        # Pick A Theme
        style.theme_use('default')

        # Configure the Treeview Colors
        style.configure("Treeview",background="lavender",foreground="black",rowheight=35,fieldbackground="lavender")
        style.map('Treeview',background=[('selected','plum')])
        
        tv = ttk.Treeview(new5,yscrollcommand=tree_scroll.set, selectmode="extended")
        tree_scroll.config(command=tv.yview)
        
        tv['columns']=('ID', 'NAME', 'STATUS','SIZE','PRICE')
        tv.column('#0', width=0, stretch=NO)
        tv.column('ID', anchor=CENTER, width=100)
        tv.column('NAME', anchor=CENTER, width=250)
        tv.column('STATUS', anchor=CENTER, width=240)
        tv.column('SIZE', anchor=CENTER, width=200)
        tv.column('PRICE', anchor=CENTER, width=200)
        
        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('ID', text='ID', anchor=CENTER)
        tv.heading('NAME', text='NAME', anchor=CENTER)
        tv.heading('STATUS', text='STATUS', anchor=CENTER)
        tv.heading('SIZE', text='SIZE', anchor=CENTER)
        tv.heading('PRICE', text='PRICE', anchor=CENTER)

        tv.tag_configure('oddrow', background="white")
        tv.tag_configure('evenrow', background="lavender")

        tv.pack()
        
        def select_record(e):
            global o1,o2,o3,o4,o5,b5e
            new41=Toplevel(new5)
            new41.title("ITEM")
            new41c=Canvas(new41, width=700, height=500)
            new41.resizable(width=False, height=False)
            new41c.pack(fill="both", expand=True)
            bg1=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\ca3.png")
            new41c.create_image(0,0, image=b5e, anchor="nw")
            new41c.create_text(350,50, text=" ITEM DETAILS", font=("ARIAL", 30), fill="black")
            # Grab record Number
            selected = tv.focus()
            # Grab record values
            values = tv.item(selected, 'values')
            
            def orders():
                messagebox.showinfo(title="CART",message="YOUR ITEM HAS BEEN ADDED TO THE CART")
                global cid,o1,o2,o5
                sql2="INSERT INTO orders_table(cid,oid,name,price)VALUES(%s,%s,%s,%s)"
                v2=(int(cid),int(o1),o2,int(o5))
                mr.execute(sql2,v2)
                mc.commit()

            o1=values[0]
            o2=values[1]
            o3=values[2]
            o4=values[3]
            o5=values[4]
            
            l1= Label(new41, text='CAID', fg='black',font=26)
            l2= Label(new41, text='NAME', fg='black',font=26)
            l3= Label(new41, text='STATUS', fg='black',font=26)
            l4= Label(new41, text='SIZE', fg='black',font=26)
            l5= Label(new41, text='PRICE', fg='black',font=26)
            l1.pack()
            l2.pack()
            l3.pack()
            l4.pack()
            l5.pack()
            
            new41c.create_window(70, 140, window=l1,anchor='w')
            new41c.create_window(70, 180, window=l2,anchor='w')
            new41c.create_window(70, 220, window=l3,anchor='w')
            new41c.create_window(70, 260, window=l4,anchor='w')
            new41c.create_window(70, 300, window=l5,anchor='w')
            new41c.create_text(300,150, text=o1, font=("ARIAL", 26), fill="black")
            new41c.create_text(300,190, text=o2, font=("ARIAL", 26), fill="black")
            new41c.create_text(300,230, text=o3, font=("ARIAL", 26), fill="black")
            new41c.create_text(300,270, text=o4, font=("ARIAL", 26), fill="black")
            new41c.create_text(300,310, text=o5, font=("ARIAL", 26), fill="black")
            cart_btn = Button(new41, text="Add to cart", font=("Arial", 12), width=25, fg="black",command=orders)
            cart_window = new41c.create_window(450, 250, anchor="nw", window=cart_btn)

        tv.bind("<ButtonRelease-1>", select_record)
        insert_tree()

    #HOMEAPPLIANCE AND FURNITURE WINDOW 
    def newwin6():
        
        new6=Toplevel(new)
        new6.title(" HOMEAPPLIANCE AND FURNITURE")
        n6canvas=Canvas(new6, width=1000, height=250)
        new6.configure(bg="lavender")
        new6.resizable(width=False, height=False)
        n6canvas.pack(fill="both", expand=True)
        b6e=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\hf3.png")
        n6canvas.create_image(0,0, image=b6, anchor="nw")
        n6canvas.create_text(500,50, text="HOMEAPPLIANCE AND FURNITURE MENU", font=("ARIAL", 30), fill="black")
        n6canvas.create_text(500,100, text=" CLICK TO VIEW ITEM DETAILS", font=("ARIAL", 30), fill="black")
        
        def insert_tree():
            mr.execute("select* from homeappliance_and_furniture ")
            rec=mr.fetchall()
            l=[]
            for i in rec:
                l.append(i)
            
            #global count
            count = 0
            for i in l:
                if count % 2 == 0:
                    tv.insert(parent='', index='end', iid=count, text='', values=(i[0],i[1],i[2],i[3],i[4]), tags=('evenrow',))
                else:
                    tv.insert(parent='', index='end', iid=count, text='', values=(i[0],i[1],i[2],i[3],i[4]), tags=('oddrow',))
                count+=1
        

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(new6)
        tree_scroll.pack(side=RIGHT, fill=Y)
        
        # Add Style
        style = ttk.Style()

        # Pick A Theme
        style.theme_use('default')

        # Configure the Treeview Colors
        style.configure("Treeview",background="lavender",foreground="black",rowheight=35,fieldbackground="lavender")
        style.map('Treeview',background=[('selected','plum')])
        
        tv = ttk.Treeview(new6,yscrollcommand=tree_scroll.set, selectmode="extended")
        tree_scroll.config(command=tv.yview)
        
        tv['columns']=('ID', 'NAME', 'STATUS','SPECIFICATIONS','PRICE')
        tv.column('#0', width=0, stretch=NO)
        tv.column('ID', anchor=CENTER, width=100)
        tv.column('NAME', anchor=CENTER, width=175)
        tv.column('STATUS', anchor=CENTER, width=175)
        tv.column('SPECIFICATIONS', anchor=CENTER, width=400)
        tv.column('PRICE', anchor=CENTER, width=120)
        
        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('ID', text='ID', anchor=CENTER)
        tv.heading('NAME', text='NAME', anchor=CENTER)
        tv.heading('STATUS', text='STATUS', anchor=CENTER)
        tv.heading('SPECIFICATIONS', text='SPECIFICATIONS', anchor=CENTER)
        tv.heading('PRICE', text='PRICE', anchor=CENTER)

        tv.tag_configure('oddrow', background="white")
        tv.tag_configure('evenrow', background="lavender")

        tv.pack()
        
        def select_record(e):
            global o1,o2,o3,o4,o5,b6e
            new41=Toplevel(new6)
            new41.title("ITEM")
            new41c=Canvas(new41, width=1000, height=500)
            new41.resizable(width=False, height=False)
            new41c.pack(fill="both", expand=True)
            bge1=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\hf2.png")
            new41c.create_image(0,0, image=b6e, anchor="nw")
            new41c.create_text(350,50, text=" ITEM DETAILS", font=("ARIAL", 30), fill="white")
            # Grab record Number
            selected = tv.focus()
            # Grab record values
            values = tv.item(selected, 'values')
            
            def orders():
                messagebox.showinfo(title="CART",message="YOUR ITEM HAS BEEN ADDED TO THE CART")
                global cid,o1,o2,o5
                sql2="INSERT INTO orders_table(cid,oid,name,price)VALUES(%s,%s,%s,%s)"
                v2=(int(cid),int(o1),o2,int(o5))
                mr.execute(sql2,v2)
                mc.commit()

            o1=values[0]
            o2=values[1]
            o3=values[2]
            o4=values[3]
            o5=values[4]
            
            l1= Label(new41, text='HFID', fg='black',font=26)
            l2= Label(new41, text='NAME', fg='black',font=26)
            l3= Label(new41, text='STATUS', fg='black',font=26)
            l4= Label(new41, text='SPECIFIATION', fg='black',font=26)
            l5= Label(new41, text='PRICE', fg='black',font=26)
            l1.pack()
            l2.pack()
            l3.pack()
            l4.pack()
            l5.pack()
            
            new41c.create_window(70, 140, window=l1,anchor='w')
            new41c.create_window(70, 180, window=l2,anchor='w')
            new41c.create_window(70, 220, window=l3,anchor='w')
            new41c.create_window(70, 260, window=l4,anchor='w')
            new41c.create_window(70, 330, window=l5,anchor='w')
            new41c.create_text(300,145, text=o1, font=("ARIAL", 20), fill="black")
            new41c.create_text(300,185, text=o2, font=("ARIAL", 20), fill="black")
            new41c.create_text(300,225, text=o3, font=("ARIAL", 20), fill="black")
            new41c.create_text(450,295, text=o4, font=("ARIAL", 20), fill="black")
            new41c.create_text(300,335, text=o5, font=("ARIAL", 20), fill="black")
            cart_btn = Button(new41, text="Add to cart", font=("Arial", 12), width=25, fg="black",command=orders)
            cart_window = new41c.create_window(350, 350, anchor="nw", window=cart_btn)

        tv.bind("<ButtonRelease-1>", select_record)
        insert_tree()

    #MAIN WINDOW FOR CUSTOMER
    def newwinc():
        global new,bgac
        new=Toplevel(root2)
        new.title("MENU")
        ncanvas=Canvas(new, width=1000, height=630)
        new.resizable(width=False, height=False)
        ncanvas.pack(fill="both", expand=True)
        bgac1=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\a1.png")
        ncanvas.create_image(0,0, image=bgac, anchor="nw")
        ncanvas.create_text(500,100, text="MAIN MENU", font=("Helvetica", 30), fill="black")

        btn1 = Button(new, text="YOUR DETAILS", font=("Arial", 16), width=15, fg="black", command=newwin1)
        btn1_window = ncanvas.create_window(100, 150, anchor="nw", window=btn1)
        btn2 = Button(new, text="MY CART", font=("Arial", 16), width=15, fg="black", command=newwin2)
        btn2_window = ncanvas.create_window(100, 250, anchor="nw", window=btn2)
        btn4 = Button(new, text=" Electronics ", font=("Arial", 16), width=19, fg="black", command=newwin4)
        btn4_window = ncanvas.create_window(650, 150, anchor="nw", window=btn4)
        btn5 = Button(new, text="Clothing &Accesories", font=("Arial", 12), width=25, fg="black", command=newwin5)
        btn5_window = ncanvas.create_window(650, 250, anchor="nw", window=btn5)
        btn6 = Button(new, text=" Homeappliance & furniture", font=("Arial", 12), width=25, fg="black", command=newwin6)
        btn6_window = ncanvas.create_window(650, 350, anchor="nw", window=btn6)

    #LOGIN FUNCTION
    def loginchk():
        global ei_entry2,pw_entry2,cid
        a=ei_entry2.get()
        b=pw_entry2.get()
        mr.execute("select* from login")
        rec=mr.fetchall()
        q=0
        for i in rec:
            if i[2]==a and i[3]==b:
                cid=i[0]
                newwinc()
                q=1
        if q==0:    
            messagebox.showinfo(title="ACCESS DENIED",message="Wrong email_id or password...try again")
            
    #SIGNUP FUCTION
    def signup():
        global new,bgac
        new=Toplevel(root2)
        new.title("SIGN UP")
        ncanvas=Canvas(new, width=1000, height=630)
        new.resizable(width=False, height=False)
        ncanvas.pack(fill="both", expand=True)
        bs=ImageTk.PhotoImage(file ="E:\\CSC XII-A\\Project\\images\\a1.png")
        ncanvas.create_image(0,0, image=bgac, anchor="nw")
        ncanvas.create_text(500,70, text="SIGN UP", font=("Helvetica", 30), fill="black")
        
        l1= Label(new, text='CID', fg='black',font=26)
        l2= Label(new, text='NAME', fg='black',font=26)
        l3= Label(new, text='EMAIL', fg='black',font=26)
        l4= Label(new, text='PASSWORD', fg='black',font=26)
        l5= Label(new, text='PHONE', fg='black',font=26)
        l6= Label(new, text='ADDRESS', fg='black',font=26)
        l1.pack()
        l2.pack()
        l3.pack()
        l4.pack()
        l5.pack()
        l6.pack()
        
        ncanvas.create_window(70, 140, window=l1,anchor='w')
        ncanvas.create_window(70, 180, window=l2,anchor='w')
        ncanvas.create_window(70, 220, window=l3,anchor='w')
        ncanvas.create_window(70, 260, window=l4,anchor='w')
        ncanvas.create_window(70, 310, window=l5,anchor='w')
        ncanvas.create_window(70, 360, window=l6,anchor='w')
        
        id_entry = Entry(new, font=("Arial", 18), width=20, fg="black", bd=0)
        name_entry = Entry(new, font=("Arial", 18), width=20, fg="black", bd=0)
        email_entry = Entry(new, font=("Arial", 18), width=20, fg="black", bd=0)
        password_entry = Entry(new, font=("Arial", 18), width=20, fg="black", bd=0)
        phone_entry = Entry(new, font=("Arial", 18), width=20, fg="black", bd=0)
        address_entry = Entry(new, font=("Arial", 18), width=20, fg="black", bd=0)
        
        id_window = ncanvas.create_window(200, 120, anchor="nw", window=id_entry)
        name_window = ncanvas.create_window(200, 160, anchor="nw", window=name_entry)
        email_window = ncanvas.create_window(200, 207, anchor="nw", window=email_entry)
        password_window = ncanvas.create_window(200, 245, anchor="nw", window=password_entry)
        phone_window = ncanvas.create_window(200, 295, anchor="nw", window=phone_entry)
        address_window = ncanvas.create_window(200, 345, anchor="nw", window=address_entry)

        def custadd():
            e1=id_entry.get()
            e2=name_entry.get()
            e3=email_entry.get()
            e4=password_entry.get()
            e5=phone_entry.get()
            e6=address_entry.get()
            sql1="INSERT INTO login VALUES(%s,%s,%s,%s,%s,%s)"
            v1=(int(e1),e2,e3,e4,e5,e6)
            mr.execute(sql1,v1)
            mc.commit()
            messagebox.showinfo(title="Signed up",message="CONGRATULATIONS!!! you have successfully signed up")
            
        add_btn = Button(new, text="Sign up", font=("Arial", 16), width=12, fg="black",command=custadd)
        add_btn_window = ncanvas.create_window(335, 395, anchor="nw", window=add_btn)
        
    label1= Label(my_canvas, text='Email', fg='black',font=26)
    label2= Label(my_canvas, text='Password', fg='black',font=26)
    label1.pack()
    label2.pack()
    
    my_canvas.create_window(400, 265, window=label1)
    my_canvas.create_window(400, 315, window=label2)

    ei_entry2 = Entry(root2, font=("Arial", 18), width=14, fg="black", bd=0)
    pw_entry2 = Entry(root2, font=("Arial", 18), width=14, fg="black", bd=0)

    ei_window = my_canvas.create_window(500, 250, anchor="nw", window=ei_entry2)
    pw_window = my_canvas.create_window(500, 300, anchor="nw", window=pw_entry2)

    cid=0
    sign_btn = Button(root2, text="Sign up", font=("Arial", 16), width=12, fg="black", command=signup)
    sign_btn_window = my_canvas.create_window(345, 350, anchor="nw", window=sign_btn)
    
    login_btn = Button(root2, text="Login", font=("Arial", 16), width=12, fg="black", command=loginchk)
    login_btn_window = my_canvas.create_window(515, 350, anchor="nw", window=login_btn)

btn_m1 = Button(rootmain, text="ADMIN", font=("Arial", 16), width=15, fg="black",command=admin)
btn_m1_window = my_mcanvas.create_window(250, 300, anchor="nw", window=btn_m1)

btn_m2 = Button(rootmain, text="CUSTOMER", font=("Arial", 16), width=15, fg="black",command=customer)
btn_m2_window = my_mcanvas.create_window(570, 300, anchor="nw", window=btn_m2)

rootmain.mainloop()
