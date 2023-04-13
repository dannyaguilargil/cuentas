console.log("entro en planilla")
document.querySelector('#pdffFilesss').addEventListener('change', () => {

    let pdffFile = document.querySelector('#pdffFilesss').files[0];
    let pdffFileURL = URL.createObjectURL(pdffFile) + "#toolbar=0";

    document.querySelector('#vistaPreviasss').setAttribute('src', pdffFileURL);
})

