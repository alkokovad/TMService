let line = document.querySelector('.line_here');
if (screen.width > screen.height){
    line.classList.add('.search_line_wide')
}
if (screen.height > screen.width){
    line.classList.add('.search_line_thin')
}