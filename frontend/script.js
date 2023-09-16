document.querySelector(".FileButton").addEventListener('dragover', (e) => {
    e.preventDefault()
});
document.querySelector(".FileButton").addEventListener('drop', (e) => {
    document.getElementById('file').files = e.dataTransfer.files;
    e.preventDefault()
});

