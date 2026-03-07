-- rc 기준으로 조인해야하고 count 할때는 a 테이블로 해야 0이 나온다. **
with recursive rc as (
    select 0 as h
    
    union all
    
    select h+1 as h
    from rc
    where h < 23
)

select h as HOUR, count(a.DATETIME) as COUNT
from rc
left outer join ANIMAL_OUTS a on rc.h = hour(a.DATETIME)
group by 1
order by 1