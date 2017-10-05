# -*- coding: utf-8 -*-
import time
from flask_restful import Resource, reqparse

from models.reserve import ReserveModel

class Reserve(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('topic',
        required=True,
        help = "The topic cannot be blank!!"
    )

    parser.add_argument('name',
        required=True,
        help = "The room cannot be blank!!"
        )

    parser.add_argument('division',
        required=True,
        help = "The division cannot be blank!!"
        )

    parser.add_argument('timeslot',
        type = int,
        required=True,
        help="The location cannot be blank!!"
    )

    parser.add_argument('room_id',
        type = int,
        required=True,
        help="The location cannot be blank!!"
        )

    parser.add_argument('date',
        required=True,
        help="The location cannot be blank!!"
    )

    def get(self, id):

        reserve = ReserveModel.find_by_room_id(id)

        if reserve :
            return reserve.json()

        return {'message': 'reserve not found'}, 404

    def post(self):

        data = self.parser.parse_args()

        # if ReserveModel.find_by_name(data['name']):
        #     return {'message': 'มีชื่อห้องประชุม {} แล้วในระบบ'.format(data['name'])}, 400
        data['iat'] = time.strftime('%x')

        if ReserveModel.find_by_used_room(room_id=data['room_id'],date= data['date'], timeslot=data['timeslot']):
            return {'message': 'ช่วงเวลาดังกล่าวมีผู้ใช้งานแล้ว'}, 400

        reserve  = ReserveModel(**data)

        try:
            reserve.save_to_db()
        except:
            return {'message': 'Error occur inserting the room'}, 500

        return reserve.json(), 201


    def put(self, id):
        pass

    def delete(self, id):
        pass

class ReserveList(Resource):
    def get(self):
        return {'reserves': [reserve.json() for reserve in ReserveModel.query.all()]}
