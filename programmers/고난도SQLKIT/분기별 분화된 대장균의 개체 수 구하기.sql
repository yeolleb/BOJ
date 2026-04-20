-- 분기별 분화된 대장균의 개체 수 구하기
select
    case
        when month(DIFFERENTIATION_DATE) <= 3 then '1Q'
        when month(DIFFERENTIATION_DATE) <= 6 then '2Q'
        when month(DIFFERENTIATION_DATE) <= 9 then '3Q'
        when month(DIFFERENTIATION_DATE) <= 12 then '4Q'
    end as QUARTER, count(*) as ECOLI_COUNT
from ECOLI_DATA
group by 1
order by 1