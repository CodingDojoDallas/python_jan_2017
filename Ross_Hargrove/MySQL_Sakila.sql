-- 1.
SELECT address.city_id, customer.first_name, customer.last_name, customer.email, address.address FROM customer
JOIN address ON customer.address_id = address.address_id
WHERE city_id = 312

-- 2.
SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = "comedy"

-- 3.
SELECT actor.actor_id, CONCAT(actor.first_name," ",actor.last_name) as actor_name, film.film_id, film.title, film.description, film.release_year FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
WHERE actor.actor_id = 5

-- 4.
SELECT store.store_id, city.city_id, customer.first_name, customer.last_name, customer.email, address.address FROM customer
JOIN address ON customer.address_id = address.address_id
JOIN store ON customer.store_id = store.store_id
JOIN city on address.city_id = city.city_id
WHERE store.store_id = 1 AND (city.city_id = 1 OR city.city_id = 42 OR city.city_id = 312 OR city.city_id = 459)

-- 5.
SELECT film.title, film.description, film.release_year, film.rating, film.special_features FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.rating = "G" AND film.special_features LIKE "%behind the scenes" AND actor.actor_id = 15

-- 6.
SELECT film.film_id, film.title, actor.actor_id, CONCAT(actor.first_name," ",actor.last_name) AS actor_name, actor.last_update  FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369

-- 7.
SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, film.rental_rate FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE film.rental_rate = 2.99 AND category.name = "drama"

-- 8.
SELECT actor.actor_id, CONCAT(actor.first_name," ",actor.last_name), film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = "action" AND actor.first_name = "SANDRA" AND actor.last_name = "KILMER"