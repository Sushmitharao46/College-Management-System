import mysql.connector as mysql
db = mysql.connect(host = 'localhost',user = 'root',password = "",database = 'college')
command_handler = db.cursor(buffered = True)
def student_session(username):
    while 1:
        print("")
        print("Student menu")
        print("")
        print("1. View Register")
        print("2. Download register")
        print("3. logout")
        user_option = input(str("option: "))
        if user_option == "1":
            print("displaying register")
            print("")
            username = (str(username),)
            command_handler.execute("select date,username,status from attendance where username = %s",username)
            records = command_handler.fetchall()
            for record in records:
                print(record)
        elif user_option == "2":
            print("Downloading register")
            username = (str(username),)
            command_handler.execute("select date,username,status from attendance where username = %s",username)
            records = command_handler.fetchall()
            for record in records:
                with open("C:/Users/91829/Downloads/Register.txt","w") as f:
                    f.write(str(records)+"\n")
                f.close()
            print("all records saved")
        elif user_option == "3":
            break;
        else:
            print("No valid option was selected")

        


def teacher_session():
    while 1:
        print("")
        print("teacher menu")
        print("1. Mark students register")
        print("2. View register")
        print("3. logout")
        user_option = input(str("option: "))
        if user_option == "1":
            print("")
            print("mark student register")
            command_handler.execute("SELECT USERNAME from USERS WHERE privilege = 'student'")
            records = command_handler.fetchall()
            date = input(str("Date: dd/mm/yyyy"))
            for record in records:
                record = str(record).replace("'","")
                record = str(record).replace(",","")
                record = str(record).replace("(","")
                record = str(record).replace(")","")
                status = input(str("status for"+str(record)+"P/A/L:"))
                query_vals = (str(record),date,status)
                command_handler.execute("insert into attendance(username,date,status) values (%s,%s,%s)",query_vals)
                db.commit()
                print(record+"marked as"+status)
        elif user_option == "2":
            print("")
            print("Viewing all students registers")
            command_handler.execute("SELECT USERNAME, DATE, STATUS FROM attendance")
            records = command_handler.fetchall()
            print("displaying all records")
            for record in records:
                print(record)
        elif user_option == "3":
            break;
        else:
            print("enter valid input")



def admin_session():
    while 1:
        print("")
        print("Admin Menu")
        print("1. Register new student")
        print("2. Register new teacher")
        print("3. Delete existing student")
        print("4. Delete new teacher")
        print("5. Logout")
        user_option = input(str("option:"))
        if user_option == "1":
            print("")
            print("Register new student")
            username = input(str("Student Username:"))
            password = input(str("student password:"))
            query_vals = (username,password)
            command_handler.execute("insert into users (username,password,privilege) VALUES (%s,%s,'student')",query_vals)
            db.commit()
            print(username + "has been registered as student")
        elif user_option == "2":
            print("")
            print("Register new teacher")
            username = input(str("Teacher Username:"))
            password = input(str("Teacher password:"))
            query_vals = (username,password)
            command_handler.execute("insert into users (username,password,privilege) VALUES (%s,%s,'teacher')",query_vals)
            db.commit()
            print(username + "has been registered as teacher")
        elif user_option == "3":
            print("")
            print("Delete Existing Student Account")
            username = input(str("Student Username:"))
            query_vals = (username,"student")
            command_handler.execute("delete from users where username = %s and privilege = %s",query_vals)
            db.commit()
            if command_handler.rowcount<1:
                print("User not found")
            else:
                print(username +"has been deleted")
        elif user_option == "4":
            print("")
            print("Delete Existing Teacher Account")
            username = input(str("Teacher Username:"))
            query_vals = (username,"teacher")
            command_handler.execute("delete from users where username = %s and privilege = %s",query_vals)
            db.commit()
            if command_handler.rowcount<1:
                print("User not found")
            else:
                print(username +"has been deleted")
        elif user_option == "5":
            break;
        else:
            print("No valid option selected")
def auth_student():
    print("")
    print("Student's Login")
    print("")
    username = input(str("username: "))
    password = input(str("password: "))
    query_vals = (username,password)
    command_handler.execute("select username from users where username = %s and password = %s and privilege = 'student'",query_vals)
    if command_handler.rowcount<=0:
          print("login not found")#change this later
    else:
        student_session(username) 
    
def auth_teacher():
    print("")
    print("Teacher Login")
    print("")
    username = input(str("username: "))
    password = input(str("password: "))
    query_vals = (username,password)
    command_handler.execute("select * from users where username = %s and password = %s and privilege = 'teacher'",query_vals)
    if command_handler.rowcount<=0:
          print("login not found")#change this later
    else:
        teacher_session() 
def auth_admin():
    print("")
    print("admin login")
    print("")
    username = input(str("Username:"))
    password = input(str("Password:"))
    if username == "admin":
        if password == "password":
            admin_session()
        else:
            print("incorrect password")
    else:
        print("login details not recognised")

def main():
    while 1:
        print("welcome to college system")
        print("")
        print("1. login as student")
        print("2. login as teacher")
        print("3. login as admin")
        print("4. Exit")
        user_option = input(str("option:"))
        if user_option == '1':
            auth_student()
        elif user_option == '2':
            auth_teacher()
        elif user_option == '3':
            auth_admin()
        elif user_option == "4":
            exit()
        else:
            print("not valid")

main()

