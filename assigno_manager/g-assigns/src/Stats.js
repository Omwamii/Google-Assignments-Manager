// import React from 'react';
// import { Bar } from 'react-chartjs-2';
// import { stats } from './data';

// const labels = Object.keys(stats);
// const statData = Object.values(stats);

// const Stats = () => {
//   const data = {
//     labels: labels,
//     datasets: [
//       {
//         label: 'Grades avg per unit',
//         data: statData,
//         borderWidth: 1,
//       },
//     ],
//   };

//   const options = {
//     scales: {
//       yAxes: [
//         {
//           ticks: {
//             beginAtZero: true,
//           },
//         },
//       ],
//     },
//   };

//   return (
//     <div>
//       <h2>Grades Chart</h2>
//       <Bar data={data} options={options} />
//     </div>
//   );
// };


import React, { useState, useEffect } from 'react';
import { Chart } from 'primereact/chart';
import { stats } from './data';
import Navbar from './Navbar';

export default function Stats() {
    const labels = Object.keys(stats);
    const statData = Object.values(stats);
    const chartData = {
            labels: labels,
            datasets: [
              {
                label: 'Average grades per unit',
                data: statData,
                borderWidth: 1,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 205, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(201, 203, 207, 0.2)'
                  ],
                  borderColor: [
                    'rgb(255, 99, 132)',
                    'rgb(255, 159, 64)',
                    'rgb(255, 205, 86)',
                    'rgb(75, 192, 192)',
                    'rgb(54, 162, 235)',
                    'rgb(153, 102, 255)',
                    'rgb(201, 203, 207)'
                  ]
              }]
          };

      const chartOptions = {
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: true,
          },
        },
      ],
    },
  };

    return (
      <div>
        <Navbar />
        <div id='chart' className='app-content'>
            <Chart type="bar" data={chartData} options={chartOptions} />
        </div>
      </div>
    )
}