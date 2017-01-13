select countries.name,languages.percentage,languages.language 
from countries
join languages
on countries.id=languages.country_id
where languages.language='Slovene'
order by languages.percentage;

select countries.name,sum(cities.id)as Total_Cities from cities
join countries
ON cities.country_id=countries.id
group by countries.id
order by Total_Cities;

select countries.name,cities.country_id, cities.name,cities.population
from cities
join countries
on cities.country_id=countries.id
where countries.name='Mexico'
and cities.population > 500000
order by cities.population;

select countries.name,languages.percentage,languages.language 
from countries
join languages
on countries.id=languages.country_id
where languages.percentage >89
order by languages.percentage;

select name from countries
where population > 100000
and surface_area < 501;

select name, life_expectancy from countries
where government_form like '%Monarchy'
and life_expectancy > 75
and capital > 200;

select countries.name,cities.name,cities.district,format(cities.population,0) as population from cities
join countries
on cities.country_code = countries.code
where cities.district like '%Aires'
and cities.population > 500000;

select region,count(region) as total from countries 
where region in(select distinct region from countries)
group by region
order by region;


