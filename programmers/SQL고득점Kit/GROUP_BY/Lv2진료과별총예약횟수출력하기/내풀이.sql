-- 코드를 입력하세요
SELECT MCDP_CD '진료과코드', count(pt_no) '5월예약건수' from appointment
where APNT_YMD like '2022-05%'
group by mcdp_cd
order by count(pt_no), mcdp_cd

-- 1 2 3 4 5