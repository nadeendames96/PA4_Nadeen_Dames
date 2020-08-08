from contact import Contact
from contact_book import ContactBook

# create contact for Cookie Monster

cookie = Contact("Cookie", "Monster")
cookie.add_phone("12345678", "Work")
cookie.add_phone("00123456", "Cookie Line")
cookie.add_label("Cookie")
cookie.add_label("Friend")

# call update_name() on cookie
# cookie.update_name(lname="Monster Too")
# cookie.update_name(fname="Yummy Cookie")
# cookie.update_name(fname="Yummy Cookie", lname="Monster Too")
# print(cookie)

# create contact for Don Music

don = Contact("Don", "Music")

# call add lebal
don.add_label("Music")
don.add_label("Friend")

# call add phone numbers
don.add_phone("0788878888","IT")
print(don)
# create contact for Roosevelt Franklin
roosevelt = Contact("Roosevelt", "Franklin")
# call add email
roosevelt.add_email("nana1196@hotmail.com")
roosevelt.add_email("lolo895@hotmail.com")
roosevelt.print_list_emails()

print(type(roosevelt))
# create a contact book
sesame_street = ContactBook()

# add contacts to contact book
sesame_street.add(cookie)
sesame_street.add(don)
sesame_street.add(roosevelt)
sesame_street.search_by_label("Music")
sesame_street.print_book()
#print(sesame_street.search_by_label("Music"))
# print the number of contacts in contact book
print(len(sesame_street.contacts))

# print all contacts
sesame_street.print_all_contacts()

# delete contct from list contacts
sesame_street.delete_contact(don)
sesame_street.delete_contact(don)