import os
from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as MessageBox
from fonksiyonlar import fonksiyonlar

class adminEkran:
  def __init__(self, master=None):
     self.master=master
     self.master.geometry("600x700+420+55")
     self.master.resizable(height=0, width=0)
     master.title(" Yönetici ")

     #frames

     self.top= Frame(master, height=100 , bg= "white")
     self.top.pack(fill=X)

     self.bottom= Frame(master, height=600, bg="#82E0AA")
     self.bottom.pack(fill=X)

     #top Frame design
     self.heading= Label(self.top, text="Banka Yönetim Sistemi", font="arial 15 bold", bg="white")
     self.heading.place(x= 180, y=30)

     #buttons

     #create acc
     self.ca= Button(self.bottom, text=" Müşteri oluştur ", font="arial 13 bold", command=self.musteri_Olustur, width=20)
     self.ca.place(x=40, y=50)
     self.ca_lbl = Label(self.bottom, text="> Yeni müşteri oluştur", bg="#82E0AA", font="arial 13 bold")
     self.ca_lbl.place(x=280, y=52)

     #yeni para birimi
     self.Be= Button(self.bottom, text=" Kur işlemleri ", font="arial 13 bold", command=self.kur_guncelle, width=20)
     self.Be.place(x=40, y=120)
     self.be_lbl = Label(self.bottom, text="> Mevcut para birimlerini güncelle", bg="#82E0AA", font="arial 13 bold")
     self.be_lbl.place(x=280, y=122)

     #yeni kur ekle
     self.Caa= Button(self.bottom, text=" Kur işlemleri ", font="arial 13 bold", command=self.kur_ekle, width=20)
     self.Caa.place(x=40, y=190)
     self.caa_lbl = Label(self.bottom, text="> Yeni para birimi ekle", bg="#82E0AA", font="arial 13 bold")
     self.caa_lbl.place(x=280, y=192)

     #maas güncelle
     self.Bw= Button(self.bottom, text="Maaş güncelle ", font="arial 13 bold", command=self.maas_guncelle, width=20)
     self.Bw.place(x=40, y=260)
     self.bw_lbl = Label(self.bottom, text="> Çalışanların maaşını değiştir", bg="#82E0AA", font="arial 13 bold")
     self.bw_lbl.place(x=280, y=262)

     # Kredi ve gecikme faiz oranı
     self.Bd= Button(self.bottom, text=" Kredi faiz oranı ", font="arial 13 bold", command=self.kforani_degistir, width=20)
     self.Bd.place(x=40, y=330)
     self.bd_lbl = Label(self.bottom, text="> Kredi ve gecikme faiz oranını güncelle ", bg="#82E0AA", font="arial 13 bold")
     self.bd_lbl.place(x=280, y=332)

     # txd list
     self.kfo= Button(self.bottom, text=" İşlemleri listele ", font="arial 13 bold", command=self.islem_listele, width=20)
     self.kfo.place(x=40, y=400)
     self.kfo_lbl = Label(self.bottom, text="> İşlem geçmişini görüntüle ", bg="#82E0AA", font="arial 13 bold")
     self.kfo_lbl.place(x=280, y=402)


  def musteri_Olustur(self):
     musteriOlustur(Toplevel(self.master))
  def kur_guncelle(self):
     kurGuncelle(Toplevel(self.master))
  def kur_ekle(self):
     kurEkle(Toplevel(self.master))
  def maas_guncelle(self):
     maasGuncelle(Toplevel(self.master))
  def islem_listele(self):
     islemListele(Toplevel(self.master))
  def kforani_degistir(self):
     kforaniDegistir(Toplevel(self.master))

