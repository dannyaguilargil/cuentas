
console.log("entro al acript de pdf")
document.querySelector('#pdffFile').addEventListener('change', () => {
//remplazo pdffFile por archivo para una prueba de la subir dal d
    let pdffFile = document.querySelector('#pdffFile').files[0];
    let pdffFileURL = URL.createObjectURL(pdffFile) + "#toolbar=0";

    document.querySelector('#vistaPrevia').setAttribute('src', pdffFileURL);
})

//MODIFICARLO PORQUE NO PERMITE LA PREVISUALIZACION 
/*
document.addEventListener('DOMContentLoaded', function() {
    console.log("entro al script de pdf");

    var fileInputs = document.querySelectorAll('input[type="file"]');
    fileInputs.forEach(function(fileInput) {
        fileInput.addEventListener('change', function(event) {
            var inputFile = event.target.files[0];
            var inputFileURL = URL.createObjectURL(inputFile) + "#toolbar=0";

            var previewFrame = event.target.parentNode.querySelector('.pdf-preview');
            previewFrame.setAttribute('src', inputFileURL);
        });
    });
});
*/