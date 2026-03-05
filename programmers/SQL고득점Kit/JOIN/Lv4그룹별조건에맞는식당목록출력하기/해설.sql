-- 코드를 입력하세요
SELECT mp.MEMBER_NAME, rr.REVIEW_TEXT, date_format(rr.REVIEW_DATE, '%Y-%m-%d') REVIEW_DATE from member_profile mp
join rest_review rr on mp.member_id = rr.member_id
join (
    select member_id from rest_review
    group by member_id
    order by count(*) desc
    limit 1
) top
on mp.member_id = top.member_id
order by rr.review_date, rr.review_text
