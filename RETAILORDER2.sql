USE ORDER_DATA;
SELECT * FROM RETAILORDER;
SELECT * FROM RETAILORDER2;

#1. Orders shipped via Standard Class Ship Mode
SELECT r2.Order_Id, r2.Order_Date, r2.Ship_Mode, r2.Product_Id, r.Category, r2.Quantity, r2.Sales, r2.Profit FROM RETAILORDER2 r2 JOIN RETAILORDER r ON r2.Product_Id = r.Product_Id WHERE r2.Ship_Mode = 'Standard Class' LIMIT 100;

#2. Orders with product details using a join between RetailOrder and RetailOrder2
SELECT r2.Order_Id, r2.Order_Date,  r2.Product_Id, r.Category, r.Sub_Category, r2.Quantity, r2.Sales, r2.Profit FROM RETAILORDER2 r2 JOIN RETAILORDER r ON r2.Product_Id = r.Product_Id LIMIT 100;

#3. Finding Cities with the highest sales
SELECT City, SUM(Sales) AS Total_Sales FROM RETAILORDER2 GROUP BY City ORDER BY Total_Sales DESC LIMIT 10;

#4. Finding Most common sub-category sold
SELECT Category, Sub_Category, COUNT(*) AS Total_Sold FROM RETAILORDER2 GROUP BY Category, Sub_Category ORDER BY Total_Sold DESC LIMIT 1;

#5. Orders with a discount greater than 10%
SELECT Order_Id, Order_Date, Product_Id, Quantity, Discount, Sales, Profit FROM RETAILORDER2 WHERE Discount > 10 LIMIT 50;

#6. Orders where Loss Occurs
SELECT Order_Id, Order_Date, Product_Id, Quantity, Discount, Sales, Profit FROM RETAILORDER2 WHERE Profit < 0 LIMIT 100;

#7. Compute Total Sales per Category using joins
SELECT r.Order_Id, r2.Category, SUM(r2.Sales) AS Total_Sales FROM RETAILORDER2 r2 JOIN RETAILORDER r ON r2.Product_Id = r.Product_Id GROUP BY r.Order_Id, r2.Category ORDER BY Total_Sales DESC;

#8. Orders placed in a Particular City
SELECT r.Order_Id, r.Order_Date, r2.City FROM RETAILORDER2 r2 JOIN RETAILORDER r ON r2.Product_Id = r.Product_Id WHERE r2.City = 'New York City';

#9. Products and their Sub categories
SELECT r.Category, r2.Sub_Category FROM RETAILORDER2 r2 JOIN RETAILORDER r ON r2.Product_Id = r.Product_Id LIMIT 100;

#10. Finding Product with the Lowest Total Sales
SELECT r.Order_Id, r2.Category, r2.Sub_Category, SUM(r2.Sales) AS Total_Sales FROM RETAILORDER r2 JOIN RETAILORDER r ON r2.Product_Id = r.Product_Id GROUP BY  r.Order_Id, r2.Category, r2.Sub_Category ORDER BY Total_Sales ASC LIMIT 100;

