''' There is a hotel in which birthday party is organized.
and in that party the peoples in age group 10-20 and 20-40 and above 40
are invited so what you have to do is, ask the name to the peoples and their age,
also give them some greetings
and before this  you have to print the name of the hotel.
if the gest is between 10-20 tell him to go to the third floor,
if the gest is between 20-40 tell him to go to the second floor and if the gest is above 40
then tell him to go to the first floor. '''

print('Welcome to Hotel Aannapurna !')
a = input("Please enter your Name ")
b = int(input("Enter age "))

if b < 10:
    print("Sorry ! You are not allowd here ")
elif b <= 20:
    print(" Hello", a,"!    You have to go onto the third floor")

elif b <= 40:
    print("Hello", a,"!     You have to go onto the second floor")

elif b > 40:
    print("Hello", a,"!     You have to go onto the first floor")

