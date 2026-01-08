async function loadBlogs() {
  checkAuth();

  const res = await fetch(`${API_BASE_URL}/blog/`, {
    headers: authHeader()
  });

  const blogs = await res.json();
  const container = document.getElementById("blogs");

  container.innerHTML = "";

  blogs.forEach(blog => {
    container.innerHTML += `
      <div>
        <h3>${blog.title}</h3>
        <p>${blog.body}</p>
        <button onclick="deleteBlog(${blog.id})">Delete</button>
      </div>
    `;
  });
}

async function createBlog() {
  const title = document.getElementById("title").value;
  const body = document.getElementById("body").value;

  await fetch(`${API_BASE_URL}/blog/`, {
    method: "POST",
    headers: authHeader(),
    body: JSON.stringify({ title, body })
  });

  window.location.href = "/dashboard";
}

async function deleteBlog(id) {
  await fetch(`${API_BASE_URL}/blog/${id}`, {
    method: "DELETE",
    headers: authHeader()
  });

  loadBlogs();
}
