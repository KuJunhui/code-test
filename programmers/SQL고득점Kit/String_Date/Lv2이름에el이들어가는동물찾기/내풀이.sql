-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME from animal_ins
where animal_type = 'Dog' and name regexp('el')
order by name
