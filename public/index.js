window.addEventListener('load', () => {

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

    })

    budget_form.addEventListener('submit', (e) => {
        //logic for submitting a new budget
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
    //starts the shopping algorithm in listAlgo.py when start-shopping-button is clicked
    startShoppingButton.addEventListener('click', async () => {
        const resultsContainer = document.getElementById('results-container');
        resultsContainer.innerHTML = '';

        // Getting user input data from HTML
        const items = [];
        const itemList = document.querySelectorAll('.item');

        itemList.forEach((itemElement) => {
            const text = itemElement.querySelector('.text').value;
            const priority = itemElement.querySelector('.dropdown').value;

            items.push({ text, priority });
        });

        const budget = document.getElementById('new-budget-input').value;

        // Creating a JSON object with the collected data
        const shoppingData = {
            items,
            budget,
        };

        // Convert the JSON object to a JSON string
        const jsonData = JSON.stringify(shoppingData, null, 2);

        //turns user input into json File for listAlgo.py to take as input
        const shoppingResponse = await fetch('/save-json', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(shoppingData),
        });

        //displays loading message while final shopping list is being calculated
        document.getElementById('loading-message').innerText = 'Finding your optimal shopping list...';

        // Send the data to backend and triggers listAlgo to start searching online
        const startShoppingResponse = await fetch('/start-shopping', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(shoppingData),
        });


        
        if (startShoppingResponse.ok) {
            //checks if startShoppingResponse is valid response to prevent asynchronization issues

            //deletes loading message when startShoppingResponse loads valid shopping list
            document.getElementById('loading-message').innerText = '';
            console.log("response loaded")
            const startShoppingResult = await startShoppingResponse.json();
            
            //checks if valid response, else loads error
            if (startShoppingResult.success) {
              console.log('File saved successfully:', startShoppingResult.filename);

              //displaying items on webpage
              localStorage.setItem('finalShoppingList', JSON.stringify(startShoppingResult.results));
              displayResults(startShoppingResult.results);
            } else {
              console.error('Error running shopping list algo.');
            }
        }
    });
});


function displayResults(results) {
    // Getting results section
    const resultsContainer = document.getElementById('results-container');

    // Clear previous search results
    resultsContainer.innerHTML = '';

    // Create correctly formatted items for each result
    results.forEach(result => {

        if (result.keyword === "remainingUserInputBudget") {
            // checks if result is the remaining budget result and displays it on the webpage

            const budgetEl = document.createElement('div');
            budgetEl.innerHTML = `<strong>Budget remaining: $</strong>${result.price}`;

            resultsContainer.appendChild(budgetEl); // Adding budget info to container
        } else {
            //If result item is not budget, create a regular item result div for it

            const resultEl = document.createElement('div');
            resultEl.classList.add('result-item');

            // Adds item keyword, which is the item that the user inputted into the webpage
            const keywordSpan = document.createElement('span');
            keywordSpan.classList.add('keyword');
            keywordSpan.textContent = result.keyword;
            resultEl.appendChild(keywordSpan);

            // Adds item priority, which was user-inputted as well
            const prioritySpan = document.createElement('span');
            prioritySpan.classList.add('priority');
            prioritySpan.textContent = `Priority: ${result.priority}`;
            resultEl.appendChild(prioritySpan);

            // Adds price of item as found on the online listing
            const priceSpan = document.createElement('span');
            priceSpan.classList.add('price');
            priceSpan.textContent = `Price: $${result.price}`;
            resultEl.appendChild(priceSpan);

            // Link to online item listing
            const buyLink = document.createElement('span');
            buyLink.classList.add('buy-link');
            buyLink.innerHTML = `<a href="${result.link}" target="_blank">Link here</a>`;
            resultEl.appendChild(buyLink);

            // Append the item result div to correct section
            resultsContainer.appendChild(resultEl);
        }

    });
}
