SELECT 
    s.user_id,
    CASE 
        WHEN COUNT(c.action) > 0 THEN 
            ROUND(SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) / COUNT(c.action), 2)
        ELSE 0
    END AS confirmation_rate
FROM 
    Signups s
LEFT JOIN 
    Confirmations c
ON 
    s.user_id = c.user_id
GROUP BY 
    s.user_id;
