from models import AppUser
import re


def validate_data(data):
    if not data.get('email'):
        return 'Please enter an email.'
    elif not data.get('username'):
        return  'Please enter a username'
    elif not data.get('password'):
        return 'Please enter a password'
    email = data['email']
    password = data['password']
    username = data['username']


def validata_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    print(AppUser.objects.filter(email=email))

    if(re.fullmatch(regex, email)):
        return True
 
    else:
        return False

# def validata_password(password):
email1 = 'hello@gmail.xom'
print(validata_email(email1))