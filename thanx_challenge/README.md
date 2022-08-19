# Challenge
At Thanx, we offer our merchants the ability to run a VIP engagement program
for their customers (users). In order for a user to become a VIP at a
merchant, a user needs to spend above the threshold set, for two consecutive
months.
For example if the threshold is $100, a user that spends $100 in January and
$100 in February, would become VIP. On the other hand, a user that spends
$100 in January and $85 in February, would not become VIP.
Given the below purchase data, write a program that takes a threshold and
purchase data as input and returns all users who would qualify for VIP in the
most recent month.
Optional: allow for a variable number of consecutive months as input.
Optional: add logic to generate sample purchase data
 
## Interpretation
The input of this version of the program is going to a json that was shared (I've added a couple of examples in order to test the different possibilities).
This program is going to create a data frame with all the transactions, analyze the monthly purchases per user and check if the total amount is equal or higher than the threshold for the last n consecutives months.
The outputs are:
* a dictionary with the status of all of the customers
* a dictionary with only the vip customers
 
## Explanation
In this folder you will find:
* pur_list.json : this is the input file
* functions.py : here we have all the functions that are going to be use
* main.py : the main file which runs the program
* exploratory.ipynb : this was the notebook that I used to build the code