import datetime

def get_jalali_today():
    d = datetime.date.today()
    gy, gm, gd = d.year - 1600, d.month - 1, d.day - 1
    g_days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    g_day_no = 365 * gy + (gy + 3) // 4 - (gy + 99) // 100 + (gy + 399) // 400
    g_day_no += g_days[gm] + gd
    if gm > 1 and ((gy % 4 == 0 and gy % 100 != 0) or gy % 400 == 0):
        g_day_no += 1
    j_day_no = g_day_no - 79
    j_np = j_day_no // 12053
    j_day_no %= 12053
    jy = 979 + 33 * j_np + 4 * (j_day_no // 1461)
    j_day_no %= 1461
    if j_day_no >= 366:
        jy += (j_day_no - 1) // 365
        j_day_no = (j_day_no - 1) % 365
    for i, dm in enumerate([31] * 6 + [30] * 5 + [29]):
        if j_day_no < dm:
            return jy, i + 1, j_day_no + 1
        j_day_no -= dm
