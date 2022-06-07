import os
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
from fonksiyonlar import fonksiyonlar
from datetime import date

class musteriTemsilciEkran:
  def __init__(self, master=None):
     self.master=master
     self.master.geometry("600x720+420+70")
     self.master.resizable(height=0, width=0)
     master.title("Müşteri temsilcisi")
     # TODO: hepsine title koy

     #frames
     self.top= Frame(master, height=100 , bg= "white")
     self.top.pack(fill=X)

     self.bottom= Frame(master, height=630, bg="#82E0AA")
     self.bottom.pack(fill=X)

     #top Frame design

     self.heading= Label(self.top, text="Banka Yönetim Sistemi", font="arial 15 bold", bg="white")
     self.heading.place(x= 180, y=30)

     #buttons

     #Createacc
     self.ca= Button(self.bottom, text=" Müşteri oluştur ", font="arial 13 bold", command=self.musteri_Olustur, width=20)
     self.ca.place(x=40, y=50)
     self.ca_lbl = Label(self.bottom, text="> Yeni müşteri oluştur", bg="#82E0AA", font="arial 13 bold")
     self.ca_lbl.place(x=280, y=52)

     #Balance enquiry
     self.Be= Button(self.bottom, text=" Bakiye sorgulama ", font="arial 13 bold", command=self.bakiye_goster, width=20)
     self.Be.place(x=40, y=120)
     self.be_lbl = Label(self.bottom, text="> Hesap Bakiyesini göster", bg="#82E0AA", font="arial 13 bold")
     self.be_lbl.place(x=280, y=122)

     #Check Accounnt
     self.Caa= Button(self.bottom, text=" Hesap detayları ", font="arial 13 bold", command=self.musteri_goster, width=20)
     self.Caa.place(x=40, y=190)
     self.caa_lbl = Label(self.bottom, text="> Hesap detaylarını göster", bg="#82E0AA", font="arial 13 bold")
     self.caa_lbl.place(x=280, y=192)

     #Balance Withdraw
     self.Bw= Button(self.bottom, text=" Para çekme ", font="arial 13 bold", command=self.bakiye_cek, width=20)
     self.Bw.place(x=40, y=260)
     self.bw_lbl = Label(self.bottom, text="> Kullanıcı Hesabından Para Çek", bg="#82E0AA", font="arial 13 bold")
     self.bw_lbl.place(x=280, y=262)

     #Balance Deposit
     self.Bd= Button(self.bottom, text=" Para yatır ", font="arial 13 bold", command=self.bakiye_yatir, width=20)
     self.Bd.place(x=40, y=340)
     self.bd_lbl = Label(self.bottom, text="> Kullanıcı Hesabına Para Yatır", bg="#82E0AA", font="arial 13 bold")
     self.bd_lbl.place(x=280, y=342)

     #Delete Account
     self.Au= Button(self.bottom, text=" Hesap sil ", font="arial 13 bold", command=self.musteri_sil, width=20)
     self.Au.place(x=40, y=410)
     self.bd_lbl = Label(self.bottom, text="> Müşteri hesabını sil", bg="#82E0AA", font="arial 13 bold")
     self.bd_lbl.place(x=280, y=412)
     # updt Account
     self.Au= Button(self.bottom, text=" Müşteri güncelle ", font="arial 13 bold", command=self.musteri_guncelle, width=20)
     self.Au.place(x=40, y=480)
     self.bd_lbl = Label(self.bottom, text="> Müşteri hesabını güncelle", bg="#82E0AA", font="arial 13 bold")
     self.bd_lbl.place(x=280, y=482)
      # islem listele
     self.Au = Button(self.bottom, text=" Görüntüle ", font="arial 13 bold", command=self.islem_listele,
                      width=20)
     self.Au.place(x=40, y=550)
     self.bd_lbl = Label(self.bottom, text="> Müşteri işlemlerini listele", bg="#82E0AA", font="arial 13 bold")
     self.bd_lbl.place(x=280, y=552)

  def musteri_sil(self):
     musteriSil(Toplevel(self.master))
  def musteri_Olustur(self):
     musteriOlustur(Toplevel(self.master))
  def musteri_goster(self):
     musteriGoster(Toplevel(self.master))
  def musteri_guncelle(self):
     musteriGuncelle(Toplevel(self.master))
  def bakiye_goster(self):
     bakiyeGoster(Toplevel(self.master))
  def bakiye_yatir(self):
     paraYatir(Toplevel(self.master))
  def bakiye_cek(self):
     paraCek(Toplevel(self.master))
  def islem_listele(self):
     islemListele(Toplevel(self.master))
