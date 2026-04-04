-- 262
-- 클라이언트나 드라이버 중 밴이 안당한 사람들 중에서 날짜별 취소율 구하기
select request_at as Day, round(count(if(status like 'cancelled%', 1, NULL)) / count(*), 2) as 'Cancellation Rate'
from Trips t
join Users uc on uc.role = 'client' and t.client_id = uc.users_id
join Users ud on ud.role = 'driver' and t.driver_id = ud.users_id
where uc.banned = 'No' and ud.banned = 'No'
    and request_at between '2013-10-01' and '2013-10-03'
group by day(request_at)
order by request_at