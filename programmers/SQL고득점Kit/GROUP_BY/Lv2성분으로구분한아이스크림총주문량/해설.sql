-- 코드를 입력하세요
SELECT ii.INGREDIENT_TYPE, sum(fh.TOTAL_ORDER) TOTAL_ORDER from first_half fh
join icecream_info ii on fh.flavor = ii.flavor
group by ii.ingredient_type
order by fh.total_order
