import os
from tkinter import *
import tkinter.messagebox as MessageBox
from fonksiyonlar import fonksiyonlar
from datetime import date

class musteriEkran:
  def __init__(self, master=None):
     self.master=master
     self.master.geometry("600x580+420+105")
     self.master.resizable(height=0, width=0)
     master.title(" Müşteri ")

     #frames

     self.top= Frame(master, height=100 , bg= "white")
     self.top.pack(fill=X)

     self.bottom= Frame(master, height=530, bg="#AED6F1")
     self.bottom.pack(fill=X)


     self.heading= Label(self.top, text="Banka Yönetim Sistemi", font="arial 15 bold", bg="white")
     self.heading.place(x= 180, y=30)


     #buttons

     #Balance enquiry
     self.gnc= Button(self.bottom, text=" Bilgileri güncelle ", font="arial 13 bold", command=self.musteri_guncelle,
                      width=20)
     self.gnc.place(x=80, y=100)
     self.gnc_lbl = Label(self.bottom, text="> Bilgileri güncelle", bg="#AED6F1", font="arial 13 bold")
     self.gnc_lbl.place(x=320, y=102)

     self.ck = Button(self.bottom, text=" Para çek ", font="arial 13 bold", command=self.para_cek, width=20)
     self.ck.place(x=80, y=150)
     self.ck_lbl = Label(self.bottom, text="> Hesaptan para çek", bg="#AED6F1", font="arial 13 bold")
     self.ck_lbl.place(x=320, y=152)

     self.ck = Button(self.bottom, text=" Para yatır ", font="arial 13 bold", command=self.para_yatir, width=20)
     self.ck.place(x=80, y=200)
     self.ck_lbl = Label(self.bottom, text="> Hesaba para yatır", bg="#AED6F1", font="arial 13 bold")
     self.ck_lbl.place(x=320, y=202)

     self.ck = Button(self.bottom, text=" Bakiye öğren ", font="arial 13 bold", command=self.bakiye_goster, width=20)
     self.ck.place(x=80, y=250)
     self.ck_lbl = Label(self.bottom, text="> Hesap bakiyesini göster ", bg="#AED6F1", font="arial 13 bold")
     self.ck_lbl.place(x=320, y=252)

     self.ck = Button(self.bottom, text=" Para transferi yap ", font="arial 13 bold", command=self.para_transfer, width=20)
     self.ck.place(x=80, y=300)
     self.ck_lbl = Label(self.bottom, text="> Hesaba para gönder ", bg="#AED6F1", font="arial 13 bold")
     self.ck_lbl.place(x=320, y=302)

     self.ck = Button(self.bottom, text=" Hesap oluştur ", font="arial 13 bold", command=self.crt_bankacc,
                      width=20)
     self.ck.place(x=80, y=350)
     self.ck_lbl = Label(self.bottom, text="> Yeni banka hesabı aç ", bg="#AED6F1", font="arial 13 bold")
     self.ck_lbl.place(x=320, y=352)


  def musteri_guncelle(self):
      musteriGuncelle(Toplevel(self.master))
  def para_cek(self):
      paraCek(Toplevel(self.master))
  def para_yatir(self):
      paraYatir(Toplevel(self.master))
  def bakiye_goster(self):
     bakiyeGoster(Toplevel(self.master))
  def para_transfer(self):
     paraTransfer(Toplevel(self.master))
  def crt_bankacc(self):
     crtbankacc(Toplevel(self.master))

class musteriGuncelle:
   def __init__(self, master=None):
      self.master = master
      self.master.geometry("750x650+200+20")
      self.master.resizable(height=0, width=0)
      fonksiyonlar.getloginid(self)

      def sub():
         if (e_fname.get() == "" or e_lname.get() == "" or e_passw.get() == "" or e_email.get() == ""
                 or e_phone_no.get() == ""):
            MessageBox.showinfo("Güncelleme başarısız", "Tüm alanlar doldurulmalıdır.")
         else:
            try:
               fonksiyonlar.connect(self)
               self.cursor.execute(
                  "update customer set firstname= '" + e_fname.get() + "' ,lastname= '" + e_lname.get() + "' , password= '" + e_passw.get() + "',email= '" + e_email.get() + "' , phone= '" + e_phone_no.get() + "'  where customer_id='" + self.loginid + "'")
               MessageBox.showinfo("Update status", "Updated Sucessfully")
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

      # buttons and labels
      custid = Label(self.bottom, text="Müşteri numaranız : "+self.loginid, font="arial 14 bold", bg="#AED6F1", fg="#2471A3")
      custid.place(x=40, y=45)

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

