function pairUpBuddies(datesAndMembersList)  {
    let copyList = [...datesAndMembersList];
    let theRestOldStudents = [];

    // Filter out dates with no members
    copyList = copyList.filter(([date, members]) => members.length > 0);

    // Sort datesAndMembersList by the number of members in descending order
    copyList.sort((a, b) => b[1].length - a[1].length);


    while (copyList.length !== 0) {
        let datesAndMembers = copyList.pop();
        let date = datesAndMembers[0];
        let members = datesAndMembers[1];

        // console.log("members: " + members);

        let newStudent = [];
        let oldStudent = [];

        for (let name of members) {
            if (name === '') continue;

            if (membersInCntTable[name] <= 2) {
                if (membersSemesters[name] <= 2) {
                    newStudent.push(name);
                } else {
                    oldStudent.push(name);
                }
            }

        }

        for (let buddy1 of newStudent) {
            let buddy2 = null;
            if (oldStudent.length !== 0) buddy2 = oldStudent.pop();

            // Initializing buddies[date] if it doesn't exist
            if (!(date in buddies)) {
                buddies[date] = [];
            }

            if (membersInCntTable[buddy1] <= 2 && membersInCntTable[buddy2] <= 2)
                buddies[date].push({ [buddy1]: buddy2 });
            else if (membersInCntTable[buddy1] <= 2 && membersInCntTable[buddy2] === null)
                buddies[date].push({ [buddy1]: null})

            addHisDays(buddy1);
            if (buddy2 !== null) addHisDays(buddy2);
        }


        if (oldStudent.length !== 0) {
            theRestOldStudents.push([date, [...oldStudent]]);
        }

        pairTheRest(theRestOldStudents);
    }

}

function pairTheRest(oldStudents) {

    oldStudents.reverse();

    while (oldStudents.length !== 0) {

        let datesAndMembers = oldStudents.pop();
        let date = datesAndMembers[0];
        let members = datesAndMembers[1];

        while (members.length >= 2) {
            let buddy1 = members.shift();
            let buddy2 = members.pop();

            if (membersInCntTable[buddy1] > 2 && membersInCntTable[buddy2] > 2) {
                continue;
            }

            if (!(date in buddies)) {
                buddies[date] = [];
            }

            if (membersInCntTable[buddy1] > 2) {
                buddies[date].push({[buddy2]: null});
                addHisDays(buddy1);
                continue;
            }

            if (membersInCntTable[buddy2] > 2) {
                buddies[date].push({[buddy1]: null});
                addHisDays(buddy2);
                continue;
            }

            if (membersInCntTable[buddy1] <= 2 && membersInCntTable[buddy2] <= 2) {
                buddies[date].push({ [buddy1]: buddy2 });
                addHisDays(buddy1);
                addHisDays(buddy2);
            }

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

}
