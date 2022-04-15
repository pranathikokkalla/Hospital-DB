-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: lol4
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.21.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Billing`
--

DROP TABLE IF EXISTS `Billing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Billing` (
  `Bill number` int NOT NULL,
  `Patient Id` int NOT NULL,
  `Room Cost` int DEFAULT NULL,
  `Doctor Cost` int NOT NULL,
  `Date of Bill` varchar(11) NOT NULL,
  PRIMARY KEY (`Bill number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Billing`
--

LOCK TABLES `Billing` WRITE;
/*!40000 ALTER TABLE `Billing` DISABLE KEYS */;
INSERT INTO `Billing` VALUES (1,1,120000,2000,'24/10/2021'),(2,2,12000,3000,'22/10/2021'),(3,3,0,1000,'24/10/2021'),(4,4,0,2000,'25/10/2021');
/*!40000 ALTER TABLE `Billing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Contact_number`
--

DROP TABLE IF EXISTS `Contact_number`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Contact_number` (
  `Phone number` varchar(11) NOT NULL,
  `Patient Id` int NOT NULL,
  PRIMARY KEY (`Phone number`,`Patient Id`),
  KEY `Contact_number_ibfk_1` (`Patient Id`),
  CONSTRAINT `Contact_number_ibfk_1` FOREIGN KEY (`Patient Id`) REFERENCES `Outpatient` (`Patient Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Contact_number`
--

LOCK TABLES `Contact_number` WRITE;
/*!40000 ALTER TABLE `Contact_number` DISABLE KEYS */;
INSERT INTO `Contact_number` VALUES ('9999999910',3),('9999999999',3),('9876543210',4);
/*!40000 ALTER TABLE `Contact_number` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Department`
--

DROP TABLE IF EXISTS `Department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Department` (
  `Department Id` int NOT NULL,
  `Department Name` varchar(50) NOT NULL,
  PRIMARY KEY (`Department Id`,`Department Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Department`
--

LOCK TABLES `Department` WRITE;
/*!40000 ALTER TABLE `Department` DISABLE KEYS */;
INSERT INTO `Department` VALUES (1,'Cardiology'),(2,'General'),(3,'Emergengy Care');
/*!40000 ALTER TABLE `Department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Doctor`
--

DROP TABLE IF EXISTS `Doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Doctor` (
  `Fees` int NOT NULL,
  `Starting Hour` varchar(6) NOT NULL,
  `Ending Hour` varchar(6) NOT NULL,
  `Staff Id` int NOT NULL,
  PRIMARY KEY (`Staff Id`),
  CONSTRAINT `Doctor_1` FOREIGN KEY (`Staff Id`) REFERENCES `Staff` (`Staff Id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Doctor`
--

LOCK TABLES `Doctor` WRITE;
/*!40000 ALTER TABLE `Doctor` DISABLE KEYS */;
INSERT INTO `Doctor` VALUES (1000,'11:00','15:00',1),(2000,'09:00','12:00',2),(3000,'10:00','14:00',3);
/*!40000 ALTER TABLE `Doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Finance1`
--

DROP TABLE IF EXISTS `Finance1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Finance1` (
  `Bill number` int NOT NULL,
  `Month` int NOT NULL,
  PRIMARY KEY (`Bill number`,`Month`),
  CONSTRAINT `Finance1_ibfk_1` FOREIGN KEY (`Bill number`) REFERENCES `Billing` (`Bill number`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Finance1`
--

LOCK TABLES `Finance1` WRITE;
/*!40000 ALTER TABLE `Finance1` DISABLE KEYS */;
INSERT INTO `Finance1` VALUES (1,10),(2,10),(3,10),(4,10);
/*!40000 ALTER TABLE `Finance1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Finance2`
--

DROP TABLE IF EXISTS `Finance2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Finance2` (
  `Expenditure` int NOT NULL,
  `Income` int NOT NULL,
  `Bill number` int NOT NULL,
  PRIMARY KEY (`Bill number`),
  CONSTRAINT `Finance2_ibfk_1` FOREIGN KEY (`Bill number`) REFERENCES `Billing` (`Bill number`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Finance2`
--

LOCK TABLES `Finance2` WRITE;
/*!40000 ALTER TABLE `Finance2` DISABLE KEYS */;
INSERT INTO `Finance2` VALUES (2000,30000,1),(2000,4000,2),(20000,4000,3),(2000,500,4);
/*!40000 ALTER TABLE `Finance2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Inpatient`
--

DROP TABLE IF EXISTS `Inpatient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Inpatient` (
  `Patient Id` int NOT NULL,
  `First name` varchar(50) NOT NULL,
  `Middle name` varchar(50) DEFAULT NULL,
  `Last name` varchar(50) NOT NULL,
  `H.no` varchar(20) DEFAULT NULL,
  `Pin_code` int NOT NULL,
  `Street no.` int DEFAULT NULL,
  `City` varchar(50) NOT NULL,
  `State` varchar(50) NOT NULL,
  `Date of admission` varchar(11) NOT NULL,
  `Date of discharge` varchar(11) NOT NULL,
  PRIMARY KEY (`Patient Id`),
  CONSTRAINT `Inpatient_ibfk_2` FOREIGN KEY (`Patient Id`) REFERENCES `Patient Info` (`Patient Id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Inpatient`
--

LOCK TABLES `Inpatient` WRITE;
/*!40000 ALTER TABLE `Inpatient` DISABLE KEYS */;
INSERT INTO `Inpatient` VALUES (1,'Sai','Pranathi','Kokkalla','2-1/1',500018,21,'Hyd','Telangana','23/10/2021','26/10/2021'),(2,'Indra','Deepika','Evuri','2-1/5',500018,22,'Hyd','Telangana','24/10/2021','27/10/2021');
/*!40000 ALTER TABLE `Inpatient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Nurse`
--

DROP TABLE IF EXISTS `Nurse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Nurse` (
  `Staff Id` int NOT NULL,
  `Nurse Id` int DEFAULT NULL,
  `No. of days per month` int NOT NULL,
  PRIMARY KEY (`Staff Id`),
  CONSTRAINT `Nurse_1` FOREIGN KEY (`Staff Id`) REFERENCES `Staff` (`Staff Id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Nurse`
--

LOCK TABLES `Nurse` WRITE;
/*!40000 ALTER TABLE `Nurse` DISABLE KEYS */;
INSERT INTO `Nurse` VALUES (4,4,27),(5,5,28),(6,7,20),(7,7,24);
/*!40000 ALTER TABLE `Nurse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Outpatient`
--

DROP TABLE IF EXISTS `Outpatient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Outpatient` (
  `Patient Id` int NOT NULL,
  `First name` varchar(50) NOT NULL,
  `Middle name` varchar(50) NOT NULL,
  `Last name` varchar(50) NOT NULL,
  `H.no` varchar(20) DEFAULT NULL,
  `Pin_code` int NOT NULL,
  `Street no.` int DEFAULT NULL,
  `City` varchar(50) NOT NULL,
  `State` varchar(50) NOT NULL,
  PRIMARY KEY (`Patient Id`),
  CONSTRAINT `Outpatient_ibfk_1` FOREIGN KEY (`Patient Id`) REFERENCES `Patient Info` (`Patient Id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Outpatient`
--

LOCK TABLES `Outpatient` WRITE;
/*!40000 ALTER TABLE `Outpatient` DISABLE KEYS */;
INSERT INTO `Outpatient` VALUES (3,'Sri','Loukya','Pappula','2-1/10',500020,21,'Hyd','Telangana'),(4,'Divya','Varshini','Yakkanti','2-1/50',500050,22,'Panaji','Goa');
/*!40000 ALTER TABLE `Outpatient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Patient Info`
--

DROP TABLE IF EXISTS `Patient Info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Patient Info` (
  `Patient Id` int NOT NULL,
  `Date` int NOT NULL,
  `Month` int NOT NULL,
  `Year` int NOT NULL,
  `Gender` varchar(2) NOT NULL,
  `Height` int NOT NULL,
  `Weight` int NOT NULL,
  PRIMARY KEY (`Patient Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Patient Info`
--

LOCK TABLES `Patient Info` WRITE;
/*!40000 ALTER TABLE `Patient Info` DISABLE KEYS */;
INSERT INTO `Patient Info` VALUES (1,22,10,2003,'F',180,54),(2,1,1,2001,'F',175,55),(3,2,2,2002,'F',175,56),(4,4,4,2004,'F',176,30);
/*!40000 ALTER TABLE `Patient Info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Room`
--

DROP TABLE IF EXISTS `Room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Room` (
  `Cost per day` int NOT NULL,
  `Status` tinyint(1) NOT NULL,
  `No.of days stayed` int NOT NULL,
  `Room No` int NOT NULL,
  `Floor No` int NOT NULL,
  PRIMARY KEY (`Room No`,`Floor No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Room`
--

LOCK TABLES `Room` WRITE;
/*!40000 ALTER TABLE `Room` DISABLE KEYS */;
INSERT INTO `Room` VALUES (2000,0,0,1,1),(30000,1,4,1,2),(20000,1,6,2,1),(3000,0,0,2,2);
/*!40000 ALTER TABLE `Room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Staff`
--

DROP TABLE IF EXISTS `Staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Staff` (
  `Staff Id` int NOT NULL,
  `Dept_Id` int DEFAULT NULL,
  `Date` int NOT NULL,
  `Month` int NOT NULL,
  `Year` int NOT NULL,
  `Salary` int NOT NULL,
  `H.no` varchar(20) NOT NULL,
  `Pin_Code` int NOT NULL,
  `Street.no` int DEFAULT NULL,
  `City` varchar(50) NOT NULL,
  `State` varchar(50) NOT NULL,
  `Gender` varchar(2) NOT NULL,
  `First_Name` varchar(50) NOT NULL,
  `Middle_Name` varchar(50) DEFAULT NULL,
  `Last_Name` varchar(50) NOT NULL,
  PRIMARY KEY (`Staff Id`),
  KEY `Staff_ibfk_1` (`Dept_Id`),
  CONSTRAINT `Staff_ibfk_1` FOREIGN KEY (`Dept_Id`) REFERENCES `Department` (`Department Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Staff`
--

LOCK TABLES `Staff` WRITE;
/*!40000 ALTER TABLE `Staff` DISABLE KEYS */;
INSERT INTO `Staff` VALUES (1,1,2,10,2002,100000,'1/2-1',500016,38,'Hyderabad','Telangana','F','Astha',NULL,'Gill'),(2,2,2,10,2002,300000,'1/2-1',500016,39,'Hyderabad','Telangana','M','Warner',NULL,'David'),(3,3,4,12,2003,250000,'1/2-5',500018,60,'Hyderabad','Andhra','F','Samantha','Ruthprabhu','Akkineni'),(4,1,14,2,2001,200000,'1/21-56',500018,44,'Jaipur','Rajasthan','F','Ameya',NULL,'Sharma'),(5,2,17,4,2003,200000,'3/2-51',500028,43,'Vizag','Andhra','M','Vithesh','Reddy','Adala'),(6,3,28,2,1999,15000,'1/2',500018,40,'Mumbai','Maharashtra','F','Shreeya',NULL,'Gupta'),(7,3,20,8,1990,18000,'1/4-81B',500088,49,'Kolkata','West bengal','M','Praneeth','Varma','smith');
/*!40000 ALTER TABLE `Staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Treatment`
--

DROP TABLE IF EXISTS `Treatment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Treatment` (
  `Bill number` int NOT NULL,
  `Staff Id` int NOT NULL,
  `Patient Id` int NOT NULL,
  PRIMARY KEY (`Bill number`,`Staff Id`,`Patient Id`),
  KEY `Treatment_ibfk_2` (`Staff Id`),
  KEY `Treatment_ibfk_3` (`Patient Id`),
  CONSTRAINT `Treatment_ibfk_1` FOREIGN KEY (`Bill number`) REFERENCES `Billing` (`Bill number`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Treatment_ibfk_2` FOREIGN KEY (`Staff Id`) REFERENCES `Staff` (`Staff Id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `Treatment_ibfk_3` FOREIGN KEY (`Patient Id`) REFERENCES `Outpatient` (`Patient Id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Treatment`
--

LOCK TABLES `Treatment` WRITE;
/*!40000 ALTER TABLE `Treatment` DISABLE KEYS */;
INSERT INTO `Treatment` VALUES (3,1,3),(4,2,4),(3,4,3),(4,5,4);
/*!40000 ALTER TABLE `Treatment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-26 18:12:39
