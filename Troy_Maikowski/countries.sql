-- #1
SELECT countries.name, languages.language, languages.percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = "Slovene"
ORDER BY languages.percentage DESC;

-- #2
SELECT countries.name, COUNT(cities.name) FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY COUNT(cities.name) DESC;

-- #3
SELECT cities.name, cities.population FROM cities
JOIN countries ON cities.country_id = countries.id
WHERE countries.name = "Mexico" AND cities.population > 500000
ORDER BY cities.population DESC;

-- #4
SELECT languages.language, languages.percentage FROM languages
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

-- #5
SELECT countries.name, countries.surface_area, countries.population FROM countries
WHERE countries.surface_area < 501 AND countries.population > 500000;

-- #6
SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy FROM countries
WHERE countries.government_form = "Constitutional Monarchy" AND countries.capital > 200 AND countries.life_expectancy > 75;

-- #7
SELECT countries.name, cities.district, cities.name, cities.population FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE cities.district = "Buenos Aires" AND cities.population > 500000;

-- #8
SELECT countries.region, COUNT(countries.name) FROM countries
GROUP BY countries.region
ORDER BY COUNT(countries.name) DESC;