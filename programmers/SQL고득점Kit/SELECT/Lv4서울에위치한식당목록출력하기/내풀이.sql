-- 코드를 입력하세요
SELECT r_i.REST_ID, r_i.REST_NAME, r_i.FOOD_TYPE, r_i.FAVORITES, r_i.ADDRESS, round(avg(r_r.REVIEW_SCORE), 2) SCORE from REST_INFO r_i
join REST_REVIEW r_r on r_i.REST_ID = r_r.REST_ID
where r_i.address like '서울%'
group by r_i.REST_ID, r_i.REST_NAME, r_i.FOOD_TYPE, r_i.FAVORITES, r_i.ADDRESS
order by SCORE desc, r_i.FAVORITES desc
