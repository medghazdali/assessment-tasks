interface ProductSalesRecord {
  productName: string;
  soldCount: number;
  month: number;
}

interface ProductSalesPerMonthRecord {
  month: number;
  products: {
    productName: string;
    soldCount: number;
  }[];
}

export const dataFirstChart: ProductSalesRecord[] = [
  {
    productName: "Bar 1",
    soldCount: 10,
    month: 1,
  },
  {
    productName: "Bar 2",
    soldCount: 20,
    month: 1,
  },
  {
    productName: "Bar 3",
    soldCount: 30,
    month: 1,
  },
  {
    productName: "Bar 1",
    soldCount: 40,
    month: 2,
  },
  {
    productName: "Bar 2",
    soldCount: 50,
    month: 2,
  },
  {
    productName: "Bar 3",
    soldCount: 60,
    month: 2,
  },
  {
    productName: "Bar 1",
    soldCount: 70,
    month: 3,
  },
  {
    productName: "Bar 2",
    soldCount: 80,
    month: 4,
  },
];

export const dataSecondChart: ProductSalesPerMonthRecord[] = [
  {
    month: 1,
    products: [
      {
        productName: "Product 1",
        soldCount: 46025,
      },
      {
        productName: "Product 2",
        soldCount: 38912,
      },
      {
        productName: "Product 3",
        soldCount: 19990,
      },
    ],
  },
  {
    month: 2,
    products: [
      {
        productName: "Product 1",
        soldCount: 22025,
      },
      {
        productName: "Product 2",
        soldCount: 56912,
      },
      {
        productName: "Product 3",
        soldCount: 70990,
      },
    ],
  },
  {
    month: 3,
    products: [
      {
        productName: "Product 2",
        soldCount: 22025,
      },
      {
        productName: "Product 3",
        soldCount: 56912,
      },
      {
        productName: "Product 4",
        soldCount: 70990,
      },
    ],
  },
];

export const months = [
  "Jan",
  "Feb",
  "Mar",
  "Apr",
  "May",
  "Jun",
  "July",
  "Aug",
  "Sep",
  "Oct",
  "Nov",
  "Dec",
];
