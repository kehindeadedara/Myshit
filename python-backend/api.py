import flask

class UserData():
    def __init__(self):
        super().__init__()

    def get_user_data(self):
        pass

    def authorize_user(self):
        pass

    def authenticate_image(self):
        pass


app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ['GET'])
def home():
    return "<h1>UT1 project API</h1>"



if __name__ == "__main__":
    app.run()