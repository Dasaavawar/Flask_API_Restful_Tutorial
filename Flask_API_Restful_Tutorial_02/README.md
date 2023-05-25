# Tutorial API REST- Flask (cipher/decipher)
REST API - Flask. This is a basic API that provides 2 endpoints, to encrypt and decrypt information using the RC4 algorithm used in WEP. This application is developed for the Cloud Solutions Development course.

# App
To run the application follow the instructions below:

## Create a new virtual environment
* ```$ python3 -m venv new_environment```
* ```$ source new_environment/bin/activate```

## Install requirements
* ```$ pip install flask``` 
* ```$ pip install flask-restful```
* ```$ pip install flask-marshmallow```

## Configure environment variables
* ```$ export FLASK_APP=app.py```
* ```$ export FLASK_DEBUG=1```
* ```$ export FLASK_ENV=development```

## Run
* ```$ flask run -h 0.0.0.0```

## Using the virtual services
* Use Postman (or any equivalent tool) to realize the post requests to the respective available endpoints. 
* Route Endpoint 1 [POST]: ```http://ip_servidor:5000/cipher```
* Route Endpoint 2 [POST]: ```http://ip_servidor:5000/decipher```
* Both Endpoints require a JSON with the following format:  
```{"message" : "Text to Cipher/Decipher", "key": "Key to Cipher/Decipher"}```

## Loading tests (Basics)
### Install Apache Benchmark
* ```$ sudo apt-get install apache2-utils```  
### Create JSON files
* Create a JSON file from the example (you will find a couple of available examples within the repository):  
```{"message" : "Text to Cipher/Decipher", "key": "Key to Cipher/Decipher"}```
### Running the command 
* ```$ ab -n 1000 -c 100 -p data-cipher.json -T application/json -rk http://ip_server:5000/cipher```
* ```$ ab -n 1000 -c 100 -p data-descipher.json -T application/json -rk http://ip_server:5000/decipher```  

where:
* ```-k (keepAlive)```. Making multiple requests within one HTTP session, browser functionality by nature
* ```-r (flag)```. Indicates that the connection (socket) is not closed when receiving errors
* ```-n (requests)```. Total number of requests to execute
* ```-c (concurrency)```. Number of concurrent connections
* ```-p (file.json)```. JSON that is sent in the request body
* ```-T application/json```. Specifies the data structure of the body


# RC4 ciphering based for the project:
* [https://github.com/g2jun/RC4-Python](https://github.com/g2jun/RC4-Python)
