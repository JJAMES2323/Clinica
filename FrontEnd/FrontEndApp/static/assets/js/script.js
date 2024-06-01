
document.getElementById("btn_open").addEventListener("click", open_close_menu);


var side_menu = document.getElementById("menu_side");
var btn_open = document.getElementById("btn_open");
var body = document.getElementById("body");


    function open_close_menu(){
        body.classList.toggle("body_move");
        side_menu.classList.toggle("menu__side_move");
    }



if (window.innerWidth < 760){

    body.classList.add("body_move");
    side_menu.classList.add("menu__side_move");
}



window.addEventListener("resize", function(){

    if (window.innerWidth > 760){

        body.classList.remove("body_move");
        side_menu.classList.remove("menu__side_move");
    }

    if (window.innerWidth < 760){

        body.classList.add("body_move");
        side_menu.classList.add("menu__side_move");
    }

});

document.addEventListener("DOMContentLoaded", function () {
    const registroForm = document.getElementById("registroForm");
    const registrarOption = document.getElementById("registrarOption");
    const actualizarForm = document.getElementById("actualizarForm");
    const actualizarOption = document.getElementById("actualizarOption");
    const eliminarForm=document.getElementById("eliminarForm");
    const eliminarOption=document.getElementById("eliminarOption");
    const cerrarForm = document.getElementById("cerrarForm");
    const cerrarFormA = document.getElementById("cerrarFormA");
    const cerrarFormE = document.getElementById("cerrarFormE");
    const registroFormAdmin = document.getElementById("registroFormAdmin");
    const registrarOptionAdmin = document.getElementById("registrarOptionAdmin");
    const cerrarFormAdmin = document.getElementById("cerrarFormAdmin");

    registrarOption.addEventListener("click", function (e) {
        e.preventDefault();
        cerrarFormularioAbierto(); // Cierra el formulario abierto actualmente
        registroForm.style.display = "block";
    });

    actualizarOption.addEventListener("click", function (e) {
        e.preventDefault();
        cerrarFormularioAbierto(); 
        actualizarForm.style.display = "block";
    });

    eliminarOption.addEventListener("click", function (e) {
        e.preventDefault();
        console.log("Eliminar opción clickeada");
        cerrarFormularioAbierto(); 
        eliminarForm.style.display = "block";
    });

    registrarOptionAdmin.addEventListener("click", function (e) {
        e.preventDefault();
        console.log("Se registro el boton");
        cerrarFormularioAbierto();
        registroFormAdmin.style.display = "block";
    });

    cerrarForm.addEventListener("click", function () {
        registroForm.style.display = "none";
    });

    cerrarFormA.addEventListener("click", function () {
        actualizarForm.style.display = "none";
    });

    cerrarFormE.addEventListener("click", function () {
        eliminarForm.style.display = "none";
    });

    cerrarFormAdmin.addEventListener("click", function () {
        registroFormAdmin.style.display = "none";
    });

    function cerrarFormularioAbierto() {
        registroForm.style.display = "none";
        actualizarForm.style.display = "none";
        eliminarForm.style.display = "none"
        // Agrega más formularios si es necesario
    }
});








