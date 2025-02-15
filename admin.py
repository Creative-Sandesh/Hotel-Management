class Admin:
    def __init__(self, system):
        self.system = system
        
        def adminMenu(self, user):
            print("Admin Menu:")
            print("1. Manage Staff")
            print("2. View Sales Report")
            print("3. View Customer Feedback")
            print("4. Update Profile")
            choice = input("Enter your Choice: ")
            if choice == '1':
                self.manageStaff()
            elif choice == '2':
                self.viewSalesReport()
            elif choice == '3':
                self.viewCustomerFeedback()
            elif choice == '4':
                self.updateProfile()
            else:
                print("Invalid Choice. Please try again. ")
                
            def manageStaff(self):
                print("Manage Staff:")
            
            def viewSalesReport(self):
                print("View Sales Report:")
            
            def viewCustomerFeedback(self):
                print("View Customer Feedback:")
            
            def updateProfile(self):
                print("Update Profile:")
        