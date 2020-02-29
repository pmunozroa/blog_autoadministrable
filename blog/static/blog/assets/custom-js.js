let boton = document.querySelector("#clear");
let input = document.querySelector("#filter-input");
let form = document.querySelector("#form-filter");
let main = document.querySelector("#main");
let secondary = document.querySelector("#filter");
function filtering(e) {
  e.preventDefault();
  if (input.value.length > 3) {
    let data = new FormData(form);
    let url = form.getAttribute("data-filter-url");
    fetch(url, { method: "POST", body: data })
      .then(resp => resp.text())
      .then(resp => {
        main.setAttribute("style", "display:none");
        secondary.innerHTML = "";
        secondary.innerHTML = resp;
        secondary.setAttribute("style", "display:flex");
      })
      .catch(() => {
        main.setAttribute("style", "display:flex");
        secondary.setAttribute("style", "display:none");
      });
  } else {
    main.setAttribute("style", "display:flex");
    secondary.setAttribute("style", "display:none");
  }
}

function clear() {
  input.value = "";
  main.setAttribute("style", "display:flex");
  secondary.setAttribute("style", "display:none");
}

input.addEventListener("change", filtering);
form.addEventListener("submit", filtering);
boton.addEventListener("click", clear);
