from flask import Blueprint, redirect, session, url_for
from flask_login import login_required, logout_user

logout_ = Blueprint("logout", __name__, template_folder="templates")


@logout_.route("/devorbit/logout")
@login_required
def logout():
    if "user" in session:
        session.pop("user", None)
        logout_user()
    return redirect(url_for("login.login_page"))