class musteriSil:
   def __init__(self, master=None):
      self.master = master
      self.master.geometry("700x500+200+20")
      self.master.resizable(height=0, width=0)

      def dlt():
         acc_no = DoubleVar()
         acc_no = (e_acc_no.get())

         if (acc_no == ""):
            MessageBox.showinfo("Hata", "Lütfen müşteri numarası giriniz")
         else:
            fonksiyonlar.connect(self)
            self.cursor.execute("delete from customer where customer_id='" + acc_no + "'")
            self.cursor.execute("delete from bankacc where customer_id='" + acc_no + "'")
            self.con.commit()
            e_acc_no.delete(0, 'end')
            lb.delete(0, 'end')
            lb.delete(1, 'end')
            lb.delete(2, 'end')
            lb.delete(3, 'end')
            lb.delete(4, 'end')
            lb.delete(5, 'end')
            lb.delete(6, 'end')
            lb.delete(7, 'end')
            lb.delete(8, 'end')

            MessageBox.showinfo("Silme işlemi", "Başarılı bir şekilde silindi")
            self.con.close()

      def sub():
         acc_no = DoubleVar()
         acc_no = (e_acc_no.get())

         if (acc_no == ""):
            MessageBox.showinfo("Hata", "Lütfen müşteri numarası giriniz")
         elif not (acc_no.isnumeric()):
            MessageBox.showinfo("Hata", "Müşteri numarası tamsayı girilmelidir")
         else:
            fonksiyonlar.connect(self)
            self.cursor.execute("select * from customer where customer_id='" + acc_no + "'")
            myresult = self.cursor.fetchall()
            if (len(myresult) == 0):
               MessageBox.showinfo("Hata", "Müşteri numarası bulunamadı")
            else:
            # print(myresult)
               e_acc_no.delete(0, 'end')
               lb.delete(0, 'end')
               lb.delete(1, 'end')
               lb.delete(2, 'end')
               lb.delete(3, 'end')
               lb.delete(4, 'end')
               lb.delete(5, 'end')
               lb.delete(6, 'end')
               lb.delete(7, 'end')
               lb.delete(8, 'end')
               for x in myresult:
                  lb.insert(1, "Hesap numarası :" + str(x[0]))
                  lb.insert(2, "Şifre : " + str(x[1]))
                  lb.insert(3, "Ad : " + x[2])
                  lb.insert(4, "Soyad : " + x[3])
                  lb.insert(5, "email : " + x[4])
                  lb.insert(6, "Telefon numarası : " + str(x[5]))

            self.con.close()

      # frames

      self.top = Frame(master, height=100, bg="white")
      self.top.pack(fill=X)

      self.bottom = Frame(master, height=800, bg="#AED6F1")
      self.bottom.pack(fill=X)

      # top Frame design

      self.heading = Label(self.top, text="Müşteriyi sil", font="arial 18 bold", bg="white")
      self.heading.place(x=265, y=30)

      # bottom Frame Design

      # buttons and label
      acc_no = DoubleVar()
      acc_no = Label(self.bottom, text="Müşteri numarası : ", font="arial 14 bold", bg="#AED6F1")
      acc_no.place(x=100, y=50)

      detail = Label(self.bottom, text="Müşteri detayları --> ", font="arial 14 bold", bg="#AED6F1")
      detail.place(x=100, y=120)

      # entry

      e_acc_no = Entry(self.bottom, width=15)
      e_acc_no.place(x=320, y=55)

      # list
      lb = Listbox(self.bottom, height=15, width=60)
      lb.place(x=320, y=95)

      # submit
      self.submit = Button(self.bottom, text=" Bilgileri göster ", font="arial 15 bold", width="20", command=sub)
      self.submit.place(x=45, y=200)

      self.delt = Button(self.bottom, text=" SİL ", font="arial 15 bold", width="20", command=dlt)
      self.delt.place(x=45, y=300)

