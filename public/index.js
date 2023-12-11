window.addEventListener('load', () => {
    //loadItems(); //loads any items previously saved in shopping list tab

    //item form
    const item_form = document.querySelector('#new-item-form');
    const item_input = document.querySelector('#new-item-input');
    const list_el = document.querySelector('#items');

    const budget_form = document.querySelector('#budget-edit-form');
    const budget_input = document.querySelector('#new-budget-input');

    const lastValidBudget = '';

    item_form.addEventListener('submit', (e) => {    //logic for pressing submit button
        e.preventDefault();

        const item = item_input.value;

        if (item) {
            const item_el = document.createElement("div"); //creating item element
            item_el.classList.add("item");
    
            const item_content_el = document.createElement("div"); //creating item content (item text)
            item_content_el.classList.add("content")
    
            //add item content to item_el element
            item_el.appendChild(item_content_el);
    
            const item_input_el = document.createElement("input");
            item_input_el.classList.add("text");
            item_input_el.type = "text";
            item_input_el.value = item;
            item_input_el.setAttribute("readonly", "readonly");
    
            item_content_el.appendChild(item_input_el);

            //Priority dropdown element

            //adding label to dropdown
            const label_el = document.createElement("label");
            label_el.textContent = "Select priority level:";

            const dropdown_el = document.createElement("select");
            dropdown_el.classList.add("dropdown");

            //3 options: high, medium, or low priority; default is high priority
            const option1 = document.createElement("option");
            option1.value = "high";
            option1.text = "High";

            const option2 = document.createElement("option");
            option2.value = "med";
            option2.text = "Medium";

            const option3 = document.createElement("option");
            option3.value = "low";
            option3.text = "Low";

            dropdown_el.appendChild(option1);
            dropdown_el.appendChild(option2);
            dropdown_el.appendChild(option3);

            //Adding dropdown to item_el
            item_el.appendChild(label_el);
            item_el.appendChild(dropdown_el);
    
            //making actions class for edit and delete buttons
            const item_actions_el = document.createElement("div");
            item_actions_el.classList.add("actions");
    
            //edit button
            const item_edit_el = document.createElement("button");
            item_edit_el.classList.add("edit");
            item_edit_el.innerHTML = "Edit";
    
            //delete button
            const item_delete_el = document.createElement("button");
            item_delete_el.classList.add("delete");
            item_delete_el.innerHTML = "Delete";
    
            //adding buttons to actions
            item_actions_el.appendChild(item_edit_el);
            item_actions_el.appendChild(item_delete_el);
    
            //appending actions to item_el
            item_el.appendChild(item_actions_el);
    
            //appending item_el element to list_el
            list_el.appendChild(item_el);
    
            //set input value to blank after "submit" button clicked
            item_input.value = "";
            
    
            //edit button logic
            item_edit_el.addEventListener('click', () => {
                if (item_edit_el.innerText.toLowerCase() == "edit") {
                    //removing readonly attr from item text
                    item_input_el.removeAttribute("readonly");
                    item_input_el.focus();
    
                    //change edit button to say "save"
                    item_edit_el.innerText = "Save";
                } else {
                    item_input_el.setAttribute("readonly", "readonly");
                    item_edit_el.innerText = "Edit";
                }
            })
    
            //remove button logic
            item_delete_el.addEventListener('click', () => {
                list_el.removeChild(item_el);
            })
        }

        //saveItems();

    })

    budget_form.addEventListener('submit', (e) => {
        e.preventDefault();

        const newBudget = budget_input.value;
        const warningDiv = document.getElementById('invalid-budget-warning');

        if (newBudget && !isNaN(newBudget)) {
            budget_input.value = newBudget;
            warningDiv.innerHTML = ''; // Clear the warning message
        } else {
            budget_input.value = ''; // Clear the input value
            warningDiv.innerHTML = 'Budget must be a number';
        }
    });
    
    const startShoppingButton = document.getElementById('start-shopping-button');
    //open new page when start shopping button is clicked
    startShoppingButton.addEventListener('click', async () => {
        // Collect data from the HTML elements
        const items = [];
        const itemList = document.querySelectorAll('.item');

        itemList.forEach((itemElement) => {
            const text = itemElement.querySelector('.text').value;
            const priority = itemElement.querySelector('.dropdown').value;

            items.push({ text, priority });
        });

        const budget = document.getElementById('new-budget-input').value;

        // Create a JSON object with the collected data
        const shoppingData = {
            items,
            budget,
        };

        // Convert the JSON object to a JSON string
        const jsonData = JSON.stringify(shoppingData, null, 2);

        const shoppingResponse = await fetch('/save-json', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(shoppingData),
        });

        document.getElementById('loading-message').innerText = 'Calculating the best shopping list...';

        // Send the data to the new endpoint that runs the Python script
        const startShoppingResponse = await fetch('/start-shopping', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(shoppingData),
        });

        document.getElementById('loading-message').innerText = '';
        
        if (startShoppingResponse.ok) {
            console.log("response loaded")
            const startShoppingResult = await startShoppingResponse.json();
            
            if (startShoppingResult.success) {
              console.log('File saved successfully:', startShoppingResult.filename);
              localStorage.setItem('finalShoppingList', JSON.stringify(startShoppingResult.results));
              window.location.href = '/result.html';
            } else {
              console.error('Error running shopping list algo.');
            }
        }
    });
});


