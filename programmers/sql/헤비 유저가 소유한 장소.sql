-- 호스트 아이디가 2번 이상인 행 출력하기

-- v1. 상관 서브쿼리 (효율 낮음)
SELECT * FROM PLACES p1
WHERE 2 <= (select count(*) from PLACES p2 where p1.HOST_ID = p2.HOST_ID)

-- v2. 그룹 (효율 상승)
SELECT * FROM PLACES p1
    WHERE p1.HOST_ID IN 
    (SELECT p2.HOST_ID FROM PLACES p2 GROUP BY p2.HOST_ID HAVING COUNT(p2.HOST_ID) >= 2)