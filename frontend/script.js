function handleFileSelect(evt) {
    evt.stopPropagation();
    evt.preventDefault();

    var files = evt.dataTransfer.files; // FileList object.
    var file = files[0]; 
    if (file.type.match('application/pdf')) {
      // Do something with the PDF file 
    } else {
      alert('Please drop a PDF file.');
    }
  }

  function handleDragOver(evt) {
    evt.stopPropagation();
    evt.preventDefault();
    evt.dataTransfer.dropEffect = 'copy'; 
  }

  // Setup the dnd listeners.
  window.addEventListener('DOMContentLoaded', (event) => {
    var dropZone = document.getElementById('drop_zone');
    dropZone.addEventListener('dragover', handleDragOver, false);
    dropZone.addEventListener('drop', handleFileSelect, false);
  });