document.addEventListener("DOMContentLoaded", () => {
  const themeToggle = document.getElementById("theme-toggle");

  // ===== CARGAR TEMA =====
  const savedTheme = localStorage.getItem("theme") || "light";
  document.documentElement.setAttribute("data-theme", savedTheme);

  updateIcon(savedTheme);

  // ===== SWITCH =====
  if (themeToggle) {
    themeToggle.addEventListener("click", () => {
      const current = document.documentElement.getAttribute("data-theme");
      const newTheme = current === "dark" ? "light" : "dark";

      document.documentElement.setAttribute("data-theme", newTheme);
      localStorage.setItem("theme", newTheme);

      updateIcon(newTheme);
    });
  }

  function updateIcon(theme) {
    if (!themeToggle) return;
    themeToggle.textContent = theme === "dark" ? "DARK" : "LIGHT";
  }
});
