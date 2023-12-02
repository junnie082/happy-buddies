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

let inputList = document.getElementById("inputList");
let datesAndMembersList = [];


// Function to create buttons for members of each semester
function createSemesterButtons() {
    const semesterButtonsContainer = document.getElementById('semesterButtons');

    // Loop through each semester
    for (let semester = 2; semester <= 10; semester += 2) {
        const semesterDiv = document.createElement('div');
        semesterDiv.classList.add('semester');

        const semesterHeading = document.createElement('h3');
        semesterHeading.textContent = `Semester ${semester}`;
        semesterDiv.appendChild(semesterHeading);

        const semesterMembersDiv = document.createElement('div');
        semesterMembersDiv.classList.add('semester-members');

        // Loop through members to find those belonging to this semester
        for (const member in membersSemesters) {
            if (membersSemesters[member] === semester) {
                const memberButton = document.createElement('button');
                memberButton.textContent = member;
                memberButton.id = "memberButton"
                memberButton.addEventListener('click', () => {
                    const selectedDate = document.getElementById('selectedDate').value;
                    if (selectedDate.trim() !== '') {
                        addMember(selectedDate, member);
                        datesAndMembersList.push([selectedDate, member]);
                        // Call functions to print and update the displayed list here
                        printDatesAndMembersList();
                        updateDisplayList();
                    } else {
                        alert('Please select a date.');
                    }
                });

                semesterMembersDiv.appendChild(memberButton);
            }
        }

        semesterDiv.appendChild(semesterMembersDiv);
        semesterButtonsContainer.appendChild(semesterDiv);
    }
}

// Call the function to create semester buttons
createSemesterButtons();




function updateDisplayList() {
    const inputList = document.getElementById('inputList');
    inputList.innerHTML = '';

    // Filter out entries with no members and sort by date
    datesAndMembersList
        .filter(([_, members]) => Array.isArray(members) && members.length > 0)
        .sort((a, b) => new Date(a[0]) - new Date(b[0]))
        .forEach(([date, members]) => {
            const listItem = document.createElement('li');
            listItem.classList.add('list-item');

            const dateText = document.createElement('span');
            dateText.textContent = `${date} `;
            dateText.classList.add('date-text');
            listItem.appendChild(dateText);

            if (Array.isArray(members)) {
                members.forEach(member => {
                    const memberText = document.createElement('span');
                    memberText.textContent = member;
                    memberText.classList.add('list-member');

                    const deleteButton = document.createElement('button');
                    deleteButton.textContent = 'Delete';
                    deleteButton.id = 'deleteBtn';
                    deleteButton.onclick = function () {
                        removeMemberFromDate(member, date);
                        updateDisplayList();
                    };

                    listItem.appendChild(memberText);
                    listItem.appendChild(deleteButton);
                    listItem.appendChild(document.createTextNode(' '));
                });
            } else {
                const memberText = document.createElement('span');
                memberText.textContent = members;
                memberText.classList.add('list-member');

                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Delete';
                deleteButton.id = 'deleteBtn'; // Assign ID to deleteButton
                deleteButton.onclick = function () {
                    removeMemberFromDate(members, date);
                    updateDisplayList();
                };

                listItem.appendChild(memberText);
                listItem.appendChild(deleteButton);
                listItem.appendChild(document.createTextNode(' '));
            }

            inputList.appendChild(listItem);
        });
}



function createMembersTable() {
    const membersTableDiv = document.getElementById('membersTable');
    membersTableDiv.innerHTML = ''; // Clear previous content

    const tableHeading = document.createElement('h2');
    tableHeading.textContent = 'Counted Training Days'; // Removed < > from the heading text
    membersTableDiv.appendChild(tableHeading);

    const membersList = document.createElement('ul');
    membersList.classList.add('members-list');

    let memberCount = 0; // Track member count in each row

    for (const member in membersInCntTable) {
        const participationCount = membersInCntTable[member];

        const memberItem = document.createElement('li');
        memberItem.textContent = `${member}: ${participationCount}`;

        // Apply appropriate class based on participation count
        if (participationCount === 3) {
            memberItem.classList.add('blue');
        } else if (participationCount === 1 || participationCount === 2) {
            memberItem.classList.add('yellow');
        } else {
            memberItem.classList.add('red');
        }

        membersList.appendChild(memberItem);
        memberCount++;
    }

    membersTableDiv.appendChild(membersList);
}


// Function to update member count table continuously
setInterval(createMembersTable, 500); // Update every 0.5 seconds

// Call the createMembersTable function initially to populate the table
createMembersTable();



function removeMemberFromDate(member, date) {
    datesAndMembersList = datesAndMembersList.map(([existingDate, members]) => {
        if (existingDate === date) {
            const updatedMembers = Array.isArray(members)
                ? members.filter(name => name !== member)
                : members; // If 'members' is not an array, retain the original value

            return [existingDate, updatedMembers];
        }
        return [existingDate, members];
    });

    updateDisplayList();
}



document.querySelectorAll('.member-button').forEach(button => {
    button.addEventListener('click', function () {
        document.querySelectorAll('.member-button').forEach(btn => {
            btn.classList.remove('selected');
        });

        button.classList.add('selected');
    });
});


function printDatesAndMembersList() {
    console.log('Dates and Members:');
    datesAndMembersList.forEach(([date, members]) => {
        console.log(`Date: ${date}`);
        console.log('Members:');
        if (Array.isArray(members)) {
            members.forEach(member => {
                console.log(member);
            });
        } else {
            console.log(members); // Display non-array members directly
        }
    });
}



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


function checkIfMembersExist(addMemberNames) {
    let membersList = addMemberNames.map(name => name.trim());

    // Get the valid member names from membersSemesters object
    const validMembers = Object.keys(membersSemesters);

    // Check if all entered member names exist in the valid members list
    return membersList.every(name => validMembers.includes(name));
}

function mergeBuddiesToList() {
    const existingMembers = datesAndMembersList.flatMap(([_, members]) => members);

    for (const date in buddies) {
        if (Object.prototype.hasOwnProperty.call(buddies, date)) {
            const buddyPairs = buddies[date];

            const members = [];
            buddyPairs.forEach(pair => {
                const keys = Object.keys(pair);
                const buddy1 = keys[0];
                const buddy2 = pair[keys[0]];

                if (existingMembers.includes(buddy1)) {
                    members.push(buddy1);
                }
                if (buddy2 && existingMembers.includes(buddy2)) {
                    members.push(buddy2);
                }
            });

            datesAndMembersList.push([date, members]);
        }
    }
}







// Perform actions using these classes