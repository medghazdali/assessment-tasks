import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  BarElement,
  CategoryScale,
  LinearScale,
  Title,
  Tooltip,
  Legend
);

interface BarChartProps {
  title: string;
  labels: string[];
  datasets: any[];
  stacked?: boolean;
}

export default function BarChart({
  title,
  labels,
  datasets,
  stacked = false,
}: BarChartProps) {
  return (
    <div style={{ marginBottom: 40 }}>
      <h3>{title}</h3>
      <Bar
        data={{
          labels,
          datasets,
        }}
        options={{
          responsive: true,
          plugins: {
            legend: { position: "top" },
            title: { display: true, text: title },
          },
          scales: {
            x: { stacked },
            y: { stacked },
          },
        }}
      />
    </div>
  );
}
