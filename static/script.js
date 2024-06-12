function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    eel.login(username, password)(response => {
        alert(response);
    });
}

function openRegister() {
    // Open register modal or new page
}

function showScoreboard() {
    eel.get_top_users()(users => {
        let scoreboard = "Top Users:\n";
        users.forEach(user => {
            scoreboard += `${user[0]} - ${user[1]} seconds\n`;
        });
        alert(scoreboard);
    });
}
