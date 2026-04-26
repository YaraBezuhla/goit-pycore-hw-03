from datetime import datetime, timedelta

def get_upcoming_birthdays(users):

    current_day = datetime.now().date()
    #current_day = datetime(2026, 2, 26).date() #for the February 29 birthday test
    greeting_days = []
    end_date = current_day + timedelta(days=7)
    
    for user in users:
        birth_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        try:
            birthday = birth_date.replace(year=current_day.year)
        except ValueError:
            birthday = birth_date.replace(year=current_day.year, day = 28)

        if birthday < current_day:
            try:
                birthday = birth_date.replace(year=current_day.year + 1)
            except ValueError:
                birthday = birth_date.replace(year=current_day.year + 1, day = 28)       

        congratulation_date = birthday

        if congratulation_date.weekday() == 5:
            congratulation_date += timedelta(days=2) 
        elif congratulation_date.weekday() == 6:
            congratulation_date += timedelta(days=1)  

        if current_day <= congratulation_date <= end_date:
            greeting_days.append({
                 "name": user["name"],
                 "greeting_day": congratulation_date.strftime("%Y-%m-%d"),
                 "birthday": birth_date.strftime("%Y-%m-%d")
        })       
        
    print(f"This week's list of greetings: {greeting_days}")  


users = [
    {"name": "John Doe", "birthday": "1985.04.27"},
    {"name": "Jane Smith", "birthday": "1990.05.01"},
    {"name": "Jane Doe", "birthday": "1990.04.26"},
    {"name": "Jan D", "birthday": "1990.06.01"},
    {"name": "test", "birthday": "2000.02.29"}
]

get_upcoming_birthdays(users)    