from flask import Blueprint, render_template, request, redirect, flash, url_for
from app.database import get_db_connection
from app.utils import get_jalali_today
from app.constants import SECTIONS, STATIONS, REASONS, UNITS

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def index():
    return render_template(
        "index.html", 
        sections=SECTIONS, 
        today=get_jalali_today(), 
        stations=STATIONS, 
        reasons=REASONS, 
        units=UNITS
    )

@main_bp.route("/add/<t>", methods=["POST"])
def add(t):
    date = f"{request.form['year']}/{request.form['month']}/{request.form['day']}"
    data = {"date": date}
    
    for f, _, _ in SECTIONS[t]["fields"]:
        data[f] = request.form.get(f)
        
    table_mapping = {
        "main_prod": "main_production", 
        "stoppages": "line_stoppages", 
        "inventory": "chassis_inventory", 
        "parts_shortage": "parts_shortage"
    }
    
    tbl = table_mapping.get(t)
    if not tbl:
        flash("بخش نامعتبر است.", "danger")
        return redirect(url_for('main.index'))
        
    cols = ",".join(data.keys())
    placeholders = ",".join(["?"] * len(data))
    
    conn = get_db_connection()
    conn.execute(f"INSERT INTO {tbl} ({cols}) VALUES ({placeholders})", list(data.values()))
    conn.commit()
    conn.close()
    
    flash("✅ اطلاعات با موفقیت ذخیره شد", "success")
    return redirect(url_for('main.index'))
