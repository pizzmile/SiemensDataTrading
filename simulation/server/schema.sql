create table device
(
    idDevice    INT(10) auto_increment
        primary key,
    name        VARCHAR(45)  not null,
    description VARCHAR(256) not null
);

create table processedWork
(
    idprocessedWorks INT(10) auto_increment
        primary key,
    timestamp        TIMESTAMP(19) not null,
    duration         INT(10)       not null,
    defective        TINYINT(3)    not null,
    success          TINYINT(3)    not null,
    idDevice         INT(10)       not null,
    constraint generatedBy
        foreign key (idDevice) references device (idDevice)
);

create index generatedBy_idx
    on processedWork (idDevice);

create table user
(
    iduser   INT(10) auto_increment
        primary key,
    username VARCHAR(45) not null,
    password VARCHAR(45) not null
);

