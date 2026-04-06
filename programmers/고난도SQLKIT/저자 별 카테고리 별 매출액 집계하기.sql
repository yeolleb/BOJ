-- 저자 별 카테고리 별 매출액 집계하기
select b.AUTHOR_ID, a.AUTHOR_NAME, CATEGORY, sum(price * sales) as TOTAL_SALES
from BOOK b
join AUTHOR a on b.AUTHOR_ID = a.AUTHOR_ID
join BOOK_SALES s on b.BOOK_ID = s.BOOK_ID
where year(s.SALES_DATE) = 2022 and month(s.SALES_DATE) = 1
group by 1, 3
order by 1 asc, 3 desc