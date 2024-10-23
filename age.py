from datetime import datetime

def get_current_date():
    return datetime.now()


def calculate_age(date):
    store_date_info = date.split("-")
    store_current_date = get_current_date()

    age = calc_year_diff(int(store_date_info[2]),store_current_date)

    if (store_current_date.month < int(store_date_info[1])) or  (store_current_date.month == int(store_date_info[1]) and store_current_date.day < int(store_date_info[0])):
        return age-1
    return age

def calc_year_diff(year_now,year):
    return year.year - year_now

if __name__ == "__main__":
    #print(calculate_age("DD-MM-YYYY"))
    pass
