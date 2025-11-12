import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="watermelonsugarhigh@007",
    database="wsh1"
)

print(mydb)

mycursor = mydb.cursor()

print("Welcome To The Platform")
h = 'y'
while h.lower() == 'y':
    print("1. Add To Shoppers List:")
    print("2. To delete Row.")
    print("3. To Update:")
    print("4. Show ShopperLog:")
    t = int(input("Enter Either 1, 2, 3, or 4: "))
    
    if t == 1:
        a = input("Enter name: ")
        b = input("Enter address: ")
        c = input("Enter phone: ")
        d = input("Enter age: ")
        e = input("Enter gender: ")
        sql = "INSERT INTO ShopperLog (name, address, phone, age, gender) VALUES (%s, %s, %s, %s, %s)"
        val = (a, b, c, d, e)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted. Thank you!")
    
    elif t == 2:
        f = input("Remove What? (Enter Name Of User): ")
        sql1 = "DELETE FROM ShopperLog WHERE name = %s"
        adr = (f,)
        mycursor.execute(sql1, adr)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted. Thank you!")
    
    elif t == 3:
        f = input("Enter what to change (e.g., address, name, phone, age, gender): ").lower()
        q = input(f"Enter new {f}: ")
        r = input("Enter name: ")
        sql = f"UPDATE ShopperLog SET {f} = %s WHERE name = %s"
        val = (q, r)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected.")
    
    elif t == 4:
        mycursor.execute("SELECT * FROM ShopperLog")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
    
    else:
        print("Invalid option. Please enter 1, 2, 3, or 4.")
    
    h = input("Do you want to continue? Press 'Y' or 'y' to continue: ")
