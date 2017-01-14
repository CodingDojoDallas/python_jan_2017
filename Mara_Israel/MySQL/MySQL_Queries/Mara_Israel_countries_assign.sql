SELECT * FROM countries
SELECT * FROM cities
SELECT * FROM languages

-- Number 1 --
SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id -- LEFT JOIN
WHERE language = 'slovene'. -- languages.language = 'Slovene'
ORDER BY percentage DESC: -- languages.percentage

-- Number 2 --
SELECT cities.name, COUNT(cities.id) AS cities_num
FROM countries
LEFT JOIN cities ON countries.id = cities.country_id
GROUP BY countries.id
ORDER BY cities_num DESC:

-- Number 3 --
SELECT cities.name, cities.population
FROM cities -- countries
JOIN countries ON countries.id = cities.country_id -- LEFT JOIN cities
WHERE countries.name = 'Mexico' AND cities.population > 500000
ORDER BY cities.population DESC:

-- Number 4--
SELECT countries.name , languages.language, languages.percentage
FROM languages -- countries
JOIN countries ON countries.id = languages.country_id -- left join languages
WHERE languages.percentage > 89
ORDER BY percentage DESC:

-- Number 5 --
SELECT countries.name, countries.surface_area, countries.population 
FROM countries
WHERE countries.surface_area < 501 AND countries.population > 100000:

-- Number 6 --
SELECT countries.name, countries.government_form, countries.capital , countries.life_expectancy 
FROM countries
WHERE countries.government_form = 'Constitutional Monarchy' 
AND countries.capital > 200 
AND countries.life_expectancy > 75:


-- Number 7 --
SELECT countries.name, cities.name , cities.district , cities.population
FROM cities -- countries
JOIN countries ON countries.id = cities.country_id -- left join cities
WHERE countries.name = 'Argentina' 
AND cities.district = 'Buenos Aires' 
AND cities.population > 500000

-- Number 8 --
SELECT countries.region, COUNT(countries.id) AS country_num
FROM countries
GROUP BY countries.region
ORDER BY country_num DESC:



