let line = document.querySelector(".line_here");
let menu = document.querySelector(".menu_here");

function set_design_for_line(){
  if (window.screen.width > screen.height){
    line.classList.remove("search_line_thin");
    line.classList.add('search_line_wide');
    console.log("нет, я здесь");
  }
  else{
    line.classList.remove("search_line_wide");
    line.classList.add('search_line_thin');
    console.log("я здесь");
  }
}

function set_design_for_menu(){
  if (window.screen.width > screen.height){
    menu.classList.remove("menu_circle_thin");
    menu.classList.add('menu_circle_wide');
    console.log("нет, я здесь");
  }
  else{
    menu.classList.remove("menu_circle_wide");
    menu.classList.add('menu_circle_thin');
    console.log("я здесь");
  }
}

document.addEventListener("DOMContentLoaded", function(event) {window.onresize = function() {
set_design_for_menu();
set_design_for_line()
};});