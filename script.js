const membersInCntTable = {
            // Initialize members in counting table
            "류창수": 0, "진성우": 0, "유도현": 0, "한종한": 0,
            "한영숙": 0, "김해슬": 0, "김우찬": 0, "박찬경": 0,
            "김선국": 0, "최태오": 0, "김성민": 0, "함민우": 0,
            "이용헌": 0, "이수연": 0, "서연우": 0, "안민혁": 0,
            "강지수": 0, "전효정": 0, "최승혜": 0, "박수겸": 0,
            "오효석": 0, "이의린": 0, "임채영": 0, "윤희정": 0,
            "김담우": 0, "김찬희": 0, "장승호": 0, "방재현": 0,
            "정기호": 0, "조시은": 0, "성예진": 0, "심혜원": 0,
            "이준": 0, "문성원": 0, "김형준": 0
};


const membersSemesters = {
            // Initialize members with their semester days
            "류창수": 10, "진성우": 10, "유도현": 10, "한종한": 10,
            "한영숙": 10, "김해슬": 10, "김우찬": 10, "박찬경": 10,
            "김선국": 8, "최태오": 8, "김성민": 8, "함민우": 8,
            "이용헌": 8, "이수연": 8, "서연우": 8, "안민혁": 8,
            "강지수": 6,  "전효정": 6,  "최승혜": 6,  "박수겸": 6,
            "오효석": 6,  "이의린": 4,  "임채영": 4, "윤희정": 4,
            "김담우": 4, "김찬희": 4, "장승호": 4, "방재현": 4,
            "정기호": 4, "조시은": 2,  "성예진": 2, "심혜원": 2,
            "이준": 2, "문성원": 2,  "김형준": 2
};

buddies = {

};

function getMemberNames() {
    return Object.keys(members);
}

function addHisDays(name) {
    membersInCntTable[name] += 1;
}

function resetCntTable() {
    for (let name in membersInCntTable) {
        membersInCntTable[name] = 0;
    }
}

function countTrainDays(buddies) {
    for (let date in buddies) {
        for (let pair of buddies[date]) {
            let buddy1 = Object.keys(pair)[0];
            let buddy2 = Object.values(pair)[0];

            if (buddy1 !== null) this.membersInCntTable[buddy1] += 1;
            if (buddy2 !== null) this.membersInCntTable[buddy2] += 1;
        }
    }
}

function pairUpBuddies(datesAndMembersList)  {
    let copyList = [...datesAndMembersList];
    let theRestOldStudents = [];

    while (copyList.length !== 0) {
        let datesAndMembers = copyList.pop();
        let date = datesAndMembers[0];
        let members = datesAndMembers[1];

        let newStudent = [];
        let oldStudent = [];


        for (let name of members) {
            if (name === '') continue;

            if (membersSemesters[name] <= 2) {
                newStudent.push(name);
            } else {
                oldStudent.push(name);
            }
        }

        for (let buddy1 of newStudent) {
            let buddy2 = null;
            if (oldStudent.length !== 0) buddy2 = oldStudent.pop();

            // Initializing buddies[date] if it doesn't exist
            if (!(date in buddies)) {
                buddies[date] = [];
            }

            // Pushing data into buddies[date]
            buddies[date].push({ [buddy1]: buddy2 });

            addHisDays(buddy1);
            if (buddy2 !== null) addHisDays(buddy2);
        }

        if (oldStudent.length !== 0) {
            theRestOldStudents.push([date, [...oldStudent]]);
        }
    }

    pairTheRest(theRestOldStudents);

    return buddies;
}

function pairTheRest(oldStudents) {
    while (oldStudents.length !== 0) {
        let datesAndMembers = oldStudents.pop();
        let date = datesAndMembers[0];
        let members = datesAndMembers[1];

        while (members.length >= 2) {
            let buddy1 = members.pop();
            let buddy2 = members.pop();

            if (membersInCntTable[buddy1] > 2 && membersInCntTable[buddy2] > 2) {
                continue;
            }

            // Pairing logic for buddies based on the counting table
            if (!(date in buddies)) {
                buddies[date] = [];
            }

            buddies[date].push({ [buddy1]: buddy2 });

            addHisDays(buddy1);
            addHisDays(buddy2);
        }

        if (members.length === 1) {
            let buddy = members.pop();

            if (membersInCntTable[buddy] <= 2) {
                if (!(date in buddies)) {
                    buddies[date] = [];
                }
                buddies[date].push({ [buddy]: null });

                addHisDays(buddy);
            }
        }
    }

    // Call this function to print membersInCntTable
    // printMembersInCntTable();

}

function printMembersInCntTable() {
    console.log('Members in Count Table:');
    for (const member in membersInCntTable) {
        console.log(`${member}: ${membersInCntTable[member]}`);
    }
}



// Perform actions using these classes
