const { expect } = require('chai');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;
const fs = require('fs');

const html = fs.readFileSync('index.html', 'utf8');
const dom = new JSDOM(html);

global.window = dom.window;
global.document = dom.window.document;

const { yourFunctionToTest } = require('./main');

describe('Shopping List Functionality', () => {
  let newItemInput, newItemForm, itemsList, budgetInput, budgetForm, startShoppingButton;

  beforeEach(() => {
    newItemInput = document.createElement('input');
    newItemInput.id = 'new-item-input';

    newItemForm = document.createElement('form');
    newItemForm.id = 'new-item-form';
    newItemForm.appendChild(newItemInput);

    itemsList = document.createElement('div');
    itemsList.id = 'items';

    budgetInput = document.createElement('input');
    budgetInput.id = 'new-budget-input';

    budgetForm = document.createElement('form');
    budgetForm.id = 'budget-edit-form';
    budgetForm.appendChild(budgetInput);

    startShoppingButton = document.createElement('input');
    startShoppingButton.type = 'button';
    startShoppingButton.id = 'start-shopping-button';

    document.body.appendChild(newItemForm);
    document.body.appendChild(itemsList);
    document.body.appendChild(budgetForm);
    document.body.appendChild(startShoppingButton);
  });

  afterEach(() => {
    document.body.innerHTML = '';
  });

  it('should add a new item to the list', () => {
    // Simulate user input
    newItemInput.value = 'New Item';

    // Trigger form submission
    newItemForm.dispatchEvent(new Event('submit'));

    // Check if the item was added to the list
    const items = itemsList.getElementsByClassName('item');
    expect(items.length).to.equal(1);

    // Check if the item content is correct
    const itemText = items[0].getElementsByClassName('text')[0].value;
    expect(itemText).to.equal('New Item');
  });

  it('should edit an existing item', () => {
    // Add an item to the list
    newItemInput.value = 'Item to Edit';
    newItemForm.dispatchEvent(new Event('submit'));

    // Find the edit button and trigger a click
    const editButton = itemsList.querySelector('.edit');
    editButton.dispatchEvent(new Event('click'));

    // Check if the item text is editable
    const itemInput = itemsList.querySelector('.text');
    expect(itemInput.hasAttribute('readonly')).to.be.false;

    // Simulate editing the item
    itemInput.value = 'Edited Item';

    // Trigger form submission (save)
    newItemForm.dispatchEvent(new Event('submit'));

    // Check if the item text is updated
    const updatedItemText = itemsList.querySelector('.text').value;
    expect(updatedItemText).to.equal('Edited Item');
  });

  it('should delete an existing item', () => {
    // Add an item to the list
    newItemInput.value = 'Item to Delete';
    newItemForm.dispatchEvent(new Event('submit'));

    // Check if the item is in the list
    const itemsBeforeDelete = itemsList.getElementsByClassName('item');
    expect(itemsBeforeDelete.length).to.equal(1);

    // Find the delete button and trigger a click
    const deleteButton = itemsList.querySelector('.delete');
    deleteButton.dispatchEvent(new Event('click'));

    // Check if the item is removed from the list
    const itemsAfterDelete = itemsList.getElementsByClassName('item');
    expect(itemsAfterDelete.length).to.equal(0);
  });

  it('should update the budget', () => {
    // Simulate user input
    budgetInput.value = '150';

    // Trigger form submission
    budgetForm.dispatchEvent(new Event('submit'));

    // Check if the budget input value is updated
    const updatedBudgetValue = budgetInput.value;
    expect(updatedBudgetValue).to.equal('150');
  });

  it('should not update the budget if the input is not a number', () => {
    // Simulate invalid user input
    budgetInput.value = 'Not a Number';

    // Trigger form submission
    budgetForm.dispatchEvent(new Event('submit'));

    // Check if the budget input value remains unchanged
    const unchangedBudgetValue = budgetInput.value;
    expect(unchangedBudgetValue).to.equal('');

    // Check if a warning message is displayed
    const warningDiv = document.getElementById('invalid-budget-warning');
    expect(warningDiv.innerHTML).to.equal('Budget must be a number');
  });

  it('should start shopping and open a new page', () => {
    // Spy on the window.open method
    const openSpy = sinon.spy(window, 'open');

    // Trigger click on the start shopping button
    startShoppingButton.dispatchEvent(new Event('click'));

    // Restore the original window.open method
    openSpy.restore();
  });
});
