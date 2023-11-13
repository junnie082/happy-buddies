class Members:
    def __init__(self):
        # 멤버이름 : [활동학기수, 가능날짜]
        self.members = {
            "류창수": [10, []], "진성우": [10, []], "유도현": [10, []], "한종한": [10, []],
            "한영숙": [10, []], "김해슬": [10, []], "김우찬": [10, []], "박찬경": [10, []],
            "김선국": [8, []], "최태오": [8, []], "김성민": [8, []], "함민우": [8, []],
            "이용헌": [8, []], "이수연": [8, []], "서연우": [8, []], "안민혁": [8, []],
            "강지수": [6, []], "전효정": [6, []], "최승혜": [6, []], "박수겸": [6, []],
            "오효석": [6, []], "이의린": [4, []], "임채영": [4, []], "윤희정": [4, []],
            "김담우": [4, []], "김찬희": [4, []], "장승호": [4, []], "방재현": [4, []],
            "정기호": [4, []], "조시은": [2, []], "성예진": [2, []], "심혜원": [2, []],
            "이준": [2, []], "문성원": [2, []], "김형준": [2, []]
        }

    def editName(self, original_name, changed_name):
        self.members[original_name] = changed_name

    def editSemester(self, name, changed_semester):
        self.members[name][0] = changed_semester

    def editDates(self, name, possibleDates):
        self.members[name][1] = possibleDates

    def addOneSemester(self):
        for name, lists in self.members.items():
            self.members[name][0] += 1
    def addMember(self, name, semester, dates):
        self.members.append({self.name: [self.semester, []]})

    def addPossibleDateInMember(self, name, date):
        self.members[name][1].append(date)