import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


# from security import authenticate,identity
# from resources.user import UserRegister
# from resources.item import Item, ItemList
# from resources.store import Store,StoreList
from resources.room import Room, RoomList
from resources.reserve import Reserve, ReserveList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "CCND"
api = Api(app)

#jwt = JWT(app, authenticate, identity) #/auth

# api.add_resource(Store,'/store/<string:name>')

api.add_resource(Room,'/room','/room/<string:id>')
api.add_resource(RoomList,'/rooms')
api.add_resource(Reserve,'/reserve','/reserve/<string:id>')
api.add_resource(ReserveList,'/reserves')
# api.add_resource(Item, '/item/<string:name>')
# api.add_resource(ItemList,'/items')
# api.add_resource(StoreList,'/stores')
# api.add_resource(UserRegister,'/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)

    @app.before_first_request
    def create_table():
        db.create_all()

    app.run(port=3000, debug=True)
