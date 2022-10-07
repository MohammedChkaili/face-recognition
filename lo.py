
import os
import shutil
from tkinter import filedialog, ttk
import mysql.connector
import tkinter.messagebox as MessageBox
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk







def run():
    exec(open("kk.py").read())
    

def out():
    root.destroy()   


def ajout():
    window2 = tk.Toplevel()
    window2.geometry('750x500')
    window2.title("add users")
    window2.configure(bg="#4065A4")
    window2.iconbitmap("C:\\Users\\pc\\Desktop\\rf\\face.ico")
    labele = tk.Label(window2, text="Admin name", fg="white", bg="#4065A4", font=('Comic Sans MS', 10))
    labele.place(x=50, y=140)
    labele1 = tk.Label(window2, text="Admin work", fg="white", bg="#4065A4", font=('Comic Sans MS', 10))
    labele1.place(x=50, y=190)
    labele2 = tk.Label(window2, text="Annee de travail", fg="white", bg="#4065A4", font=('Comic Sans MS', 10))
    labele2.place(x=50, y=240)
    e_labele=tk.Entry(window2, width=26, bg="white")
    e_labele.place(x=190,y=140)
    e_labele1 = tk.Entry(window2, width=26, bg="white")
    e_labele1.place(x=190, y=190)
    e_labele2 = tk.Entry(window2, width=26, bg="white")
    e_labele2.place(x=190, y=240)
    instruction=tk.Label(window2,text="New admin information",fg="white", bg="#4065A4", font=('Comic Sans MS', 10))
    instruction.place(x=40,y=40)
    psi=tk.Label(window2,text="Browse image",fg="white", bg="#4065A4", font=('Comic Sans MS', 10))
    psi.place(x=500,y=40)

    def brow():
        file_path = filedialog.askopenfilename(initialdir=os.getcwd(),title="select the image",filetypes=(("JPG File","*.jpg"),("All Files","*.*")))
        img=Image.open(file_path)
        print(file_path)
        img_resized=img.resize((200,200)) 
        img=ImageTk.PhotoImage(img_resized)
        
        labelphoto = Label(window2)
        labelphoto.grid(row=1,column=3)
        labelphoto.place(x=454,y=100)
        labelphoto.image=img
        labelphoto['image']=img
                                                                                                        
        shutil.move(file_path , "C:/Users/pc/Desktop/rf/faces")
        
    
    browse=tk.Button(window2, text="browse", font=('Comic Sans MS', 10), width=18, fg="white",
                                    bg="#4065A4", command=brow)
    browse.place(x=500,y=350)
    
    
    def done():
            if (e_labele.get()=="" or e_labele1.get()==""):
                    MessageBox.showwarning("warning","empty filed!!")
            else:
                
                res=MessageBox.askquestion('Warning', 'Ajouter '+e_labele.get()+' au liste des admins')
                if res == 'yes':
                   con = mysql.connector.connect(host="localhost", user="root", password="Mchkaili-80@80", database="app")
                   cursor = con.cursor()
                   cursor.execute( "insert into admin values('" + e_labele.get() + "','" +e_labele1.get()+"','" + e_labele2.get()+"' )")
                   cursor.execute("commit");
                   insertdata=e_labele.get()+" est devenu admin"
                   e_labele.delete(0, 'end')
                   e_labele1.delete(0, 'end')
                   e_labele2.delete(0, 'end')
                   
                   con.close();
                
                   MessageBox.showinfo("info",insertdata)
                elif res=='no' :
                    MessageBox.showinfo("info","ok")
                else:
                    MessageBox.showinfo("info","eroooooooor")
                
                


    done = tk.Button(window2, text="Ajouter", font=('Comic Sans MS', 10), width=18, fg="white",
                                    bg="#4065A4", command=done)
    done.place(x=190,y=350)

    window2.mainloop()
    
