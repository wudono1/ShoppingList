window.addEventListener('load', () => {

    //item form
    const item_form = document.querySelector('#new-item-form');
    const item_input = document.querySelector('#new-item-input');
    const list_el = document.querySelector('#items');

    const budget_form = document.querySelector('#budget-edit-form');
    const budget_input = document.querySelector('#new-budget-input');

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
        e.preventDefault();

        const newBudget = budget_input.value;
        if (newBudget && !(isNaN(newBudget))) {
            budget_input.value = newBudget;
            var div = document.getElementById(elementID);
            div.innerHTML = "";
        } else {
            var div = document.getElementById('invalid-budget-warning');
            alert(budget_input.value);
            div.innerHTML += 'Budget must be a number';
            
        }
        
    })
})