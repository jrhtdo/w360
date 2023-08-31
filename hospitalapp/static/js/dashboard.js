// let monthEl = document.querySelector(".date h1");

// let monthInx = new Date().getMonth();
// let months = [
//   "Jan",
//   "Feb",
//   "Mar",
//   "Apr",
//   "May",
//   "June",
//   "July",
//   "Aug",
//   "Sept",
//   "Oct",
//   "Nov",
//   "Dec",
// ];

// monthEl.innerText = months[monthInx];

var barChartOptions = {
  series: [
    {
      data: [250, 430, 448, 470, 540, 580, 690],
    },
  ],
  chart: {
    type: "bar",
    height: 350,
    toolbar: {
      show: false,
    },
  },
  colors: ["#2979ff"],
  plotOptions: {
    bar: {
      distributed: true,
      horizontal: false,
      // width: "10%",
      columnWidth: "30%",
      barHeight: "30%",
    },
  },
  dataLabels: {
    enabled: false,
  },
  legend: {
    show: false,
  },
  xaxis: {
    categories: [
      "15/7/23",
      "25/7/23",
      "26/7/23",
      "05/8/23",
      "10/8/23",
      "14/8/23",
      "26/8/23",
    ],
    yaxis: {
      categories: ["0", "20", "40", "60", "80", "100"],
    },
  },
};

var barChart = new ApexCharts(
  document.getElementById("bar-chart"),
  barChartOptions
);
barChart.render();
