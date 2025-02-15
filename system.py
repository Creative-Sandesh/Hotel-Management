from user import User
from admin import Admin
from manager import Manager
from chef import Chef
from customer import Customer

#creating the constructure
class System:
    def __init__(self):
        self.users=[] #constructor method initializes an empty list called users to store instances of User
        self.load_user_from_file()
        
    #method for adding user data to User class instance
    def add_user(self, username , email, password, role):
        user= User(username,email, password, role)
        self.users.append(user)
        self.save_user_from_file()
        
    #for login 
    def login(self, username , password):
        for user in self.users:
            if user.username== username:
                if user.password== password:
                    user.resetLoginAttempts()
                    return user
                else:
                    user.incrementLoginAttempts()
                    if user.loginAttempts >=3:
                        print("Login attempt exceed")
                        return None
                    print(f"Invalid password. Attempt {user.loginAttempts}/3.")
                    self.save_user_to_file()
                    return None
        print("User not found.")
        return None
    
    
    # sign Up page
    def signup(self, username ,email, password,role):
        for user in self.users:
            if user.username== username:
                print("Username already exists.")
                return
        self.add_user(username, email, password,role)
        print("User signed up successfully!")
        
        
    # method for save the signup data
    def save_users_to_file(self):
        with open ('data.txt','w') as file:
            for user in self.users:
                file.write(f"{user.username},{user.email},{user.password},{user.role}\n")
    
    #method for load the stored from text file
    def load_users_to_file(self):
        try:
            with open('data.txt','r') as file:
                for line in file:
                    username, email, password, role = line.strip().split(',')
                    user = User(username,email,password,role)
                    self.users.append(user)
        except FileNotFoundError:
            pass
                    
        
    
    #for Menu page
    def menu(self, user):
        if user.role == "Admin":
            self.adminMenu(user)
        elif user.role=="Manager":
            self.managerMenu(user)
        elif user.role=="Chef":
            self.chefMenu(user)
        elif user.role=="Customer":
            self.customerMenu(user)
    
    # method for menu of different user
    def adminMenu(self, user):
        print("Admin Menu:")
        pass
    
    def managerMenu(self, user):
        print("Manager Menu:")
        pass
    
    def chefMenu(self, user):
        print("Chef Menu:")
        pass
    
    def customerMenu(self, user):
        print("Customer Menu:")
        pass 

    
    
            
    
    
    
           
    
    
    
    