class musteriOlustur:
   def __init__(self, master=None):
      self.master = master
      self.master.geometry("900x700+200+0")
      self.master.resizable(height=0, width=0)
      fonksiyonlar.getloginid(self)

      def sub():
         password = DoubleVar()
         phone_no = DoubleVar()
         fname = (e_fname.get())
         lname = (e_lname.get())
         password = (e_password.get())
         email = (e_email.get())
         phone_no = (e_phone_no.get())

         if (fname == "" or lname == "" or password == "" or email == "" or phone_no == ""):
            MessageBox.showinfo("Hatalı giriş", "Tüm alanlar doldurulmalı")
         else:
            try:
               fonksiyonlar.connect(self)
               self.cursor.execute('insert into customer(password,firstname,lastname,email,phone,customerserv_id) values(?,?,?,?,?,?);',
                                   (password, fname, lname, email, phone_no,self.loginid)
                                   )
               self.con.commit()
               MessageBox.showinfo("Durum", "Oluşturma başarılı")
               e_fname.delete(0, 'end')
               e_lname.delete(0, 'end')
               e_password.delete(0, 'end')
               e_email.delete(0, 'end')
               e_phone_no.delete(0, 'end')
               self.con.close()
            except:
               MessageBox.showinfo("Hata", "İsim, soyisim karakterlerden; şifre tamsayılardan oluşmalıdır")


      # frames

      self.top = Frame(master, height=100, bg="white")
      self.top.pack(fill=X)

      self.bottom = Frame(master, height=800, bg="#AED6F1")
      self.bottom.pack(fill=X)

      # top Frame design

      self.heading = Label(self.top, text="Yeni müşteri oluştur", font="arial 18 bold", bg="white")
      self.heading.place(x=370, y=30)

      # bottom Frame Design

      # buttons and label

      fname = Label(self.bottom, text="İsim ", font="arial 14 bold", bg="#AED6F1")
      fname.place(x=40, y=110)

      lname = Label(self.bottom, text="Soyisim", font="arial 14 bold", bg="#AED6F1")
      lname.place(x=40, y=165)

      sifre = Label(self.bottom, text="Şifre", font="arial 14 bold", bg="#AED6F1")
      sifre.place(x=40, y=220)

      email = Label(self.bottom, text="Email ", font="arial 14 bold", bg="#AED6F1")
      email.place(x=40, y=330)

      phone_no = DoubleVar()
      phone_no = Label(self.bottom, text="Telefon numarası ", font="arial 14 bold", bg="#AED6F1")
      phone_no.place(x=40, y=385)

      # entry

      e_fname = Entry(self.bottom, width=60)
      e_fname.place(x=320, y=110)

      e_lname = Entry(self.bottom, width=60)
      e_lname.place(x=320, y=165)

      e_password = Entry(self.bottom, width=60)
      e_password.place(x=320, y=220)

      e_email = Entry(self.bottom, width=60)
      e_email.place(x=320, y=330)

      e_phone_no = Entry(self.bottom, width=60)
      e_phone_no.place(x=320, y=385)

      # submit
      self.submit = Button(self.bottom, text=" Oluştur ", font="arial 15 bold", width="30", command=sub)
      self.submit.place(x=320, y=500)

