drop table Events;
create table Events(
    id  integer primary key,
    user_id integer,
    text text,
    time datetime
)