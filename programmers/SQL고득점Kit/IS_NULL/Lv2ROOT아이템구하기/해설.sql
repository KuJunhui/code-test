-- 코드를 작성해주세요
select ii.ITEM_ID, ii.ITEM_NAME from item_info ii
join item_tree it on ii.item_id = it.item_id
where it.parent_item_id is null
order by ii.item_id
