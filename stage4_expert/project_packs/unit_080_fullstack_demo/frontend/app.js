const API_BASE = "http://127.0.0.1:8000";

async function request(path, options = {}) {
  const response = await fetch(`${API_BASE}${path}`, {
    headers: {
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
    ...options,
  });

  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }

  return response.json();
}

async function loadTodos() {
  const data = await request("/api/todos");
  renderTodos(data.items);
  document.getElementById("status-text").textContent = `${data.items.length} task(s)`;
}

function renderTodos(items) {
  const list = document.getElementById("todo-list");
  list.innerHTML = "";

  items.forEach((item) => {
    const li = document.createElement("li");
    li.className = `todo-item${item.done ? " is-done" : ""}`;
    li.innerHTML = `
      <span class="todo-title">${item.title}</span>
      <button type="button">Toggle</button>
    `;

    li.querySelector("button").addEventListener("click", async () => {
      await request(`/api/todos/${item.id}`, { method: "PATCH" });
      await loadTodos();
    });

    list.appendChild(li);
  });
}

document.getElementById("todo-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  const input = document.getElementById("title");
  const title = input.value.trim();

  if (!title) {
    return;
  }

  await request("/api/todos", {
    method: "POST",
    body: JSON.stringify({ title }),
  });

  input.value = "";
  await loadTodos();
});

loadTodos().catch((error) => {
  document.getElementById("status-text").textContent = error.message;
});
