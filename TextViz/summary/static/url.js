const reloadLink = document.getElementById("reloadLink");
const summarizeButton = document.getElementById("summarizeButton");
const processButton = document.getElementById("processButton");
const urlArea = document.getElementById("urlArea");
const summarizeURLButton = document.getElementById("summarizeURLButton");


reloadLink.addEventListener("click", () => {
  chrome.runtime.reload();
});


