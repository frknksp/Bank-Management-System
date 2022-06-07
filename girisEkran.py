import os
from tkinter import *
import tkinter.messagebox as MessageBox
from adminEkran import adminEkran
from musteriTemsilciEkran import musteriTemsilciEkran
from musteriEkran import musteriEkran
from fonksiyonlar import *

class girisEkran:
  def __init__(self,master=None):
     self.master=master
     self.master.geometry("600x580+420+95")
     self.master.resizable(height=0, width=0)
     master.title(" Banka ")

     #frames
     self.top= Frame(master, height=140 , bg= "#F2D7D5")
     self.top.pack(fill=X)

     self.bottom= Frame(master, height=530, bg="#58D68D")
     self.bottom.pack(fill=X)

     #top Frame design
     file=os.getcwd()
     self.top_image = PhotoImage(file=file+"/icon/money1.png")
     self.top_image_label = Label(self.top, image=self.top_image, bg="#F2D7D5")
     self.top_image_label.place(x=70, y=15)

     self.top_image2 = PhotoImage(file=file+"/icon/money1.png")
     self.top_image2_label = Label(self.top, image=self.top_image, bg="#F2D7D5")
     self.top_image2_label.place(x=430, y=15)

     self.heading= Label(self.top, text="Banka Yönetim Sistemi", font="arial 15 bold", bg="#F2D7D5")
     self.heading.place(x= 180, y=30)
     self.heading= Label(self.top, text="Giriş", font="arial 19 bold", bg="#F2D7D5")
     self.heading.place(x= 280, y=90)

     #Label and entries
     self.user_lbl = Label(self.bottom, text="ID numarası : ", bg="#58D68D", font="arial 15 bold")
     self.user_lbl.place(x=90, y=100)

     self.pass_lbl = Label(self.bottom, text="Şifre : ", bg="#58D68D", font="arial 15 bold")
     self.pass_lbl.place(x=90, y=180)

     e_user= Entry(self.bottom, width= 40)
     e_user.place(x=240, y=105)

     e_pass= Entry(self.bottom,show='*' , width= 40)
     e_pass.place(x=240, y=185)

     i= StringVar(self.master, "1")

     Radiobutton(self.bottom, text="Banka Müdürü",  value="1", bg="#82E0AA", variable=i,width="15",height="2",relief="solid").place(x=100, y=260)
     Radiobutton(self.bottom, text="Müşteri Temsilcisi",  value="2", bg="#82E0AA", variable=i,width="15",height="2",relief="solid").place(x=248, y=260)
     Radiobutton(self.bottom, text="Müşteri",  value="3", bg="#82E0AA", variable=i,width="15",height="2",relief="solid").place(x=400, y=260)

     def giris():
         user= StringVar()
         passw= StringVar()
         user= (e_user.get())
         passw=(e_pass.get())
         mode= (i.get())
         if (user == "" or passw == "" ):
             MessageBox.showinfo("Hatalı giriş", "Tüm alanlar doldurulmalıdır.")
         else:
             if (mode == "1"):
                 fonksiyonlar.connect(self)
                 if not(user.isnumeric()):
                     MessageBox.showinfo("Hatalı giriş", "ID tamsayı olmalıdır.")
                 else:
                     self.cursor.execute("select * from manager where manager_id='" + user + "'")
                     myresult = self.cursor.fetchall()
                     print(myresult)
                     if (len(myresult) == 0):
                         MessageBox.showinfo("Kayıt Bulunamadı!", "Bu ID ile ilgili bir kayıt bulunamadı.")
                     else:
                         for x in myresult:
                             idchck = str(x[0])
                             pwchck = str(x[1])
                             if (user == idchck and passw == pwchck):
                                 MessageBox.showinfo("Başarılı", "Yönetici olarak giriş yapıldı")
                                 self.master.withdraw()
                                 adminEkran(Toplevel(self.master))
                             else:
                                 MessageBox.showinfo("Hatalı giriş", "ID veya şifre hatalı")

             if(mode == "2"):
                 fonksiyonlar.connect(self)
                 if not(user.isnumeric()):
                     MessageBox.showinfo("Hatalı giriş", "ID tamsayı olmalıdır.")
                 else:
                     self.cursor.execute("update loginidtbl set lastloginid= " + user)
                     self.con.commit()
                     self.cursor.execute("select * from custserv where customerserv_id='" + user + "'")
                     myresult = self.cursor.fetchall()
                     if (len(myresult) == 0):
                         MessageBox.showinfo("Kayıt Bulunamadı!","Bu ID ile ilgili bir kayıt bulunamadı.")
                     else:
                         for x in myresult:
                             idchck=str(x[0])
                             pwchck=str(x[1])
                             if (user == idchck and passw == pwchck):
                                 MessageBox.showinfo("Başarılı", "Müşteri temsilcisi olarak giriş yapıldı")
                                 self.master.withdraw()
                                 musteriTemsilciEkran(Toplevel(self.master))
                             else:
                                 MessageBox.showinfo("Hatalı giriş", "ID veya şifre hatalı")

             if(mode == "3"):
                 fonksiyonlar.connect(self)
                 if not(user.isnumeric()):
                     MessageBox.showinfo("Hatalı giriş", "ID tamsayı olmalıdır.")
                 else:
                     self.cursor.execute("update loginidtbl set lastloginid= " + user)
                     self.con.commit()
                     self.cursor.execute("select * from customer where customer_id='" + user + "'")
                     myresult = self.cursor.fetchall()
                     if (len(myresult) == 0):
                         MessageBox.showinfo("Kayıt Bulunamadı!", "Bu ID ile ilgili bir kayıt bulunamadı.")
                     else:
                         for x in myresult:
                             idchck=str(x[0])
                             pwchck=str(x[1])
                             if (user == idchck and (passw) == pwchck):
                                 MessageBox.showinfo("Başarılı", "Müşteri olarak giriş yaptınız")
                                 self.master.withdraw()
                                 musteriEkran(Toplevel(self.master))
                             else:
                                 MessageBox.showinfo("Hatalı giriş", "ID veya şifre hatalı")


     # submit
     self.submit= Button(self.bottom, text="Giriş ", font="arial 15 bold", width="30", command=giris)
     self.submit.place(x=105 , y=335)

root = Tk()
top = girisEkran(root)
root.mainloop()
