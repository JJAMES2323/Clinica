
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
    const cerrarForm = document.getElementById("cerrarForm");

    registrarOption.addEventListener("click", function (e) {
        e.preventDefault();
        registroForm.style.display = "block";
    });

    cerrarForm.addEventListener("click", function () {
        registroForm.style.display = "none";
    });

});








