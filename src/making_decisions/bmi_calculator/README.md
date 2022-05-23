# BMI Calculator

You’ll often need to see if one value is within a certain range and alter the flow of a program as a result.

Create a program to calculate the body mass index (BMI) for a person using the person’s height in inches and weight in pounds. The program should prompt the user for weight and height.

Calculate the BMI by using the following formula:

bmi = (weight / (height × height)) * 703


If the BMI is between 18.5 and 25, display that the person is at a normal weight. If they are out of that range, tell them if they are underweight or overweight and tell them to consult their doctor.

## Example Output
Your BMI is 19.5.
You are within the ideal weight range.

or

Your BMI is 32.5.
You are overweight. You should see your doctor.


## Constraint
Ensure your program takes only numeric data. Don’t
let the user continue unless the data is valid.



#### Inputs, Processes, Outputs
Nouns = body mass index, height (inches), weight (lbs)
Verbs = calculate, prompt, display


#### Test Cases
Inputs: height(72), weight(250)
Expected result: 33.9. You are overweight. Please consult your doctor
Actual result:

Inputs: height(72), weight(182)
Expected result: 24.68. You are within the idea weight range.
Actual result:

Inputs: height(50), weight(200)
Expected result: 56.24. You are overweight. Please consult your doctor
Actual result:

Inputs: height(50), weight(50)
Expected result: 14.06. You are underweight. Please consult your doctor
Actual result:

Inputs: height(w), weight(A)
Expected result: please enter numeric values for height(inches) and weight(lbs)
Actual result: