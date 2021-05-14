CREATE TABLE `city` (
  `id` int(11) NOT NULL,
  `cityName` varchar(30) NOT NULL
);

--
-- Dumping data for table `city`
--

--INSERT INTO `city` (`id`, `cityName`) VALUES
--(1, 'pune'),
--(2, 'apple'),
--(3, 'city c'),
--(4, 'city d'),
--(5, 'city e');

-- --------------------------------------------------------

--
-- Table structure for table `emp`
--

CREATE TABLE `employee` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `score` int(11) NOT NULL
);

--
-- Dumping data for table `emp`
--
--
--INSERT INTO `employee` (`id`, `name`, `cityId`, `score`) VALUES
--(21, 'a', 1, 5),
--(22, 'b', 2, 4),
--(23, 'c', 3, 6),
--(24, 'd', 4, 4),
--(25, 'e', 5, 6),
--(26, 'g', 1, 2),
--(27, 'h', 2, 9),
--(28, 'i', 3, 4),
--(29, 'j', 4, 3),
--(30, 'k', 5, 6);
--
----
---- Indexes for dumped tables
----
--
----
---- Indexes for table `city`
----
--ALTER TABLE `city`
--  ADD PRIMARY KEY (`id`),
--  ADD KEY `id` (`id`);
--
----
---- Indexes for table `emp`
----
--ALTER TABLE `employee`
--  ADD PRIMARY KEY (`id`),
--  ADD KEY `cityId` (`cityId`);
--
----
---- AUTO_INCREMENT for dumped tables
----
--
----
---- AUTO_INCREMENT for table `emp`
----
--ALTER TABLE `employee`
--  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
----
---- Constraints for dumped tables
----
--
----
---- Constraints for table `emp`
----
--ALTER TABLE `employee`
--  ADD CONSTRAINT `emp_ibfk_1` FOREIGN KEY (`cityId`) REFERENCES `city` (`id`);
--
--/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
--/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
--/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
