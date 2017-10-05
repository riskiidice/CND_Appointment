# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse

from models.room import RoomModel

class Room(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('name',
        required=True,
        help = "The room cannot be blank!!"
    )

    parser.add_argument('location',
        required=True,
        help="The location cannot be blank!!"
    )

    def get(self, id):

        room = RoomModel.find_by_id(id)

        if room :
            return room.json()

        return {'message': 'Item not found'}, 404

    def post(self):

        data = self.parser.parse_args()

        if RoomModel.find_by_name(data['name']):
            return {'message': 'มีชื่อห้องประชุม {} แล้วในระบบ'.format(data['name'])}, 400

        room  = RoomModel(**data)

        try:
            room.save_to_db()
        except:
            return {'message': 'Error occur inserting the room'}, 500

        return room.json(), 201


    def put(self, id):
        pass

    def delete(self, id):
        pass

class RoomList(Resource):
    def get(self):
        return {'rooms': [room.json() for room in RoomModel.query.all()]}
