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
INSERT INTO `regteach` VALUES ('sfddfdf','qww','9337006139','dgfhjhgjh','Your Nick Name','q','xyz'),('rama','kesh','123','kesh@gmail.com','Your Nick Name','keshaba','admin'),('Satabdi','Palit','9337006139','satabdipalit6@gmail.com','Your Nick Name','sat','1234');
/*!40000 ALTER TABLE `regteach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stdattendance`
--

DROP TABLE IF EXISTS `stdattendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stdattendance` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Student_ID` varchar(50) DEFAULT NULL,
  `Roll_No` varchar(50) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `time` time NOT NULL,
  `date` date NOT NULL,
  `attendance` varchar(10) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Student_ID` (`Student_ID`),
  CONSTRAINT `stdattendance_ibfk_1` FOREIGN KEY (`Student_ID`) REFERENCES `student` (`Student_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stdattendance`
--

LOCK TABLES `stdattendance` WRITE;
/*!40000 ALTER TABLE `stdattendance` DISABLE KEYS */;
INSERT INTO `stdattendance` VALUES (1,'F22066007015',' 22-CS/12',' OM PRAKASH','16:39:10','2025-04-22','Absent'),(2,'F22066007021','    22-CS/32','    KESHABA','16:30:48','2025-04-23',' Present');
/*!40000 ALTER TABLE `stdattendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Student_ID` varchar(20) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Department` varchar(100) DEFAULT NULL,
  `Course` varchar(100) DEFAULT NULL,
  `Year` varchar(20) DEFAULT NULL,
  `Semester` varchar(20) DEFAULT NULL,
  `Division` varchar(20) DEFAULT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Mobile_No` varchar(15) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Roll_No` varchar(50) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Teacher_Name` varchar(100) DEFAULT NULL,
  `PhotoSample` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Student_ID` (`Student_ID`),
  UNIQUE KEY `Roll_No` (`Roll_No`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (18,'F230066007002','S.Palit','CSE','DIPLOMA','2023-26','Semester-3','Morning','Male','2000-04-01','9337006139','bdk','23/cs-01','satabdipalit6@gmail.com','x','Yes'),(19,'F22066007015','OM PRAKASH','CSE','DIPLOMA','2022-25','Semester-6','Morning','Male','2000-01-01','12345678','ASURALI','22-CS/12','test@gmail.com','TEST','Yes'),(20,'F22066007021','KESHABA','CSE','DIPLOMA','2022-25','Semester-6','Morning','Male','2001-01-01','1234567890','KESHABA GHATA','22-CS/32','test@gmail.com','TEST1','Yes'),(21,'F22066007020','purna','CSE','DIPLOMA','2022-25','Semester-6','Morning','Male','2006-04-22','74185296','aradi','22/cs-16','purna@gmail.com','jmj','Yes'),(22,'F22066007017','PRAVAT','CSE','DIPLOMA','2022-25','Semester-6','Morning','Male','2006-08-12','8457935118','asurali','22-CS/14','pravat@gmail.com','sp',''),(23,'F22066007027','UTTAM','CSE','DIPLOMA','2022-25','Semester-6','Morning','Male','2003-07-29','852046555','dhushri','22-CS/27','uttam@gmail.com','SP','Yes'),(25,'f22066007018','Abinash','CSE','DIPLOMA','2022-25','Semester-6','Morning','Male','2006-05-30','24569875','asurali','22-cs/02','aabinash@gmail.com','sb','Yes');
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

-- Dump completed on 2025-04-23 14:59:27
