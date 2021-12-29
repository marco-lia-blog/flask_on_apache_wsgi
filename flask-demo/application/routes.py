"""Some routes."""
from flask import Blueprint, render_template
from datetime import datetime


# Blueprint Configuration
main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@main_bp.route('/', methods=['GET'])
def dashboard():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return render_template(
        'welcome.jinja2',
        title='Flask on Apache with mod_wsgi', current_time=current_time
    )

