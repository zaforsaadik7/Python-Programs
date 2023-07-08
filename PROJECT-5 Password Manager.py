import random

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\\()*+,-./:;<=>?@[\\\\]^_`{|}~'

def password_generator(length= 8):
    password= ''.join(random.choice(characters) for i in range(length))
    return password

def store_password(account, password) :
    with open('password.txt', 'a') as file:
        file.write(f'{account}:{password}')

def retrieve_password(account):
    with open ('password.txt', 'r') as file: 
        for line in file:
            if line.startswith(account):
                return line.split(':')[1].strip()
    return None
def main():
    while True:
            print('1. Generate a new password.')
            print('2. Store a password.')
            print('3. Retreive password.')
            print('4. Quit.')
    
            choice= input('Insert your choice:')
            if choice== '1':
                length=int(input('Enter password length:'))
                password= password_generator(length)
                print(f'Generated password:{password}')
            elif choice== '2':
                account= input('Insert your account name:')
                password= input('Insert password:')
                store_password(account, password)
                print('Password stored successfully.')
            elif choice== '3':
                account= input('Insert account name:')
                password= retrieve_password(account)
                if password:
                    print(f'Password: {password}')
                else:
                    print('Account not found.')
            elif choice== "4":
                print('Thank you for your cooperation.')
                break
if __name__ == '__main__':
    main()
