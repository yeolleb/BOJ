-- 재귀 문법 숙지 **
-- https://thinkcatlog.tistory.com/entry/MySQL-%EC%9E%AC%EA%B7%80-%EC%BF%BC%EB%A6%AC-Recursive-Common-Table-Expressions
with recursive rc as (
    -- 초기 조건
    select ID, 1 as gen
    from ECOLI_DATA
    where PARENT_ID is null
    
    union all

    -- 반복 조건    
    select e.id, gen+1 as gen
    from rc
    join ECOLI_DATA e on rc.id = e.PARENT_ID
)

select ID 
from rc
where gen = 3