user = "Linn"
user_pw = 2468

user_name = input('username: ')
password = int(input('password: '))

if user_name == user and user_pw == password:
    print("You have Login successfully!")
elif user_name != user and user_pw == password:
    print("Worong username. Plz, try again!")
elif user_name == user and user_pw != password:
    print("Worong password. Plz, try again!") 
elif user_name != user and user_pw != password:
    print("Worng username and password! Plz, try again")   