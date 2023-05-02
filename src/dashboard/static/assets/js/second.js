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

fetch("http://127.0.0.1:8000/api/orderTOP10/")
  .then((response) => response.json())
  .then((data) => {
    const labels = data.map((item) => item.label);
    const values = data.map((item) => item.value);
    console.log(data);
    const chartData = {
      labels: labels,
      datasets: [
        {
          label: "Mon graphique",
          data: values,
        },
      ],
    };

    const ctx = document.getElementById("myChart").getContext("2d");
    const myChart = new Chart(ctx, {
      type: "bar",
      data: chartData,
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: "top",
          },
        },
      },
    });
  });
