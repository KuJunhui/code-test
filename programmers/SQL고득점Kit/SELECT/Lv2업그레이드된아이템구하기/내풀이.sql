-- 코드를 작성해주세요
select i.ITEM_ID, i.ITEM_NAME, i.RARITY from item_info i
join item_tree t on i.item_id = t.item_id
where t.parent_item_id in (
    select i.item_id from item_info i
    where i.rarity = 'RARE'
)
group by i.item_id
order by i.item_id desc
