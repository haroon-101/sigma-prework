import datetime


def age(birthday):
    today = datetime.date.today()
    day, month, year = birthday.split("-")
    res = today.year - int(year)
    if (int(month) > today.month) or (int(month) == today.month and int(day) > today.day):
        res -=1
    
    return res
        

if __name__ == "__main__":
    print(age("20-10-2002"))
