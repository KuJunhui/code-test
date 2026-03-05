-- 코드를 작성해주세요
select sum(hrg.SCORE) SCORE, hre.EMP_NO, hre.EMP_NAME, hre.POSITION, hre.EMAIL from hr_employees hre
join hr_grade hrg on hre.emp_no = hrg.emp_no
group by hre.EMP_NO
order by sum(hrg.SCORE) desc
limit 1
