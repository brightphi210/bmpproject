// ========================= dashbord side bar ======================
let sidebar = document.querySelector('.dash_1');
let dash_2 = document.querySelector('.dash_2');
let dash_12 = document.querySelector('.dash_12');

function closemenu() {
  sidebar.classList.toggle('close')
  dash_2.classList.toggle('dash_margin')
  dash_12.classList.toggle('close')
}