-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 19, 2018 at 09:59 AM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `onlineattendance`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `email` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `type` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`email`, `password`, `mobile`, `type`) VALUES
('amit@gmail.com', '123', '987', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `attendancetable`
--

CREATE TABLE `attendancetable` (
  `id` int(11) NOT NULL,
  `sid` int(11) NOT NULL,
  `course` varchar(100) NOT NULL,
  `semester` int(11) NOT NULL,
  `date1` date NOT NULL,
  `subjectid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `attendancetable`
--

INSERT INTO `attendancetable` (`id`, `sid`, `course`, `semester`, `date1`, `subjectid`) VALUES
(1, 2, 'bba', 2, '2018-07-18', 2),
(2, 2, 'bba', 2, '2018-07-18', 2),
(3, 2, 'Btech_IT', 1, '2018-07-19', 5),
(4, 2, 'Btech_IT', 1, '2018-07-19', 5),
(5, 4, 'Btech_IT', 1, '2018-07-19', 5),
(6, 5, 'Btech_IT', 1, '2018-07-19', 5);

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE `courses` (
  `coursename` varchar(100) NOT NULL,
  `duration` varchar(20) NOT NULL,
  `description` text NOT NULL,
  `department` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`coursename`, `duration`, `description`, `department`) VALUES
('BCA', '3 Year', 'BCA course', 'Computer_Science'),
('BSC_Agriculture', '3 Year', 'Agri Dept', 'Agriculture'),
('Btech_cse', '4 year', 'cse course', 'Computer_Scince'),
('Btech_IT', '4 year', 'IT course', 'Information_Technology'),
('Btech_ME', '4 year', 'ME course', 'Mechanical'),
('Hotel_Management', '4 year', 'HM', 'Management');

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `deptname` varchar(33) NOT NULL,
  `hodname` varchar(33) NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`deptname`, `hodname`, `description`) VALUES
('Agriculture', 'Ramandeep_Kaur', 'ARG Dept'),
('Civil', 'Harmanjeet_singh', 'Civil dept'),
('Computer_Science', 'Gurpreet_singh', 'Computer Science dept'),
('Electrical', 'Rakesh_Gupta', 'Electrical dept'),
('Information_Technology', 'Amit_Kumar', 'IT dept'),
('Management', 'Harmanjeet_singh', 'Manage'),
('Mechanical', 'Rohit_Sharma', 'Mechanical dept');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `studentid` int(11) NOT NULL,
  `rollno` varchar(10) NOT NULL,
  `studentname` varchar(100) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `course` varchar(100) NOT NULL,
  `semester` int(11) NOT NULL,
  `mobileno` varchar(20) NOT NULL,
  `address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `pmobileno` varchar(100) NOT NULL,
  `paddress` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`studentid`, `rollno`, `studentname`, `fname`, `gender`, `course`, `semester`, `mobileno`, `address`, `email`, `pmobileno`, `paddress`) VALUES
(2, '1', 'Karamjit_singh', 'Sarabjit_singh', 'Male', 'Btech_IT', 1, '9501559169', 'batala', 'karam@gmail.com', '123', 'batala'),
(3, '3', 'Gurman_singh', 'Harmanjeet_singh', 'Male', 'Btech_IT', 1, '9348765035', 'guru nanak nagar ,batala', 'gurman@gmail.com', '9750034658', 'guru nanak nagar ,batala'),
(4, '4', 'Arpanjot_Singh', 'Hardeep_Singh', 'Male', 'Btech_IT', 1, '7307527466', 'GT  Road ,Amritsar', 'Arpan@gmail.com', '9501559169', 'GT Road ,Amritsar'),
(5, '5', 'Amit_Kumar', 'Ramesh_Kumar', 'Male', 'Btech_IT', 1, '7307527466', 'Hall Gate  Road ,Amritsar', 'Amit@gmail.com', '9501559169', 'Hall Gate Road ,Amritsar'),
(6, '6', 'Jadeep_Kumar', 'Ramesh_Kumar', 'Male', 'Btech_cse', 4, '7307527466', 'Maharaja Road ,Amritsar', 'jadeep@gmail.com', '9501559169', 'Maharaja Road ,Amritsar'),
(7, '8', 'Diljeet_Singh', 'Harmeet_Singh', 'Male', 'Btech_cse', 4, '7307527466', 'Simble Chowk ,Amritsar', 'diljeet@gmail.com', '9501559169', 'Simble Chowk ,Amritsar'),
(8, '9', 'Rahul_Kumar', 'Sunil_Kumar', 'Male', 'Btech_cse', 4, '7307527466', 'Simble Chowk ,Amritsar', 'rahul@gmail.com', '9501559169', 'Simble Chowk ,Amritsar'),
(9, '10', 'Jignesh_Verma', 'Sunil_Verma', 'Male', 'Btech_cse', 4, '7307527466', 'Model Town ,Batala', 'jignesh@gmail.com', '9501559169', 'Model Town ,Batala'),
(10, '11', 'Aisha_Shetty', 'Sunil_Shetty', 'Female', 'Btech_ME', 5, '9501559169', 'Model Town ,Amritsar', 'Aisha@gmail.com', '7307527466', 'Model Town ,Amritsar'),
(11, '12', 'Amisha_Raina', 'Ambar_Raina', 'Female', 'Btech_ME', 5, '9501559169', 'Model Town ,Amritsar', 'amisha@gmail.com', '7307527466', 'Model Town ,Amritsar'),
(12, '13', 'Simranjeet_Kaur', 'Karamjit_Singh', 'Female', 'BCA', 2, '9501559169', 'Karuna Nagar ,Amritsar', 'simran@gmail.com', '7307527466', 'Karuna Nagar ,Amritsar'),
(13, '14', 'Manpreet_Kaur', 'Karamjit_Singh', 'Female', 'BCA', 2, '9501559169', 'Armaan Nagar ,Amritsar', 'manpret@gmail.com', '7307527466', 'Armaan Nagar ,Amritsar');

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE `subject` (
  `sid` int(11) NOT NULL,
  `sname` varchar(100) NOT NULL,
  `description` text NOT NULL,
  `tid` int(100) NOT NULL,
  `cname` varchar(100) NOT NULL,
  `semester` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `subject`
--

INSERT INTO `subject` (`sid`, `sname`, `description`, `tid`, `cname`, `semester`) VALUES
(1, 'Engg_Chemistry', 'Chemistry\n', 13, 'Btech_cse', 4),
(2, 'OOPS', 'OPS\n', 12, 'BCA', 2),
(3, 'Boi_Potney', 'Agri\n', 16, 'BSC_Agriculture', 4),
(4, 'EME', 'EME\n', 15, 'Btech_ME', 5),
(5, 'Engg_Phy', 'Physics\n', 14, 'Btech_IT', 1);

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `tid` int(11) NOT NULL,
  `tname` varchar(100) NOT NULL,
  `mobileno` varchar(20) NOT NULL,
  `address` varchar(100) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `qualification` varchar(100) NOT NULL,
  `experience` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`tid`, `tname`, `mobileno`, `address`, `gender`, `qualification`, `experience`, `email`, `password`) VALUES
(12, 'Gopi_Singh', '9501559169', 'batala', 'Male', 'M.tech', '10 year', 'gopi@gmail.com', 'gopi'),
(13, 'Ramandeep_Kaur', '9115859979', 'batala', 'Female', 'B.tech', '2 year', 'raman@gmail.com', 'raman'),
(14, 'Rohit_Sharma', '8360659198', 'batala', 'Male', 'BCA', '2 year', 'rohit@gmail.com', 'rohit'),
(15, 'Karamjit_Singh', '9501559169', 'Power Colony ,Batala', 'Male', 'M.tech', '2 year', 'karam@gmail.com', 'karam'),
(16, 'Harmandeep_Singh', '7307527466', 'Queen Road ,Amritsar', 'Male', 'MCA', '3 year', 'Harman@gmail.com', 'harman');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `attendancetable`
--
ALTER TABLE `attendancetable`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`coursename`),
  ADD KEY `department` (`department`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`deptname`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`studentid`),
  ADD KEY `course` (`course`);

--
-- Indexes for table `subject`
--
ALTER TABLE `subject`
  ADD PRIMARY KEY (`sid`),
  ADD KEY `tid` (`tid`),
  ADD KEY `cname` (`cname`);

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`tid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attendancetable`
--
ALTER TABLE `attendancetable`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `studentid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `subject`
--
ALTER TABLE `subject`
  MODIFY `sid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `teacher`
--
ALTER TABLE `teacher`
  MODIFY `tid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_ibfk_1` FOREIGN KEY (`course`) REFERENCES `courses` (`coursename`);

--
-- Constraints for table `subject`
--
ALTER TABLE `subject`
  ADD CONSTRAINT `subject_ibfk_1` FOREIGN KEY (`tid`) REFERENCES `teacher` (`tid`),
  ADD CONSTRAINT `subject_ibfk_2` FOREIGN KEY (`cname`) REFERENCES `courses` (`coursename`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
