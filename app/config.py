import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will not pass'
    MONGO_URI = "mongodb+srv://kenny:Kennedy1@scrapper.yz48y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"