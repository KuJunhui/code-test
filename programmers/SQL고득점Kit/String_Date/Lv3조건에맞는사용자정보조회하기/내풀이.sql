-- 코드를 입력하세요
SELECT u.USER_ID, u.NICKNAME,
concat(
    u.CITY, ' ',
    u.STREET_ADDRESS1, ' ',
    u.STREET_ADDRESS2)
전체주소,
concat(
    substring(u.tlno, 1, 3), '-',
    substring(u.tlno, 4, 4), '-',
    substring(u.tlno, 8, 4)
)
전화번호
from used_goods_user u
join used_goods_board b on u.user_id = b.writer_id
where (
    select count(*) from used_goods_board b
    where u.user_id = b.writer_id
) >= 3
group by u.user_id
order by u.user_id desc
