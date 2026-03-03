select year(sales_date) as YEAR, month(sales_date) as MONTH, 
        count(distinct USER_ID) as PURCHASED_USERS, 
        round(count(distinct USER_ID) / (
            select count(USER_ID)
            from USER_INFO
            where year(JOINED) = 2021)
        , 1) as PUCHASED_RATIO
from (
    select s.*
    from ONLINE_SALE s
    join USER_INFO u on u.USER_ID = s.USER_ID
    where year(u.JOINED) = 2021) t
group by year(sales_date), month(sales_date)
order by 1, 2