-- 코드를 입력하세요
SELECT fp.PRODUCT_ID, fp.PRODUCT_NAME, sum(fp.PRICE * fo.amount) TOTAL_SALES from food_product fp
join food_order fo on fp.product_id = fo.product_id and fo.produce_date like '2022-05%'
group by fp.product_id
order by TOTAL_SALES desc, fp.product_id
