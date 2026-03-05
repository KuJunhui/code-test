-- 코드를 입력하세요
SELECT ao.ANIMAL_ID, ao.NAME from animal_outs ao
left join animal_ins ai
on ao.animal_id = ai.animal_id
where ai.animal_id is null
order by ao.animal_id