function saveItems() { //save items for when page is loaded back
    const items = [];
    const itemList = document.querySelectorAll('.item');
    itemList.forEach((itemElement) => {
        const text = itemElement.querySelector('.text').value;
        const priority = itemElement.querySelector('.dropdown').value;
        items.push({ text, priority });
    });
    localStorage.setItem('items', JSON.stringify(items));
}

function loadItems() {
    const savedItems = JSON.parse(localStorage.getItem('items')) || [];
    savedItems.forEach(itemData => {
        addItemToPage(itemData.text, itemData.priority);
    });
    
    // Load and set the budget
    const savedBudget = localStorage.getItem('budget');
    if (savedBudget) {
        document.getElementById('new-budget-input').value = savedBudget;
    }
}

function addItemToPage(text, priority) {
    const list_el = document.querySelector('#items');
    
    // Create item element
    const item_el = document.createElement("div");
    item_el.classList.add("item");

    // Create item content (item text)
    const item_content_el = document.createElement("div");
    item_content_el.classList.add("content");

    // Add item content to item_el element
    item_el.appendChild(item_content_el);

    // Input for item text
    const item_input_el = document.createElement("input");
    item_input_el.classList.add("text");
    item_input_el.type = "text";
    item_input_el.value = text;
    item_input_el.setAttribute("readonly", "readonly");

    item_content_el.appendChild(item_input_el);

    // Label for priority dropdown
    const label_el = document.createElement("label");
    label_el.textContent = "Select priority level:";

    // Priority dropdown element
    const dropdown_el = document.createElement("select");
    dropdown_el.classList.add("dropdown");

    // Options: high, medium, or low priority
    const optionHigh = document.createElement("option");
    optionHigh.value = "high";
    optionHigh.text = "High";
    dropdown_el.appendChild(optionHigh);

    const optionMedium = document.createElement("option");
    optionMedium.value = "med";
    optionMedium.text = "Medium";
    dropdown_el.appendChild(optionMedium);

    const optionLow = document.createElement("option");
    optionLow.value = "low";
    optionLow.text = "Low";
    dropdown_el.appendChild(optionLow);

    // Set the dropdown to the saved priority
    dropdown_el.value = priority;

    // Adding label and dropdown to item_el
    item_el.appendChild(label_el);
    item_el.appendChild(dropdown_el);

    // Actions div for edit and delete buttons
    const item_actions_el = document.createElement("div");
    item_actions_el.classList.add("actions");

    // Edit button
    const item_edit_el = document.createElement("button");
    item_edit_el.classList.add("edit");
    item_edit_el.innerText = "Edit";
    item_actions_el.appendChild(item_edit_el);

    // Delete button
    const item_delete_el = document.createElement("button");
    item_delete_el.classList.add("delete");
    item_delete_el.innerText = "Delete";
    item_actions_el.appendChild(item_delete_el);

    // Append actions to item_el
    item_el.appendChild(item_actions_el);

    // Append item_el to the list on the page
    list_el.appendChild(item_el);

    // Logic for edit button
    item_edit_el.addEventListener('click', () => {
        if (item_edit_el.innerText.toLowerCase() === "edit") {
            item_input_el.removeAttribute("readonly");
            item_input_el.focus();
            item_edit_el.innerText = "Save";
        } else {
            item_input_el.setAttribute("readonly", "readonly");
            item_edit_el.innerText = "Edit";
        }
    });

    // Logic for delete button
    item_delete_el.addEventListener('click', () => {
        list_el.removeChild(item_el);
    });
}
