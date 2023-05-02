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

let myData;

function fetchMyData() {
  const response = fetch("http://127.0.0.1:8000/api/customers/")
    .then((response) => response.json())
    .then((data) => {
      // myData = data;
      return data;
      // Appel d'une fonction qui utilise myData
    })
    .catch((error) => console.error(error));
  return response;
}

console.log(fetchMyData());
