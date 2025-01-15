# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 18:19:39 2024

@author: JackD
"""
#Stored Passwords
def StoredPasswords(checkPass):
    #List of passwords
	passwordsList = ('123456', '123456789', '12345', 'qwerty', 'password', '12345678', '111111', '123123', '1234567890', '1234567',
				 'qwerty123', '000000', '1q2w3e', 'aa12345678', 'abc123', 'password1', '1234', 'qwertyuiop', '123321', 'password123',
				 '1q2w3e4r5t', 'iloveyou', '654321', '666666', '987654321', '123', '123456a', 'qwe123', '1q2e3e4r', '7777777',
				 '1qaz2wsx', '123qwe', 'zxcvbnm', '121212', 'asdasd', 'a123456', '555555', 'dragon', '112233', '123123123', 'monkey',
				 '11111111', 'qazwsx', '159753', 'asdfghjkl', '222222', '1234qwer', 'qwerty1', '123654', '123abc')

	for userPassword in passwordsList:
        #Checking for weak password
		if checkPass == userPassword:
			found = 'Your password is too common. Please consider changing it.' #if the password if found in list
			print(f'Password was found at index: {passwordsList.index(checkPass)}') #returning index number
			return found

	notFound = 'You have a strong password' #Prompting a strong password if not found
	return notFound

#Getting Username and Password
def getUserPass():
	usernameSet = input('Enter Your Username: ') #Prompting for username 
	userPassword = input('Enter Your Password: ') #Prompting for password

	result = StoredPasswords(userPassword) #Holds password

	print(result)

#Main function
def main():
	getUserPass()

#Calling main
if __name__ == '__main__':
	main()
    
    