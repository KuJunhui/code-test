-- 코드를 입력하세요
SELECT ai.ANIMAL_ID, ai.ANIMAL_TYPE, ai.NAME from animal_ins ai
join animal_outs ao on ai.animal_id = ao.animal_id
and ai.sex_upon_intake like 'Intact%' and ao.sex_upon_outcome in ('Spayed Female', 'Neutered Male')
order by ai.animal_id
