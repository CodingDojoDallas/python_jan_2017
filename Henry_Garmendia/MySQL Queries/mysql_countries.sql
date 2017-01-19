
-- 1 - What query would you run to get all the countries that speak Slovene. 
-- Your query should return the name of the country, language and language percentage. 
-- You query should arrange the result by language percentage in descending order.

select countries.name, languages.language, languages.percentage 
from countries
join languages on countries.id = languages.country_id
where languages.language = "Slovene"
order by languages.percentage desc;

select countries.name, languages.language, languages.percentage 
from countries
from countries
left join languages on countries.id = languages.country_id
where languages.language = "Slovene"
order by languages.percentage desc;

-- 2 - What query would you run to display the total number of cities for each country. 
-- Your query should return the name of the country and the total number of cities. 
-- You query should arrange the result by number of cities in descending order.

select countries.name, count(cities.name) 
from countries
join cities on countries.id = cities.country_id
group by countries.name
order by count(cities.name) desc;

select countries.name, count(cities.name) as cities_num 
from countries
left join cities on countries.id = cities.country_id
group by countries.id
order by cities_num desc;

-- 3 - What query would you run to get all the cities in Mexico with a population of greater than 500,000. 
-- Your query should arrange the result by population in descending order.

select cities.name, cities.population 
from cities
join countries on cities.country_id = countries.id
where countries.name = 'Mexico' and cities.population > 500000
order by cities.population desc;

select cities.name, cities.population 
from countries
left join cities on country_id = cities.countries_id
where countries.name = 'Mexico' and cities.population > 500000
order by cities.population desc;

-- 4 - What query would you run to get all language in each country with a percentage greater than 89%. Your query
-- should arrange the result by percentage in descending order.

select countries.name, languages.language, languages.percentage 
from countries
left join languages on countries.id = languages.country_id
where languages.percentage > 89.00 -- I couldn't get it to work like in the image
order by languages.percentage desc;

select countries.name, languages.language, languages.percentage 
from countries
left join languages on countries.id = languages.country_id
where languages.percentage > 89.00
order by languages.percentage desc;

-- 5 - What query would you run to get all the countries with Surface Area below 501 and 
-- Population greater than 100,000.

select countries.name, countries.surface_area, countries.population 
from countries
where 501 < countries.surface_area and countries.population > 1000000;

select countries.name, countries.surface_area, countries.population 
from countries
where countries.surface_area < 501 and countries.population > 1000000;

-- 6 - What query would you run to get all Constitutional Monarchy Countries with a capital greater than 200 and a life
-- expectancy greater than 75 years.

select countries.name, countries.government_form, countries.capital, countries.life_expectancy 
from countries
where countries.government_form = "Constitutional Monarchy" 
and countries.capital > 200 
and countries.life_expectancy > 75;
-- order by substr(name, length(name)-7);

select countries.name, countries.government_form, countries.capital, countries.life_expectancy 
from countries
where countries.government_form = "Constitutional Monarchy" 
and countries.capital > 200 
and countries.life_expectancy > 75;

-- 7 - What query would you run to get all the cities of Argentina inside the Buenos Aires district and have population
-- greater than 500,000. The query should return the Country Name, City Name, District and Population.

select countries.name, cities.name, cities.district, cities.population 
from countries
join cities on countries.id = cities.country_id
where cities.district = "Buenos Aires" 
and cities.population > 500000;

select countries.name, cities.name, cities.district, cities.population 
from countries
left join cities on countries.id = cities.country_id
where countries.name = 'Argentina'
and cities.district = 'Buenos Aires' 
and cities.population > 500000;

-- 8 - What query would you run to summarize the number of countries in each region. The query should display the
-- name of the region and the number of countries. Also, the query should arrange the result by number of
-- countries in descending order.

select countries.region, count(countries.name) 
from countries
group by countries.region
order by count(countries.name) desc;

select countries.region, count(countries.name)  as country_num
from countries
group by countries.region
order by country_num desc;







