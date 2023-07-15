# AirBnB_clone

Project Description:
This is the first part of the AirBnB clone project towards building our first full web application
 where we work on the backend of the project while using a console
application as our interface with the help of the cmd module in python.

Command interpreter functionalities:
Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc...
Do operations on objects (count, compute stats, etc...)
Update attributes of an object
Destroy an object

How it works:
Clone the repository.
Navigate to the base directory of the AirBnB clone project.

run: ./console.py to launch it in interactive mode or

echo "help" | ./console.py in non-interactive mode.

To create an instance run:
create "classname". Example:
create BaseModel

To print the string representation of an instance run:
show "classname" "instance_id". Example:
show BaseModel 1234-1234-1234

To delete an instance run:
destroy "classname" "instance_id". Example:
destroy BaseModel 1234-1234-1234

To print all instances run:
all or
all "classname". Example:
all BaseModel

To update an instance run:
update "classname" "instance_id" "attribute_name" "attribute_value". Example:
update BaseModel 1234-1234-1234 email "aibnb@mail.com".

To get help about all commands available in the console run:
help or ?

To exit the console run:
quit or EOF

