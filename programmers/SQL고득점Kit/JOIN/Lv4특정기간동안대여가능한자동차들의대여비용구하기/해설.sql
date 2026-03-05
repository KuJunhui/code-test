-- 코드를 입력하세요
SELECT c.CAR_ID, c.CAR_TYPE,
floor(c.daily_fee * 30 * (100 - p.discount_rate)/100) FEE from CAR_RENTAL_COMPANY_CAR c
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN p on c.car_type = p.car_type and p.duration_type = '30일 이상'
where c.car_type in ('세단', 'suv')
and not exists(
    select 1
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY h
    where h.car_id = c.car_id
    and h.start_date <= '2022-11-30'
    and h.end_date >= '2022-11-01'
)
and floor(c.daily_fee * 30 * (100 - p.discount_rate)/100) >= 500000
and floor(c.daily_fee * 30 * (100 - p.discount_rate)/100) < 2000000
order by FEE desc, c.car_type, c.car_id desc
