-- 코드를 입력하세요
SELECT h.HISTORY_ID,
round(
    c.daily_fee * (datediff(h.end_date, h.start_date) + 1)
    * (100 - coalesce(p.discount_rate, 0))/100
)
FEE
from car_rental_company_rental_history h
join car_rental_company_car c on h.car_id = c.car_id
left join car_rental_company_discount_plan p on c.car_type = p.car_type
and p.duration_type = case
    when datediff(h.end_date, h.start_date) + 1 >= 90 then '90일 이상'
    when datediff(h.end_date, h.start_date) + 1 >= 30 then '30일 이상'
    when datediff(h.end_date, h.start_date) + 1 >= 7 then '7일 이상'
    else null
end
where c.car_type = '트럭'
order by fee desc, h.history_id desc
