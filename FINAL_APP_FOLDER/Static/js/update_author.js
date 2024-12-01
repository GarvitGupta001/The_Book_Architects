const searchInput = document.getElementById('book_title');
const preface = document.getElementById('book_preface');
const publisher = document.getElementById('publisher_name');
const vendor = document.getElementById('vendor_name');
const bookSuggestionList = document.getElementById('bookSuggestionList');

searchInput.addEventListener('input', async (e) => {
    const title = e.target.value;
    if (title.length > 2) {
        try {
            const response = await fetch(`/book_search?search=${encodeURIComponent(title)}`);
            var suggestions = await response.json();
            bookSuggestionList.innerHTML = '';
            suggestions.forEach(suggestion => {
                const li = document.createElement('li');
                li.textContent = suggestion.title;
                li.addEventListener('click', () => {
                    searchInput.value = suggestion.title;
                    preface.value = suggestion.preface;
                    publisher.value = suggestion.publisher;
                    vendor.value = suggestion.vendor;
                    shelf.value = suggestion.shelf_id;
                    price.value = suggestion.price;
                    availability.value = suggestion.availability;
                    dop.value = suggestion.date_of_publishing;
                    dos.value = suggestion.shelf_date;
                    dob.value = suggestion.bought_on;
                    bookSuggestionList.innerHTML = '';
                });
                li.classList.add("suggestion  ")
                bookSuggestionList.appendChild(li);
            });
        } catch (error) {
            console.error('Error fetching suggestions:', error);
            suggestions = [];
        }
    } else {
        bookSuggestionList.innerHTML = '';
    }
});