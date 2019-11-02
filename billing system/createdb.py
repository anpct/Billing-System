import mysql.connector
conn = mysql.connector.connect(
  host="sql12.freesqldatabase.com",
  user="sql12309921",
  passwd="Xi3n2q13aJ",
  database="sql12309921",
  port=3306
)
cursor = conn.cursor()
cursor.execute("CREATE TABLE EMP_DETAILS(EID INT(10) PRIMARY KEY, NAME VARCHAR(20), PASSWORD VARCHAR(20), PHNO INT(10) UNIQUE)")
cursor.execute("CREATE TABLE ADMIN_DETAILS(AID INT(10) PRIMARY KEY, NAME VARCHAR(20), PASSWORD VARCHAR(20), PHNO INT(10) UNIQUE)")
cursor.execute("CREATE TABLE ITEM_DETAILS(IID INT(10) PRIMARY KEY, NAME VARCHAR(20), COST VARCHAR(20))")
cursor.execute("CREATE TABLE BILLS(DATETIME VARCHAR(40), EID INT(20), AMOUNT DOUBLE, REFNO INT(10))")
