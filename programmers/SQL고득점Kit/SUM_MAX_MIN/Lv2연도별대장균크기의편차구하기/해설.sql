-- 코드를 작성해주세요
select year(DIFFERENTIATION_DATE) YEAR, max(SIZE_OF_COLONY) over (partition by year(differentiation_date)) - SIZE_OF_COLONY as YEAR_DEV, ID from ecoli_data
order by year, year_dev
