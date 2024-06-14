-- List all bands with Glam rock as their main style, ranked by their longevity

USE holberton;

SELECT 
    name AS band_name,
    CASE
        WHEN split IS NULL THEN 2022 - formed
        ELSE split - formed
    END AS lifespan
FROM 
    metal_bands
WHERE 
    genre = 'Glam rock'
ORDER BY 
    lifespan DESC;
