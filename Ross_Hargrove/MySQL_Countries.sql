-- 1.
SELECT countries.name, languages.language, languages.percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = "Slovene"
ORDER BY languages.percentage DESC

-- 2.
SELECT countries.name, COUNT(cities.name) FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY COUNT(cities.name) DESC

-- 3.
SELECT cities.population, cities.name FROM cities
JOIN countries ON cities.country_id = countries.id
WHERE cities.population > 500000 AND countries.name = "Mexico"
ORDER BY cities.population DESC

-- 4.
SELECT countries.name, languages.language, languages.percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC

-- 5.
SELECT name, surface_area, population FROM countries
WHERE surface_area < 501 AND population > 100000

-- 6.
SELECT name, government_form, capital, life_expectancy FROM countries
WHERE government_form = "Constitutional Monarchy" AND capital > 200 AND life_expectancy > 75

-- 7.
SELECT countries.name, cities.name, cities.district, cities.population FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = "Argentina" AND cities.district = "Buenos Aires" AND cities.population > 500000

-- 8.
SELECT region, COUNT(name) FROM countries
GROUP BY region
ORDER BY COUNT(name) DESC