class musteriOlustur:
   def __init__(self, master=None):
      self.master = master
      self.master.geometry("900x700+200+0")
      self.master.resizable(height=0, width=0)

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
               self.cursor.execute(
                  'insert into customer(password,firstname,lastname,email,phone,customerserv_id) values(?,?,?,?,?,?);',
                  (password, fname, lname, email, phone_no, 1)
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
               MessageBox.showinfo("Durum", "İsim ve soyisim karakterlerden oluşmalıdır")

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

      # entries

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

class kurGuncelle:
   def __init__(self, master=None):
      self.master = master
      self.master.geometry("700x400+200+20")
      self.master.resizable(height=0, width=0)

      def sub():
         ccyname = DoubleVar()
         ccyname = (e_ccyname.get())
         lb.delete(0, 'end')
         if (ccyname == ""):
            MessageBox.showinfo("Hatalı giriş", "Kur ismi giriniz")
         else:
            fonksiyonlar.connect(self)
            self.cursor.execute("select * from currency where currency_name='" + ccyname + "'")
            myresult = self.cursor.fetchall()
            for x in myresult:
               print(x)
               lb.insert(0, x[2])
            # self.cursor.execute("commit")
            self.con.close()
      def updt():
         ccyvalue = DoubleVar()
         ccyvalue = (e_ccyvalue.get())
         ccyname = (e_ccyname.get())
         lb.delete(0, 'end')
         if (ccyname == ""or ccyvalue == ""):
            MessageBox.showinfo("Hatalı giriş", "Kur ismi giriniz")
         else:
            fonksiyonlar.connect(self)
            self.cursor.execute("update currency set currency_price='" + ccyvalue +"'  where currency_name='" + ccyname + "'")
            # myresult = self.cursor.fetchall()
            # for x in myresult:
            #    print(x)
            #    lb.insert(0, x[2])
            self.con.commit()
            self.con.close()

      # frames

      self.top = Frame(master, height=100, bg="white")
      self.top.pack(fill=X)

      self.bottom = Frame(master, height=800, bg="#AED6F1")
      self.bottom.pack(fill=X)

      # top Frame design

      self.heading = Label(self.top, text="Kur değerini güncelleme", font="arial 18 bold", bg="white")
      self.heading.place(x=265, y=30)

      # bottom Frame Design

      # buttons and label
      ccyname = DoubleVar()
      ccyname = Label(self.bottom, text="Güncellenecek Kur ismi ", font="arial 14 bold", bg="#AED6F1")
      ccyname.place(x=40, y=55)

      detail = Label(self.bottom, text="Mevcut Kur değeri -> ", font="arial 14 bold", bg="#AED6F1")
      detail.place(x=40, y=110)

      ccyvalue = Label(self.bottom, text="Güncellenecek değer -> ", font="arial 14 bold", bg="#AED6F1")
      ccyvalue.place(x=40, y=165)

      # entries

      e_ccyname = Entry(self.bottom, width=60)
      e_ccyname.place(x=320, y=55)

      e_ccyvalue = Entry(self.bottom, width=60)
      e_ccyvalue.place(x=320, y=165)

      # list
      lb = Entry(self.bottom, width=60)
      lb.place(x=320, y=110)

      # submit
      self.submit = Button(self.bottom, text=" Göster ", font="arial 15 bold", width="20", command=sub)
      self.submit.place(x=45, y=210)

      self.updt = Button(self.bottom, text=" Güncelle ", font="arial 15 bold", width="20", command=updt)
      self.updt.place(x=350, y=210)

class kurEkle:
   def __init__(self, master=None):
      self.master = master
      self.master.geometry("700x400+200+20")
      self.master.resizable(height=0, width=0)

      def ekle():
         ccyvalue = DoubleVar()
         ccyvalue = (e_ccyvalue.get())
         ccyname = (e_ccyname.get())
         # lb.delete(0, 'end')
         if (ccyname == "" or ccyvalue == ""):
            MessageBox.showinfo("Hatalı giriş", "Kur ismi ve kur değeri giriniz")
         else:
            fonksiyonlar.connect(self)
            self.cursor.execute('insert into currency(currency_name,currency_price) values(?,?);',
                   (ccyname,ccyvalue)
                   )
            self.con.commit()
            MessageBox.showinfo("Durum", "Oluşturma başarılı")
            self.con.close()

      # frames

      self.top = Frame(master, height=100, bg="white")
      self.top.pack(fill=X)

      self.bottom = Frame(master, height=800, bg="#AED6F1")
      self.bottom.pack(fill=X)

      # top Frame design

      self.heading = Label(self.top, text="Yeni para birimi ekleme", font="arial 18 bold", bg="white")
      self.heading.place(x=235, y=30)

      # bottom Frame Design

      # buttons and label
      ccyname = DoubleVar()
      ccyname = Label(self.bottom, text="Eklenecek Kur ismi ", font="arial 14 bold", bg="#AED6F1")
      ccyname.place(x=40, y=55)

      ccyvalue = Label(self.bottom, text="Kur değeri -> ", font="arial 14 bold", bg="#AED6F1")
      ccyvalue.place(x=40, y=106)

      # entries

      e_ccyname = Entry(self.bottom, width=60)
      e_ccyname.place(x=320, y=55)

      e_ccyvalue = Entry(self.bottom, width=60)
      e_ccyvalue.place(x=320, y=110)

      # submit
      self.submit = Button(self.bottom, text=" Ekle ", font="arial 15 bold", width="20", command=ekle)
      self.submit.place(x=250, y=200)

class maasGuncelle:
   def __init__(self, master=None):
      self.master = master
      self.master.geometry("700x400+200+20")
      self.master.resizable(height=0, width=0)

      def updt():
         yenimaas = DoubleVar()
         yenimaas = (e_yenimaas.get())
         if (yenimaas == ""):
            MessageBox.showinfo("Hatalı giriş", "Maaş bilgisi giriniz")
         elif not (yenimaas.isnumeric()):
            MessageBox.showinfo("Hata", "Yeni maaş tamsayı girilmelidir")
         else:
            fonksiyonlar.connect(self)
            self.cursor.execute("update manager set emp_salary='" + yenimaas + "'")
            self.con.commit()
            MessageBox.showinfo("Durum", "Maaş güncellendi")
            self.con.close()

      # frames

      self.top = Frame(master, height=100, bg="white")
      self.top.pack(fill=X)

      self.bottom = Frame(master, height=800, bg="#AED6F1")
      self.bottom.pack(fill=X)

      # top Frame design

      self.heading = Label(self.top, text="Çalışanların maaş ücretini güncelle", font="arial 18 bold", bg="white")
      self.heading.place(x=150, y=30)

      # bottom Frame Design

      # buttons and label
      yenimaas = DoubleVar()
      yenimaas = Label(self.bottom, text="Yeni maaş ->", font="arial 14 bold", bg="#AED6F1")
      yenimaas.place(x=40, y=53)

      # entries

      e_yenimaas = Entry(self.bottom, width=40)
      e_yenimaas.place(x=275, y=55)

      # submit
      self.submit = Button(self.bottom, text=" Güncelle ", font="arial 15 bold", width="20", command=updt)
      self.submit.place(x=250, y=200)

class kforaniDegistir:
   def __init__(self, master=None):
      self.master = master
      self.master.geometry("700x400+200+20")
      self.master.resizable(height=0, width=0)

      def updtfaiz():
         faizorani = DoubleVar()
         faizorani = (e_faizorani.get())
         if (faizorani == ""):
            MessageBox.showinfo("Hatalı giriş", "Faiz oranı giriniz")
         elif not (faizorani.isnumeric()):
            MessageBox.showinfo("Hata", "Faiz oranı tamsayı girilmelidir")
         else:
            fonksiyonlar.connect(self)
            self.cursor.execute("update crdratio set int_ratio='" + faizorani + "'")
            self.con.commit()
            MessageBox.showinfo("Durum", "Oran güncellendi")
            self.con.close()
      def updtkredi():
         krediorani = DoubleVar()
         krediorani = (e_krediorani.get())
         if (krediorani == ""):
            MessageBox.showinfo("Hatalı giriş", "Kredi oranı giriniz")
         elif not (krediorani.isnumeric()):
            MessageBox.showinfo("Hata", "Kredi oranı tamsayı girilmelidir")
         else:
            fonksiyonlar.connect(self)
            self.cursor.execute("update crdratio set credit_ratio='" + krediorani + "'")
            self.con.commit()
            MessageBox.showinfo("Durum", "Oran güncellendi")
            self.con.close()

      # frames

      self.top = Frame(master, height=100, bg="white")
      self.top.pack(fill=X)

      self.bottom = Frame(master, height=800, bg="#AED6F1")
      self.bottom.pack(fill=X)

      # top Frame design

      self.heading = Label(self.top, text="Kredi ve gecikme faiz oranını güncelle", font="arial 18 bold", bg="white")
      self.heading.place(x=150, y=30)

      # bottom Frame Design

      # buttons and label
      krediorani = DoubleVar()
      krediorani = Label(self.bottom, text="Yeni kredi oranı ->", font="arial 14 bold", bg="#AED6F1")
      krediorani.place(x=40, y=53)

      faizorani = DoubleVar()
      faizorani = Label(self.bottom, text="Yeni faiz oranı ->", font="arial 14 bold", bg="#AED6F1")
      faizorani.place(x=40, y=103)

      # entries

      e_krediorani = Entry(self.bottom, width=40)
      e_krediorani.place(x=275, y=55)

      e_faizorani = Entry(self.bottom, width=40)
      e_faizorani.place(x=275, y=103)


      # submit
      self.submitk = Button(self.bottom, text=" Krediyi güncelle ", font="arial 15 bold", width="20", command=updtkredi)
      self.submitk.place(x=85, y=200)

      self.submitf = Button(self.bottom, text=" Faizi güncelle ", font="arial 15 bold", width="20", command=updtfaiz)
      self.submitf.place(x=360, y=200)

class islemListele:
   def __init__(self, master=None):
      self.master = master
      self.master.geometry("800x700+200+0")
      self.master.resizable(height=0, width=0)

      def show():

         for item in tree.get_children():
            tree.delete(item)

         xislem = (e_islem.get())
         fonksiyonlar.connect(self)
         self.cursor.execute("Select * from transactions")
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

