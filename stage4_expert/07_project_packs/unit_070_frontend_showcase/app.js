const projects = [
  {
    title: "Study Tracker",
    description: "A dashboard that helps beginners record daily study habits.",
    tags: ["JavaScript", "UI", "Dashboard"],
    result: "Clear daily flow with one-click status updates.",
  },
  {
    title: "Recipe Notes",
    description: "A small tool to organize recipes and mark favorites.",
    tags: ["HTML", "CSS", "UI"],
    result: "Simple information layout with strong readability.",
  },
  {
    title: "Task Focus Board",
    description: "A board that separates tasks into now, next, and later.",
    tags: ["JavaScript", "Productivity", "Dashboard"],
    result: "Improves decision-making by reducing clutter.",
  },
  {
    title: "Travel Memory Page",
    description: "A visual page for story-driven trip highlights.",
    tags: ["HTML", "CSS", "Storytelling"],
    result: "Turns static content into a more narrative experience.",
  },
];

const allTags = ["All", ...new Set(projects.flatMap((project) => project.tags))];
let activeTag = "All";

function renderFilters() {
  const container = document.getElementById("filters");
  container.innerHTML = "";

  allTags.forEach((tag) => {
    const button = document.createElement("button");
    button.className = `filter-button${tag === activeTag ? " is-active" : ""}`;
    button.textContent = tag;
    button.addEventListener("click", () => {
      activeTag = tag;
      renderFilters();
      renderProjects();
    });
    container.appendChild(button);
  });
}

function getVisibleProjects() {
  if (activeTag === "All") {
    return projects;
  }
  return projects.filter((project) => project.tags.includes(activeTag));
}

function renderProjects() {
  const visibleProjects = getVisibleProjects();
  const list = document.getElementById("project-list");
  const count = document.getElementById("project-count");

  count.textContent = `${visibleProjects.length} project(s)`;
  list.innerHTML = "";

  visibleProjects.forEach((project) => {
    const card = document.createElement("article");
    card.className = "project-card";

    const tags = project.tags.map((tag) => `<span class="tag">${tag}</span>`).join("");

    card.innerHTML = `
      <h3>${project.title}</h3>
      <p>${project.description}</p>
      <div class="tag-list">${tags}</div>
      <p class="result"><strong>Result:</strong> ${project.result}</p>
    `;

    list.appendChild(card);
  });
}

renderFilters();
renderProjects();
