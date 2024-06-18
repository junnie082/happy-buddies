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

    datesAndMembersList.sort((a, b) => new Date(a[0]) - new Date(b[0]));


    // Track printed dates
    const printedDates = new Set();
    const resultHeading = document.createElement('h2');
    resultHeading.textContent = 'Result';
    resultDiv.appendChild(resultHeading);
    // Loop through the datesAndMembersList and display the paired results
    datesAndMembersList.forEach(([date, members]) => {
        if (!printedDates.has(date)) {
            const buddiesForDate = buddies[date] || [];
            // Check if there are any buddy pairs for this date
            if (buddiesForDate.length > 0) {
                const dateHeading = document.createElement('h3');
                dateHeading.id = 'dateHeading';
                dateHeading.textContent = `▶ ${date}`;
                resultDiv.appendChild(dateHeading);

                const pairContainer = document.createElement('div');
                pairContainer.classList.add('pair-container');
                pairContainer.style.display = 'flex'; // Set to display items in a row
                pairContainer.style.gap = '20px'; // Add spacing between items

                buddiesForDate.forEach(pair => {
                    const buddyName = Object.keys(pair)[0];
                    const buddyValue = pair[buddyName] || 'None';

                    let buddyValueSemester = 'X';
                    if (buddyValue !== 'None') {
                        buddyValueSemester = membersSemesters[buddyValue];
                    }

                    const pairText = document.createElement('p');
                    pairText.textContent = `${buddyName}(${membersSemesters[buddyName]}) - ${buddyValue}(${buddyValueSemester})`;
                    pairText.style.border = '2px solid #3498db'; // Thicker border
                    pairText.style.borderRadius = '10px'; // Rounded border
                    pairText.style.padding = '10px'; // Add padding to create space between text and border

                    pairContainer.appendChild(pairText);
                });

                resultDiv.appendChild(pairContainer);
                printedDates.add(date); // Add the printed date to the set
            }
        }
    });

    // cntMembers();
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
    resetMemberButtons();
}

// Function to reset member buttons to white
// Function to reset all buttons to white
function resetAllButtons() {
    const buttons = document.querySelectorAll('.semester-members button');
    buttons.forEach(button => {
        button.style.backgroundColor = '';
        button.style.color = '';
    });
}

// Event listener for the resetBtn
document.getElementById('resetBtn').addEventListener('click', () => {
    resetAllButtons(); // Call the function to reset all buttons
});



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

