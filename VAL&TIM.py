import datetime

def line():
    print("=" * 50)
def key_list():
    try:
        with open("masterkeys.txt", "r") as f:
            master_keys = f.read().splitlines()
        return master_keys
    except FileNotFoundError:
        print("Invalid")
        return[]
    except Exception as e:
        print(f"Error occured {e}")
        return []
    
def sign_up_master_key(master_key):
   try:
        with open("masterkeys.txt","a") as f:
            f.write(f"{master_key}\n")
        print("Masterkey saved")  
   except:
       print("Invalid")

   
       
def verify_master_key(key):
    keylist = key_list()
    if key in keylist:
        return True
    else:   
        print("Invalid")
        return None 
    
def save_attendance(master_key,name, log):
    try:
        current_time = datetime.datetime.now()
        time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        week =current_time.strftime("%A")
        file_attendance =f"{master_key}.txt"

        with open(file_attendance, "a") as file:
            file.write(f"{name},{log}, {time}, {week} \n")
    except Exception as e:
        print(f"Error occured when logging attendance {e}")
def loging(master_key,name):
    try:
        if not name:
            raise ValueError("This cannot be empty")
        save_attendance(master_key, name, "log")
        print("Your attendance has been recorded")
    except:
        print("Error occured")
def view_attendance(key):
    file_attendance = f"{key}.txt"
    try:
        with open(file_attendance, "r") as f:
            print("Name \t log \t\t time \t\t day of week ")
            line()
            for i in f:
                result = i.strip().split(",")
                print(f"{result[0]} \t {result[1]} \t {result[2]} \t{result[3]}")
    except FileNotFoundError:
        print("Error occured")
def delete_attendance():
    try:
        with open("attendance.txt", "w") as f:
            f.truncate(0)
        print("Attendance is now empty")
    except:
        print("Error occured")

def main_menu(key):
    while True:
        print()
        line()
        print("Welcome")
        print("\n1. Write attendance")
        print("2. View attendace")
        print("3. Delete attendace")
        print("4. Exit")

        
        choice = input("Enter your choice: ")

        if choice == "1":
            print()
            name = input("Enter the name of the student: ")
            loging(key, name)
        elif choice =="2":
            print()
            print("This is the attendance record")
            view_attendance(key)
        elif choice == "3":
            delete_attendance()
        elif choice == "4":
            print("Have a nice day!")
            break
        else:
            print("Plese selecet valid choice")
def main():
    master_key = key_list()
    while True:
        print()
        line()
        print("Welcome to Online attendance sheet")
        line()

        
        print("\n1. Create master key: ")
        print("2. Enter the master key:")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            key = input("Enter masterkey: ")
            sign_up_master_key(key)
            master_key.append(key)
        elif choice =="2":
            key = input("Enter masterkey: ") 
            if verify_master_key(key):
                main_menu(key)
        elif choice == "3":
            print("Have a Good day!!")
            break
        else:
            print("Invalid input")

if __name__ =="__main__":
    main()


        