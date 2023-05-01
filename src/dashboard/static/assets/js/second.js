async function MaFonction() {
  let response = await fetch("http://127.0.0.1:8000/api/customers/", {
    method: "get",
    headers: {
      "Content-type": "application/json",
    },
  });
  let data = await response.json();
  console.log(data);
}
