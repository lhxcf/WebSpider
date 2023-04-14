CREATE TABLE `publicopinionanalysis`.`companyInfo`(
	company VARCHAR(80) NOT NULL,
	title VARCHAR(80) NOT NULL,
	href VARCHAR(160) NOT NULL,
	date DATE NOT NULL,
	source VARCHAR(80) NOT NULL,
	score int NOT NULL,
	PRIMARY KEY(company)
);
CREATE TABLE goods(
	Name VARCHAR(80) NOT NULL PRIMARY KEY,
    Price FLOAT NOT NULL,
    No VARCHAR(20)
)

