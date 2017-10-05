from db import db

class ReserveModel(db.Model):
    __tablename__ = 'reserves'
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(255))
    name = db.Column(db.String(100))
    division = db.Column(db.String(50))
    timeslot = db.Column(db.Integer)
    date = db.Column(db.String(10))
    iat = db.Column(db.String(10))

    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    room = db.relationship('RoomModel')

    def __init__(self, topic, name, division, timeslot, date, iat, room_id):
        self.topic = topic
        self.name = name
        self.division = division
        self.timeslot = timeslot
        self.date = date
        self.iat = iat
        self.room_id = room_id

    def json(self):
        return { 'topic':self.topic, 'name': self.name, 'division': self.division, 'timeslot': self.timeslot, 'date': self.date, 'iat' :self.iat}

    @classmethod
    def find_by_room_id(cls, id):
        return cls.query.filter_by(room_id=id).first()

    @classmethod
    def find_by_used_room(cls, **kwargs):
        return cls.query.filter_by(room_id=kwargs.get('room_id'),date=kwargs.get('date'),timeslot=kwargs.get('timeslot')).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
