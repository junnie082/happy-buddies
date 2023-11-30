class CountingTable:
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

    def addHisDays(self, name):
        self.membersInCntTable[name] += 1

    def resetCntTable(self):
        for name, _ in self.membersInCntTable.items():
            self.membersInCntTable[name] = 0

    def countTrainDays(self, buddies):
        for date, pairs in list(buddies.items()):
            for member in pairs:
                buddy1 = list(member.keys())[0]
                buddy2 = list(member.values())[0]
                print("pairs: " + str(pairs))
                if buddy1 != None: self.membersInCntTable[str(buddy1)] += 1
                if buddy2 != None: self.membersInCntTable[str(buddy2)] += 1