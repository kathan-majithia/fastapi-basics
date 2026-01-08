function checkAuth(){
    const token = localStorage.getItem("token")
    if(!token){
        window.location.href = "index.html"
    }
}

function authHeader(){
    return{
        "Authorization": `Bearer ${localStorage.getItem("token")}`,
        "Content-Type": "application/json"
    }
}