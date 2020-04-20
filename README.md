# machineLearningApiTemplate
Template for deploying ML models

The models and the API are distinct entities. This program provides the skeleton
to service multiple models. All models should be placed in the model zoo directory.

When a new model is added follow the following steps:
* Functions to process the response, make the prediction and return the request are added to modelZoo
* A \[model]Api.py file is added to modelAPI/api that specifies the URL
* The model is added to the model loader class

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