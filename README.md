# machineLearningApiTemplate
Template for deploying ML models

# Set Up and Execution
This program using a Makefile to organize the code base.
To begin run the following command from the terminal:

`make install`

To turn on the API use the command:

`make run`

## API Specifications
###URLS
|   		|   									|
| ------------- | ---------------							|
| path		| `modelURL`								|
| method 	| `POST` 								|
| headers 	| `content-type: 'application/json'` 					|

### Request Contract
```json
{
"input format": "data"
}
```
### Reponse Contract
```json
{
"ouput format": "data"
}
```