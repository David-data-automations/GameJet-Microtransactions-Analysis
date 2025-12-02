-- SEGMENTATION: Creates user personas based on total revenue spent.
-- Used as the base CTE for subsequent analytical tasks.

SELECT
    A.udid,
    SUM(b.rev) AS total_spent_cents,
    CASE
        WHEN SUM(b.rev) IS NULL OR SUM(b.rev) = 0 THEN 'free_player'
        WHEN SUM(b.rev) < 2000 THEN 'minnow'
        WHEN SUM(b.rev) < 10000 THEN 'dolphin'
        ELSE 'whale'
    END AS persona
FROM
    game_jet.users AS a
LEFT JOIN
    game_jet.iaps AS b ON a.udid = b.udid
GROUP BY
    a.udid
ORDER BY
    total_spent_cents DESC;
