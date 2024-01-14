
let sidebar = document.querySelector('.dash_1');
let dash_2 = document.querySelector('.dash_2');
let dash_12 = document.querySelector('.dash_12');

// localStorage.setItem('dash_2', dash_2)
function closemenu() {
  sidebar.classList.toggle('open')
  dash_2.classList.toggle('dash_margin')
  dash_12.classList.toggle('close')
}



// --------------------------- AJAX Django CSRF_TOKEN--------------------
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie("csrftoken");



// ================ getting all buttons =======================
let btns = document.querySelectorAll("#update-cart");

btns.forEach((btn) => {
  btn.addEventListener("click", addToCart);
});

function addToCart(e) {

  let product_id = this.dataset.product;
  let action = this.dataset.action;
  let url = "/add_to_cart";


  fetch(url, {
    method: "POST",
    headers: { "content-Type": "applicaton/json", "X-CSRFToken": csrftoken },
    body: JSON.stringify({ productid: product_id, action: action }),
  })
    .then((res) => res.json())
    .then((data) => {
      document.getElementById("num_of_items").innerHTML = data;
      console.log(action, product_id);
      location.reload();
    })
    .catch((error) => {
      console.log(error);
    });
}




let plan_btn = document.getElementById('#select_plan')


btns.forEach((btn) => {
  btn.addEventListener("click", SelectPlan);
});

function SelectPlan(e) {

  let product_id = this.dataset.product;
  let url = "/select_plan";


  fetch(url, {
    method: "POST",
    headers: { "content-Type": "applicaton/json", "X-CSRFToken": csrftoken },
    body: JSON.stringify({ productid: product_id }),
  })
    .then((res) => res.json())
    .then((data) => {
      document.getElementById("pack_name").innerHTML = data;
      console.log(product_id);
      location.reload();
    })
    .catch((error) => {
      console.log(error);
    });
}


// ============= messages =======================
let msg = document.querySelector('.messages')
msg.classList.add('msg')
setTimeout(() => msg.remove(), 3000)




