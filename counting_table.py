from dates import Dates

date = Dates()
class CountingTable:
    # [신입생수, 재학생수]
    def __init__(self, month):
        self.firstMonth = [[0, 0] for _ in range(date.calculate_days(month[0]))]
        self.secondMonth = [[0, 0] for _ in range(date.calculate_days(month[1]))]