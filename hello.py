# This program says hello and asks for my name.

print('hello world');
print('What is your name');
myName = input();
print('It is nice to meet you ,' + myName);
print('The length of your name is : ');
print(len(myName));
print('What is your age');
myAge = input();
print('You will be ' + str(int(myAge)+1) + ' in a year');
