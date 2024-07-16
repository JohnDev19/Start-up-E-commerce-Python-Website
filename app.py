from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

from routes import main, auth, product, cart
app.register_blueprint(main)
app.register_blueprint(auth)
app.register_blueprint(product)
app.register_blueprint(cart)

if __name__ == '__main__':
    app.run(debug=True)