SECTIONS = {
    "main_prod": {
        "title": "تولید و تحویل",
        "fields": [
            ("actual", "تولید واقعی", "number"),
            ("plan", "برنامه تولید", "number"),
            ("commercial_count", "تولید تجاری شده", "number"),
            ("customer_delivery", "تحویل به مشتری", "number")
        ]
    },
    "stoppages": {
        "title": "اطلاعات توقف خط",
        "fields": [
            ("duration", "زمان توقف (ساعت)", "text"),
            ("station", "ایستگاه توقف", "select"),
            ("reason", "علت توقف", "select"),
            ("responsible_unit", "واحد مسئول", "select"),
            ("start_time", "ساعت شروع", "time"),
            ("end_time", "ساعت پایان", "time")
        ]
    },
    "inventory": {
        "title": "موجودی شاسی‌ها",
        "fields": [
            ("factory_chassis", "شاسی کارخانه", "number"),
            ("customs_chassis", "شاسی گمرک", "number"),
            ("kite_need", "نیاز کایت و بال", "number"),
            ("side_need", "نیاز ساید", "number")
        ]
    },
    "parts_shortage": {
        "title": "کسری قطعات",
        "fields": [
            ("item_code", "کد کالا", "text"),
            ("item_desc", "شرح کالا", "text"),
            ("item_qty", "تعداد", "number"),
        ]
    }
}

STATIONS = ["بدون توقف", "C01", "C02", "C04", "C07", "C12", "K05", "K07"]
REASONS  = ["برنامه مدیریتی", "تست", "تعمیرات", "کمبود مواد", "عملکرد اپراتور", "سایر"]
UNITS    = ["تولید", "مهندسی", "کیفیت", "مدیریت", "تأمین خارج"]
