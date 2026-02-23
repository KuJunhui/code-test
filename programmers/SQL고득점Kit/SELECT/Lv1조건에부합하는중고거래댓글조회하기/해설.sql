-- 코드를 입력하세요
SELECT ugb.TITLE, ugb.BOARD_ID, ugr.REPLY_ID, ugr.WRITER_ID, ugr.CONTENTS, DATE_FORMAT(ugr.CREATED_DATE, '%Y-%m-%d') CREATED_DATE from USED_GOODS_BOARD ugb
join USED_GOODS_REPLY ugr on ugb.BOARD_ID = ugr.BOARD_ID
where ugb.CREATED_DATE like '2022-10%'
order by ugr.CREATED_DATE, ugb.TITLE
