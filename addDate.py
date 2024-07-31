from datetime import datetime, timedelta

class myDate():
    def __init__(self, day, month , year):
        self.day = day
        self.month = month
        self.year = year
        self.date = datetime(year, month, day)
        
    def addDays(self, days) -> 'myDate' :
        new_date = self.date + timedelta(days=days)
        return myDate(new_date.day, new_date.month, new_date.year)
    def __str__(self):
        return self.date.strftime("%d-%m-%Y")
class Main:
    @staticmethod
    def main():
        original_date = myDate(31, 7, 2024)
        print(f"original Date: {original_date}")
        
        
        new_Date = original_date.addDays(30)
        print(f"new date after adding 30 days: {new_Date}")
if __name__ == "__main__":
    Main.main()