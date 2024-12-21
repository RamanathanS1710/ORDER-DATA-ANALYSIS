import mysql.connector
import streamlit as st
import pandas as pd

connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1710',
        database='ORDER_DATA'
    )

print('connected')

cursor = connection.cursor()

cursor.execute("SELECT * FROM RETAILORDER")
print(cursor.fetchall())
print(cursor.column_names)

st.title('ORDER DATA ANALYSIS')


# Define SQL queries
queries_tab1 = {
        "1. Find top 10 highest revenue-generating products": "SELECT Product_Id, Sub_Category, SUM(Sales) AS Total_Revenue FROM RETAILORDER GROUP BY Product_Id, Sub_Category ORDER BY Total_Revenue DESC LIMIT 10;",
        "2. Find the top 5 cities with the highest profit margins": "SELECT City, SUM(Profit) AS Total_Profit, SUM(Sales) AS Total_Revenue, (SUM(Profit) / SUM(Sales)) AS Profit_Margin FROM RETAILORDER GROUP BY City ORDER BY Profit_Margin DESC LIMIT 5;",
        "3. Calculate the total discount given for each category": "SELECT Category, SUM(Discount) AS Total_Discount FROM RETAILORDER GROUP BY Category;",
        "4. Find the average sale price per product category": "SELECT Category, AVG(List_Price) AS Avg_Sale_Price FROM RETAILORDER GROUP BY Category;",
        "5. Find the region with the highest average sale price": "SELECT City, AVG(List_Price) AS Avg_Sale_Price FROM RETAILORDER GROUP BY City ORDER BY Avg_Sale_Price DESC LIMIT 1;",
        "6. Find the total profit per category": "SELECT Category, SUM(Profit) AS Total_Profit FROM RETAILORDER GROUP BY Category ORDER BY Total_Profit;",
        "7. Identify the top 3 segments with the highest quantity of orders": "SELECT City, Category, SUM(Quantity) AS Total_Quantity FROM RETAILORDER GROUP BY City, Category ORDER BY Total_Quantity DESC LIMIT 3;",
        "8. Determine the average discount percentage given per region": "SELECT City, AVG(CASE WHEN Discount = 0 THEN 0 ELSE (Discount / List_Price) * 100 END) AS Avg_Discount_Percentage FROM RETAILORDER  GROUP BY City ORDER BY Avg_Discount_Percentage LIMIT 50;",
        "9. Find the product category with the highest total profit": "SELECT Category, SUM(Profit) AS Total_Profit FROM RETAILORDER GROUP BY Category ORDER BY Total_Profit DESC LIMIT 1;",
        "10. Calculate the total revenue generated per year": "SELECT EXTRACT(YEAR FROM Order_Date) AS Order_Year, SUM(Quantity * List_Price) AS Total_Revenue FROM RETAILORDER GROUP BY Order_Year ORDER BY Total_Revenue;",
        }

queries_tab2 = {
        "11. Orders shipped via Standard Class Ship Mode": "SELECT r2.Order_Id, r2.Order_Date, r2.Ship_Mode, r2.Product_Id, r.Category, r2.Quantity, r2.Sales, r2.Profit FROM RETAILORDER2 r2 JOIN RETAILORDER r ON r2.Product_Id = r.Product_Id WHERE r2.Ship_Mode = 'Standard Class' LIMIT 100;",
        "12. Orders with product details using a join between RetailOrder and RetailOrder2": "SELECT r2.Order_Id, r2.Order_Date,  r2.Product_Id, r.Category, r.Sub_Category, r2.Quantity, r2.Sales, r2.Profit FROM RETAILORDER2 r2 JOIN RETAILORDER r ON r2.Product_Id = r.Product_Id LIMIT 100;",
        "13. Finding Cities with the highest sales": "SELECT City, SUM(Sales) AS Total_Sales FROM RETAILORDER2 GROUP BY City ORDER BY Total_Sales DESC LIMIT 10;",
        "14. Finding Most common sub-category sold": "SELECT Category, Sub_Category, COUNT(*) AS Total_Sold FROM RETAILORDER2 GROUP BY Category, Sub_Category ORDER BY Total_Sold DESC LIMIT 1;",
        "15. Orders with a discount greater than 10%": "SELECT Order_Id, Order_Date, Product_Id, Quantity, Discount, Sales, Profit FROM RETAILORDER2 WHERE Discount > 10 LIMIT 50;",
        "16. Orders where Loss Occurs": "SELECT Order_Id, Order_Date, Product_Id, Quantity, Discount, Sales, Profit FROM RETAILORDER2 WHERE Profit < 0 LIMIT 100;",
        "17. Compute Total Sales per Category using joins": "SELECT r.Order_Id, r2.Category, SUM(r2.Sales) AS Total_Sales FROM RETAILORDER2 r2 JOIN RETAILORDER r ON r2.Product_Id = r.Product_Id GROUP BY r.Order_Id, r2.Category ORDER BY Total_Sales DESC;",
        "18. Orders placed in a Particular City": "SELECT r.Order_Id, r.Order_Date, r2.City FROM RETAILORDER2 r2 JOIN RETAILORDER r ON r2.Product_Id = r.Product_Id WHERE r2.City = 'New York City';",
        "19. Products and their Sub categories": "SELECT r.Category, r2.Sub_Category FROM RETAILORDER2 r2 JOIN RETAILORDER r ON r2.Product_Id = r.Product_Id LIMIT 100;",
        "20. Finding Product with the Lowest Total Sales": "SELECT r.Order_Id, r2.Category, r2.Sub_Category, SUM(r2.Sales) AS Total_Sales FROM RETAILORDER r2 JOIN RETAILORDER r ON r2.Product_Id = r.Product_Id GROUP BY  r.Order_Id, r2.Category, r2.Sub_Category ORDER BY Total_Sales ASC LIMIT 100",

}


# Tab layout
tab1, tab2 = st.tabs(["Queries 1-10", "Queries 11-20"])

# Tab 1 for first 10 queries
with tab1:
    st.header("Queries 1-10")
    selected_query_tab1 = st.selectbox("Select a query:", list(queries_tab1.keys()), key="tab1")
    if selected_query_tab1:
        query = queries_tab1[selected_query_tab1]
        cursor.execute(query)
        column_names = [desc[0] for desc in cursor.description]
        result = cursor.fetchall()
        df = pd.DataFrame(result, columns=column_names)
        st.table(df)

# Tab 2 for next 10 queries
with tab2:
    st.header("Queries 11-20")
    selected_query_tab2 = st.selectbox("Select a query:", list(queries_tab2.keys()), key="tab2")
    if selected_query_tab2:
        query = queries_tab2[selected_query_tab2]
        cursor.execute(query)
        column_names = [desc[0] for desc in cursor.description]
        result = cursor.fetchall()
        df = pd.DataFrame(result, columns=column_names)
        st.table(df)
        df = pd.DataFrame(result, columns=column_names)
        st.table(df)



