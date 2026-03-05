-- 코드를 작성해주세요
select p.ID, count(c.id) CHILD_COUNT
from ecoli_data p
left join ecoli_data c on p.id = c.parent_id
group by p.id
order by p.id
