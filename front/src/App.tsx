import "./styles.css";
import BarChart from "./components/BarChart";
import { dataFirstChart, dataSecondChart, months } from "./constants";

export default function App() {
  // First Chart - Total Sales per Product
  const productTotals: Record<string, number> = {};
  dataFirstChart.forEach(({ productName, soldCount }) => {
    productTotals[productName] = (productTotals[productName] || 0) + soldCount;
  });
  const firstChartLabels = Object.keys(productTotals);
  const firstChartData = [
    {
      label: "Total Sold",
      data: Object.values(productTotals),
      backgroundColor: "rgba(75, 192, 192, 0.6)",
    },
  ];

  // Second Chart - Stacked Sales by Month
  const productSet = new Set<string>();
  dataSecondChart.forEach(({ products }) =>
    products.forEach((p) => productSet.add(p.productName))
  );
  const allProducts = Array.from(productSet);

  const productColorMap: Record<string, string> = {};
  const colors = [
    "#FF6384",
    "#36A2EB",
    "#FFCE56",
    "#4BC0C0",
    "#9966FF",
    "#FF9F40",
  ];
  allProducts.forEach((prod, idx) => {
    productColorMap[prod] = colors[idx % colors.length];
  });

  const stackedDatasets = allProducts.map((productName) => ({
    label: productName,
    data: months.map((_, i) => {
      const monthData = dataSecondChart.find((d) => d.month === i + 1);
      if (!monthData) return 0;
      const product = monthData.products.find(
        (p) => p.productName === productName
      );
      return product?.soldCount || 0;
    }),
    backgroundColor: productColorMap[productName],
  }));

  return (
    <div className="App">
      <h1>Sales Charts</h1>
      <BarChart
        title="Total Sales per Product"
        labels={firstChartLabels}
        datasets={firstChartData}
      />
      <BarChart
        title="Monthly Sales - Stacked by Product"
        labels={months}
        datasets={stackedDatasets}
        stacked
      />
    </div>
  );
}
