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


# xyz
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


# Auth admin
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


# Get user details
def get_user_details(username):
    try:
        cur.execute("SELECT EID, NAME, PHNO FROM EMP_DETAILS WHERE EID='{}'".format(username))
        row = cur.fetchone()
        return row
    except Exception:
        return False


# Get admin details
def get_admin_details(username):
    try:
        cur.execute("SELECT AID, NAME, PHNO FROM ADMIN_DETAILS WHERE AID='{}'".format(username))
        row = cur.fetchone()
        return row
    except Exception:
        return False


# Get all item details
def get_items():

    try:
        cur.execute("SELECT * FROM ITEM_DETAILS ORDER BY IID ASC")
        rows = cur.fetchall()
        return rows
    except Exception:
        return False


# Get cost of an item
def get_cost(item):
    try:
        cur.execute("SELECT * FROM ITEM_DETAILS WHERE NAME='{}'".format(item))
        rows = cur.fetchone()
        return rows[2]
    except Exception:
        return False


# Store bill permanently
def store(datetimev, username, total_cost, ref):
    sql = "INSERT INTO BILLS VALUES ('{}', {}, {}, {})".format(datetimev.strftime("%d-%m-%Y  %H:%M"), username, total_cost, ref)
    cur.execute(sql)
    conn.commit()


# Get all employees
def get_all_employees():
    cur.execute("SELECT * FROM EMP_DETAILS ORDER BY EID ASC")
    rows = cur.fetchall()
    return rows


# Get all sales
def get_all_sales():
    cur.execute("SELECT * FROM BILLS")
    rows = cur.fetchall()
    return rows


# Add user
def add_user_to_db(username, name, password, phno):
    sql = "INSERT INTO EMP_DETAILS VALUES ({}, '{}', '{}', {})".format(username, name, password, phno)
    cur.execute(sql)
    conn.commit()


# Check if item exists
def ck_item_exists(id):
    try:
        cur.execute("SELECT * FROM ITEM_DETAILS WHERE IID='{}'".format(id))
        row = cur.fetchone()
        return row
    except Exception:
        return False


# Add item to database
def add_item_to_db_data(itemid, name, cost):
    try:
        sql = "INSERT INTO ITEM_DETAILS VALUES ({}, '{}', {})".format(itemid, name, cost)
        cur.execute(sql)
        conn.commit()
    except Exception:
        return False


# Remove user from database
def remove_user(username):
    try:
        sql = "DELETE FROM EMP_DETAILS WHERE EID={}".format(username)
        cur.execute(sql)
        conn.commit()
    except Exception:
        return False


# Remove item from database
def remove_item(id):
    try:
        sql = "DELETE FROM ITEM_DETAILS WHERE IID={}".format(id)
        cur.execute(sql)
        conn.commit()
    except Exception:
        return False


# Update price of an item
def update_price(item_name, cost):
    try:
        sql = "UPDATE ITEM_DETAILS SET COST={} WHERE NAME='{}'".format(cost, item_name)
        cur.execute(sql)
        conn.commit()
    except Exception:
        return False


# Get all related sales
def get_all_sales_related(username):
    try:
        cur.execute("SELECT * FROM BILLS WHERE EID={}".format(username))
        rows = cur.fetchall()
        return rows
    except Exception:
        return False


# Delete bill from database
def delete_bill_db(ref):
    try:
        sqlpre = "INSERT INTO DELETED_BILLS SELECT * FROM BILLS WHERE REFNO={}".format(ref)
        cur.execute(sqlpre)
        conn.commit()
        sql = "DELETE FROM BILLS WHERE REFNO={}".format(ref)
        cur.execute(sql)
        conn.commit()
    except Exception:
        return False


# Get all deleted bills
def get_all_deleted():
    try:
        sql = "SELECT * FROM DELETED_BILLS ORDER BY DATETIME ASC"
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except Exception:
        return False