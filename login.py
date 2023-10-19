correct_username = "Linn"
correct_pw = "2468ab"

user_name = input('username: ')
password =input('password: ')

if user_name == correct_username and password == correct_pw:
    print("You have Login successfully!")
elif user_name != correct_username and password == correct_pw:
    print("Worong username. Plz, try again!")
elif user_name == correct_username and password != correct_pw:
    print("Worong password. Plz, try again!") 
elif user_name != correct_username and password != correct_pw:
    print("Worng username and password! Plz, try again")      