class musteriGoster:
   def __init__(self, master=None):
      self.master = master
      self.master.geometry("750x650+200+20")
      self.master.resizable(height=0, width=0)

      def sub():
         acc_no = DoubleVar()
         acc_no = (e_acc_no.get())

         if (acc_no == ""):
            MessageBox.showinfo("Hata", "Lütfen müşteri numarası giriniz")
         elif not (acc_no.isnumeric()):
            MessageBox.showinfo("Hata", "Müşteri numarası tamsayı girilmelidir")
         else:
            e_fname.delete(0, END)
            e_lname.delete(0, END)
            e_pw.delete(0, END)
            e_address.delete(0, END)
            e_phone_no.delete(0, END)
            e_amount.delete(0, END)
            fonksiyonlar.connect(self)
            self.cursor.execute("select * from customer where customer_id='" + acc_no + "'")
            myresult = self.cursor.fetchall()
            if(len(myresult)==0):
               MessageBox.showinfo("Hata", "Müşteri numarası bulunamadı")
            else:
               self.cursor.execute("select * from bankacc where customer_id='" + acc_no + "'")
               myresultb = self.cursor.fetchall()
               for x in myresultb:
                  e_amount.insert(0, x[3])
               print(myresult)
               for x in myresult:
                  # e_acc_no.insert(0, x[0])
                  e_fname.insert(0, x[2])
                  e_lname.insert(0, x[3])
                  e_pw.insert(0, x[1])
                  # e_amount.insert(0, x[4])
                  e_address.insert(0, x[4])
                  e_phone_no.insert(0, x[5])

               self.con.close()

      # frames

      self.top = Frame(master, height=100, bg="white")
      self.top.pack(fill=X)

      self.bottom = Frame(master, height=800, bg="#AED6F1")
      self.bottom.pack(fill=X)

      # top Frame design

      self.heading = Label(self.top, text="Müşteri detaylarını göster", font="arial 18 bold", bg="white")
      self.heading.place(x=255, y=30)

      # bottom Frame Design

      # buttons and label
      acc_no = DoubleVar()
      acc_no = Label(self.bottom, text="Hesap Numarasını giriniz -> ", font="arial 14 bold", bg="#AED6F1")
      acc_no.place(x=40, y=55)

      fname = Label(self.bottom, text="İsim ", font="arial 14 bold", bg="#AED6F1")
      fname.place(x=40, y=110)

      lname = Label(self.bottom, text="Soyisim ", font="arial 14 bold", bg="#AED6F1")
      lname.place(x=40, y=165)

      passw = Label(self.bottom, text="Şifre ", font="arial 14 bold", bg="#AED6F1")
      passw.place(x=40, y=220)

      amount = DoubleVar()
      amount = Label(self.bottom, text="Miktar ", font="arial 14 bold", bg="#AED6F1")
      amount.place(x=40, y=330)

      address = Label(self.bottom, text="Adres ", font="arial 14 bold", bg="#AED6F1")
      address.place(x=40, y=385)

      phone_no = DoubleVar()
      phone_no = Label(self.bottom, text="Telefon Numarası ", font="arial 14 bold", bg="#AED6F1")
      phone_no.place(x=40, y=440)


      # entry

      e_acc_no = Entry(self.bottom, width=40)
      e_acc_no.place(x=320, y=55)

      e_fname = Entry(self.bottom, width=40)
      e_fname.place(x=320, y=110)

      e_lname = Entry(self.bottom, width=40)
      e_lname.place(x=320, y=165)

      e_pw = Entry(self.bottom, width=40)
      e_pw.place(x=320, y=220)

      e_amount = Entry(self.bottom, width=40)
      e_amount.place(x=320, y=330)

      e_address = Entry(self.bottom, width=40)
      e_address.place(x=320, y=385)

      e_phone_no = Entry(self.bottom, width=40)
      e_phone_no.place(x=320, y=440)


      # entry

      # submit
      self.submit = Button(self.bottom, text=" Göster ", font="arial 15 bold", width="10", command=sub)
      self.submit.place(x=600, y=55)

      self.qt = Button(self.bottom, text="Çıkış", font="arial 15 bold", width="10", command=quit)
      self.qt.place(x=600, y=200)

class musteriGuncelle:
   def __init__(self, master=None):
      self.master = master
      self.master.geometry("750x650+200+20")
      self.master.resizable(height=0, width=0)

      def sub():
         acc_no = DoubleVar()
         acc_no = (e_acc_no.get())

         if (acc_no == ""):
            MessageBox.showinfo("Hatalı giriş", "Müşteri numarası girilmelidir.")
         else:
            if(e_fname.get()=="" or e_lname.get()=="" or e_passw.get()=="" or e_email.get()==""
                    or e_phone_no.get()=="" ):
               MessageBox.showinfo("Güncelleme başarısız", "Tüm alanlar doldurulmalıdır.")
            else:
               try:
                  fonksiyonlar.connect(self)
                  self.cursor.execute("select * from customer where customer_id='" + acc_no + "'")
                  myresult = self.cursor.fetchall()
                  print(myresult)
                  if(len(myresult)==0):
                     MessageBox.showinfo("Hata", "Müşteri bulunamadı")
                  else:
                     self.cursor.execute(
                        "update customer set firstname= '" + e_fname.get() + "' ,lastname= '" +
                        e_lname.get() + "' , password= '" + e_passw.get() + "',email= '" + e_email.get()
                        + "' , phone= '" + e_phone_no.get() + "'  where customer_id='" + acc_no + "'")
                     MessageBox.showinfo("Durum", "Güncelleme Başarılı")
                     self.con.commit()
                     self.con.close()
               except:
                  MessageBox.showinfo("Durum", "İsim ve soyisim karakterlerden oluşmalıdır")

      # frames

      self.top = Frame(master, height=100, bg="white")
      self.top.pack(fill=X)

      self.bottom = Frame(master, height=900, bg="#AED6F1")
      self.bottom.pack(fill=X)

      # top Frame design
      self.heading = Label(self.top, text="Hesap detaylarını değiştir", font="arial 18 bold", bg="white")
      self.heading.place(x=255, y=30)

      # bottom Frame Design

      # buttons and label
      acc_no = DoubleVar()
      acc_no = Label(self.bottom, text="Hesap numarası ", font="arial 14 bold", bg="#AED6F1")
      acc_no.place(x=40, y=40)

      fname = Label(self.bottom, text="İsim ", font="arial 14 bold", bg="#AED6F1")
      fname.place(x=40, y=95)

      lname = Label(self.bottom, text="Soyisim ", font="arial 14 bold", bg="#AED6F1")
      lname.place(x=40, y=150)

      passw = Label(self.bottom, text="Şifre ", font="arial 14 bold", bg="#AED6F1")
      passw.place(x=40, y=205)

      email = Label(self.bottom, text="Email ", font="arial 14 bold", bg="#AED6F1")
      email.place(x=40, y=260)

      phone_no = DoubleVar()
      phone_no = Label(self.bottom, text="Telefon numarası ", font="arial 14 bold", bg="#AED6F1")
      phone_no.place(x=40, y=315)

      # entries

      e_acc_no = Entry(self.bottom, width=40)
      e_acc_no.place(x=320, y=40)

      e_fname = Entry(self.bottom, width=40)
      e_fname.place(x=320, y=95)

      e_lname = Entry(self.bottom, width=40)
      e_lname.place(x=320, y=150)

      e_passw = Entry(self.bottom, width=40)
      e_passw.place(x=320, y=205)

      e_email = Entry(self.bottom, width=40)
      e_email.place(x=320, y=260)

      e_phone_no = Entry(self.bottom, width=40)
      e_phone_no.place(x=320, y=315)

      # entries

      # submit
      self.submit = Button(self.bottom, text=" Güncelle ", font="arial 15 bold", width="10", command=sub)
      self.submit.place(x=600, y=55)

      self.qt = Button(self.bottom, text=" Çıkış ", font="arial 15 bold", width="10", command=quit)
      self.qt.place(x=600, y=200)

