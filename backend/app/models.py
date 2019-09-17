"""
Contains Databse model classes
"""

from hashlib import md5
from datetime import datetime
import uuid 
from flask import current_app
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login

class Party(UserMixin, db.Model):
    """
    Represents a party invited to the wedding
    """
    id = db.Column(db.String(6), unique=True)
    email = db.Column(db.String(120), primary_key=True)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    osa = db.Column(db.Boolean)
    guests = db.relationship('Guest', backref='party', lazy='dynamic')

    @staticmethod
    def create_id(email):
        """
        Retry creating uniqe ID.
        """
        counter = 0
        size = 10
        while True:
            hash = uuid.uuid1().hex[:size]
            counter += 1
            try:
                existing = db.session.query(Party).filter_by(id=hash).one()
                current_app.logger.debug("ID exist {}. For email".format(hash, email))
            except:
                return hash
            if counter > 10:
                size += 2
                current_app.logger.debug("Trying to generate id for {}. On try {}".format(email, counter))


    def __repr__(self):
        return '<Party {}, {}>'.format(self.id, self.email)
    
    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "osa": self.osa,
            "guests": [g.to_dict() for g in self.guests.all()],
        }

    @staticmethod
    def create_party(data):
        id_ = Party.create_id(data["email"])
        party = Party(id=id_, email=data["email"], osa=False)
        db.session.add(party)
        for guest_data in data["guests"]:
            guest = Guest(name=guest_data["name"], party=party)
            db.session.add(guest)
        return party

    def update_party(self, data):
        
        # kolla att data inte redan satt
        
        for guest_data in data["guests"]:
            try:
                guest = self.guests.filter_by(name=guest_data["name"]).one()
                guest.coming = True if guest_data["coming"] in ("True", "true") else False
                guest.food = guest_data["food"]
                guest.drink = guest_data["drink"]
                guest.allergy = guest_data["allergy"]
                current_app.logger.info("Updated guest: {} ".format(guest.to_dict()))
            except orm.exc.NoResultFound:
                msg = "No guest with name {} in party {}".format(
                    guest_data["name"],
                    data["id"]
                )
                current_app.logger.warning(msg)
                msg = "Hittar ingen gäst med namnet {}. ".format(
                    guest_data["name"],
                )
                raise ValueError(msg)
            self.osa = True

    @staticmethod
    @login.user_loader
    def load_user(id_):
        """
        Return user base on id.
        """
        return Party.query.get(id_)



class Guest(db.Model):
    """
    Represents a Guest
    """
    name = db.Column(db.String(140), primary_key=True)
    coming = db.Column(db.Boolean, nullable=True)
    food = db.Column(db.String(140))
    drink = db.Column(db.String(140))
    allergy = db.Column(db.String(255))
    party_id = db.Column(db.Integer, db.ForeignKey('party.email'), primary_key=True)

    def __repr__(self):
        return '<Guest: {}, coming: {} with party {}>'.format(self.name, self.coming, self.party_id)

    def to_dict(self):
        return {
            "name": self.name,
            "coming": self.coming,
            "food": self.food,
            "drink": self.drink,
            "allergy": self.allergy,
        }
