-- Number 1 --
SELECT city.city_id, city.city,  customer.first_name, customer.last_name, customer.email , address.address
FROM city
LEFT JOIN address ON city.city_id = address.city_id
JOIN customer ON address.city_id = customer.address_id
WHERE city.city_id = 312

-- Number 2 --
SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS 'genre'
FROM film_category
LEFT JOIN film ON film_category.film_id = film.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name ='Comedy'

-- Number 3 --
SELECT actor.actor_id, CONCAT(actor.first_name,' ', actor.last_name) AS actor_name, film.film_id, film.title, film.description, film.release_year
FROM film_actor
LEFT JOIN film ON film_actor.film_id = film.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 5

-- Number 4 --
SELECT  store.store_id, city.city_id, customer.first_name, customer.last_name, customer.email , address.address
FROM address
LEFT JOIN city ON address.city_id = city.city_id
JOIN customer ON address.address_id = customer.address_id
LEFT JOIN store ON customer.store_id = store.store_id
WHERE (city.city_id = 1 OR city.city_id = 42 OR city.city_id = 312 OR city.city_id = 459)
AND store.store_id = 1

-- Number 5 --
SELECT film.title, film.description, film.release_year, film.rating, film.special_features
FROM film_actor
LEFT JOIN film ON film_actor.film_id = film.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.special_features LIKE '%Behind%'
AND actor.actor_id = 15
AND film.rating = 'G'

-- Number 6 --
SELECT film.film_id, film.title, actor.actor_id, CONCAT(actor.first_name,' ', actor.last_name) AS actor_name
FROM film_actor
LEFT JOIN film ON film_actor.film_id = film.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369

-- Number 7 --
SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS 'genre', film.rental_rate
FROM film_category
LEFT JOIN film ON film_category.film_id = film.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name ='Drama'
AND  film.rental_rate = 2.99

-- Number 8 --
SELECT actor.actor_id, CONCAT(actor.first_name,' ', actor.last_name) AS actor_name, film.title, film.description, film.release_year, film.rating, category.name AS 'genre'
FROM film
LEFT JOIN film_actor ON film_actor.film_id = film.film_id
LEFT JOIN actor ON actor.actor_id = film_actor.actor_id
LEFT JOIN film_category ON film_category.film_id = film.film_id
LEFT JOIN category ON category.category_id = film_category.category_id
WHERE actor.first_name = 'SANDRA'
AND actor.last_name = 'KILMER'
AND category.name = 'Action'

-- using four left joins parses the information without the information having to have a value






