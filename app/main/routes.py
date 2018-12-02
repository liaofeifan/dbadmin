from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from app import db
#from app.main.forms import ***
from app.models import User
from app.main import bp




@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
#@login_required
def index():
    return render_template('index.html')
