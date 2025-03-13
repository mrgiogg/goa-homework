# with costumers enterd waliue dicaide if the inputed password is correct or not
#then inform the user by sending the masige to the 'access granted' or 'access denied' format

correct_password = 1234

#users inputed password

user_password = int(input("please_enter_your_password:"))


#checking passwod


if user_password == correct_password:
    print("access_granted")
else :
    print("access_denied")




