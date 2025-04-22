
from flask import Blueprint, render_template, request, redirect, url_for # type: ignore

from pyexpat.errors import messages
from flask import render_template, request, redirect, url_for, flash, session # type: ignore
from flask import render_template, request, redirect, url_for, flash, session # type: ignore
from flask_login import current_user, login_user, logout_user # type: ignore
from flask_login.utils import login_required # type: ignore

from aetherios.models import Aetherios

rt = Blueprint('routes', __name__)

@rt.route('/')
def appear():
    return "helloworld"
