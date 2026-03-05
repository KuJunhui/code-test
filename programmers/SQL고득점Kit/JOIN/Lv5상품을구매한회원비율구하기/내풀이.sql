-- 코드를 입력하세요
SELECT year(os.sales_date) YEAR, month(os.sales_date) MONTH,
count(distinct os.user_id) PURCHASED_USERS,
round(count(distinct os.user_id)/
      (select count(*) from user_info ui
       where year(ui.joined) = '2021'), 1) PURCHASED_RATIO
from online_sale os
join user_info ui on os.user_id = ui.user_id
where year(ui.joined) = '2021'
group by year, month
order by year, month
