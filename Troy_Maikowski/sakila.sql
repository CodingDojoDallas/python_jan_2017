Use sakila;

-- #1
SELECT customer.first_name, customer.last_name, customer.email, address.address, address.city_id FROM customer
JOIN address ON customer.address_id = address.address_id
WHERE city_id = 312;

-- #2
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = "Comedy";

-- #3
SELECT film.title, film.description, film.release_year FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 5;

-- #4
SELECT customer.first_name, customer.last_name, customer.email, address.address FROM customer
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
WHERE customer.store_id = 1 AND city.city_id IN (1, 42, 312, 459);

-- #5
SELECT film.title, film.description, film.release_year, film.rating, film.special_features FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.rating = 'G' AND film.special_features LIKE '%behind the scenes%' AND actor.actor_id = 15;

-- #6
SELECT film.film_id, film.title, actor.actor_id, CONCAT_WS(' ', actor.first_name, actor.last_name) AS actor_name FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;

-- #7
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
JOIN payment ON rental.rental_id = payment.rental_id
WHERE payment.amount = 2.99;

-- #8
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE CONCAT_WS(' ', actor.first_name, actor.last_name) = "SANDRA KILMER";
