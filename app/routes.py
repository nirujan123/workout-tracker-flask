from flask import Blueprint, render_template, request
from .db import init_db, insert_workout, get_all_workouts

bp = Blueprint("main", __name__)

@bp.route("/")
def home():
    return render_template("home.html")

@bp.route("/add", methods=["POST"])
def add_workout():
    date = request.form.get("date")
    exercise = request.form.get("exercise")
    sets = request.form.get("sets")
    reps = request.form.get("reps")
    weight = request.form.get("weight")

    insert_workout(date, exercise, sets, reps, weight)

    return render_template(
        "result.html",
        date=date,
        exercise=exercise,
        sets=sets,
        reps=reps,
        weight=weight
    )

@bp.route("/init-db")
def init_db_route():
    init_db()
    return "Database initialised!"

@bp.route("/workouts")
def workouts():
    rows = get_all_workouts()
    return render_template("workouts.html", workouts=rows)

@bp.route("/debug-routes")
def debug_routes():
    return "Routes file loaded ✅"
