--CREATE TABLE `employee` (
--  `id` int(11) NOT NULL,
--  `name` varchar(50) NOT NULL,
--  `city` varchar(50) NOT NULL,
--  `mobile_no` varchar(50) NOT NULL,
--  `nationality` varchar(50) NOT NULL,
--  `salary` int(10) NOT NULL,
--  `designation` varchar(50) NOT NULL,
--  `dependents` int(11) NOT NULL
--);
CREATE TABLE `employee` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `mobile_no` varchar(50) NOT NULL,
  `nationality` varchar(50) NOT NULL,
  `salary` int(10) NOT NULL,
  `designation` varchar(50) NOT NULL,
  `dependents` int(11) NOT NULL
);

CREATE TABLE `city` (
  `id` int(11) NOT NULL,
  `cityName` varchar(30) NOT NULL
) ;

ALTER TABLE `employee`
  ADD CONSTRAINT `fk1` FOREIGN KEY (`cityId`) REFERENCES `city` (`id`);

CREATE TABLE `student` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `mobile_no` varchar(50) NOT NULL,
  `nationality` varchar(50) NOT NULL,
  `marks` int(10) NOT NULL,
  `class` varchar(50) NOT NULL,
  `rank` int(11) NOT NULL
);

CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `names` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `mobile_no` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `postalCode` int(10) NOT NULL,
  `bill_amount` int(10) NOT NULL,
  `payment_mode` int(10) NOT NULL,
  `phone_number` int(10) NOT NULL,
  `items` int(10) NOT NULL,
  `postalCode` int(10) NOT NULL,
);
CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `price` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL,
  `quantity` int(50) NOT NULL
);
ALTER TABLE `customer`
  ADD CONSTRAINT `fk2` FOREIGN KEY (`productId`) REFERENCES `product` (`id`);


CREATE TABLE `book` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `price` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL,
  `rating` varchar(50) NOT NULL,
  `copies_sold` varchar(50) NOT NULL,
  `pages` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL,
  `genre` varchar(50) NOT NULL,
  `writer` varchar(50) NOT NULL,
  `author` varchar(50) NOT NULL,
);



CREATE TABLE `movie` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `release` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL,
  `director` varchar(50) NOT NULL,
  `genre` varchar(50) NOT NULL,
  `release_date` varchar(50) NOT NULL,
  `release_day` varchar(50) NOT NULL,
  `release_year` varchar(50) NOT NULL,
  `release_month` varchar(50) NOT NULL,
  `writer` varchar(50) NOT NULL,
  `rating` varchar(50) NOT NULL,
  `runtime` varchar(50) NOT NULL,
  `duration` varchar(50) NOT NULL,
  `collection` varchar(50) NOT NULL,
  `actor` varchar(50) NOT NULL,
);


CREATE TABLE `restaurant` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `names` varchar(50) NOT NULL,
  `rating` varchar(50) NOT NULL,
  `cuisine` varchar(50) NOT NULL,
  `cuisine_type` varchar(50) NOT NULL,
  `location` varchar(50) NOT NULL,
  `daily_income` varchar(50) NOT NULL,
  `cost` varchar(50) NOT NULL,
  `home_delivery` varchar(50) NOT NULL,
  `average_cost` varchar(50) NOT NULL
);



