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
    //printDatesAndMembersList();

    // Track printed dates
    const printedDates = new Set();

    // Loop through the datesAndMembersList and display the paired results
    datesAndMembersList.forEach(([date, members]) => {
        if (!printedDates.has(date)) {
            const buddiesForDate = buddies[date] || [];
            // Check if there are any buddy pairs for this date
            if (buddiesForDate.length > 0) {
                const dateHeading = document.createElement('h3');
                dateHeading.id = "dateHeading";
                dateHeading.textContent = `▶  ${date}`;
                resultDiv.appendChild(dateHeading);
                const buddiesList = document.createElement('ul');

                if (Array.isArray(members)) { // Check if members is an array
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
                } else {
                    console.error('Members is not an array:', members);
                }

                resultDiv.appendChild(buddiesList);
                printedDates.add(date); // Add the printed date to the set
            }
        }
    });

    // Append the resultDiv to the container
    container.appendChild(resultDiv);
    buddies = {};
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


function addMember(date, name) {
    const doneButton = document.getElementById('doneBtn');
    doneButton.disabled = false;
    doneButton.style.backgroundColor = '';

    let selectedDate = date.trim();
    let addMemberName = name.trim();

    resetCntTable();

    if (selectedDate === "" || addMemberName === "") {
        alert("Please select a date and enter member names.");
        return;
    }

    // Check if all entered member names exist in the membersSemesters object
    if (!checkIfMembersExist([addMemberName])) {
        alert("Please enter valid member names.");
        return;
    }

    // Find if the selected date already exists in datesAndMembersList
    const existingDateIndex = datesAndMembersList.findIndex(([date]) => date === selectedDate);

    if (existingDateIndex !== -1) {
        const [, existingMembers] = datesAndMembersList[existingDateIndex];

        // Check if the member already exists for the selected date
        if (!existingMembers.includes(addMemberName)) {
            existingMembers.push(addMemberName);
        } else {
            return;
        }
    } else {
        // Add a new entry for the selected date with the member
        datesAndMembersList.push([selectedDate, [addMemberName]]);
    }

    // Update the displayed list
    updateDisplayList();
}

