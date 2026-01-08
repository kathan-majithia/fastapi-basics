async function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const formdata = new URLSearchParams();
    formdata.append("username", email);
    formdata.append("password", password);

    const res = await fetch(`${API_BASE_URL}/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: formdata.toString()
    });

    if (!res.ok) {
        console.error(await res.text());
        alert("Invalid credentials");
        return;
    }

    const data = await res.json();
    localStorage.setItem("token", data.access_token);
    window.location.href = "/dashboard";
}
