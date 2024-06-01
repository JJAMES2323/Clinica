document.getElementById("btn_open").addEventListener("click", open_close_menu);

var side_menu = document.getElementById("menu_side");
var btn_open = document.getElementById("btn_open");
var body = document.getElementById("body");

function open_close_menu() {
    body.classList.toggle("body_move");
    side_menu.classList.toggle("menu__side_move");
}

if (window.innerWidth < 760) {
    body.classList.add("body_move");
    side_menu.classList.add("menu__side_move");
}

window.addEventListener("resize", function () {
    if (window.innerWidth > 760) {
        body.classList.remove("body_move");
        side_menu.classList.remove("menu__side_move");
    }

    if (window.innerWidth < 760) {
        body.classList.add("body_move");
        side_menu.classList.add("menu__side_move");
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const registroForm = document.getElementById("registroForm");
    const registrarOption = document.getElementById("registrarOption");

    // Función para habilitar o deshabilitar campos según el estado del checkbox
    function toggleFields(checkbox, fields) {
        fields.querySelectorAll('input, textarea').forEach(element => {
            element.disabled = !checkbox.checked;
        });
    }

    registrarOption.addEventListener("click", function (e) {
        e.preventDefault();
        cerrarFormularioAbierto();
        console.log("se registro click");
        registroForm.style.display = "block";
    });

    function cerrarFormularioAbierto() {
        registroForm.style.display = "none";
    }
});

