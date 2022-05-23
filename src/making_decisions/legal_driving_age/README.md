# Legal Driving Age 
You can test for equality, but you may need to test to see how a number compares to a known value and display a message if the number is too low or too high.
Write a program that asks the user for their age and compare it to the legal driving age of sixteen. If the user is sixteen or older, then the program should display “You are old enough
to legally drive.” If the user is under sixteen, the program should display “You are not old enough to legally drive.”

## Challenges

If the user enters a number that’s less than zero or enters non-numeric data, display an error message that asks the user to enter a valid age.

Instead of hard-coding the driving age in your program logic, research driving ages for various countries and create a lookup table for the driving ages and countries. Prompt for the age, and display which countries the user can legally drive in.


### Example Output
What is your age? 15
You are not old enough to legally drive.
Or
What is your age? 35
You are old enough to legally drive.

### Constraints
Use a single output statement.
Use a ternary operator to write this program. If your
language doesn’t support a ternary operator, use a regular if/else statement, and still use a single output statement to display the message.


###### Inputs Processes Outputs
Verbs : asks, compare, display 

Nouns : age, legal driving age 




###### Test case
Inputs: 15
Expected result: You are not old enough to legally drive
Actual result: 

Inputs: 16
Expected result: You are old enough to legally drive
Actual result:

Inputs: 27
Expected result: You are old enough to legally drive
Actual result:

Inputs: 30.2
Expected result: Please enter a valid age.
Actual result:




