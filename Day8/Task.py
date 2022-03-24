print('Welcome to Hello World Hospital !')
a = input("Please enter your Name ")

print('1 Heart Problem ')
print('2 Skin Problem ')
print('3 Knee Problem ')
print('4 Children Care ')

x = int(input('Please Enter the Number '))

b = int(input("Enter Your age "))
if x == 1:
    print('Welcome Dear,', a,'! Your selected problem is: 1 Heart Problem ')
elif x == 2:
    print('Welcome Dear,', a,'! Your selected problem is: 2 Skin Problem')
elif x == 3:
    print('Welcome Dear,', a,'! Your selected problem is: 3 Knee Problem')
elif x == 4:
    print('Welcome Dear,', a,'! Your selected problem is: 4 Children Care')



if b < 10:
    print(" Go to room no 1")
elif b <= 20:
    print(" Go to room no 2")

elif b <= 40:
    print("Go to room no 3")

elif b > 40:
    print("Go to room no 4")

print('Pahile Counter la paise jama karjo....!')