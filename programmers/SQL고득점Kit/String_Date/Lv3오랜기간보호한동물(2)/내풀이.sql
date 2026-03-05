-- 코드를 입력하세요
SELECT i.ANIMAL_ID, i.NAME from animal_ins i
join animal_outs o on o.animal_id = i.animal_id
order by datediff(o.datetime, i.datetime) desc
limit 2
