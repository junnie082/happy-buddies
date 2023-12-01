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
let dateMemberMap = new Map(); // Map to store date-member pairs
var datesAndMembersList = [];

// Function to add a member to the list


function done() {
    const container = document.querySelector('.container');
    const resultDiv = document.getElementById('pairedBuddies');
    const doneButton = document.getElementById('doneBtn');

    // Change the appearance of the Done button
    doneButton.disabled = true;
    doneButton.style.backgroundColor = 'darkgray'; // Change color to dark gray



    // Clear the previous results
    resultDiv.innerHTML = '';

    // Merge buddies to datesAndMembersList
    mergeBuddiesToList();

    // Pair buddies based on the updated datesAndMembersList
    pairUpBuddies(datesAndMembersList);
    printDatesAndMembersList();

    // Loop through the datesAndMembersList and display the paired results
    datesAndMembersList.forEach(([date, members]) => {
        const buddiesForDate = buddies[date] || [];
        // Check if there are any buddy pairs for this date
        if (buddiesForDate.length > 0) {
            const dateHeading = document.createElement('h3');
            dateHeading.id = "dateHeading";
            dateHeading.textContent = `▶  ${date}`;
            resultDiv.appendChild(dateHeading);
            const buddiesList = document.createElement('ul');

            members.forEach(member => {
                const buddyPair = buddiesForDate.find(pair => Object.keys(pair)[0] === member);
                if (buddyPair) {
                    const buddyName = Object.keys(buddyPair)[0];
                    const buddyValue = buddyPair[buddyName] || 'None';
                    const buddyItem = document.createElement('li');
                    buddyItem.id = "buddyItem";

                    let buddyValueSemester = 'X';
                    if (buddyValue !== 'None') {
                        buddyValueSemester = membersSemesters[buddyValue];
                    }
                    buddyItem.textContent = `${buddyName}(${membersSemesters[buddyName]}) - ${buddyValue}(${buddyValueSemester})`;
                    buddiesList.appendChild(buddyItem);
                }
            });

            resultDiv.appendChild(buddiesList);
        }
    });


    // Append the resultDiv to the container
    container.appendChild(resultDiv);

    buddies = {};
}


// Assume existing code for membersInCntTable

// Function to create members table with colored backgrounds
// Function to create members table with colored backgrounds
// Function to create members table with colored backgrounds
// Function to create members table with colored backgrounds
function createMembersTable() {
    const membersTableDiv = document.getElementById('membersTable');
    membersTableDiv.innerHTML = ''; // Clear previous content

    const tableHeading = document.createElement('h2');
    tableHeading.textContent = '<Counted Training Days>';
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
    datesAndMembersList = datesAndMembersList.map(([listDate, listMembers]) => {
        if (listDate === date) {
            return [listDate, listMembers.filter(m => m !== member)];
        }
        return [listDate, listMembers];
    });
}

function reset() {
    const doneButton = document.getElementById('doneBtn');
    doneButton.disabled = false;
    doneButton.style.backgroundColor = '';
    resetCntTable();
    datesAndMembersList = [];
    buddies = {};
    inputList.innerHTML = '';
    pairedBuddies.innerHTML = ''; // Clears the paired results
}

function printDatesAndMembersList() {
        console.log('Dates and Members:');
        datesAndMembersList.forEach(([date, members]) => {
        console.log(`Date: ${date}`);
        console.log(`Members: ${members.join(', ')}`);
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

function addMember() {

    const doneButton = document.getElementById('doneBtn');
    doneButton.disabled = false;
    doneButton.style.backgroundColor = '';

    let selectedDate = document.getElementById("selectedDate").value;
    let addMemberNames = document.getElementById("memberNames").value;

    resetCntTable();

    if (selectedDate.trim() === "" || addMemberNames.trim() === "") {
        alert("Please select a date and enter member names.");
        return;
    }

    let membersToAdd = addMemberNames.split(',').map(name => name.trim());

    // Check if all entered member names exist in the membersSemesters object
    if (!checkIfMembersExist(addMemberNames)) {
        alert("Please enter valid member names.");
        return;
    }

    // Check if the member already exists for the selected date
    const existingMember = datesAndMembersList.find(([date]) => date === selectedDate);

    if (existingMember) {
        const [, existingMembers] = existingMember;

        for (let name of membersToAdd) {
            if (!existingMembers.includes(name)) {
                existingMembers.push(name);
            }
        }
    } else {
        datesAndMembersList.push([selectedDate, membersToAdd]);
    }

    // Update the displayed list
    updateDisplayList();
}

function checkIfMembersExist(addMemberNames) {
    let membersList = addMemberNames.split(",").map(name => name.trim());

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


function updateDisplayList() {
    // Clear the displayed list
    document.getElementById("inputList").innerHTML = "";

    // Sort dates with no members
    datesAndMembersList = datesAndMembersList.filter(([date, members]) => members.length > 0);

    // Sort dates before displaying
    datesAndMembersList.sort((a, b) => new Date(a[0]) - new Date(b[0]));

    // Populate the displayed list based on sorted datesAndMembersList
    datesAndMembersList.forEach(([date, members]) => {
        let listItem = document.createElement("li");
        listItem.classList.add('list-item'); // Add the class to the list item

        // Create the date element
        let dateText = document.createElement("span");
        dateText.textContent = date + " ";
        dateText.classList.add('date-text'); // Add this line to apply the class to the date element

        dateText.textContent = date + " ";
        listItem.appendChild(dateText);

        members.forEach(member => {
            let memberText = document.createElement("span");
            memberText.textContent = member;
            memberText.classList.add('list-member');

            let deleteButton = document.createElement("button");
            deleteButton.id = "deleteBtn";
            deleteButton.textContent = "Delete";
            deleteButton.onclick = function () {

                removeMemberFromDate(member, date);
                updateDisplayList(); // Update the displayed list after deletion
            };

            listItem.appendChild(memberText);
            listItem.appendChild(deleteButton);
            listItem.appendChild(document.createTextNode(' '));
        });

        document.getElementById("inputList").appendChild(listItem);
    });
}

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

}




// Perform actions using these classes
