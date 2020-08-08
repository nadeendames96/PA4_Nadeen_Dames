from contact import Contact

# class ContactBook

class ContactBook:
    def __init__(self):
        self.contacts = list()

    # add contacts
    def add(self, contact):
        self.contacts.append(contact)

    # retraive contacts
    def get_contact(self, contact, keyword):
        if contact.fname.lower() or contact.lname.lower() or contact.email.lower() == keyword.lower():
            return contact
        else:
            return None
    # delete contact
    def delete_contact(self,contact):
        if contact in self.contacts:
            print("Successful removing Contact...")
            self.contacts.remove(contact)
        else:
             print("contact not exist.")

    # Search method
    def search(self, keyword=""):
        # local variable
        results = list()

        for contact in self.contacts:
            contact = self.get_contact(contact, keyword.lower())

            # check contact not equals none
            if contact != None:
                # appeand list of results
                results.append(contact)

                # check if found any results
            if len(results) > 0:
                print(
                    f"Found {len(results)} results matching the keyword '{keyword}'.")
                for contact in results:
                    print(contact)
            else:
                print(f"No results found matching the keyword: '{keyword}'.")

    # print all contacts 
    def print_all_contacts(self):
        # print all contacts in contact book 
        for contact in self.contacts:
            print(contact)
    pass
     

    def search_by_label(self,label):
        results = list()
        print(f" Searching for {label}")
        for contact in self.contacts:
            # check contact not equals none
            
            if contact.check_label(label):
                # appeand list of results
                results.append(contact)

        if len(results)!=0:
            for contact in results:
                print(contact)
        else:
            print("Not Founded")        

    
    def print_book(self):
        print(f"Total contacts {len(self.contacts)}")
        count_without_phone=0
        count_without_email=0
        for contact in self.contacts:
          if len(contact.phone_numbers)==0:
              count_without_phone+=1

          if len(contact.emails)==0:
                count_without_email+=1        
        print(f"Total contacts without phone numers {count_without_phone} \n total contacts without emails {count_without_email}")


    