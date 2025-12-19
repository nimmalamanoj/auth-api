from flask import Flask
from auth import auth_bp

app = Flask(__name__)

app.register_blueprint(auth_bp)


print(app.url_map)

@app.route('/')
def home():
    return "Server is running"


if __name__ == '__main__':
    app.run(debug=True)
