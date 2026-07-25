'''Abstraction:
    *Design a Phone class with methods to call_contact and take_picture. 
    Abstract away any internal processing details and focus on creating a user friendly interface.'''

class Phone:
    def call_contact(self, contact_name):
        print(f"Calling {contact_name}...")

    def take_picture(self):
        print("Taking a picture...")

# Create an object of the Phone class
my_phone = Phone()
# Call the methods to demonstrate abstraction
my_phone.call_contact("Abhi")
my_phone.take_picture()
