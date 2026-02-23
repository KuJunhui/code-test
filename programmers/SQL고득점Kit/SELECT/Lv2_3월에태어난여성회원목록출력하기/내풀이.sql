-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') DATE_OF_BIRTH from MEMBER_PROFILE
where date_of_birth like '%-03-%'
and gender = 'W'
and tlno is not null
order by member_id
