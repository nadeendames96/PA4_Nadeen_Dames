# Class Contact

class Contact:
    def __init__(self, fname, lname):
        # instance attributes
        self.fname = fname
        self.lname = lname
        self.emails = list()
        self.phone_numbers = dict()
        self.labels = list()

        print(f"A new contact for '{self.fname}' has been created.")
    # instance method
    # Override
    def __str__(self):
        return f"""
        Contact information for {self.lname.capitalize()}, {self.fname.capitalize()}.
        Contact has {len(self.phone_numbers)} phone numbers and {len(self.labels)} labels
         and {len(self.emails)} emails
        .
        """
    # appeand phone number to the contact list of phone numbers 
    def add_phone(self, phone_number, label):
        # add phone number to list of phone numbers
        self.phone_numbers[label.lower()] = phone_number
        if(self.phone_numbers==0):
            label="primary"
    # appeand label to the contact list of lables
    def add_label(self, label):
        self.labels.append(label)

    def add_email(self,email):
        self.emails.append(email)
        

    def print_list_emails(self):
        for email in self.emails:
            print(f"{self.fname} has email {email}")    

    def check_label(self,label):
        if label in self.labels:
            return True
        else:
             return False   
    def update_name(self,fname,lname):
        if fname!='':
            self.fname=fname
        if lname!='':
            self.lname=lname
        return (f"After update firstname and lastname: {self.fname},{self.lname} ")    