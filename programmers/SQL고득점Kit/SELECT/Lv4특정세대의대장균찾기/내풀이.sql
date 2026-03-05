-- 코드를 작성해주세요
select c.ID from ecoli_data gp
left join ecoli_data p on p.parent_id = gp.id and gp.parent_id is null
left join ecoli_data c on c.parent_id = p.id
where c.id is not null
order by c.id
