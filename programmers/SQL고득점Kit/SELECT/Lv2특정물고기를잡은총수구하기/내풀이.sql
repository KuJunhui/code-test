-- 코드를 작성해주세요
select count(*) FISH_COUNT from fish_info f
join fish_name_info i on f.fish_type = i.fish_type
and i.fish_name in ('BASS', 'SNAPPER')
