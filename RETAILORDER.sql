CREATE DATABASE ORDER_DATA;
USE ORDER_DATA;
SELECT * FROM RETAILORDER;

#1. Find top 10 highest revenue-generating products
SELECT Product_Id, Sub_Category, SUM(Sales) AS Total_Revenue
FROM RETAILORDER
GROUP BY Product_Id, Sub_Category
ORDER BY Total_Revenue DESC
LIMIT 10;

#2. Find the top 5 cities with the highest profit margins
SELECT City, SUM(Profit) AS Total_Profit, SUM(Sales) AS Total_Revenue, 
       (SUM(Profit) / SUM(Sales)) AS Profit_Margin
FROM RETAILORDER
GROUP BY City
ORDER BY Profit_Margin DESC
LIMIT 5;

#3. Calculate the total discount given for each category
SELECT Category, SUM(Discount) AS Total_Discount
FROM RETAILORDER
GROUP BY Category;

#4. Find the average sale price per product category
SELECT Category, AVG(List_Price) AS Avg_Sale_Price
FROM RETAILORDER
GROUP BY Category;

#5. Find the region with the highest average sale price
SELECT City, AVG(List_Price) AS Avg_Sale_Price
FROM RETAILORDER
GROUP BY City
ORDER BY Avg_Sale_Price DESC
LIMIT 1;

#6. Find the total profit per category
SELECT Category, SUM(Profit) AS Total_Profit
FROM RETAILORDER
GROUP BY Category
ORDER BY Total_Profit;

#7. Identify the top 3 segments with the highest quantity of orders
SELECT City, Category, SUM(Quantity) AS Total_Quantity
FROM RETAILORDER
GROUP BY City, Category
ORDER BY Total_Quantity DESC
LIMIT 3;

#8. Determine the average discount percentage given per region
SELECT City, 
       AVG(CASE WHEN Discount = 0 THEN 0 ELSE (Discount / List_Price) * 100 END) AS Avg_Discount_Percentage
FROM RETAILORDER 
GROUP BY City
ORDER BY Avg_Discount_Percentage;

#9. Find the product category with the highest total profit
SELECT Category, SUM(Profit) AS Total_Profit
FROM RETAILORDER
GROUP BY Category
ORDER BY Total_Profit DESC
LIMIT 1;

#10. Calculate the total revenue generated per year
SELECT EXTRACT(YEAR FROM Order_Date) AS Order_Year, SUM(Quantity * List_Price) AS Total_Revenue
FROM RETAILORDER
GROUP BY Order_Year
ORDER BY Total_Revenue;