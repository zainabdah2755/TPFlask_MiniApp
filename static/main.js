document.addEventListener("DOMContentLoaded", function () {

    const deleteButtons = document.querySelectorAll(".delete-btn");

    deleteButtons.forEach(btn => {
        btn.addEventListener("click", function (event) {
            const ok = confirm("suprimmer cette tachhe ?");
            if (!ok) {
                event.preventDefault(); } });
    });
});
document.addEventListener("DOMContentLoaded", function () {

    const searchInput = document.getElementById("search");
    const tasks = document.querySelectorAll("li");

    searchInput.addEventListener("input", function () {
        const search = this.value.toLowerCase();

        tasks.forEach(task => {
            const text = task.textContent.toLowerCase();
            task.style.display = text.includes(search) ? "" : "none";
        });
    });

});