def suppr():
    window3 = tk.Tk()
    window3.geometry('1200x500')
    window3.title("Remove admin")
    window3.configure(bg="#4065A4")
    window3.iconbitmap("C:\\Users\\pc\\Desktop\\rf\\face.ico")
    lab = tk.Label(window3, text="Admin nom", fg="white", bg="#4065A4", font=('Comic Sans MS', 10))
    lab.place(x=50, y=140)
    lab1 = tk.Label(window3, text="Admin travail", fg="white", bg="#4065A4", font=('Comic Sans MS', 10))
    lab1.place(x=50, y=190)
    lab2 = tk.Label(window3, text="Annee de travail ", fg="white", bg="#4065A4", font=('Comic Sans MS', 10))
    lab2.place(x=50, y=240)
    e_lab=tk.Entry(window3, width=26, bg="white")
    e_lab.place(x=190,y=140)
    e_lab1 = tk.Entry(window3, width=26, bg="white")
    e_lab1.place(x=190, y=190)

    instr=tk.Label(window3,text="Admin information",fg="white", bg="#4065A4", font=('Comic Sans MS', 10))
    instr.place(x=70,y=40)
    instr1=tk.Label(window3,text="Admins disponible",fg="white", bg="#4065A4", font=('Comic Sans MS', 10))
    instr1.place(x=600,y=30)
    tableau = ttk.Treeview(window3, columns=('nom', 'travail', 'annee'))
    tableau.heading('nom', text='nom')
    tableau.heading('travail', text='travail')
    tableau.heading('annee', text='annee')

    tableau['show'] = 'headings'
    tableau.place(x=480, y=90)

    con = mysql.connector.connect(host="localhost", user="root", password="Mchkaili-80@80", database="app")
    cursor = con.cursor()
    cursor.execute("select * from admin")
    rows = cursor.fetchall()
    for row in rows:
        tableau.delete()
        tableau.insert('', 'end', iid=row[0], values=(row[0],row[1]))

    con.close()

    def do():
            if (e_lab.get()=="" or e_lab1.get()==""):
                    MessageBox.showwarning("warning","empty filed!!")
            else:
                res=MessageBox.askquestion('Warning', 'Supprimer '+e_lab.get()+' de la liste des admins')
                if res == 'yes':
                   con = mysql.connector.connect(host="localhost", user="root", password="Mchkaili-80@80", database="app")
                   cursor = con.cursor()
                   cursor.execute("Delete from admin where name='" + e_lab.get() + "'")
                   
                   cursor.execute("commit");
                   inser=e_lab.get()+" n'est plus admin"
                   e_lab.delete(0, 'end')
                   e_lab1.delete(0, 'end')
                   
            
                  
                   
                   con.close();
                
                   MessageBox.showinfo("info",inser)
                elif res=='no' :
                    MessageBox.showinfo("info","ok")
                else:
                    MessageBox.showinfo("info","eroooooooor")
                


    dod = tk.Button(window3, text="remove", font=('Comic Sans MS', 10), width=18, fg="white",
                                    bg="#4065A4", command=do)
    dod.place(x=40,y=350)

    window3.mainloop()
    




root=Tk()
root.configure(bg="#4065A4")

root.iconbitmap("C:\\Users\\pc\\Desktop\\rf\\face.ico")


root.geometry('800x400')
img1= tk.PhotoImage(file="C:\\Users\pc\\Desktop\\rf\\gogo.png")
l= tk.Label(root,image= img1,bg="#4065A4")
l.place(x=60, y=90)
img2= tk.PhotoImage(file="C:\\Users\pc\\Desktop\\rf\\fa.png")

vi= tk.Label(root,image= img2,bg="#4065A4")
vi.place(x=250, y=90)

root.title("Smart Lock")
ro=tk.Label(root, text="Smart Lock Based On Facial Recognition Model",font=('Comic Sans MS',14),bg="#4065A4",fg="white")
ro.place(x=55,y=28)
bo=tk.Label(root, text="Smart lock unlock the door when",font=('Comic Sans MS',13),bg="#4065A4",fg="white")
bo.place(x=230,y=250)
ho=tk.Label(root, text="A person face on webcam belong",font=('Comic Sans MS',13),bg="#4065A4",fg="white")
ho.place(x=230,y=290)
vo=tk.Label(root, text="    To autorised name database",font=('Comic Sans MS',13),bg="#4065A4",fg="white")
vo.place(x=230,y=330)
lo=tk.Button(root, text="Ajouter un admin",font=('Comic Sans MS',10),bg="#4065A4",fg="white",width=18,command=ajout)
lo.place(x=600,y=280)
button=tk.Button(root,text="Lock",command=run,width=18,font=('Comic Sans MS',10),bg="#4065A4",fg="white")
button.place(x=600,y=340)
button1=tk.Button(root,text="Supprimer un admin",width=18,font=('Comic Sans MS',10),bg="#4065A4",fg="white",command=suppr)
button1.place(x=600,y=224)
quit1=tk.Button(root,text="Quitter",command=out,width=18,font=('Comic Sans MS',10),bg="#4065A4",fg="white")
quit1.place(x=30,y=338)


root.mainloop()
   