class bakiyeGoster:
   def __init__(self, master=None):
      self.master = master
      self.master.geometry("700x400+200+20")
      self.master.resizable(height=0, width=0)

      def sub():
         acc_no = DoubleVar()
         acc_no = (e_acc_no.get())
         lb.delete(0, 'end')
         if (acc_no == ""):
            MessageBox.showinfo("Hatalı giriş", "Müşteri numarası girilmeli")
         elif not (acc_no.isnumeric()):
            MessageBox.showinfo("Hata", "Müşteri numarası tamsayı girilmelidir")
         else:
            fonksiyonlar.connect(self)
            self.cursor.execute("select balance from bankacc where acc_id='" + acc_no + "'")
            myresult = self.cursor.fetchall()
            if (len(myresult) == 0):
               MessageBox.showinfo("Hata", " Hesap mevcut değil")
            else:
               for x in myresult:
                  print(x)
                  lb.insert(0, x[0])
               # self.cursor.execute("commit")
            self.con.close()

      # frames

      self.top = Frame(master, height=100, bg="white")
      self.top.pack(fill=X)

      self.bottom = Frame(master, height=800, bg="#AED6F1")
      self.bottom.pack(fill=X)

      # top Frame design

      self.heading = Label(self.top, text="Bakiye sorgulama", font="arial 18 bold", bg="white")
      self.heading.place(x=265, y=30)

      # bottom Frame Design

      # buttons and label
      acc_no = DoubleVar()
      acc_no = Label(self.bottom, text="Müşteri numarası ", font="arial 14 bold", bg="#AED6F1")
      acc_no.place(x=40, y=55)

      detail = Label(self.bottom, text="Bakiye -> ", font="arial 14 bold", bg="#AED6F1")
      detail.place(x=40, y=110)

      # entries

      e_acc_no = Entry(self.bottom, width=60)
      e_acc_no.place(x=320, y=55)

      # list
      lb = Entry(self.bottom, width=60)
      lb.place(x=320, y=110)

      # submit
      self.submit = Button(self.bottom, text=" Göster ", font="arial 15 bold", width="52", command=sub)
      self.submit.place(x=45, y=200)


