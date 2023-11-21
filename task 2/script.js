document.addEventListener("DOMContentLoaded", function () {
    const taskInput = document.getElementById("task");
    const addButton = document.getElementById("addButton");
    const taskList = document.getElementById("taskList");

    addButton.addEventListener("click", function () {
        const taskText = taskInput.value.trim();

        if (taskText !== "") {
            const li = document.createElement("li");
            li.innerHTML = `
                <span>${taskText}</span>
                <button class="delete-button">Delete</button>
            `;

            taskList.appendChild(li);

            taskInput.value = "";
        }
    });

    taskList.addEventListener("click", function (event) {
        if (event.target.classList.contains("delete-button")) {
            event.target.parentElement.remove();
        }
    });
});
