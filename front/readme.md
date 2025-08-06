The task is to create 2 bar charts and render some data.
Please use chartjs library (included in package.json) for charts 

First bar chart:
- use dataFirstChart variable from src/constants.ts file
- this variable contains records about sales of products in a store
    - productName - name of a product (each product has unique name => ProductSalesRecord with same productName relate to single product)
	   - soldCount - number of products sold in specific month
	   - month - number of a month in which sale was recorded
- The barchart should showcase a total sales overview per product
    - X axis should consist of product names
    - Y axis should showcase Total value of sold product (across all recorded months)

Second bar chart (stacked bar chart):
- use dataSecondChart variable from src/constants.ts file
- this variable contains records about sales of products in a store but in a different format (grouped by month):
    - month - number of a month in which sale was recorded
    - products - list of products sold that month
        - productName - unique name of product
        - soldCount - number of products sold
- We want to see a stacked barchart showcasing sales of distinct products across month
    - X axis should consist of month names (you can use months array defined in constants.ts)
    - Y axis should showcase total value of sold products (each product should have its unique color and be part of "stacked bar")

P.S. In an ideal scenario, you should create a reusable component for 2 charts