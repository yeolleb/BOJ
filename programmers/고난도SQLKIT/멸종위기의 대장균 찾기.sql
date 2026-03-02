with recursive rc as (
    select ID, 1 as GEN, PARENT_ID
    from ECOLI_DATA
    where PARENT_ID is null
    
    union all
    
    select e.ID, GEN+1 as GEN, e.PARENT_ID
    from rc
    join ECOLI_DATA e on e.PARENT_ID = rc.ID
)

-- NOT IN 풀이
select count(ID) as COUNT, GEN as GENERATION
from rc
where ID not in (
    select PARENT_ID
    from ECOLI_DATA
    -- NOT IN을 쓸 때 서브쿼리 결과에 NULL이 하나라도 섞여 있으면 결과가 아무것도 안 나온다.
    where PARENT_ID is not null
)
group by GEN
order by 2


-- LEFT OUTER JOIN 풀이

select count(ID) as COUNT, rc.GEN as GENERATION
from rc
left outer join (
    select GEN, PARENT_ID
    from rc
    group by GEN, PARENT_ID
) T
on rc.ID = T.PARENT_ID
-- LEFT OUTER JOIN은 조건에 안 맞는 걸 걸러내는 게 아니라, 왼쪽 rc에 있는 모든 행을 일단 무조건 다 살려둔다. 
-- 그리고 조건에 맞춰서 오른쪽(T) 데이터를 옆에 갖다 붙이는데, 짝이 없으면 **NULL**로 채워 넣는다.
WHERE T.PARENT_ID IS NULL
group by rc.GEN
order by 2