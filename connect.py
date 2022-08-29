import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="py_database"
)

# onion.ws

choose = (0,1,2)

while True:
  
  pic = int(input("(0)insert (1)show (2)delete: "))
  if pic == choose[0]:
    print("Insert data")
    name = str(input("Name: "))
    address = str(input("Address: "))
    number = int(input("Number: "))

    mycursor = mydb.cursor()
    sql = "INSERT INTO info (name, address, number) VALUES (%s, %s, %s)"
    val = (name, address, number)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

  elif pic == choose[1]:
    print('show data')
    mycursor = mydb.cursor()
    show = "SELECT * FROM info info"
    mycursor.execute(show)
    myresult = mycursor.fetchall()
    print(myresult)

  elif pic == choose[2]:
    print('delete data')
    mycursor = mydb.cursor()
    delete = int(input("Enter id to delete data: "))
    remove = "DELETE FROM info WHERE id = %s"
    idNum = delete
    mycursor.execute(remove, idNum)
    mydb.commit()

