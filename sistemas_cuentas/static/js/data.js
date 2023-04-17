let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6] },
        { orderable: false, targets: [5, 6] },
        { searchable: false, targets: [0, 5, 6] }
    ],
    pageLength: 4,
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listProgrammers();

    dataTable = $("#datatable-programmers").DataTable(dataTableOptions);
    dataTableIsInitialized = true;
};

const listProgrammers = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/list_usuarios');
        const data = await response.json();
        console.log(data);

        let content = ``;
        data.usuarios.forEach((usuario, index) => {
            content += `
                <tr>
                    <td>${index + 1}</td>
                    <td>${usuario.nombre}</td>
                    <td>${usuario.segundonombre}</td>
                    <td>${usuario.primerapellido}</td>
                    <td>${usuario.segundoapellido}</td>
                    <td>${usuario.cedula}</td>
                    <td>
                    <button class='btn btn-sm btn-outline-success' data-bs-toggle="modal" data-bs-target="#exampleModal" ><i class='fas fa-eye'></i></button>
                    <button class='btn btn-sm btn-outline-primary' data-bs-toggle="modal" data-bs-target="#exampleModal" ><i class='fas fa-user-edit'></i></button>
                    </td>
                   
                </tr>`;
                
                //intentando agregar el value
                /*
                $('#datatable-programmers tbody').on('click','.exampleModal', function(){
                    console.log("entro al ejemplo");
                    $('#nombre').val(usuario.nombre);
                })  
                */
                //intentando agregar el value
                //$('#nombre').val(usuario.nombre);
        });
        tableBody_programmers.innerHTML = content;
    
    } catch (ex) {
        alert(ex);
    }
};


window.addEventListener("load", async () => {
    await initDataTable();
});



/*
    //PRUEBA DE MOSTRAR USUARIOS
    $('#datatable-programmers tbody').on('click','.editar', function(){ 
        let usuario = dataTable.row($(this).parents()).data();
        $('#nombre').val(usuario.nombre);
      })
    //PRUEBA DE MOSTRAR USUARIOS
*/