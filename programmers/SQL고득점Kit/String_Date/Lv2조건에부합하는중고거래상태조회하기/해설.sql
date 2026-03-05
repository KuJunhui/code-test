-- 코드를 입력하세요
SELECT b.BOARD_ID, b.WRITER_ID, b.TITLE, b.PRICE,
case
    when b.status = 'SALE' then '판매중'
    when b.status = 'RESERVED' then '예약중'
    when b.status = 'DONE' then '거래완료'
end as STATUS
from used_goods_board b
where b.created_date = '2022-10-05'
order by b.board_id desc
