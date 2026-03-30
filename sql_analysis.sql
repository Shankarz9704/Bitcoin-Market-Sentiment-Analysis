-- 🔹 STEP 7: SQL ANALYSIS
-- Load `bitcoin_data.csv` into a MySQL, PostgreSQL, or SQL Server database.

-- 1. Table Creation
CREATE TABLE IF NOT EXISTS bitcoin (
    Date DATE,
    Sentiment VARCHAR(20),
    Price FLOAT
);

-- Note: Use your database's bulk import tool (like COPY in PostgreSQL or LOAD DATA INFILE in MySQL) 
-- to load the CSV into this table.


-- 2. Average price by sentiment
SELECT 
    Sentiment, 
    ROUND(AVG(Price), 2) AS AvgPrice
FROM bitcoin
GROUP BY Sentiment
ORDER BY AvgPrice DESC;


-- 3. Trend analysis (Monthly Average Price)
-- (Note: MySQL syntax. In PostgreSQL, use TO_CHAR(Date, 'YYYY-MM'))
SELECT 
    DATE_FORMAT(Date, '%Y-%m') AS Month, 
    ROUND(AVG(Price), 2) AS AvgPrice
FROM bitcoin
GROUP BY Month
ORDER BY Month ASC;


-- 4. Count the number of days in each market sentiment phase
SELECT 
    Sentiment, 
    COUNT(*) AS TotalDays
FROM bitcoin
GROUP BY Sentiment
ORDER BY TotalDays DESC;


-- 5. Find the day with the highest Bitcoin price
SELECT 
    Date, 
    Sentiment, 
    Price
FROM bitcoin
ORDER BY Price DESC
LIMIT 1;


-- 6. Find the day with the lowest Bitcoin price
SELECT 
    Date, 
    Sentiment, 
    Price
FROM bitcoin
ORDER BY Price ASC
LIMIT 1;
