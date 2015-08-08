CREATE TABLE category (
    id integer PRIMARY KEY,
    name varchar(255)
);

CREATE TABLE priority (
    id integer PRIMARY KEY,
    name varchar(255),
    value integer
);

CREATE TABLE todo (
    id integer PRIMARY KEY,
    category_id integer REFERENCES category (id),
    priority_id integer REFERENCES priority (id),
    description varchar(255),
    creation_date date,
    is_done boolean
);
