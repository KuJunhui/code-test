-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, coalesce(FREEZER_YN, 'N') from food_warehouse
where address like '경기도%'
order by warehouse_id