class paraYatir(object):
   def __init__(self, master=None):
      self.master = master
      self.master.geometry("700x500+500+200")
      self.master.resizable(height=0, width=0)
      self.filepath = os.getcwd()

      def upd():
         acc_no = DoubleVar()
         acc_no = (e_acc_no.get())
         if (acc_no == ""):
            MessageBox.showinfo("Gerekli alanlar doldurulmalı", "Lütfen hesap numarası giriniz")
         else:
            fonksiyonlar.connect(self)
            self.cursor.execute("select balance from bankacc where acc_id='" + acc_no + "'")
            myresul = self.cursor.fetchall()
            for x in myresul:
               # print(x)
               e_gncbky.insert(0, x[0])
            # self.cursor.execute("commit")
            self.con.commit()
            MessageBox.showinfo("Bakiye durumu", "Başarıyla Yatırıldı")
            self.con.close()

      def updt():
         amtn = dp.get()
         acc_no = DoubleVar()
         acc_no = (e_acc_no.get())
         fonksiyonlar.connect(self)
         # self.cursor.execute("update bankacc set balance= balance - ('" + amtn + "') where acc_id='" + acc_no + "'")
         self.cursor.execute("select balance from bankacc where acc_id='" + acc_no + "'")
         bakiye = self.cursor.fetchall()[0][0]
         if not (amtn.isnumeric()):
            MessageBox.showinfo("Hatalı giriş", "Tutar tamsayı olmalıdır.")
         else:
            if (int(amtn) <= 0):
               MessageBox.showinfo("Hata", "Yatırılacak tutar negatif olamaz")
            else:
               e_gncbky.delete(0, END)
               self.cursor.execute(
                  "update bankacc set balance= balance + ('" + amtn + "') where acc_id='" + acc_no + "'")
               self.con.commit()
               self.con.close()
               upd()

      def bakiye_goster():
         acc_no = DoubleVar()
         acc_no = (e_acc_no.get())
         lb.delete(0, END)
         if (acc_no == ""):
            MessageBox.showinfo("Gerekli alanlar doldurulmalı", "Lütfen hesap numarası giriniz")
         elif not (acc_no.isnumeric()):
            MessageBox.showinfo("Hata", "Müşteri numarası tamsayı girilmelidir")
         else:
            fonksiyonlar.connect(self)
            self.cursor.execute("select balance from bankacc where acc_id='" + acc_no + "'")
            myresult = self.cursor.fetchall()
            if (len(myresult) == 0):
               MessageBox.showinfo("Hata", "Müşteri numarası bulunamadı")
            else:
               for x in myresult:
                  # print(x)
                  lb.insert(0, x[0])
               self.con.commit()
               self.con.close()

      # frames

      self.top = Frame(master, height=100, bg="white")
      self.top.pack(fill=X)

      self.bottom = Frame(master, height=800, bg="#AED6F1")
      self.bottom.pack(fill=X)

      # top Frame design
      self.top_image = PhotoImage(file=self.filepath+"/icon/money1.png")
      self.top_image_label = Label(self.top, image=self.top_image, bg="white")
      self.top_image_label.place(x=50, y=15)

      self.top_image2 = PhotoImage(file=self.filepath+"/icon/money1.png")
      self.top_image2_label = Label(self.top, image=self.top_image, bg="white")
      self.top_image2_label.place(x=580, y=15)

      self.heading = Label(self.top, text="Para Yatırma", font="arial 18 bold", bg="white")
      self.heading.place(x=265, y=30)

      # bottom Frame Design

      # buttons and label
      acc_no = DoubleVar()
      acc_no = Label(self.bottom, text="Hesap numarası ", font="arial 14 bold", bg="#AED6F1")
      acc_no.place(x=40, y=55)

      detail = Label(self.bottom, text="Mevcut Bakiye ", font="arial 14 bold", bg="#AED6F1")
      detail.place(x=40, y=110)

      amt = Label(self.bottom, text="Çekilecek tutar ", font="arial 14 bold", bg="#AED6F1")
      amt.place(x=40, y=165)

      upb = Label(self.bottom, text="Güncellenmiş bakiye ", font="arial 14 bold", bg="#AED6F1")
      upb.place(x=40, y=220)

      # entries

      e_acc_no = Entry(self.bottom, width=60)
      e_acc_no.place(x=320, y=55)

      lb = Entry(self.bottom, width=60)
      lb.place(x=320, y=110)

      dp = Entry(self.bottom, width=60)
      dp.place(x=320, y=165)

      e_gncbky = Entry(self.bottom, width=60)
      e_gncbky.place(x=320, y=220)

      # submit
      self.submit = Button(self.bottom, text=" Göster ", font="arial 15 bold", width="52", command=bakiye_goster)
      self.submit.place(x=45, y=270)

      self.dep = Button(self.bottom, text=" Yatır ", font="arial 15 bold", width="52", command=updt)
      self.dep.place(x=45, y=330)