class paraCek(object):
   def __init__(self, master=None):
      self.master = master
      self.master.geometry("700x500+500+200")
      self.master.resizable(height=0, width=0)
      fonksiyonlar.getloginid(self)
      self.filepath = os.getcwd()

      def upd():
         fonksiyonlar.connect(self)
         self.cursor.execute("select balance from bankacc where customer_id='" + self.loginid + "'")
         myresul = self.cursor.fetchall()
         for x in myresul:
            # print(x)
            fb.insert(0, x[0])
         self.con.commit()
         MessageBox.showinfo("Bakiye durumu", "Başarıyla Çekildi")
         self.con.close()

      def updt():
         today = date.today()
         amtn = dp.get()
         fonksiyonlar.connect(self)
         # self.cursor.execute("update bankacc set balance= balance - ('" + amtn + "') where acc_id='" + acc_no + "'")
         self.cursor.execute("select balance from bankacc where customer_id='" + self.loginid + "'")
         bakiye = self.cursor.fetchall()[0][0]
         # print(int(amtn))
         if not (amtn.isnumeric()):
            MessageBox.showinfo("Hatalı giriş", "Tutar tamsayı olmalıdır.")
         else:
            if (int(amtn) > 0):
               if (int(amtn) > bakiye):
                  MessageBox.showinfo("Hata", "Çekilecek tutar bakiyeden büyük olamaz")
               else:
                  fb.delete(0, END)
                  self.cursor.execute(
                     "update bankacc set balance= balance - ('" + amtn + "') where customer_id='" + self.loginid + "'")
                  self.cursor.execute("select balance from bankacc where customer_id='" + self.loginid + "'")
                  resultkb = self.cursor.fetchall()[0][0]
                  print(resultkb)
                  self.cursor.execute(
                     'insert into transactions(kaynak,hedef,islem,tutar,hedef_bakiye,tarih) values(?,?,?,?,?,?);',
                     ("banka", self.loginid, "bankadan çekme", amtn, resultkb, today)
                  )
                  self.con.commit()
                  self.con.close()
                  upd()
            else:
               MessageBox.showinfo("Hata", "Çekilecek tutar negatif olamaz")

      def bakiye_goster():
         lb.delete(0, END)

         fonksiyonlar.connect(self)
         self.cursor.execute("select balance from bankacc where customer_id='" + self.loginid + "'")
         myresult = self.cursor.fetchall()
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

      self.heading = Label(self.top, text="Para Çek", font="arial 18 bold", bg="white")
      self.heading.place(x=265, y=30)

      # bottom Frame Design

      # buttons and labels

      detail = Label(self.bottom, text="Mevcut Bakiye ", font="arial 14 bold", bg="#AED6F1")
      detail.place(x=40, y=110)

      amt = Label(self.bottom, text="Çekilecek tutar ", font="arial 14 bold", bg="#AED6F1")
      amt.place(x=40, y=165)

      upb = Label(self.bottom, text="Güncellenmiş Bakiye ", font="arial 14 bold", bg="#AED6F1")
      upb.place(x=40, y=220)

      # entries

      lb = Entry(self.bottom, width=60)
      lb.place(x=320, y=110)

      dp = Entry(self.bottom, width=60)
      dp.place(x=320, y=165)

      fb = Entry(self.bottom, width=60)
      fb.place(x=320, y=220)

      # submit
      self.submit = Button(self.bottom, text=" Göster ", font="arial 15 bold", width="52", command=bakiye_goster)
      self.submit.place(x=45, y=270)

      self.dep = Button(self.bottom, text=" Para çek ", font="arial 15 bold", width="52", command=updt)
      self.dep.place(x=45, y=330)
      bakiye_goster()
