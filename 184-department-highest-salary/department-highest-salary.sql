# Write your MySQL query statement below
select d.name as "Department", e.name as "Employee", salary Salary
from Employee e
join Department d on e.departmentId = d.id
where (e.salary, e.departmentId) in (
    select max(salary), departmentId
    from Employee
    group by departmentId
);