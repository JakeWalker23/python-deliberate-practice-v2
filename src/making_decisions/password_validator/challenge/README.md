# Challenge

1.) Investigate how you can prevent the password from being displayed on the screen in clear text when typed.

2.) Create a map of usernames and passwords and ensure the username and password combinations match.

3.) Encode the passwords using Bcrypt and store the hashes in the map instead of the clear-text passwords. Then, when you prompt for the password, encrypt the password using Bcrypt and compare it with the value in your map.
