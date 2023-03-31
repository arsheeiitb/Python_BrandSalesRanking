# Python_BrandSalesRanking
Codes for Given Python Problem
This code reads in two CSV files, "Sales.csv" and "Product.csv", and merges them on the 'ProductCode' column. Then, it groups the resulting dataframe by 'BrandName' and 'ProductName', and calculates the sum of 'Sales' for each group. It then creates a new dataframe with the total sales for each 'BrandName'/'ProductName' group and adds a 'Rank' column which ranks the total sales for each group within its 'BrandName' group in descending order. Finally, it creates a new dataframe 'result_df' that only contains rows where the 'Rank' is equal to 1, meaning it only includes the top-selling product for each brand.

The resulting dataframe 'result_df' shows the top-selling product for each brand based on the 'Sales' column, as well as the total sales for that product within the given brand.
