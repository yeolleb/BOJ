-- 그냥 출력하면 TIME STAMP 형태로 출력된다...
-- DATE_FORMAT
-- %Y	4자리 연도	2023
-- %y	2자리 연도	23
-- %m	2자리 월	05
-- %d	2자리 일	09
-- %H	24시간 형식	14
-- %i	분	20
-- %s	초
SELECT b.BOOK_ID, a.AUTHOR_NAME, DATE_FORMAT(b.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK b
JOIN AUTHOR a ON b.AUTHOR_ID = a.AUTHOR_ID
WHERE b.CATEGORY = '경제'
ORDER BY 3