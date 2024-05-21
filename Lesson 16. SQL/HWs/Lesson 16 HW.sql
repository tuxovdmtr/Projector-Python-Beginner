CREATE TABLE users (
    user_id serial PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    user_type VARCHAR(50) NOT NULL
);

INSERT INTO users (user_name, email, password, user_type) VALUES
('John', 'john1@email.com', 'qwerty123', 'Guest'),
('Adam', 'adam4ever1@email.com', 'hackme', 'Host'),
('Elen', 'elentoheaven@email.com', 'jHVGAUSD2345__', 'Guest');


CREATE TABLE rooms (
    room_id serial PRIMARY KEY,
    user_id INT NOT NULL,
    amount_of_residents INT NOT NULL,
    price_per_day FLOAT NOT NULL,
    air_conditione BOOL NOT NULL,
    refrigerator BOOL NOT NULL,
    tv BOOL NOT NULL,
    pets BOOL NOT NULL,

	FOREIGN KEY (user_id) REFERENCES users (user_id)
);

INSERT INTO rooms (user_id, amount_of_residents, price_per_day, air_conditione, refrigerator, tv, pets)
VALUES 
    (1, 2, 1000, True, True, False, False),
    (2, 1, 700, False, False, True, False),
    (1, 5, 7000, True, True, True, True),
    (3, 3, 800, True, False, False, True);

CREATE TABLE reservations (
    reservation_id serial PRIMARY KEY,
    room_id INT NOT NULL,
    user_id INT NOT NULL,
    first_day DATE NOT NULL,
    last_day DATE NOT NULL,
    total_price FLOAT NOT NULL,

	FOREIGN KEY (room_id) REFERENCES rooms (room_id),
	FOREIGN KEY (user_id) REFERENCES users (user_id)
);

INSERT INTO reservations (room_id, user_id, first_day, last_day, total_price) 
VALUES 
    (3, 1, '2024-05-15', '2024-05-16', 2000),
    (4, 3, '2024-05-11', '2024-05-13', 1400),
    (3, 3, '2024-04-25', '2024-04-27', 2000);

CREATE TABLE payments (
    transaction_id serial PRIMARY KEY,
    reservation_id INT NOT NULL,
    user_id INT NOT NULL,
    payment_method VARCHAR(50) NULL,
    payment_account VARCHAR(50) NULL,
    payment_date TIMESTAMP NOT NULL,

	FOREIGN KEY (reservation_id) REFERENCES reservations (reservation_id),
	FOREIGN KEY (user_id) REFERENCES users (user_id)
);

INSERT INTO payments (reservation_id, user_id, payment_method, payment_account, payment_date) 
VALUES 
    (4, 1, 'Card', '1111 2222 3333 4444', '2024-05-15 20:15:39'),
    (5, 3, 'PayPal', 'elentoheaven@email.com', '2024-05-09 15:37:11'),
    (6, 3, 'Card', '4444 3333 2222 1111', '2024-04-25 01:11:11');


CREATE TABLE reviews (
    review_id serial PRIMARY KEY,
    room_id INT NOT NULL,
    user_id INT NOT NULL,
    user_name VARCHAR(50) NOT NULL,
    rating INT NOT NULL,
    FOREIGN KEY (room_id) REFERENCES rooms (room_id),
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);

INSERT INTO reviews (room_id, user_id, user_name, rating)
VALUES
    (3, 1, 'John', 5),
    (6, 3, 'Elen', 4);


SELECT users.user_name, users.user_id 
FROM users
RIGHT JOIN
    (
    SELECT reservations.user_id, COUNT(*) as reserv_num
    FROM reservations
    GROUP BY user_id 
    ORDER BY reserv_num DESC
    LIMIT 1
    )
as reserv_max
on users.user_id = reserv_max.user_id;