class paraCek(object):
   def __init__(self, master=None):
      self.master = master
      self.master.geometry("700x500+500+200")
      self.master.resizable(height=0, width=0)
      self.filepath = os.getcwd()

      def upd():
         acc_no = DoubleVar()
         acc_no = (e_acc_no.get())
         if (acc_no == ""):
            MessageBox.showinfo("Gerekli alanlar doldurulmalı", "Lütfen hesap numarası giriniz")
         else:
            fonksiyonlar.connect(self)
            self.cursor.execute("select balance from bankacc where acc_id='" + acc_no + "'")
            myresult = self.cursor.fetchall()
            for x in myresult:
               # print(x)
               e_gncbky.insert(0, x[0])
            self.con.commit()
            MessageBox.showinfo("Bakiye durumu", "Başarıyla Çekildi")
            self.con.close()

      def updt():
         amtn = dp.get()
         acc_no = DoubleVar()
         acc_no = (e_acc_no.get())
         fonksiyonlar.connect(self)
         # self.cursor.execute("update bankacc set balance= balance - ('" + amtn + "') where acc_id='" + acc_no + "'")
         self.cursor.execute("select balance from bankacc where acc_id='" + acc_no + "'")
         bakiye = self.cursor.fetchall()[0][0]
         if not (amtn.isnumeric()):
            MessageBox.showinfo("Hatalı giriş", "Tutar tamsayı olmalıdır.")
         else:
            if (int(amtn) > 0):
               if (int(amtn) > bakiye):
                  MessageBox.showinfo("Hata", "Çekilecek tutar bakiyeden büyük olamaz")
               else:
                  e_gncbky.delete(0, END)
                  self.cursor.execute(
                     "update bankacc set balance= balance - ('" + amtn + "') where acc_id='" + acc_no + "'")
                  # self.cursor.execute("commit")
                  self.con.commit()
                  self.con.close()
                  upd()
            else:
               MessageBox.showinfo("Hata", "Çekilecek tutar negatif olamaz")

      def bakiye_goster():
         acc_no = DoubleVar()
         acc_no = (e_acc_no.get())
         lb.delete(0, END)
         if (acc_no == ""):
            MessageBox.showinfo("Gerekli alanlar doldurulmalı", "Lütfen hesap numarası giriniz")
         elif not (acc_no.isnumeric()):
            MessageBox.showinfo("Hata", "Müşteri numarası tamsayı girilmelidir")
         else:
            fonksiyonlar.connect(self)
            self.cursor.execute("select balance from bankacc where acc_id='" + acc_no + "'")
            myresult = self.cursor.fetchall()
            if(len(myresult)==0):
               MessageBox.showinfo("Hata", "Müşteri numarası bulunamadı")
            else:
               for x in myresult:
                  # print(x)
                  lb.insert(0, x[0])
               # self.cursor.execute("commit")
               self.con.commit()
               self.con.close()

      # frames

      self.top = Frame(master, height=100, bg="white")
      self.top.pack(fill=X)

      self.bottom = Frame(master, height=800, bg="#AED6F1")
      self.bottom.pack(fill=X)

      # top Frame design

      self.top_image = PhotoImage(file=self.filepath+"/icon/money1.png")
      self.top_image_label = Label(self.top, image=self.top_image, bg="white")
      self.top_image_label.place(x=50, y=15)

      self.top_image2 = PhotoImage(file=self.filepath+"/icon/money1.png")
      self.top_image2_label = Label(self.top, image=self.top_image, bg="white")
      self.top_image2_label.place(x=580, y=15)

      self.heading = Label(self.top, text="Para Çekme", font="arial 18 bold", bg="white")
      self.heading.place(x=265, y=30)

      # bottom Frame Design

      # buttons and label
      acc_no = DoubleVar()
      acc_no = Label(self.bottom, text="Hesap numarası ", font="arial 14 bold", bg="#AED6F1")
      acc_no.place(x=40, y=55)

      detail = Label(self.bottom, text="Mevcut Bakiye ", font="arial 14 bold", bg="#AED6F1")
      detail.place(x=40, y=110)

      amt = Label(self.bottom, text="Çekilecek tutar ", font="arial 14 bold", bg="#AED6F1")
      amt.place(x=40, y=165)

      upb = Label(self.bottom, text="Güncellenmiş Bakiye ", font="arial 14 bold", bg="#AED6F1")
      upb.place(x=40, y=220)

      # entries

      e_acc_no = Entry(self.bottom, width=60)
      e_acc_no.place(x=320, y=55)

      lb = Entry(self.bottom, width=60)
      lb.place(x=320, y=110)

      dp = Entry(self.bottom, width=60)
      dp.place(x=320, y=165)

      e_gncbky = Entry(self.bottom, width=60)
      e_gncbky.place(x=320, y=220)

      # submit
      self.submit = Button(self.bottom, text=" Göster ", font="arial 15 bold", width="52", command=bakiye_goster)
      self.submit.place(x=45, y=270)

      self.dep = Button(self.bottom, text=" Para çek ", font="arial 15 bold", width="52", command=updt)
      self.dep.place(x=45, y=330)

