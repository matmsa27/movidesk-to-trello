# Movidesk to Trello
A project to create a integration between two platforms: [Movidesk](https://www.movidesk.com/) and [Trello](https://trello.com/)

- The [Movidesk](https://www.movidesk.com/) is a platform used in corporative environments to management the TI tickets on technologies companies.
- The [Trello](https://trello.com/) is a platform from Atlassian to management projects, creating boards, cards, labels, to define deadlines, responsibile colaborators and etc.

## Project description and motivation

This project has a motivation to integrate the Movidesk and Trello for work together. In a common case on in a  technology companay, the product and development team prefeer to use the tools like Trello to management the tasks, like features, bugs and etc. 

The support team works with Movidesk receiving questions, doubts and bugs from customers, all that contact from customer to company with Movidesk, is treated like `ticket`. On bugs or improvements that customers report, these tickets are atributted to product and development team, that can use the Trello normally.

With this tool, you can create a trigger on movidesk, and all the support level 3 tickets that are created, will trigger a webhook pointing out a address on this project.


### Use case in Ilhasoft Technology Company
-> To do


## Tools used
This project are building with [Python](https://www.python.org/) and the [Flask Framework](https://flask.palletsprojects.com/en/1.1.x/).

We use another librarys like:
- python-decouple
- python-requests

The specific version from each library, you can found on `pip-freeze.txt`

## How to configure and run
- First of all you need the create a pipenv environent with the command:
`pipenv install`
- And then, after install the libraries, you need the enter the environment with the command:
`pipenv shell`

- With the environment already, you need to define some environment variables to run the project. That variables are:

 | Environment Variable 	| Type   	| Description                                                                                                                                     	|
|----------------------	|--------	|-------------------------------------------------------------------------------------------------------------------------------------------------	|
| `TRELLO_KEY`         	| string 	| that you can find [here](https://trello.com/app-key)                                                                                            	|
| `TRELLO_TOKEN`       	| string 	| that you can find [here](https://trello.com/app-key)                                                                                            	|
| `TRELLO_ID_LIST`     	| string 	| and you can find follow the steps on [this docummentation](https://www.mangoblogger.com/blog/how-to-get-the-list-id-from-the-trello-api-board/) 	|

 PS: `TRELLO_ID_LIST` refers the column on trello board that will be created the new cards.
 
 
 You can define the environemnts variables with a `.env` file or using the command `export TRELLO_ID_LIST=<value>`.


