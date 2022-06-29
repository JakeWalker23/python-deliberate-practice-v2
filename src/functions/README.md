# Months To Pay Off A Credit Card

It can take a lot longer to pay off your credit card balance
than you might realize. And the formula for figuring that
out isn’t pretty. Hiding the formula’s complexity with a
function can help you keep your code organized.

Write a program that will help you determine how many
months it will take to pay off a credit card balance. The
program should ask the user to enter the balance of a credit
card and the APR of the card. The program should then
return the number of months needed.

The formula for this is

** INSERT FORMULA**

where
n is the number of months.
i is the daily rate (APR divided by 365).
b is the balance.
p is the monthly payment.


## Inputs, Processes, Outputs

nouns = prgram, months, credit card balance, APR,
verbs = determine, ask, enter, return 



## Test Cases

Inputs: Balance, APR, Monthly Repayment
Expected Result: It will take you X Months to pay off this card
Actual Result:

Inputs: 5000, 12%, 100
Expected Result: It will take you 69.4 Months to pay off this card
Actual Result:

Inputs: 5000, 1%, 1000
Expected Result: 5.0
Actual Result:

Inputs: 5000, 10%, 100 
Expected Result: 64.7
Actual Result:

Inputs: 80000, 2.5, 350
Expected Result:309.1
Actual Result:


## Example Input:

What is your balance? 5000
What is the APR on the card (as a percent)? 12
What is the monthly payment you can make? 100
It will take you 70 months to pay off this card.

Give or take +-3 months