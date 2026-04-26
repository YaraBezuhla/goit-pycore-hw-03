from datetime import datetime

def get_user_date() -> str:
    while True:
        date = input('Input the date in the format "YYYY-MM-DD": ')
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("The date you entered is incorrect. Try again.")

def get_days_from_today(date: str) -> int:
    current_date = datetime.now()
    string_to_datetime = datetime.strptime(date, "%Y-%m-%d")
    delta = current_date - string_to_datetime
        
    if delta.days < 0:
        print(f"The specified date is later than the current date. Number of days: {delta.days}")
    elif delta.days == 1:
        print(f"The difference between the current date and the specified date is {delta.days} day")
    else:
        print(f"The difference between the current date and the specified date is {delta.days} days")    

date = get_user_date()
get_days_from_today(date)