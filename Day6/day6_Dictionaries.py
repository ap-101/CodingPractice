# Task 4 On Dictionaries:- 2 examples on  duplicates not allowed.
# Example 1:-
dict1 = { 'Name' : 'Mr. Robot', 'Age' : '59', 'Job' : 'Hacker', 'Name':'hello'}
print(dict1) # O/P :- {'Name': 'hello', 'Age': '59', 'Job': 'Hacker'}

# Example 2:-
dict2 = {'Year':'1991', 'Month':'January','Day' : 'Monday',}
print(dict2) # O/P :- {'Year': '1991', 'Month': 'January', 'Day': 'Monday'}
dict2['Year'] = '1920'
print(dict2) # O/P :- {'Year': '1920', 'Month': 'January', 'Day': 'Monday'}
