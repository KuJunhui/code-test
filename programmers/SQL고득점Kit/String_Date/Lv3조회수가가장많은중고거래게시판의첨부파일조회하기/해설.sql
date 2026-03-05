-- 코드를 입력하세요
SELECT
concat('/home/grep/src/', b.BOARD_ID, '/', f.file_id, f.file_name, f.file_ext)
FILE_PATH
from used_goods_board b
join used_goods_file f on b.board_id = f.board_id
where f.board_id = (
    select b.board_id
    from used_goods_board b
    order by b.views desc
    limit 1
)
order by f.file_id desc
