"""
Contains routes for main purpose of app
"""
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import current_user, login_required
from sqlalchemy import exc
from sqlalchemy import orm
from app import db
from app.models import Party, Guest
from app.main import bp

CONTACT_MSG = "Kontakta Kim eller Andreas"

@bp.route('/create_party', methods=['POST'])
def create_party():
    """
    Route for creating parties
    """
    data = request.get_json()
    result = {
        "new": [],
        "existing": [],
    }
    respons = result, 200
    if isinstance(data, list):
        try:
            for party_data in data:
                current_app.logger.debug("POST data: {}".format(party_data))
                try:
                    existing_party = Party.query.filter_by(email=party_data["email"]).one()
                    current_app.logger.debug("Excisting email found: {}".format(existing_party.to_dict()))
                    result["existing"].append(existing_party.to_dict())
                except orm.exc.NoResultFound:
                    party = Party.create_party(party_data)
                    current_app.logger.info("Created party: {}".format(party.to_dict()))
                    result["new"].append(party.to_dict())
            db.session.commit()
        except Exception as e:
                current_app.logger.error(str(e))
                return CONTACT_MSG, 500
    else:
        return "Submit data as list", 406
    return respons



@bp.route('/update_party', methods=['PUT'])
def update_party():
    """
    Route for updating attendance for a party
    """
    respons = "Success", 200
    data = request.get_json()
    if isinstance(data, dict):
        current_app.logger.debug("PUT data: {}".format(data))
        try:
            party = Party.query.filter_by(id=data["id"]).one()
            current_app.logger.debug("Party found {}".format(party.to_dict()))
            party.update_party(data)
            db.session.commit()
            respons = party.to_dict(), 200
        except orm.exc.NoResultFound as e:
            respons = ("Party with id {} doesnt exist, using email {}".format(
                    data["id"],
                    data["email"],
                ), 
                400)
            current_app.logger.warning(respons)
            current_app.logger.debug(str(e))
            respons = CONTACT_MSG, 404
            db.session().rollback()
        except ValueError as e:
            current_app.logger.debug(str(e))
            respons = CONTACT_MSG, 404
            db.session().rollback()
    else:
        return "Submit data as dict", 406
    return respons
