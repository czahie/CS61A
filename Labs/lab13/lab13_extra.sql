CREATE TABLE pairs AS
  WITH ints(int) AS (
  SELECT 0 UNION
  SELECT int + 1  FROM ints WHERE int< 42
  )
  SELECT a.int AS x, b.int AS y FROM ints AS a, ints AS b WHERE a.int <= b.int;
