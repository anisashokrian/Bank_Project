-- open_account: (id, name, password, cash_deposit)
create table if not exists open_account(
    id integer not null,
    name text not null,
    password text not null,
    cash_deposit integer not null
);

-- deposit: (id, cash)
create table if not exists deposits(
    id integer not null,
    cash integer not null
);

-- withdraw: (id, cash, password)
create table if not exists withdraw(
    id integer not null,
    cash integer not null,
    password text not null
);
