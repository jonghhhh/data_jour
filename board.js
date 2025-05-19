document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('board-form');
    const list = document.getElementById('board-list');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const name = document.getElementById('board-name').value.trim();
        const title = document.getElementById('board-title').value.trim();
        const content = document.getElementById('board-content').value.trim();

        if (name && title && content) {
            const li = document.createElement('li');
            li.innerHTML = `<strong>${title}</strong> <span style="color:#555;">by ${name}</span><br><div style="margin-top:0.5rem;">${content}</div>`;
            list.prepend(li);

            form.reset();
        }
    });
});