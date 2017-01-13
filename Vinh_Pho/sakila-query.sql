#1
select cu.first_name, 
	   cu.last_name,
       cu.email,
       a.phone,
       a.address,
       a.address2,
       a.postal_code,
       ci.city,
       ci.city_id
from customer as cu
join address as a
on a.address_id = cu.address_id
join city as ci
on ci.city_id = a.city_id
where ci.city_id=312
order by cu.first_name;

#2
select f.title,
	   f.description,
       f.release_year,
       f.rating,
       f.special_features,
       c.name
from film as f
join film_category as fc
on f.film_id=fc.film_id
join category as c
on fc.category_id=c.category_id
where c.name = 'Comedy';

#3
select f.title,
	   f.description,
       f.release_year
from film as f
join film_actor as fa
on f.film_id=fa.film_id
join actor as a
on fa.actor_id=a.actor_id
where a.actor_id=5
order by f.title;

#4
select 
	   ci.city,
       ci.city_id,
	   cu.first_name,
	   cu.last_name,
       cu.email,
       a.address,
       s.store_id
from customer as cu
join address as a
on cu.address_id = a.address_id
join city as ci
on ci.city_id=a.city_id
join store as s
on cu.store_id=s.store_id
where s.store_id=1
and ci.city_id in (select city_id from city where city_id in (1,42,312,459))
order by ci.city_id;

#5
select f.title,
	   f.description,
       f.release_year,
       f.rating,
       f.special_features,
       a.actor_id
from film as f
join film_actor as fa
on f.film_id=fa.film_id
join actor as a
on fa.actor_id=a.actor_id
where f.rating='G'
and f.special_features like '%behind the scenes%'
and a.actor_id=15
order by f.title;

#6
select f.film_id,
	   f.title,
       a.actor_id,
	   a.first_name,
       a.last_name
from film as f
join film_actor as fa
on f.film_id=fa.film_id
join actor as a
on fa.actor_id=a.actor_id
where f.film_id=369;

#7
select f.title,
	   f.description,
       f.release_year,
       f.rating,
       f.special_features,
       f.rental_rate,
       c.name
from film as f
join film_category as fc
on f.film_id = fc.film_id
join category as c
on fc.category_id = c.category_id
where f.rental_rate ='2.99'
and c.name = 'Drama';

#8
select f.title,
	   f.description,
       f.release_year,
       f.rating,
       f.special_features,
       c.name,
       a.first_name,
       a.last_name
from film as f
join film_category as fc
on f.film_id=fc.film_id
join category as c
on fc.category_id=c.category_id
join film_actor as fa
on f.film_id=fa.film_id
join actor as a
on fa.actor_id=a.actor_id
where a.first_name='SANDRA'
and a.last_name='KILMER'
and c.name='Action'
order by f.title;