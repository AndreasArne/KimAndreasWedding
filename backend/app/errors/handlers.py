"""
Contains error handlers
"""
from flask import current_app
from app import db
from app.errors import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    """
    Error handler for code 404
    """
    current_app.logger.info(error)
    return error, "404"


@bp.app_errorhandler(500)
def internal_error(error):
    """
    Error handler for code 500
    """
    current_app.logger.info(error)
    db.session.rollback()
    return error, "500"
