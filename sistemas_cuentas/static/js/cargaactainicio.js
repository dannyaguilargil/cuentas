
//LO MISMO PARA REGISTRO PRESUPUESTAL , VISUALIZACION DEL PDF
console.log("entro al script de pdf 3")
document.querySelector('#pdffFiless').addEventListener('change', () => {

    let pdffFile = document.querySelector('#pdffFiless').files[0];
    let pdffFileURL = URL.createObjectURL(pdffFile) + "#toolbar=0";

    document.querySelector('#vistaPreviass').setAttribute('src', pdffFileURL);
})

