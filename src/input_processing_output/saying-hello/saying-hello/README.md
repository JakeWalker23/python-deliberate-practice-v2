# Problem Statement

Create a program that prompts for your name and prints a greeting using your name.

### Example Output
What is your name? Brian
Hello, Brian, nice to meet you!

### Inputs, Processes, Outputs
Inputs : name
Processes: prompts, prints
Outputs: greeting

### Test Plan
Inputs: Jake
Expected result: Hello, Jake, nice to meet you!

Inputs: Brian 
Expected result: Hello, Brian, nice to meet you!
Actual result:

Inputs: Wilma 
Expected result: Hello, Wilma, nice to meet you!
Actual result:

Inputs: 75 
Expected: Sorry, please enter a string as an input. Try again. 
Actual result:

### Psuedocode

prompt: Ask user for input

    check if input is a string.

    if not a string:
        print: Sorry, please enter a string as an input. Try again.

print: Hello, {NAME}, nice to meet you!

