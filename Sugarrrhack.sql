CREATE DATABASE  IF NOT EXISTS `sugarrrhack` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `sugarrrhack`;
-- MySQL dump 10.13  Distrib 5.6.24, for osx10.8 (x86_64)
--
-- Host: 127.0.0.1    Database: sugarrrhack
-- ------------------------------------------------------
-- Server version	5.5.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `session_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `messages` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `full_name` varchar(225) DEFAULT NULL,
  `user_name` varchar(225) DEFAULT NULL,
  `email` varchar(225) DEFAULT NULL,
  `phone_number` varchar(45) DEFAULT NULL,
  `pw_hash` varchar(225) DEFAULT NULL,
  `img` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (49,'Jay','Jay Dog Millionair','jay@mail.com','+19703137329','$2a$12$oWWhvsjdMYHHtpGT56fGoepPzprZc5RFQwzbVEJ7iSS8QndSYyKqK','http://static.ibnlive.in.com/pix/slideshow/11-2008/slumdog-millionaire-screening/slum_dog_5_630.jpg ','2015-10-02 13:28:59','2015-10-02 16:22:58','Anything, help!'),(50,'Pariece ','Pariece Hilton','pariece@mail.com','+19493850109','$2a$12$hCuqEtjpCClafI7gm7XSweQ4NFwZWosnAwxbfaDRLumbKZJIL7En.','http://sev.h-cdn.co/assets/cm/15/09/54ee39d63b1b0_-_sev-paris-hilton-1-061010-lgn.jpg ','2015-10-02 13:30:08','2015-10-02 13:42:16','One night in Pariece ;)'),(51,'Shain','Shain Bieber','shain@mail.com','+19096332350','$2a$12$SrHHilbhfrSd37roQUW2suDJUPsiBv3BtV6pRpV8lvBBTKIGifl5O','https://upload.wikimedia.org/wikipedia/commons/e/ef/Justin_Bieber_mugshot,_front.jpg','2015-10-02 13:30:37','2015-10-02 13:35:36','Don\'t stop Beliebing!'),(52,'Chad','The Chad','chad@mail.com','+17064831345','$2a$12$B/Ex01mrormToqktHe.caepoGTgdD4wT7RDs9Vx9Iq1OnEyA0b7Z2','https://media.licdn.com/media/AAEAAQAAAAAAAAMcAAAAJGY3YzQ3MjAyLTlhODUtNGRmZS04ZDY4LWEyOGE1NDdkNjc2OQ.jpg','2015-10-02 13:32:17','2015-10-02 13:46:07','Who knows...I could be faster than Michael Phelps...I\'ve just never swam.'),(53,'jared','jared','jared@mail.com','+19703137329','$2a$12$rS0jC6uGnz1n8i1Gc4Trwez7QobTry4.OrUEouHFGoFKQpGT3DbcC',NULL,'2015-10-02 16:25:10','2015-10-02 16:25:27','wooow');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-10-03  1:19:58
