// delete book
deleteBtns = document.querySelectorAll(".danger");

for (let i = 0; i < deleteBtns.length; i++) {
    const deleteBtn = deleteBtns[i];
    deleteBtn.onclick = function (e) {
        const bookId = e.target.parentElement.dataset.id;
        fetch("/" + bookId + "/delete", {
            method: "DELETE"
        })
            .then(function () {
                const item = e.target.parentElement.parentElement;
                item.remove();
            })
            .catch(function (e) {
                console.error(e);
            });
    };
}

//read book
readBtns = document.querySelectorAll(".success");

for (let i = 0; i < readBtns.length; i++) {
    const readBtn = readBtns[i];
    readBtn.onclick = function (e) {
        const bookId = e.target.parentElement.dataset.id;
        fetch("/" + bookId + "/read", {
            method: "PUT"
        })
            .then(function () {
                const closestElement = e.target.closest("li").querySelector(".book-title");
                const newDiv = document.createElement("div");
                const newContent = document.createTextNode("&#10003;");
                newDiv.appendChild(newContent);
                // add read mark
                closestElement.parentNode.insertBefore(newDiv, closestElement.nextSibling);
                // delete the buttons
                const item = e.target.parentElement;
                item.remove();
                window.location.reload(true);
            })
            .catch(function (e) {
                console.error(e);
            });
    };
}


