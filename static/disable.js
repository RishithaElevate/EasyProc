// Force fullscreen on page load
document.addEventListener("DOMContentLoaded", () => {
    if (document.documentElement.requestFullscreen) {
        document.documentElement.requestFullscreen();
    }
});

// Disable right-click
document.addEventListener("contextmenu", event => event.preventDefault());

// Disable keyboard shortcuts
document.addEventListener("keydown", function (e) {
    if (
        (e.ctrlKey && (e.key === "c" || e.key === "v" || e.key === "u")) || // Copy, Paste, View Source
        (e.key === "F12") // Dev Tools
    ) {
        e.preventDefault();
    }
});
