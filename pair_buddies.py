class PairBuddies:
    def __init__(self):
        # {날짜: [{버디1, 버디2}]}
        self.buddies = {}
        self.cnt_table = []
        self.months = []
        self.mem = {}

    def resetBuddies(self):
        self.buddies = {}


    def resetAllOfBuddies(self):
        self.cnt_table = []
        self.months = []
        self.mem = {}
    def setMembers(self, members):
        self.mem = members

    def setCntTable(self, cnt_table):
        self.cnt_table = cnt_table

    def getBuddies(self):
        return self.buddies

    def pairUpBuddies(self, datesAndMembersList):
        copyList = datesAndMembersList.copy()

        theRestOldStudents = []

        self.cnt_table.resetCntTable()

        while len(copyList) != 0:
            datesAndMembers = copyList.pop()
            date = datesAndMembers[0]
            members = datesAndMembers[1]

            newStudent = []
            oldStudent = []

            for name in members:
                if name == '': continue
                # 훈련 아직 세 번 이상 안갔다면.
                if self.cnt_table.membersInCntTable[name] <= 2:
                    # 신입생
                    if self.mem.members[name] <= 2:
                        newStudent.append(name)
                    # 재학생
                    else:
                        oldStudent.append(name)

            print("newStudetn: " + str(newStudent) + "oldStudent: " + str(oldStudent))
            # 신입생들을 먼저 재학생과 pairing 함.
            for buddy1 in newStudent:
                buddy2 = None
                if len(oldStudent) != 0: buddy2 = oldStudent.pop()

                if date not in self.buddies:
                    self.buddies[date] = [{buddy1: buddy2}]
                else:
                    self.buddies[date].append({buddy1: buddy2})

                self.cnt_table.addHisDays(buddy1)
                if buddy2 != None: self.cnt_table.addHisDays(buddy2)


            if len(oldStudent) != 0: theRestOldStudents.append([date, [student for student in oldStudent]])

        self.pairTheRest(theRestOldStudents)


    def pairTheRest(self, oldStudent):
        # 남은 동아리원들은 모두 재학생
        print("copyList: " + str(oldStudent))
        while len(oldStudent) != 0:

            datesAndMembers = oldStudent.pop()
            date = datesAndMembers[0]
            members = datesAndMembers[1]

            while len(members) >= 2:
                buddy1 = members.pop()
                buddy2 = members.pop()

                if date not in self.buddies:
                    self.buddies[date] = [{buddy1: buddy2}]

                else:
                    self.buddies[date].append({buddy1: buddy2})

                self.cnt_table.addHisDays(buddy1)
                self.cnt_table.addHisDays(buddy2)

            if len(members) == 1:
                buddy = members.pop()

                if date not in self.buddies:
                    self.buddies[date] = [{buddy: None}]
                else:
                    self.buddies[date].append({buddy: None})

                self.cnt_table.addHisDays(buddy)



