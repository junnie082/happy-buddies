from members import Members
from dates import Dates

dates = Dates()

class PairBuddies:
    def __init__(self):
        # {날짜, [{버디1, 버디2}]}
        self.buddies = {}
        self.cnt_table = []
        self.names_in_first_month = []
        self.names_in_second_month = []
        self.months = []
        self.mem = {}

    def setMembers(self, members):
        self.mem = members

    def setMonths(self, months):
        self.months = months

    def setCntTable(self, cnt_table):
        self.cnt_table = cnt_table
        self.cnt_table.sortMonthList()

    def setNamesInFirstMonth(self, names_in_first_month):
        self.names_in_first_month = names_in_first_month

    def setNamesInSecondMonth(self, names_in_second_month):
        self.names_in_second_month = names_in_second_month

    def getBuddies(self):
        return self.buddies

    def pairUpBuddies(self, monthList, namesInMonthList, month):
        # group[0] - 신입생 # group[1] - 재학생 # group[2] - 날짜
        for group in monthList:
            date = str(self.months[month]) + "." + str(group[2])
            if group[0] == 0 and group[1] == 0:
                continue
            for students in [namesInMonthList[group[2] - 1]]:
                newStudent = []
                oldStudent = []
                for student in students:
                    # 신입생
                    if self.mem.members[student][0] <= 2:
                        newStudent.append(student)
                    else:
                        oldStudent.append(student)


                for buddy1 in newStudent:
                    for buddy2 in oldStudent:

                        if (self.cnt_table.membersInCntTable[buddy1] >= 2 or self.cnt_table.membersInCntTable[buddy2] >= 2):
                            continue
                        if (buddy1 not in self.names_in_first_month[group[2] - 1]) or (buddy2 not in self.names_in_first_month[group[2] - 1]):
                            continue

                        if date not in self.buddies:
                            self.buddies[date] = [{buddy1: buddy2}]
                        else:
                            self.buddies[date].append({buddy1: buddy2})

                        self.cnt_table.membersInCntTable[buddy1] += 1
                        self.cnt_table.membersInCntTable[buddy2] += 1
                        namesInMonthList[group[2]-1].remove(buddy1)
                        namesInMonthList[group[2]-1].remove(buddy2)


    def pairTheRest(self, monthList, namesInMonthList, month):
        # 여기서는 모든 group 에 대해 group[0] = 0 이다. 재학생수 group[1] 만 0보다 큰 상태.
        for group in monthList:
            date = str(self.months[month]) + "." + str(group[2])
            if group[0] == 0 and group[1] == 0:
                continue

            while len(namesInMonthList[group[2]-1]) >= 2:
                buddy1 = namesInMonthList[group[2]-1].pop()
                buddy2 = namesInMonthList[group[2]-1].pop()

                if (self.cnt_table.membersInCntTable[buddy1] >= 2 or self.cnt_table.membersInCntTable[buddy2] >= 2):
                    continue

                if date not in self.buddies:
                    self.buddies[date] = [{buddy1: buddy2}]
                else:
                    self.buddies[date].append({buddy1: buddy2})
                self.cnt_table.membersInCntTable[buddy1] += 1
                self.cnt_table.membersInCntTable[buddy2] += 1

            if len(namesInMonthList[group[2]-1]) == 1:
                buddy = namesInMonthList[group[2]-1].pop()
                if (self.cnt_table.membersInCntTable[buddy] >= 2):
                    continue
                if date not in self.buddies:
                    self.buddies[date] = [{buddy: "null"}]
                else:
                    self.buddies[date].append({buddy: "null"})
                self.cnt_table.membersInCntTable[buddy] += 1


