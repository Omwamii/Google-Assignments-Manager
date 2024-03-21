import React, { useState, useEffect } from 'react';
import { Chart } from 'primereact/chart';
import Navbar from './Navbar';
import { ProgressSpinner } from 'primereact/progressspinner';
import axios from 'axios';

const url = 'http://localhost:8000/';

export default function Stats() {
  const [labels, setLabels] = useState(null);
  const [statData, setData] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    (async () => {
      try {
        const full_url = `${url}stats/`;
        const data = await axios.get(full_url);
        setLabels(Object.keys(data.data));
        setData(Object.values(data.data));
        setIsLoading(false);
      } catch (err) {
        console.error(err);
      }
    })();
  }, []);

  const chartData = {
    labels: labels,
    datasets: [
      {
        label: "Average grades per unit",
        data: statData,
        borderWidth: 1,
        backgroundColor: [
          "rgba(255, 99, 132, 0.2)",
          "rgba(255, 159, 64, 0.2)",
          "rgba(255, 205, 86, 0.2)",
          "rgba(75, 192, 192, 0.2)",
          "rgba(54, 162, 235, 0.2)",
          "rgba(153, 102, 255, 0.2)",
          "rgba(201, 203, 207, 0.2)",
        ],
        borderColor: [
          "rgb(255, 99, 132)",
          "rgb(255, 159, 64)",
          "rgb(255, 205, 86)",
          "rgb(75, 192, 192)",
          "rgb(54, 162, 235)",
          "rgb(153, 102, 255)",
          "rgb(201, 203, 207)",
        ],
      },
    ],
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

  if (isLoading) {
    return (
      <div>
        <Navbar />
        <div className="app-content">
          <ProgressSpinner />
        </div>
      </div>
    );
  }

  return (
    <div>
      <Navbar />
      <div id="chart" className="app-content">
        <Chart type="bar" data={chartData} options={chartOptions} />
      </div>
    </div>
  );
}