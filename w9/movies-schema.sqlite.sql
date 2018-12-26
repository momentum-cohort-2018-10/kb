CREATE TABLE reviews (
    id integer PRIMARY KEY NOT NULL,
    reviewer_id integer NOT NULL,
    movie_id integer NOT NULL,
    score integer NOT NULL
);


CREATE TABLE actors (
    id integer PRIMARY KEY NOT NULL,
    name varchar(100) NOT NULL
);


CREATE TABLE countries (
    id integer PRIMARY KEY NOT NULL,
    code varchar(2) NOT NULL
);

CREATE TABLE genres (
    id integer PRIMARY KEY NOT NULL,
    name varchar(20) NOT NULL
);


CREATE TABLE reviewers (
    id integer PRIMARY KEY NOT NULL,
    username varchar(30) NOT NULL,
    birthdate date NOT NULL,
    country_id integer,
    credits integer DEFAULT 0 NOT NULL
);


CREATE TABLE movie_actors (
    movie_id integer NOT NULL,
    actor_id integer NOT NULL
);


CREATE TABLE movie_genres (
    movie_id integer NOT NULL,
    genre_id integer NOT NULL
);


CREATE TABLE movies (
    id integer PRIMARY KEY NOT NULL,
    title varchar(255) NOT NULL,
    release_date date NOT NULL,
    budget_in_millions numeric(5,2),
    revenue_in_millions numeric(5,2),
    runtime_in_minutes integer,
    average_critic_review numeric(2,1),
    studio_id integer
);

CREATE TABLE studios (
    id integer PRIMARY KEY NOT NULL,
    name varchar(100) NOT NULL
);


