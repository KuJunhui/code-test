-- 코드를 작성해주세요
select d.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME from developers d
where (d.skill_code & (select sum(s.code) from skillcodes s
                      where s.category = 'Front End')
      ) > 0
order by d.id
