WITH ranked AS (
  SELECT
    id,
    NTILE(4) OVER (ORDER BY size_of_colony DESC) AS q
  FROM ecoli_data
)
SELECT
  id,
  CASE q
    WHEN 1 THEN 'CRITICAL'
    WHEN 2 THEN 'HIGH'
    WHEN 3 THEN 'MEDIUM'
    ELSE 'LOW'
  END AS colony_name
FROM ranked
ORDER BY id;
