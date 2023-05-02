// async function MaFonction() {
//   let response = await fetch("http://127.0.0.1:8000/api/customers/", {
//     method: "get",
//     headers: {
//       "Content-type": "application/json",
//     },
//   });
//   data = await response.json();
//   console.log(data);
// }

let mydata;
window.addEventListener("load", () => {
  fetch("http://127.0.0.1:8000/api/customers/")
    .then((response) => response.json())
    .then((data) => {
      myData = data;
    })
    .catch((error) => console.error(error));
});
