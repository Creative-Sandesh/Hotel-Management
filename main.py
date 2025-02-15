from system import System

def main():
    system = System()
    system.add_user('admin', 'admin@gmail.com','password','Admin')
    system.add_user('manager', 'manager@gmail.com','password','Manager')
    system.add_user('chef', 'chef@gmail.com','password','Chef')
    system.add_user('customer', 'customer@gmail.com','password','Customer')
    
    while True:
        print("1. Login")
        print("2. SignUp")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice =='1':
            username= input("Enter the Username: ")
            password= input("Enter the Password: ")
            user= system.login(username, password)
            if user:
                system.menu(user)
            elif choice == '2':
                username= input("Enter the Username: ")
                email = input("Enter the Email: ")
                password = input("Enter the Passwrod: ")
                role = input("Enter the Role(Admin, Manager, Chef, Customer): ")
                system.signup(username, email, password, role)
            else:
                print("Invalid Choice. Please try again. ")
        
if __name__ == "__main__":
    main()
                
            
    