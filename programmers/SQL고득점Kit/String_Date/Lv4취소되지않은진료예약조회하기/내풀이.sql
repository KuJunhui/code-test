-- 코드를 입력하세요
SELECT a.APNT_NO, p.PT_NAME, p.PT_NO, a.MCDP_CD, d.DR_NAME, a.APNT_YMD from appointment a
join patient p on a.pt_no = p.pt_no
join doctor d on d.DR_ID = a.MDDR_ID
where date_format(a.apnt_ymd, '%Y-%m-%d') = date('2022-04-13')
and a.apnt_cncl_yn = 'N' and a.mcdp_cd = 'CS'
order by a.apnt_ymd
