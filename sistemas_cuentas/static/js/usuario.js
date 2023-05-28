console.log("entro a usuario");
//script para crear el nombre del usuario en el sistema tomando primera letra y primerapellido
var nombre = document.getElementById('nombre');
var usuario = document.getElementById('usuario');

var valorOrigen = nombre.value;
var primerCampo = valorOrigen.split(' ')[0];
usuario.value = primerCampo;

var cedula = document.getElementById('cedula');
var contrasena = document.getElementById('contrasena');


cedula.addEventListener('input', function() {
  console.log("entro por aqui");
  var valorOrigen =cedula.value;
  contrasena.value = valorOrigen;
});