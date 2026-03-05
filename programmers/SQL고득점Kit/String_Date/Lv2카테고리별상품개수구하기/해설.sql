-- 코드를 입력하세요
SELECT
substring(product_code, 1, 2) CATEGORY,
count(product_code) PRODUCTS
from product
group by category
order by category
