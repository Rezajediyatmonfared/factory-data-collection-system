import sqlite3
from flask import current_app

def get_db_connection():
    # اتصال به دیتابیس با استفاده از مسیر مشخص شده در Config
    conn = sqlite3.connect(current_app.config['DB_NAME'])
    conn.row_factory = sqlite3.Row  # دسترسی به ستون‌ها با نام به جای اندیس
    return conn

def init_db():
    conn = sqlite3.connect('factory_management_new.db') # در اجرای اولیه مستقیم آدرس می‌دهیم
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS main_production(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT, actual INTEGER, plan INTEGER,
        commercial_count INTEGER, customer_delivery INTEGER)""")
    c.execute("""CREATE TABLE IF NOT EXISTS line_stoppages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT, duration REAL, station TEXT,
        reason TEXT, responsible_unit TEXT,
        start_time TEXT, end_time TEXT)""")
    c.execute("""CREATE TABLE IF NOT EXISTS chassis_inventory(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT, factory_chassis INTEGER,
        customs_chassis INTEGER, kite_need INTEGER,
        side_need INTEGER)""")
    c.execute("""CREATE TABLE IF NOT EXISTS parts_shortage(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT, item_code TEXT,
        item_desc TEXT, item_qty INTEGER)""")
    conn.commit()
    conn.close()
