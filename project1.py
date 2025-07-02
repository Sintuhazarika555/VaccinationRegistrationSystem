import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='mysqlroot',
    database='practical'
)
mycur = mydb.cursor()

# Line function
def line():
    print('- ' * 50)

# Search function
def search(se):
    sql = "SELECT * FROM vaccine WHERE certificateid = %s"
    mycur.execute(sql, (se,))
    result = mycur.fetchall()
    if result:
        for ra in result:
            print("Certificate ID:", ra[0])
            print("Name:", ra[1])
            print("Age:", ra[2])
            print("Gender:", ra[3])
            print("ID Type:", ra[4])
            print("ID Number:", ra[5])
            print("Vaccine Name:", ra[6])
            print("Dose Number:", ra[7])
            print("Gmail:", ra[8])
            print("Contact Number:", ra[9])
    else:
        print("No record found.")

# Register function
def register():
    print("Register your data by filling the following details.")
    l = int(input("Certificate ID: "))
    c = input("Name: ")
    d = int(input("Age: "))
    e = input("Gender: ")
    f = input("ID/CARD Type: ")
    g = int(input("ID/CARD Number: "))
    h = input("Vaccine Name: ")
    i = int(input("Dose (1,2) you got: "))
    j = input("Gmail: ")
    k = int(input("Contact No. (only digits): "))

    sql = "INSERT INTO vaccine VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (l, c, d, e, f, g, h, i, j, k)
    mycur.execute(sql, values)
    mydb.commit()
    print("Your data has been registered successfully.")

# Remove function
def remove():
    b = int(input("Enter Certificate ID to delete: "))
    mycur.execute("DELETE FROM vaccine WHERE certificateid = %s", (b,))
    mydb.commit()
    print("Your data has been removed.")

# Display function
def display():
    mycur.execute("SELECT * FROM vaccine")
    result = mycur.fetchall()
    print("CertificateID, Name, Age, Gender, ID Type, ID Number, Vaccine Name, Dose No, Gmail, Contact No")
    line()
    for i in result:
        print(i)
    line()

# Edit function
def edit():
    l = int(input("Enter Certificate ID to edit: "))
    c = input("New Name: ")
    d = int(input("New Age: "))
    e = input("New Gender: ")
    f = input("New ID Type: ")
    g = int(input("New ID Number: "))
    h = input("New Vaccine Name: ")
    i = int(input("New Dose No (1 or 2): "))
    j = input("New Gmail: ")
    k = int(input("New Contact Number: "))

    sql = """
    UPDATE vaccine SET 
        name=%s, age=%s, gender=%s, id=%s, idnumber=%s,
        vaccinename=%s, doseno=%s, gmail=%s, contactno=%s
    WHERE certificateid=%s
    """
    values = (c, d, e, f, g, h, i, j, k, l)
    mycur.execute(sql, values)
    mydb.commit()

    print("Data updated. Updated record:")
    search(l)

# Main Menu
line()
print("\tWELCOME TO VACCINE REGISTRATION SYSTEM")
line()
print("THANK YOU FOR VISITING.")
line()
print('''Select an option:
1 - Search for your data
2 - Register your data
3 - Remove your data
4 - Display all data
5 - Edit data''')

try:
    a = int(input("Enter your choice (1-5): "))

    if a == 1:
        b = int(input("Enter Certificate ID to search: "))
        line()
        search(b)
        line()
    elif a == 2:
        line()
        register()
        line()
    elif a == 3:
        line()
        remove()
        line()
    elif a == 4:
        line()
        display()
        print("All data displayed.")
    elif a == 5:
        line()
        edit()
        line()
    else:
        print("Invalid option selected.")
        line()

except Exception as e:
    print("Error occurred:", e)

print("THANK YOU. HAVE A NICE DAY!")
