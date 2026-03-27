select HISTORY_ID, round(DAILY_FEE * DAYS * (1 - (DISCOUNT_RATE / 100.0)), 0) as FEE
from (
    select t.*,
    case
        when p.DISCOUNT_RATE is null then 0
        else p.DISCOUNT_RATE
    end as DISCOUNT_RATE
    from (
        select HISTORY_ID, h.CAR_ID, c.CAR_TYPE, c.DAILY_FEE, DATEDIFF(END_DATE, START_DATE) + 1 as DAYS,
            case
                when DATEDIFF(END_DATE, START_DATE) + 1 >= 90 then '90일 이상'
                when DATEDIFF(END_DATE, START_DATE) + 1 >= 30 then '30일 이상'
                when DATEDIFF(END_DATE, START_DATE) + 1 >= 7 then '7일 이상'
                else null
            end as TYPE
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY h
        join CAR_RENTAL_COMPANY_CAR c on c.CAR_ID = h.CAR_ID
        where c.CAR_TYPE = '트럭'
        ) t
    left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
        on p.DURATION_TYPE = t.TYPE
        and p.CAR_TYPE = t.CAR_TYPE) r
order by 2 desc, 1 desc