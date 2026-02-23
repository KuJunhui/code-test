-- 코드를 작성해주세요
select fi.ID, fni.FISH_NAME, fi.LENGTH LENGTH from fish_info fi
join (select fish_type, max(length) max_length
     from fish_info
     group by fish_type) mx
on fi.fish_type = mx.fish_type
and fi.length = mx.max_length
join fish_name_info fni
on fi.fish_type = fni.fish_type
order by fi.id
