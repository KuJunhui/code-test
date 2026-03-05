-- 코드를 입력하세요
SELECT CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS from car_rental_company_car
where options regexp '네비게이션'
order by car_id desc
