import pyodbc

class fonksiyonlar:
    def connect(self):
        self.con = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                             'Server=YourSERVER;' # MsSQL server name
                             'Database=YourDB;'  # MsSQL Database name
                             'Trusted_Connection=yes;')
        self.cursor = self.con.cursor()

    def getloginid(self):
        fonksiyonlar.connect(self)
        self.cursor.execute("select * from loginidtbl")
        self.loginid = str(self.cursor.fetchall()[0][0])

        print(self.loginid)