class islemListele:
   def __init__(self, master=None):
      self.master = master
      self.master.geometry("800x700+200+0")
      self.master.resizable(height=0, width=0)
      fonksiyonlar.getloginid(self)

      def show():

         for item in tree.get_children():
            tree.delete(item)

         xislem = (e_islem.get())
         fonksiyonlar.connect(self)
         self.cursor.execute("select * from customer where customerserv_id='" + self.loginid + "'")
         myresult = self.cursor.fetchall()
         print(myresult)
         custservidlst = []
         for x in range(len(myresult)):
            custservidlst.append(str(myresult[x][0]))
         print(custservidlst)
         cstsrvlst=" ".join("'"+(x)+"'," for x in custservidlst)
         print(cstsrvlst[:-1])
         self.cursor.execute("Select * from transactions where kaynak in " + "("+cstsrvlst[:-1]+")" + "")
         records = self.cursor.fetchall()

         if(xislem==''):
            for i,(islem_no, kaynak, hedef, islem, tutar, kaynak_bakiye, hedef_bakiye, tarih)  \
                    in enumerate(records, start=1):
               tree.insert("", "end", values=(islem_no, kaynak, hedef, islem, tutar, kaynak_bakiye, hedef_bakiye, tarih))
         else:
            if(int(xislem)>len(records)):
               MessageBox.showinfo("Hatalı giriş", "Listelenecek kayıtlar tüm kayıtlardan büyük olamaz")
            else:
               for i,(islem_no, kaynak, hedef, islem, tutar, kaynak_bakiye, hedef_bakiye, tarih)  \
                       in enumerate(records[len(records) - int(xislem):], start=1):
                  tree.insert("", "end", values=(islem_no, kaynak, hedef, islem, tutar, kaynak_bakiye, hedef_bakiye, tarih))
         self.con.close()

      # cols =('islem_no', 'kaynak', 'hedef', 'islem', 'tutar', 'kaynak_bakiye', 'hedef_bakiye', 'tarih')
      # listBox = ttk.Treeview(master, columns=cols, show='headings')
      #
      # for col in cols:
      #    listBox.heading(col, text=col)
      #    listBox.grid(row=1, column=0, columnspan=2)

      tree = ttk.Treeview(master, selectmode="extended", columns=("H", "A", "B", "C", "D", "E", "F", "G"), show='headings')
      tree.pack(expand=YES, fill=BOTH)
      tree.heading("H", text="İşlem No")
      tree.column("H", minwidth=100, width=100, stretch=NO)
      tree.heading("A", text="Kaynak")
      tree.column("A", minwidth=100, width=100, stretch=NO)
      tree.heading("B", text="Hedef")
      tree.column("B", minwidth=100, width=100, stretch=NO)
      tree.heading("C", text="İşlem")
      tree.column("C", minwidth=100, width=100, stretch=NO)
      tree.heading("D", text="Tutar")
      tree.column("D", minwidth=100, width=100, stretch=NO)
      tree.heading("E", text="Kaynak Bakiye")
      tree.column("E", minwidth=100, width=100, stretch=NO)
      tree.heading("F", text="Hedef Bakiye")
      tree.column("F", minwidth=100, width=100, stretch=NO)
      tree.heading("G", text="Tarih")
      tree.column("G", minwidth=100, width=100, stretch=NO)


      # self.top = Frame(master, height=100, bg="white")
      # self.top.pack(fill=X)

      self.bottom = Frame(master, height=250, bg="#AED6F1")
      self.bottom.pack(fill=X)

      # entry + lbl
      islemsayisi = Label(self.bottom, text="Son x işlemi görüntüle ->", font="arial 14 bold", bg="#AED6F1")
      islemsayisi.place(x=40, y=57)

      e_islem = Entry(self.bottom, width=40)
      e_islem.place(x=275, y=60)

      # submit
      self.submit = Button(self.bottom, text=" Listele ", font="arial 15 bold", width="20", command=show)
      self.submit.place(x=275, y=100)