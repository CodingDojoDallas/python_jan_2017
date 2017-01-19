USE Twitter

SELECT * FROM users

SELECT * FROM users
WHERE last_name = "Bryant"

SELECT * FROM users
WHERE id > 3

SELECT first_name FROM users
WHERE id > 2

SELECT * FROM users
JOIN faves ON  users.id = faves.user_id
WHERE users.id > 2

SELECT * FROM users
LEFT JOIN tweets ON  users.id = tweets.user_id
WHERE users.id = 4