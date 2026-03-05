-- 코드를 입력하세요
SELECT c.CAR_ID from CAR_RENTAL_COMPANY_CAR c
join CAR_RENTAL_COMPANY_RENTAL_HISTORY h
on c.car_id = h.car_id
and h.start_date like '%-10-%'
where c.car_type = '세단'
group by c.car_id
order by c.car_id desc
