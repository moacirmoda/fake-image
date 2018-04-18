Fake Image
==========

Flask project that receive size as url parameters and returns a PNG image with 
those sizes.

How to use
----------

Access your domain with size as parameter. Example:
```
https://yourdomain.com/500x500
``` 

It will return an PNG image with those size.

Run project
-----------
* Create and activate an virtualenv with `python3`
* Install dependencies
```
pip install requirements.txt
```
* Run tests
```
python tests.py
```
* Execute flask server
```
export FLASK_APP=app.py
flask run
```