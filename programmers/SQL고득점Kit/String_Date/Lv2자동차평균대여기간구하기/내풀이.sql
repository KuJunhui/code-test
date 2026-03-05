-- 코드를 입력하세요
SELECT CAR_ID,
round(avg(datediff(end_date, start_date) + 1), 1)
AVERAGE_DURATION
from car_rental_company_rental_history
group by car_id
having avg(datediff(end_date, start_date) + 1) >= 7
order by average_duration desc, car_id desc
