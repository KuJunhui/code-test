-- 코드를 작성해주세요
select c.ID, c.GENOTYPE, p.GENOTYPE PARENT_GENOTYPE from ecoli_data p
left join ecoli_data c on c.parent_id = p.id
where c.genotype & p.genotype = p.genotype
order by c.id
