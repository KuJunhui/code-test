-- 코드를 입력하세요
SELECT b.BOOK_ID, a.AUTHOR_NAME, date_format(b.published_date, '%Y-%m-%d') PUBLISHED_DATE from book b
join author a on b.author_id = a.author_id
where b.category = '경제'
order by b.published_date
