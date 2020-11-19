CREATE DATABASE  IF NOT EXISTS `rojgarnepal` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `rojgarnepal`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: rojgarnepal
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(250) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `address` varchar(250) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES (7,'Nabil Bank','nabil','9856789723','Balaju, Kathmandu, Nepal','Nabil@bank'),(8,'Chaudhari Groups (CG)','cg','9876540212','Pulchowk, Kathmandu, Nepal','Binod@cg'),(9,'Gandaki Boarding School','gbs','9860987432','Lamachaur, Pokhara, Kaski','GBS!@#'),(10,'Himalayan Builders','himalayanbuilders','9876590323','Kalanki, Kathmandu, Nepal','Webuild'),(11,'Nescafe','nescafe','9843023901','Illam, Jhapa, Nepal','nescafe'),(12,'Bir Hospital','birhospital','9809423023','Ratnapark, Kathmandu, Nepal','Bir@123'),(13,'Daraz Nepal','daraz','9080423403','Thamel, Kathmandu, Nepal','daraz');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job`
--

DROP TABLE IF EXISTS `job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(150) DEFAULT NULL,
  `description` varchar(250) DEFAULT NULL,
  `salary` int DEFAULT NULL,
  `minQualification` varchar(250) DEFAULT NULL,
  `companyId` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_idx` (`companyId`),
  CONSTRAINT `id` FOREIGN KEY (`companyId`) REFERENCES `company` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job`
--

LOCK TABLES `job` WRITE;
/*!40000 ALTER TABLE `job` DISABLE KEYS */;
INSERT INTO `job` VALUES (7,'Content Analyst','Create/ Source content for all products listed for upload on Daraz website as per the provided guidelines',30000,'Bachelor',13),(8,'Hub Assistant\n','Satisfying the customers at hub by answering their queries and complaints as per Daraz SOPs and manage the after sales flow for walk in customers',15000,'Bachelor',13),(9,'Security Guard','Should patrol the bank areas.',10000,'Retired Army',7),(10,'Math Teacher','Should teach secondary and +2 students',40000,'Master Degree in Mathematics',9),(11,'Contruction Worker','Should carry materials in construction sites.',12000,'Not Required',10),(12,'Gardener','Should look after tea and coffee garden.',25000,'1 year Experience as gardener',11),(13,'Cleaner','Cleaning the hospital floors, windows, stairs.',10000,'Not Required',12),(14,'HR Manager','The Human Resources (HR) Officer shall provide support in efficient management of the human resources department whilst strictly complying with the HR bylaws of the company.',50000,'Bachelor, 3 years experience',8),(15,'Nurse','Should work in Operation Theatre of ENT.',30000,'B.Sc Nursing, 2 years experience',12),(16,'Cashier','Deposit and Withdraw cash for the account holders.',14000,'SLC/SEE',7),(17,'Civil Engineer','Should monitor the construction site',60000,'Master Degree, 5 years experience',10),(18,'Marketing Director','Head of marketing department and should increase sale by 5% within 1 year',100000,'Master Degree, 3 years experience',11),(19,'Senior Web Developer','Should look after all the websites and application of CG',70000,'Bachelor, 3 years experience',8),(20,'Accountant','Should look after the finance of the school.',45000,'Master Degree, 1 year experience',9);
/*!40000 ALTER TABLE `job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_application`
--

DROP TABLE IF EXISTS `job_application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_application` (
  `id` int NOT NULL AUTO_INCREMENT,
  `jobId` int NOT NULL,
  `userId` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `jobId_idx` (`jobId`),
  KEY `userId_idx` (`userId`),
  CONSTRAINT `jobId` FOREIGN KEY (`jobId`) REFERENCES `job` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `userId` FOREIGN KEY (`userId`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_application`
--

LOCK TABLES `job_application` WRITE;
/*!40000 ALTER TABLE `job_application` DISABLE KEYS */;
INSERT INTO `job_application` VALUES (6,19,26),(7,18,26),(8,9,27),(9,13,27),(10,9,28),(11,16,28),(12,11,28),(13,12,28),(14,13,28),(15,7,28),(16,8,29),(17,15,29),(18,20,29),(19,10,29),(20,19,30),(21,7,30),(22,18,30),(23,20,30),(24,11,31),(25,12,31),(26,15,31),(27,16,31),(28,9,29),(29,19,32),(30,16,32),(31,18,32),(32,20,32),(33,15,32),(34,10,35),(35,17,35),(36,7,35),(37,16,35),(38,16,34),(39,15,34),(40,17,34),(41,10,34),(42,16,33),(43,12,33),(44,20,33),(45,7,33),(46,10,32),(47,17,32),(48,20,26);
/*!40000 ALTER TABLE `job_application` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `address` varchar(250) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (26,'Anup Raj Rijal ','anup','9860809725','Thulobharang, Kathmandu, Nepal','anup'),(27,'Aayush Subedi','aayush','9832682012','Chitwan, Nepal','aayush@123'),(28,'Adit Acharya','adit','9874562134','Tulsipur, Dang, Nepal','Adit@321'),(29,'Gita Lamsal','gita','9860792132','Newroad, Pokhara, Kaski','gita'),(30,'Navaraj Rijal','navaraj','9832420101','Thulobharang, Kathmandu, Nepal','navaraj'),(31,'Apsara Rimal','apsara','9845234234','Balaju, Kathmandu, Nepal','apsara'),(32,'Simanta Pandey','simanta','9987923843','Tanahun, Nepal','Sim@Pandey'),(33,'Bibek Paudel','bibek','9894234023','Bagar, Pokhara, Nepal','Bibek@123'),(34,'Sulav Karki','sulav','9984234232','Birauta, Kaski, Nepal','Su@Love'),(35,'Ashmin Paudel','ashmin','9834234121','Lamachaur, Kaski , Nepal','AshminPaudel');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-31 13:29:29
