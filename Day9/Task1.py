# Make question bank like KBC using loops and ask the question to users and show option
# and check the answers and print the result.

print('Welcome to Aapka aapna show Kon Banega Roadpati......!')
a = input('Please enter your name ')
print('Hello ',a)
print('Your first question is :' )
print('Q 1) Who was the first lady president of India ? \n a) Pratibhatai Patil \n b) Indira Gandhi \n c) Smruti Irani\n'
      'd) None of the above') # a
q1 = input('Enter the option ')

print('Q 2) Who was the author of Mahabharata ? ')
print('a) Aadi Shankaracharya\n b) Kapil Muni\n c) Ved Vyas\n d) Rushi Markandeya') # c
q2 = input('Enter the option ')

print('Q 3) What is the full form of SEBI ?') # Securities And Exchange Board of India
print('a) Security And Export Board of India\n b) Services And Export Board of India\n c) Securities And Exchange Board of India'
      '\n d) Supply And Exchange Business of India') # c
q3 = input('Enter the option ')

print('Q 4) On which day National Mathematics day celebrated ?')
print('a) June 22\n b) May 16th\n c) December 20\n d) December 22') # d
q4 = input('Enter the option ')

print('Q 5) In which year Reserve Bank of India was established ?')
print('a) In 1935\n b) 1945\n c) 1955\n d) 1999') # a
q5 = input('Enter the option ')

x = 0

if q1 == 'a':
      x = x + 1
if q1 != 'a':
      x = 0
if q2 == 'c':
      x = x + 1
if q3 != 'c':
      x = x - 1
if q3 == 'c':
      x = x + 1
if q3 != 'c':
      x = x - 1

if q4 == 'd':
      x = x + 1
if q4 != 'd':
      x = x - 1
if q5 == 'a':
      x = x + 1
if q5 != 'a':
      x = x - 1

if x == 5:
    print('Congratulations You Scored 5/5')
elif x < 0:
      print('Your Score is 0')
else:
      print('You Scored',x,'/5')




