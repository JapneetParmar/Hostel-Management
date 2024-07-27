-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 16, 2023 at 10:09 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotelmanagement_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `newcustomers`
--

CREATE TABLE `newcustomers` (
  `Name` varchar(25) NOT NULL,
  `Mobile` bigint(20) NOT NULL,
  `E_Mail` varchar(25) NOT NULL,
  `Gender` varchar(15) NOT NULL,
  `Number_of_Members` int(10) NOT NULL,
  `Check_in_Date` date NOT NULL,
  `Check_out_Date` date NOT NULL,
  `Type_of_room` varchar(100) NOT NULL,
  `Allotted_Room_no` int(10) NOT NULL,
  `photo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `newcustomers`
--

INSERT INTO `newcustomers` (`Name`, `Mobile`, `E_Mail`, `Gender`, `Number_of_Members`, `Check_in_Date`, `Check_out_Date`, `Type_of_room`, `Allotted_Room_no`, `photo`) VALUES
('Japneet Singh', 6283243818, 'japneetparmar8@gmail.com', 'male', 1, '2023-08-16', '2023-08-18', 'Luxury Room', 101, '1692162067Id1.jpg'),
('Harmeet SIngh', 7814952314, 'harmeetparmar9@gmail.com', 'male', 2, '2023-08-16', '2023-08-23', 'Luxury Room', 102, '1692162101Id2.png'),
('Manveer Singh', 8965478541, 'manveerparmar13@gmail.com', 'male', 2, '2023-08-16', '2023-08-24', 'Creative Room', 103, '1692162142Id3.jpg'),
('Apoorv Verma', 986541236, 'apoorvverma43@gmail.com', 'male', 1, '2023-08-16', '2023-08-18', 'Lodge Room', 104, '1692162186id4.png'),
('Jaswinder Kaur', 8427466499, 'jaswinderkaur13@gmail.com', 'male', 1, '2023-08-16', '2023-08-25', 'Lodge Room', 106, '1692162227Id2.png'),
('Simran', 8965478563, 'simran8@gmail.com', 'female', 2, '2023-08-16', '2023-08-22', 'Creative Room', 107, '1692162286id4.png');

-- --------------------------------------------------------

--
-- Table structure for table `userdata`
--

CREATE TABLE `userdata` (
  `Name` varchar(25) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `UserType` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userdata`
--

INSERT INTO `userdata` (`Name`, `Password`, `UserType`) VALUES
('priya', '1234', 'Employee'),
('raman', '1234', 'Admin'),
('ria', '4567', 'Employee'),
('rohan', '789', 'Admin'),
('surya', '1289', 'Employee');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `newcustomers`
--
ALTER TABLE `newcustomers`
  ADD PRIMARY KEY (`Allotted_Room_no`);

--
-- Indexes for table `userdata`
--
ALTER TABLE `userdata`
  ADD PRIMARY KEY (`Name`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