class paraYatir(object):
   def __init__(self, master=None):
      self.master = master
      self.master.geometry("700x500+500+200")
      self.master.resizable(height=0, width=0)
      fonksiyonlar.getloginid(self)
      self.filepath = os.getcwd()

      def upd():
         fonksiyonlar.connect(self)
         self.cursor.execute("select balance from bankacc where customer_id='" + self.loginid + "'")
         myresul = self.cursor.fetchall()
         for x in myresul:
            # print(x)
            fb.insert(0, x[0])
         self.con.commit()
         MessageBox.showinfo("Bakiye durumu", "Başarıyla Yatırıldı")
         self.con.close()

      def updt():
         amtn = dp.get()
         fonksiyonlar.connect(self)
         # self.cursor.execute("update bankacc set balance= balance - ('" + amtn + "') where acc_id='" + acc_no + "'")
         self.cursor.execute("select balance from bankacc where customer_id='" + self.loginid + "'")
         # bakiye = self.cursor.fetchall()[0][0]
         # print(int(amtn))
         if not (amtn.isnumeric()):
            MessageBox.showinfo("Hatalı giriş", "Tutar tamsayı olmalıdır.")
         else:
            if (int(amtn) <= 0):
               MessageBox.showinfo("Hata", "Yatırılacak tutar negatif olamaz")
            else:
               today = date.today()
               fb.delete(0, END)
               self.cursor.execute(
                  "update bankacc set balance= balance + ('" + amtn + "') where customer_id='" + self.loginid + "'")
               self.cursor.execute("select balance from bankacc where customer_id='" + self.loginid + "'")
               resultkb = self.cursor.fetchall()[0][0]
               print(resultkb)
               self.cursor.execute(
                  'insert into transactions(kaynak,hedef,islem,tutar,kaynak_bakiye,tarih) values(?,?,?,?,?,?);',
                  (self.loginid, "banka", "bankaya yatırma", amtn, resultkb, today)
               )
               self.con.commit()
               self.con.close()
               upd()

      def bakiye_goster():
         lb.delete(0, END)
         fonksiyonlar.connect(self)
         self.cursor.execute("select balance from bankacc where customer_id='" + self.loginid + "'")
         myresult = self.cursor.fetchall()
         for x in myresult:
            lb.insert(0, x[0])
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

      self.heading = Label(self.top, text="Para Yatır", font="arial 18 bold", bg="white")
      self.heading.place(x=265, y=30)

      # bottom Frame Design

      # buttons and labels

      detail = Label(self.bottom, text="Mevcut Bakiye ", font="arial 14 bold", bg="#AED6F1")
      detail.place(x=40, y=110)

      amt = Label(self.bottom, text="Yatırılacak tutar ", font="arial 14 bold", bg="#AED6F1")
      amt.place(x=40, y=165)

      upb = Label(self.bottom, text="Güncellenmiş bakiye ", font="arial 14 bold", bg="#AED6F1")
      upb.place(x=40, y=220)

      # entries

      lb = Entry(self.bottom, width=60)
      lb.place(x=320, y=110)

      dp = Entry(self.bottom, width=60)
      dp.place(x=320, y=165)

      fb = Entry(self.bottom, width=60)
      fb.place(x=320, y=220)

      # submit
      self.submit = Button(self.bottom, text=" Göster ", font="arial 15 bold", width="52", command=bakiye_goster)
      self.submit.place(x=45, y=270)

      self.dep = Button(self.bottom, text=" Yatır ", font="arial 15 bold", width="52", command=updt)
      self.dep.place(x=45, y=330)
      bakiye_goster()

class bakiyeGoster(object):
   def __init__(self, master=None):
      self.master = master
      self.master.geometry("500x300+400+200")
      self.master.resizable(height=0, width=0)
      fonksiyonlar.getloginid(self)
      self.filepath = os.getcwd()

      def bakiye_goster():
         lb.delete(0, END)
         fonksiyonlar.connect(self)
         self.cursor.execute("select balance from bankacc where customer_id='" + self.loginid + "'")
         myresult = self.cursor.fetchall()
         print(myresult)
         for x in myresult:
            # print(x)
            lb.insert(0, x[0])
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

      self.heading = Label(self.top, text="Mevcut Bakiye", font="arial 18 bold", bg="white")
      self.heading.place(x=180, y=30)

      # bottom Frame Design

      # buttons and labels
      detail = Label(self.bottom, text="Mevcut Bakiye -> ", font="arial 14 bold", bg="#AED6F1")
      detail.place(x=55, y=86)

      # listele
      lb = Entry(self.bottom, width=20,justify="center")
      lb.place(x=240, y=90)

      # submit
      # self.submit = Button(self.bottom, text=" Göster ", font="arial 15 bold", width="52", command=bakiye_goster)
      # self.submit.place(x=45, y=200)
      bakiye_goster()

