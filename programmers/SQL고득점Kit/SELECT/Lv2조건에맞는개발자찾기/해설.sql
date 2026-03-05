-- 코드를 작성해주세요
select d.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME from developers d
where d.skill_code & (
    select sum(code) from skillcodes
    where name in ('Python', 'C#')
) > 0
order by d.id
