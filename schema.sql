drop table if exists products;
create table products (
  id integer primary key autoincrement,
  title text not null,
  text text not null
);
