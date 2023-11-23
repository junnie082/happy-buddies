class Dates:
    def __init__(self):
        self.months = []
        self.days = 0
        self.first_days = 0
        self.second_days = 0
        self.names_in_first_month = []
        self.names_in_second_month = []

    def set_month(self, months):
        self.months = months
        #self.months.append(month[0])
        #self.months.append(month[1])

    def calculate_days(self, month):
        days = 30 + (month % 2 if month <= 7 else (0 if month % 2 else 1))
        return days

    def iniNamesInFirstMonth(self):
        self.first_days = self.calculate_days(self.months[0])
        self.names_in_first_month = [[] for _ in range(self.first_days)]

    def iniNamesInSecondMonth(self):
        self.second_days = self.calculate_days(self.months[1])
        self.names_in_second_month = [[] for _ in range(self.second_days)]

    # def add_member_in_date(self, month, name):
    #     if month == self.months[0]:
    #         self.firstMonth[self.calculate_days(month) - 1].append(name)
    #     else:
    #         self.secondMonth[self.calculate_days(month) - 1].append(name)

    # def sortTheMonthList(self):
    #     self.firstMonth.sort(reverse=True)
    #     self.secondMonth.sort(reverse=True)