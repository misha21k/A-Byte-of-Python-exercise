import pickle


class Contact:
    """Contacts of address book"""
    contacts = {}  # All contacts in address book

    def __init__(self, name, address, telephone):
        """Creation of contact"""
        self.name = name
        self.address = address
        self.telephone = telephone
        print('Contact {} is created'.format(self.name))

    def __del__(self):
        """Deletion of contact"""
        print('Contact {} is deleted'.format(self.name))

    def info(self):
        """Information about contact"""
        print('Name: "{0}" address: "{1}" telephone: "{2}"'.format(self.name, self.address, self.telephone))


def addContact():
    """Creation of contact"""
    name = input('Enter new name of contact: ')
    address = input('Enter address of {}: '.format(name))
    telephone = input('Enter telephone of {}: '.format(name))
    Contact.contacts[name] = Contact(name, address, telephone)


def delContact():
    """Deletion of contact"""
    name = input('Enter name of contact for deletion: ')
    del Contact.contacts[name]


def changeContact():
    """Change of contact"""
    name = input('Enter name for change: ')
    Contact.contacts[name].address = input('Enter new address of {}: '.format(name))
    Contact.contacts[name].telephone = input('Enter new telephone of {}: '.format(name))


def infoContact():
    """Information about contact"""
    name = input('Enter name of contact for information: ')
    Contact.contacts[name].info()


def allInformation():
    """All information about contacts"""
    for contact in Contact.contacts.values():
        contact.info()


def readFile(filename):
    """Reading contacts from file"""
    try:
        file = open(filename, 'rb')
        Contact.contacts = pickle.load(file)
        file.close()
    except FileNotFoundError:
        pass


def writeFile(filename):
    """Writing contacts in file"""
    file = open(filename, 'wb')
    pickle.dump(Contact.contacts, file)
    file.close()


# Reading contacts from file
readFile('address_book.data')

print('What will you do?')
while True:
    try:
        print('Enter "A", "D", "C", "I", "All" or "E"')
        inputUser = input('"A"dd "D"elete "C"hange "I"nformation "All"Information "E"xit: ')

        if inputUser.lower() in {'a', 'add'}:  # Creation of contact
            addContact()
        elif inputUser.lower() in {'d', 'delete'}:  # Deletion of contact
            delContact()
        elif inputUser.lower() in {'c', 'change'}:  # Change of contact
            changeContact()
        elif inputUser.lower() in {'i', 'information'}:  # Information about contact
            infoContact()
        elif inputUser.lower() in {'all', 'allinformation'}:  # All information about contacts
            allInformation()
        elif inputUser.lower() in {'e', 'exit', ''}:  # Exit and writing contacts in file
            writeFile('address_book.data')
            break
        else:
            print('Wrong input')
    except KeyError:
        print('This name is not found')
    except EOFError:
        print('Wrong input')
    input()