class paraTransfer(object):
   def __init__(self, master=None):
      self.master = master
      self.master.geometry("700x500+500+200")
      self.master.resizable(height=0, width=0)
      fonksiyonlar.getloginid(self)
      self.filepath = os.getcwd()

      def upd():
         fonksiyonlar.connect(self)
         self.cursor.execute("select balance from bankacc where customer_id='" + self.loginid + "'")
         myresul = self.cursor.fetchall()
         for x in myresul:
            # print(x)
            e_bky.insert(0, x[0])
         self.con.commit()
         MessageBox.showinfo("Bakiye durumu", "Başarıyla Gönderildi")
         self.con.close()

      def updt():
         miktar = e_mktr.get()
         txid = e_txid.get()
         fonksiyonlar.connect(self)
         if not (miktar.isnumeric() and txid.isnumeric()):
            MessageBox.showinfo("Hatalı giriş", "ID ve tutar tamsayı olmalıdır.")
         else:
            # self.cursor.execute("update bankacc set balance= balance - ('" + amtn + "') where acc_id='" + acc_no + "'")
            self.cursor.execute("select balance from bankacc where customer_id='" + self.loginid + "'")
            bakiye = self.cursor.fetchall()
            self.cursor.execute("select balance from bankacc where customer_id='" + txid + "'")
            hvid = self.cursor.fetchall()
            # print(len(hvid))
            print(bakiye[0][0])
            print(int(miktar))
            if(len(hvid)==0):
               MessageBox.showinfo("Hata", "Gönderilecek hesap mevcut değil")
            else:
               if (int(miktar) <= 0 ):
                  MessageBox.showinfo("Hata", "Gönderilecek tutar negatif olamaz")
               elif(bakiye[0][0]<int(miktar)):
                  MessageBox.showinfo("Hata", "Gönderilecek tutar bakiyeden büyük olamaz")
               elif(txid==self.loginid):
                  MessageBox.showinfo("Hata", "Para gönderimi farklı hesaba yapılmalıdır")
               else:
                  today = date.today()
                  # print("Today's date:", today)
                  e_bky.delete(0, END)
                  self.cursor.execute(
                     "update bankacc set balance= balance - ('" + miktar + "') where customer_id='" + self.loginid + "'")
                  self.cursor.execute(
                     "update bankacc set balance= balance + ('" + miktar + "') where customer_id='" + txid + "'")
                  self.con.commit()
                  self.cursor.execute("select balance from bankacc where customer_id='" + self.loginid + "'")
                  resultkb = self.cursor.fetchall()[0][0]
                  # print(resultkb)
                  self.cursor.execute("select balance from bankacc where customer_id='" + txid + "'")
                  resulthb = self.cursor.fetchall()[0][0]
                  # print(resulthb)
                  self.cursor.execute(
                     'insert into transactions(kaynak,hedef,islem,tutar,kaynak_bakiye,hedef_bakiye,tarih) values(?,?,?,?,?,?,?);',
                     (self.loginid, txid, "para gönderme", miktar, resultkb, resulthb, today)
                     )
                  self.con.commit()
                  self.con.close()
                  upd()

      def bakiye_goster():
         e_bky.delete(0, END)
         fonksiyonlar.connect(self)
         self.cursor.execute("select balance from bankacc where customer_id='" + self.loginid + "'")
         myresult = self.cursor.fetchall()
         for x in myresult:
            # print(x)
            e_bky.insert(0, x[0])
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

      self.heading = Label(self.top, text="Para Gönder", font="arial 18 bold", bg="white")
      self.heading.place(x=265, y=30)

      # bottom Frame Design

      # buttons and labels

      bky = Label(self.bottom, text="Mevcut Bakiye ", font="arial 14 bold", bg="#AED6F1")
      bky.place(x=40, y=110)

      txid = Label(self.bottom, text="Gönderilecek Hesap İD ", font="arial 14 bold", bg="#AED6F1")
      txid.place(x=40, y=165)

      mktr = Label(self.bottom, text="Tutar ", font="arial 14 bold", bg="#AED6F1")
      mktr.place(x=40, y=220)

      # entries

      e_bky = Entry(self.bottom, width=40)
      e_bky.place(x=320, y=110)

      e_txid = Entry(self.bottom, width=40)
      e_txid.place(x=320, y=165)

      e_mktr = Entry(self.bottom, width=40)
      e_mktr.place(x=320, y=220)

      # submit

      self.dep = Button(self.bottom, text=" Gönder ", font="arial 15 bold", width="52", command=updt)
      self.dep.place(x=45, y=300)
      bakiye_goster()

class crtbankacc(object):
   def __init__(self, master=None):
      self.master = master
      self.master.geometry("700x500+500+200")
      self.master.resizable(height=0, width=0)
      fonksiyonlar.getloginid(self)
      self.filepath = os.getcwd()

      def crtacc():
         accnm=e_accname.get()
         fonksiyonlar.connect(self)
         self.cursor.execute("select acc_id from bankacc where customer_id='" + self.loginid + "'")
         acccount = (self.cursor.fetchall())
         print(len(acccount))
         if(len(acccount)>=1):
            MessageBox.showinfo("Hata", "Mevcut hesap")
         else:
            self.cursor.execute(
               'insert into bankacc(customer_id,acc_name,balance) values(?,?,?);',
               (self.loginid,accnm ,0)
            )
            self.con.commit()
            MessageBox.showinfo("Başarılı", "Hesap açıldı")
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

      self.heading = Label(self.top, text="Banka hesabı oluştur", font="arial 18 bold", bg="white")
      self.heading.place(x=265, y=30)

      # bottom Frame Design

      # buttons and labels

      accname = Label(self.bottom, text="Hesap adı ", font="arial 14 bold", bg="#AED6F1")
      accname.place(x=40, y=110)

      # entries

      e_accname = Entry(self.bottom, width=60)
      e_accname.place(x=320, y=110)

      # submit
      self.submit = Button(self.bottom, text=" Oluştur ", font="arial 15 bold", width="52", command=crtacc)
      self.submit.place(x=45, y=270)
