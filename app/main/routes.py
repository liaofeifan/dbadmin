from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from pyecharts import Bar, Scatter3D
from pyecharts import Page
from app import db
# from app.main.forms import ***
from app.models import User
from app.main import bp
import random


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
#@login_required
def index():
    s3d = scatter3d()
    return render_template(
        "pyecharts.html",
        myechart=s3d.render_embed(),
        host=current_app.config['REMOTE_HOST_PATH'],
        script_list=s3d.get_js_dependencies(),
    )
    # return render_template('index.html', myechart=bar.render_embed())
    #, host=current_app.config['REMOTE_HOST_PATH'], script_list=bar.get_js_dependencies()


def scatter3d():
    data = [generate_3d_random_point() for _ in range(80)]
    range_color = [
        "#313695",
        "#4575b4",
        "#74add1",
        "#abd9e9",
        "#e0f3f8",
        "#fee090",
        "#fdae61",
        "#f46d43",
        "#d73027",
        "#a50026",
    ]
    scatter3D = Scatter3D("3D scattering plot demo", width=1200, height=600)
    scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
    return scatter3D


def generate_3d_random_point():
    return [
        random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)
    ]
