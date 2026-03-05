-- 코드를 입력하세요
SELECT hour(datetime) HOUR, count(*) COUNT from animal_outs
where hour(datetime) >= 9 and hour(datetime) <= 19
group by hour(datetime)
order by hour(datetime)
