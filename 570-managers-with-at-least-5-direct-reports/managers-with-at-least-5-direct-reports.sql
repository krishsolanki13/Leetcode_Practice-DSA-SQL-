# Write your MySQL query statement below
select e1.name
from Employee e1
join Employee e2 on e1.id = e2.managerID
group by e1.id
having count(*)>=5;