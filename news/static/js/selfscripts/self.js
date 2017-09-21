document.addEventListener("dragenter", function(e){
    dropbox.style.borderColor = 'gray';
}, false);
document.addEventListener("dragleave", function(e){
    dropbox.style.borderColor = 'silver';
}, false);
dropbox.addEventListener("dragenter", function(e){
    dropbox.style.borderColor = 'gray';
    dropbox.style.backgroundColor = 'white';
}, false);
dropbox.addEventListener("dragleave", function(e){
    dropbox.style.backgroundColor = 'transparent';
}, false);
dropbox.addEventListener("dragenter", function(e){
    e.stopPropagation();
    e.preventDefault();
}, false);
dropbox.addEventListener("dragover", function(e){
    e.stopPropagation();
    e.preventDefault();
}, false);
dropbox.addEventListener("drop", function(e){
    e.stopPropagation();
    e.preventDefault();

    handleFiles(e.dataTransfer.files);

    submit.disabled = false;
}, false);