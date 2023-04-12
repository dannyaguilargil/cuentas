
//LO MISMO PARA REGISTRO PRESUPUESTAL , VISUALIZACION DEL PDF
console.log("entro al script de pdf 2")
document.querySelector('#pdffFiles').addEventListener('change', () => {

    let pdffFile = document.querySelector('#pdffFiles').files[0];
    let pdffFileURL = URL.createObjectURL(pdffFile) + "#toolbar=0";

    document.querySelector('#vistaPrevias').setAttribute('src', pdffFileURL);
})

