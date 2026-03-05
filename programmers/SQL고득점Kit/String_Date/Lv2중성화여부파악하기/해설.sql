-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME,
case when sex_upon_intake regexp('Neutered|Spayed') then 'O' else 'X'
end as 중성화
from animal_ins
order by animal_id
