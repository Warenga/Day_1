# Day_1
Andela Bootcamp 12: Day 1

### OOP example
## Employee class
This repo implements a company real-world problem by creating a Super class named 'Employee' of which Sub classes 'PartTime', 'FullTime' and 'Casual' are created. The subclasses satisfy the need to categorize the different employees and also calculate their salary separately.

## OOP concepts included:
1. Inheritance
	- PartTime, FullTime and Casual inherite from Employee
2. Polymorphism
	- The abstract method 'job_type' is included. Only the subclasses can call 'job_type'
3. Encapsulation
	- The pay attribute in Employee is set to private. Can only be accessed by running object._Employee__.pay.

## The repo contains various unittests that the application pass.
