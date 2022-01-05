## Troubleshooting Car Issues

An expert system is a type of artificial intelligence program
that uses a knowledge base and a set of rules to perform a
task that a human expert might do. Many websites are
available that will help you self-diagnose a medical issue by
answering a series of questions. And many hardware and
software companies offer online troubleshooting tools to
help people solve simple technical issues before calling a
human.

Create a program that walks the user through troubleshoot-
ing issues with a car. Use the following decision tree to build
the system:

![Expert system](src/makingDecisions/troubleshootingCarIssues/expert-system.png)

### Example Output

Is the car silent when you turn the key? y
Are the battery terminals corroded? n
The battery cables may be damaged.
Replace cables and try again.


## Constraint
• Ask only questions that are relevant to the situation and
to the previous answers. Don’t ask for all inputs at once.


## Inputs, Processes, Outputs
nouns: program, user, car, decision tree
verbs: create, walks, troubleshooting, build


## Test Case Examples:

Inputs:y, y 
Expected result: Clean terminals and try starting again.
Actual result:

Inputs: n, y
Expected result: Replace the battery.
Actual result:

Inputs: n, n, n, y, y
Expected result: Get it in for service.
Actual result:

Inputs: n, n, y
Expected result: Check spark plug connections.
Actual result:

Inputs: n, n, n, y, n
Expected result: Check to ensure the choke is opening and closing.
Actual result:


-- More tests needed for all branching logic