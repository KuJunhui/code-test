WITH RECURSIVE gen AS (
    -- 1세대: 최초 개체
    SELECT
        id,
        parent_id,
        1 AS generation
    FROM ecoli_data
    WHERE parent_id IS NULL

    UNION ALL

    -- 다음 세대들
    SELECT
        e.id,
        e.parent_id,
        g.generation + 1 AS generation
    FROM ecoli_data e
    JOIN gen g
      ON e.parent_id = g.id
),
leaf AS (
    -- 자식이 없는 개체(= 어떤 row의 parent_id로도 등장하지 않는 id)
    SELECT g.*
    FROM gen g
    LEFT JOIN ecoli_data c
      ON c.parent_id = g.id
    WHERE c.id IS NULL
)
SELECT
    COUNT(*) AS COUNT,
    generation AS GENERATION
FROM leaf
GROUP BY generation
ORDER BY generation;
