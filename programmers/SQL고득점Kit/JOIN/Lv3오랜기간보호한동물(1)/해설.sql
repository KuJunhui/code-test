-- 코드를 입력하세요
SELECT ai.NAME, ai.DATETIME from animal_ins ai
where not exists (
    select 1
    from animal_outs ao
    where ai.animal_id = ao.animal_id
)
order by ai.datetime
limit 3
