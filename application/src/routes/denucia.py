from flask import Blueprint, render_template

# Pagina off

denucia = Blueprint("denucia", __name__, template_folder="templates")


@denucia.route("/devorbit/denucia/", methods=["POST", "GET"])
def page_denucia():
    return render_template("denucia.html")
