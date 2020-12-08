import mysql.connector
conn = mysql.connector.connect(
    host="====",
    user="====",
    passwd="====",
    database="====",
    port=3306
)
cursor = conn.cursor()
cursor.execute(
    "CREATE TABLE EMP_DETAILS(EID INT(10) PRIMARY KEY, NAME VARCHAR(20), PASSWORD VARCHAR(20), PHNO INT(10) UNIQUE)")
cursor.execute(
    "CREATE TABLE ADMIN_DETAILS(AID INT(10) PRIMARY KEY, NAME VARCHAR(20), PASSWORD VARCHAR(20), PHNO INT(10) UNIQUE)")
cursor.execute(
    "CREATE TABLE ITEM_DETAILS(IID INT(10) PRIMARY KEY, NAME VARCHAR(20), COST VARCHAR(20))")
cursor.execute(
    "CREATE TABLE BILLS(DATETIME VARCHAR(40), EID INT(20), AMOUNT DOUBLE, REFNO INT(10))")
cursor.execute(
    "CREATE TABLE DELETED_BILLS(DATETIME VARCHAR(40), EID INT(20), AMOUNT DOUBLE, REFNO INT(10))")
sql = "INSERT INTO ADMIN_DETAILS VALUES (%s, %s, %s, %s)"
val = (1, "admin", "admin", 1234567890)
cursor.execute(sql, val)
conn.commit()
