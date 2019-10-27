import mysql.connector
import datetime
conn = mysql.connector.connect(
  host="sql12.freesqldatabase.com",
  user="sql12309921",
  passwd="Xi3n2q13aJ",
  database="sql12309921",
  port=3306
)
cur=conn.cursor()


def ck_details_emp(username, password):
    try:
        cur.execute("SELECT * FROM EMP_DETAILS WHERE EID='{}' AND PASSWORD='{}'".format(username, password))
        row = cur.fetchone()
        if row != None:
            return True
        else:
            return False
    except Exception:
        return False


def ck_details_admin(username, password):
    try:
        cur.execute("SELECT * FROM ADMIN_DETAILS WHERE AID='{}' AND PASSWORD='{}'".format(username, password))
        row = cur.fetchone()
        if row != None:
            return True
        else:
            return False
    except Exception:
        return False


def get_user_details(username):
    try:
        cur.execute("SELECT EID, NAME, PHNO FROM EMP_DETAILS WHERE EID='{}'".format(username))
        row = cur.fetchone()
        return row
    except Exception:
        return False


def get_admin_details(username):
    try:
        cur.execute("SELECT AID, NAME, PHNO FROM ADMIN_DETAILS WHERE AID='{}'".format(username))
        row = cur.fetchone()
        return row
    except Exception:
        return False


def get_items():
    try:
        cur.execute("SELECT * FROM ITEM_DETAILS")
        rows = cur.fetchall()
        return rows
    except Exception:
        return False

def get_cost(item):
    try:
        cur.execute("SELECT * FROM ITEM_DETAILS WHERE NAME='{}'".format(item))
        rows = cur.fetchone()
        return rows[2]
    except Exception:
        return False


def store(datetimev, username, total_cost):
    sql = "INSERT INTO BILLS VALUES ('{}', {}, {})".format(datetimev, username, total_cost)
    cur.execute(sql)
    conn.commit()
