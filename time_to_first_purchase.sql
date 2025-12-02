-- ENGAGEMENT: Calculates time between install and first purchase.

WITH first_purchase AS (
    SELECT
        a.udid,
        MIN(b.date - a.install_date) AS days_to_first_purchase
    FROM
        game_jet.users a
    JOIN
        game_jet.iaps b ON a.udid = b.udid
    GROUP BY
        a.udid
)
SELECT
    CASE
        WHEN days_to_first_purchase = 0 THEN 'Day_0_First_Purchase'
        WHEN days_to_first_purchase BETWEEN 1 AND 6 THEN 'Day_1-6_Early_Purchase'
        WHEN days_to_first_purchase BETWEEN 7 AND 13 THEN 'Days_7-13'
        WHEN days_to_first_purchase BETWEEN 14 AND 20 THEN 'Days_14-20'
        WHEN days_to_first_purchase BETWEEN 21 AND 27 THEN 'Days_21-27'
        ELSE 'Day_28_and_Beyond'
    END AS purchase_timing_bucket,
    COUNT(*) AS purchasers
FROM
    first_purchase
GROUP BY
    purchase_timing_bucket
ORDER BY
    purchasers DESC;
