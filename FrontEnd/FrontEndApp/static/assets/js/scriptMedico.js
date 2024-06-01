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
    const consultarForm = document.getElementById("consultarForm");
    const consultarOption = document.getElementById("consultarOption");
    const cerrarForm = document.getElementById("cerrarForm");
    const cerrarFormC = document.getElementById("cerrarFormC");
    const checkboxAyudaDiagnostica = document.getElementById("checkboxAyudaDiagnostica");
    const ayudaDiagnosticaFields = document.getElementById("ayudaDiagnosticaFields");
    const checkboxMedicamento = document.getElementById("checkboxMedicamento");
    const medicamentoFields = document.getElementById("medicamentoFields");
    const checkboxProcedimiento = document.getElementById("checkboxProcedimiento");
    const procedimientoFields = document.getElementById("procedimientoFields");

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

    consultarOption.addEventListener("click", function (e) {
        e.preventDefault();
        cerrarFormularioAbierto();
        console.log("se consultar click");
        consultarForm.style.display = "block";
    });

    cerrarForm.addEventListener("click", function () {
        registroForm.style.display = "none";
    });

    cerrarFormC.addEventListener("click", function () {
        consultarForm.style.display = "none";
    });

    // Deshabilitar campos al cargar la página
    toggleFields(checkboxAyudaDiagnostica, ayudaDiagnosticaFields);
    toggleFields(checkboxMedicamento, medicamentoFields);
    toggleFields(checkboxProcedimiento, procedimientoFields);

    // Habilitar/deshabilitar campos al cambiar el estado de los checkboxes
    checkboxAyudaDiagnostica.addEventListener("change", function () {
        console.log("Checkbox Ayuda Diagnóstica cambió");
        toggleFields(checkboxAyudaDiagnostica, ayudaDiagnosticaFields);
    });

    checkboxMedicamento.addEventListener("change", function () {
        console.log("Checkbox Medicamento cambió");
        toggleFields(checkboxMedicamento, medicamentoFields);
    });

    checkboxProcedimiento.addEventListener("change", function () {
        console.log("Checkbox Procedimiento cambió");
        toggleFields(checkboxProcedimiento, procedimientoFields);
    });

    function cerrarFormularioAbierto() {
        registroForm.style.display = "none";
        consultarForm.style.display = "none";
    }
});

