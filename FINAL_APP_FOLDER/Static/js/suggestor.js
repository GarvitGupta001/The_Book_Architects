const searchBook = document.getElementById('book_title');
const searchAuthor = document.getElementById('author_name');
const searchPublisher = document.getElementById('publisher_name');
const searchVendor = document.getElementById('vendor_name');
const searchMember = document.getElementById('member_name');
const searchEmployee = document.getElementById('employee_name');
const bookSuggestionList = document.getElementById('bookSuggestionList');
const authorSuggestionList = document.getElementById('authorSuggestionList');
const publisherSuggestionList = document.getElementById('publisherSuggestionList');
const vendorSuggestionList = document.getElementById('vendorSuggestionList');
const memberSuggestionList = document.getElementById('memberSuggestionList');
const employeeSuggestionList = document.getElementById('employeeSuggestionList');

if (searchBook) {
    searchBook.addEventListener('input', async (e) => {
        const title = e.target.value;
        if (title.length > 2) {
            try {
                response = await fetch(`/book_search?search=${encodeURIComponent(title)}`);
                var suggestions = await response.json()
                bookSuggestionList.innerHTML = '';
                suggestions.forEach(suggestion => {
                    const li = document.createElement('li');
                    li.innerHTML = suggestion.title;
                    li.classList.add('suggestion');
                    bookSuggestionList.appendChild(li);
                });
            } catch (error) {
                console.error('Error: ', error);
                suggestions = [];
            }
        } else {
            bookSuggestionList.innerHTML = '';
        }
    });
}

if (searchAuthor) {
    searchAuthor.addEventListener('input', async (e) => {
        const author = e.target.value;
        if (author.length > 2) {
            try {
                response = await fetch(`/author_search?search=${encodeURIComponent(author)}`);
                if (!response.ok) {
                    throw new error("fetching error");
                } else {
                    var suggestions = await response.json();
                    authorSuggestionList.innerHTML = '';
                    suggestions.forEach(suggestion => {
                        const li = document.createElement('li');
                        li.innerHTML = suggestion.name;
                        li.classList.add('suggestion');
                        authorSuggestionList.appendChild(li);
                    });
                }
            } catch (error) {
                console.error('Error: ', error);
                suggestions = [];
            }
        } else {
            authorSuggestionList.innerHTML = '';
        }
    });
}

if (searchPublisher) {
    searchPublisher.addEventListener('input', async (e) => {
        const publisher = e.target.value;
        if (publisher.length > 2) {
            try {
                response = await fetch(`/publisher_search?search=${encodeURIComponent(publisher)}`);
                var suggestions = await response.json()
                publisherSuggestionList.innerHTML = '';
                suggestions.forEach(suggestion => {
                    const li = document.createElement('li');
                    li.innerHTML = suggestion.name;
                    li.classList.add('suggestion');
                    publisherSuggestionList.appendChild(li);
                });
            } catch (error) {
                console.error('Error: ', error);
                suggestions = [];
            }
        } else {
            publisherSuggestionList.innerHTML = '';
        }
    });
}

if (searchVendor) {
    searchVendor.addEventListener('input', async (e) => {
        const vendor = e.target.value;
        if (vendor.length > 2) {
            try {
                response = await fetch(`/vendor_search?search=${encodeURIComponent(vendor)}`);
                var suggestions = await response.json()
                vendorSuggestionList.innerHTML = '';
                suggestions.forEach(suggestion => {
                    const li = document.createElement('li');
                    li.innerHTML = suggestion.name;
                    li.classList.add('suggestion');
                    vendorSuggestionList.appendChild(li);
                });
            } catch (error) {
                console.error('Error: ', error);
                suggestions = [];
            }
        } else {
            vendorSuggestionList.innerHTML = '';
        }
    });
}

if (searchMember) {
    searchMember.addEventListener('input', async (e) => {
        const member = e.target.value;
        if (member.length > 2) {
            try {
                response = await fetch(`/member_search?search=${encodeURIComponent(member)}`);
                var suggestions = await response.json()
                memberSuggestionList.innerHTML = '';
                suggestions.forEach(suggestion => {
                    const li = document.createElement('li');
                    li.innerHTML = suggestion.name;
                    li.classList.add('suggestion');
                    memberSuggestionList.appendChild(li);
                });
            } catch (error) {
                console.error('Error: ', error);
                suggestions = [];
            }
        } else {
            memberSuggestionList.innerHTML = '';
        }
    });
}

if (searchEmployee){
    searchEmployee.addEventListener('input', async (e) => {
        const employee = e.target.value;
        if (employee.length > 2) {
            try {
                response = await fetch(`/employee_search?search=${encodeURIComponent(employee)}`);
                var suggestions = await response.json()
                employeeSuggestionList.innerHTML = '';
                suggestions.forEach(suggestion => {
                    const li = document.createElement('li');
                    li.innerHTML = suggestion.name;
                    li.classList.add('suggestion');
                    employeeSuggestionList.appendChild(li);
                });
            } catch (error) {
                console.error('Error: ', error);
                suggestions = [];
            }
        } else {
            employeeSuggestionList.innerHTML = '';
        }
    });
}

document.body.addEventListener('click', (e) => {
    if (e.target.classList.contains('suggestion')) {
        const parent = e.target.parentElement;
        const input = parent.previousElementSibling;
        input.value = e.target.textContent;
        parent.innerHTML = '';
    }
});
