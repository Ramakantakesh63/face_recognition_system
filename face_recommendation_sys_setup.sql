-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: face_recognition
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `regteach`
--

DROP TABLE IF EXISTS `regteach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `regteach` (
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `contact` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `security_q` varchar(100) NOT NULL,
  `security_a` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regteach`
--

LOCK TABLES `regteach` WRITE;
/*!40000 ALTER TABLE `regteach` DISABLE KEYS */;
INSERT INTO `regteach` VALUES ('sfddfdf','qww','9337006139','dgfhjhgjh','Your Nick Name','q','xyz'),('Satabdi','Palit','9337006139','satabdipalit6@gmail.com','Your Nick Name','sat','1234');
/*!40000 ALTER TABLE `regteach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stdattendance`
--

DROP TABLE IF EXISTS `stdattendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stdattendance` (
  `Regd_no` varchar(50) NOT NULL,
  `Roll_no` varchar(50) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `time` time NOT NULL,
  `date` date NOT NULL,
  `attendance` varchar(10) NOT NULL,
  PRIMARY KEY (`Regd_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stdattendance`
--

LOCK TABLES `stdattendance` WRITE;
/*!40000 ALTER TABLE `stdattendance` DISABLE KEYS */;
/*!40000 ALTER TABLE `stdattendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `id` varchar(20) AUTO_INCREMENT,
  `Regd_no` varchar(50) NOT NULL,
  `Name` varchar(100) DEFAULT NULL,
  `Dep` varchar(50) DEFAULT NULL,
  `Course` varchar(50) DEFAULT NULL,
  `Batch` varchar(10) DEFAULT NULL,
  `Sem` varchar(20) DEFAULT NULL,
  `Divi` varchar(10) DEFAULT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Mob` varchar(15) DEFAULT NULL,
  `Address` text,
  `Roll` varchar(20) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Proctor` varchar(100) DEFAULT NULL,
  `Photo` blob,
  PRIMARY KEY (`Regd_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('F22066007006','AMIT','CSE','DIPLOMA','2022-25','Semester-6','1st Half','Male','2025-04-04','6371812179','kusuma','22-cs/05','kesh@gmail.com','JMJ',_binary 'Yes'),('F22066007017','PRAVAT','CSE','DIPLOMA','2022-25','Semester-6','1st Half','Male','2025-04-04','6371812179','kusuma','22-CS/14','kesh@gmail.com','JMJ',_binary 'Yes'),('F22066007020','PURNA','CSE','DIPLOMA','2022-25','Semester-6','1st Half','Male','2025-04-04','6371812179','kusuma','22-cs/16','kesh@gmail.com','JMJ',_binary 'Yes'),('F22066007021','Ramakanta kesh','CSE','DIPLOMA','2022-25','Semester-6','1st Half','Male','2025-04-04','6371812179','kusuma','22-cs/32','kesh@gmail.com','JMJ',_binary 'Yes'),('F22066007035','UTTAM','CSE','DIPLOMA','2022-25','Semester-6','1st Half','Male','2025-04-04','6371812179','kusuma','22-cs/27','kesh@gmail.com','JMJ',_binary 'Yes'),('F240066007001','Satabdi Palit','CSE','DIPLOMA','2024-27','Semester-6','Morning','Female','2011-04-30','9337006139','Bhadrak','24/CS-09','satabdipalit6@gmail.com','x',_binary 'Yes');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-16 16:17:42
