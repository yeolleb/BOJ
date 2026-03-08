-- 185
-- top 3 연봉자 뽑는데 같은 연봉인 사람들 다 하나로 취급
select Department, Employee, Salary
from (select d.name as Department, e.name as Employee, e.salary as Salary, 
    dense_rank() over (PARTITION BY e.departmentId order by salary desc) as rnk
    from Employee e
    join Department d on d.id = e.departmentId) t
where rnk <= 3