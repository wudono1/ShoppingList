window.addEventListener('load', () => {
    const form = document.querySelector('#new-item-form');
    const input = document.querySelector('#new-item-input');
    const list_el = document.querySelector('#items');

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const item = input.value;

        if (!item) {
            alert("Please fill out the item");
        } else {
            console.log("Success");
            return;
        }

        const item_el = document.createElement("div");
        item_el.classList.add("item");

        const item_content_el = document.createElement("div");
        item_content_el.classList.add("content")
        item_content_el.innerText = item;

        item_el.appendChild(item_content_el);

        list_el.appendChild(item_el);

    })
})