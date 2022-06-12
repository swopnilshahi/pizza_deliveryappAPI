#Generating SECRET_KEY 
#python
import secrets
secrets.token_hex(15)

pip install python-decouple
(from decouple import config) to change parameter without redeploying app
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/

https://djoser.readthedocs.io/en/latest/getting_started.html