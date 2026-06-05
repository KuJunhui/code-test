-- 코드를 입력하세요
SELECT
    a.AUTHOR_ID,
    a.AUTHOR_NAME,
    b.CATEGORY,
    sum(bs.sales * b.price) as TOTAL_SALES
from book b
join author a on b.author_id = a.author_id
join book_sales bs on bs.book_id = b.book_id
where bs.sales_date like '2022-01%'
group by a.author_id, b.category
order by b.author_id, b.category desc

-- 1 2 3 4