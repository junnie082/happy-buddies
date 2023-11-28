from dates import Dates
import pair_buddies

date = Dates()

class CountingTable:
    # firstMonth, secondMonth: [신입생수, 재학생수, 날짜]
    def __init__(self):
        self.membersInCntTable = {
            "류창수": 0, "진성우": 0, "유도현": 0, "한종한": 0,
            "한영숙": 0, "김해슬": 0, "김우찬": 0, "박찬경": 0,
            "김선국": 0, "최태오": 0, "김성민": 0, "함민우": 0,
            "이용헌": 0, "이수연": 0, "서연우": 0, "안민혁": 0,
            "강지수": 0, "전효정": 0, "최승혜": 0, "박수겸": 0,
            "오효석": 0, "이의린": 0, "임채영": 0, "윤희정": 0,
            "김담우": 0, "김찬희": 0, "장승호": 0, "방재현": 0,
            "정기호": 0, "조시은": 0, "성예진": 0, "심혜원": 0,
            "이준": 0, "문성원": 0, "김형준": 0
        }

        self.firstMonth = []
        self.secondMonth = []

    def sortMonthList(self):
        self.firstMonth.sort(reverse=True)
        self.secondMonth.sort(reverse=True)

    def initMonths(self, months):
        self.firstMonth = [[0, 0, i + 1] for i in range(date.calculate_days(months[0]))]
        if (len(months) != 1):
            self.secondMonth = [[0, 0, i + 1] for i in range(date.calculate_days(months[1]))]

    def resetCntTable(self):
        self.firstMonth = []
        self.secondMonth = []
        for name in self.membersInCntTable:
            self.membersInCntTable[name] = 0

    def resetCntTable(self):
        for name, _ in self.membersInCntTable.items():
            self.membersInCntTable[name] = 0
    def countTrainingDates(self, pair_buddies):
        print("pair_buddis.buddies: " + str(pair_buddies.buddies) + "type: " + str(type(pair_buddies.buddies)))

        for dates, pairs in pair_buddies.buddies.items():
            print("date: " + str(dates) + "pairs: " + str(pairs))
            for pair in pairs:
                buddy1 = list(pair.keys())[0]
                buddy2 = list(pair.values())[0]
                if buddy1 != None: self.membersInCntTable[buddy1] += 1
                if buddy2 != None: self.membersInCntTable[buddy2] += 1

            # for buddy1, buddy2 in pairs:
            #     if buddy1 != None: self.membersInCntTable[buddy1] += 1
            #     if buddy2 != None: self.membersInCntTable[buddy2] += 1