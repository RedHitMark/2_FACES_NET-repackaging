CREATE TABLE IF NOT EXISTS apk_files (
    sha1_hash VARCHAR(50) NOT NULL,
    file_size INT(16),
    PRIMARY KEY (sha1_hash)
);

CREATE TABLE IF NOT EXISTS entries (
    id int(16) AUTO_INCREMENT,
    title VARCHAR(500),
    description VARCHAR(500),
    original_file VARCHAR(50) NOT NULL,
    hacked_file VARCHAR(50),
    PRIMARY KEY (id),
    FOREIGN KEY (original_file) REFERENCES apk_files(sha1_hash),
    FOREIGN KEY (hacked_file) REFERENCES apk_files(sha1_hash)
);

CREATE TABLE IF NOT EXISTS virusTotalReport (
    id int(11) NOT NULL auto_increment,
    hash_1 varchar(11) NOT NULL,
    resultA varchar(50),
    PRIMARY KEY (id)
);