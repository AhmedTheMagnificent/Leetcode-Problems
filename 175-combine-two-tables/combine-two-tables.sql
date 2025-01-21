# Write your MySQL query statement below
select f.firstName, f.lastName, s.city, s.state 
from Person as f 
left join Address as s
on f.personId = s.personId;