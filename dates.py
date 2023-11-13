class Dates:
    def __init__(self):
        self.months = []
        self.days = 0
        self.first_days = 0
        self.second_days = 0
        self.firstMonth = []
        self.secondMonth = []

    def set_month(self, month):
        self.months.append(month[0])
        self.months.append(month[1])
    def calculate_days(self, month):
        days = 30 + (month % 2 if month <= 7 else (0 if month % 2 else 1))
        return days

    def days_in_first_month(self):
        self.first_days = self.calculate_days(self.months[0])
        print(self.first_days)
        self.firstMonth = [[] for _ in range(self.first_days)]

    def days_in_second_month(self):
        self.second_days = self.calculate_days(self.months[1])
        print(self.second_days)
        self.secondMonth = [[] for _ in range(self.second_days)]

    # def sortTheMonthList(self):
    #     self.firstMonth.sort(reverse=True)
    #     self.secondMonth.sort(reverse=True)