-- 코드를 작성해주세요
select ID, EMAIL, FIRST_NAME, LAST_NAME from developer_infos
where skill_1 = 'Python' or skill_2 = 'Python' or skill_3 = 'Python'
order by id
