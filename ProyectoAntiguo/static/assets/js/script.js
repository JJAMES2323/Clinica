// Agrega tus funciones JavaScript aquí
function toggleForm() {
    var form = document.getElementById("registration-form");
    form.classList.toggle("open-form");
    form.style.display = form.classList.contains("open-form") ? "block" : "none";
  }
  
  function submitForm() {
    // Agrega lógica para enviar el formulario si es necesario
  }
  
  document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("registration-form");
  
    form.addEventListener("animationend", function (event) {
      if (!form.classList.contains("open-form") && event.animationName === "fadeOut") {
        form.style.display = "none";
      }
    });
  
    // Agrega un evento al botón de cerrar
    var closeBtn = document.getElementById("close-btn");
    closeBtn.addEventListener("click", function () {
      form.classList.remove("open-form");
    });
  });
  