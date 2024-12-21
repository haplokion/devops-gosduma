-- MySQL dump 10.13  Distrib 8.0.40, for Linux (x86_64)
--
-- Host: localhost    Database: site
-- ------------------------------------------------------
-- Server version	8.0.40-0ubuntu0.24.04.1

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
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `book_id` int NOT NULL AUTO_INCREMENT,
  `book_name` varchar(64) NOT NULL,
  `book_description` text NOT NULL,
  `book_year` year NOT NULL,
  `book_publisher` varchar(64) NOT NULL,
  `book_author` varchar(64) NOT NULL,
  `book_size` int NOT NULL,
  `book_cover` int NOT NULL,
  PRIMARY KEY (`book_id`),
  KEY `book_cover` (`book_cover`),
  CONSTRAINT `books_ibfk_1` FOREIGN KEY (`book_cover`) REFERENCES `covers` (`cover_id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (65,'В Саратове помыли собаку','Собака помыта',2020,'я','Жириновский',12,67);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_to_genres`
--

DROP TABLE IF EXISTS `books_to_genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books_to_genres` (
  `book_id` int NOT NULL,
  `genre_id` int NOT NULL,
  PRIMARY KEY (`book_id`,`genre_id`),
  KEY `genre_id` (`genre_id`),
  CONSTRAINT `books_to_genres_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`) ON DELETE CASCADE,
  CONSTRAINT `books_to_genres_ibfk_3` FOREIGN KEY (`genre_id`) REFERENCES `genres` (`genre_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_to_genres`
--

LOCK TABLES `books_to_genres` WRITE;
/*!40000 ALTER TABLE `books_to_genres` DISABLE KEYS */;
INSERT INTO `books_to_genres` VALUES (65,4),(65,12);
/*!40000 ALTER TABLE `books_to_genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `covers`
--

DROP TABLE IF EXISTS `covers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `covers` (
  `cover_id` int NOT NULL AUTO_INCREMENT,
  `cover_name` varchar(64) NOT NULL,
  `cover_mime_type` varchar(16) NOT NULL,
  `cover_MD5_hash` varchar(32) NOT NULL,
  PRIMARY KEY (`cover_id`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `covers`
--

LOCK TABLES `covers` WRITE;
/*!40000 ALTER TABLE `covers` DISABLE KEYS */;
INSERT INTO `covers` VALUES (46,'dac844929440fd40187ad3bb55253993.jpg','image/jpeg','dac844929440fd40187ad3bb55253993'),(47,'2868e1bb2a514d57ab24e4b8a3f8d2fd.jpg','image/jpeg','2868e1bb2a514d57ab24e4b8a3f8d2fd'),(48,'e204d26aa06a4b427e5a43f1308181b5.jpeg','image/jpeg','e204d26aa06a4b427e5a43f1308181b5'),(49,'12871e56b82ec0e9c38be6c51101ea8a.jpeg','image/jpeg','12871e56b82ec0e9c38be6c51101ea8a'),(52,'49d771c61e3cc1a84844a58ce2bc0439.jpeg','image/jpeg','49d771c61e3cc1a84844a58ce2bc0439'),(53,'cb2a1a3868ef82c2fb7900b519b06177.jpg','image/jpeg','cb2a1a3868ef82c2fb7900b519b06177'),(54,'42595051aa44aa637621cd49f0f06b7c.jpg','image/jpeg','42595051aa44aa637621cd49f0f06b7c'),(55,'3bec273a260005cb5cb1d108ef2c8fba.jpg','image/jpeg','3bec273a260005cb5cb1d108ef2c8fba'),(57,'c6b63accba430955d249d65aa016998c.jpg','image/jpeg','c6b63accba430955d249d65aa016998c'),(58,'afd017b95a123c147f893bfc238ca4f2.jpg','image/jpeg','afd017b95a123c147f893bfc238ca4f2'),(59,'e885583c92db9d8fa83b6e4aee6015b2.jpg','image/jpeg','e885583c92db9d8fa83b6e4aee6015b2'),(60,'50c3da84f75507034d1fb01e8a7a4405.jpg','image/jpeg','50c3da84f75507034d1fb01e8a7a4405'),(61,'c5631dede93ca23eef9a8ce89e3306e2.jpg','image/jpeg','c5631dede93ca23eef9a8ce89e3306e2'),(62,'33086d20cf2164aa47294ae77267b34e.png','image/png','33086d20cf2164aa47294ae77267b34e'),(67,'b36cbf7135aad762c99422aea799df9a.png','image/png','b36cbf7135aad762c99422aea799df9a');
/*!40000 ALTER TABLE `covers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genres`
--

DROP TABLE IF EXISTS `genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genres` (
  `genre_id` int NOT NULL AUTO_INCREMENT,
  `genre_name` varchar(16) NOT NULL,
  PRIMARY KEY (`genre_id`),
  UNIQUE KEY `genre_name` (`genre_name`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genres`
--

LOCK TABLES `genres` WRITE;
/*!40000 ALTER TABLE `genres` DISABLE KEYS */;
INSERT INTO `genres` VALUES (1,'Интервью'),(3,'Новости города'),(4,'Общественная жиз'),(12,'Полезная справка'),(6,'Преступления'),(8,'Рецензия'),(9,'Скандал'),(13,'Служебная информ'),(5,'Спорт'),(10,'Справочник'),(2,'Срочные новости'),(11,'Статья'),(7,'Юридическая спра');
/*!40000 ALTER TABLE `genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `review_id` int NOT NULL AUTO_INCREMENT,
  `review_book` int NOT NULL,
  `review_user` int NOT NULL,
  `review_rating` int NOT NULL,
  `review_text` text NOT NULL,
  `review_created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`review_id`),
  KEY `review_user` (`review_user`),
  KEY `review_book` (`review_book`),
  CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`review_user`) REFERENCES `users` (`user_id`),
  CONSTRAINT `reviews_ibfk_3` FOREIGN KEY (`review_book`) REFERENCES `books` (`book_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (19,65,3,3,'Круто!!!!!!!!!!!!!','2024-11-16 06:16:21');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `role_id` int NOT NULL AUTO_INCREMENT,
  `role_name` varchar(16) NOT NULL,
  `role_description` text NOT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'administrator','суперпользователь, имеет полный доступ к системе, в том числе к созданию и удалению книг'),(2,'moderator','может редактировать данные книг и производить модерацию рецензий'),(3,'user','может оставлять рецензии');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `statistics`
--

DROP TABLE IF EXISTS `statistics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `statistics` (
  `statistic_id` int NOT NULL AUTO_INCREMENT,
  `statistic_user` int DEFAULT NULL,
  `statistic_book` int NOT NULL,
  `statistic_created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`statistic_id`),
  KEY `statistic_user` (`statistic_user`),
  KEY `statistic_book` (`statistic_book`),
  CONSTRAINT `statistics_ibfk_1` FOREIGN KEY (`statistic_user`) REFERENCES `users` (`user_id`) ON DELETE CASCADE,
  CONSTRAINT `statistics_ibfk_2` FOREIGN KEY (`statistic_book`) REFERENCES `books` (`book_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=118 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `statistics`
--

LOCK TABLES `statistics` WRITE;
/*!40000 ALTER TABLE `statistics` DISABLE KEYS */;
INSERT INTO `statistics` VALUES (109,1,65,'2024-11-16 06:09:31'),(110,NULL,65,'2024-11-16 06:15:33'),(111,NULL,65,'2024-11-16 06:15:47'),(112,NULL,65,'2024-11-16 06:15:47'),(113,3,65,'2024-11-16 06:16:04'),(114,3,65,'2024-11-16 06:16:21'),(115,NULL,65,'2024-11-16 09:22:57'),(116,NULL,65,'2024-11-16 09:22:57'),(117,NULL,65,'2024-11-16 09:23:19');
/*!40000 ALTER TABLE `statistics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `user_login` varchar(16) NOT NULL,
  `user_password_hash` varchar(64) NOT NULL,
  `user_surname` varchar(32) NOT NULL,
  `user_name` varchar(32) NOT NULL,
  `user_patronym` varchar(32) DEFAULT NULL,
  `user_role` int NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `user_role` (`user_role`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`user_role`) REFERENCES `roles` (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','f03b56db82f6b9a856f518d4d34628e2','Админов','Админ','Админович',1),(2,'moderator','8cb7641b517b421ddcf1c0254bbb954a','Модератов','Модератор','Модератович',2),(3,'user','f118583f69bfa487bddc493b5eab0f83','Юзеров','Юзер','Юзерович',3);
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

-- Dump completed on 2024-11-22 20:21:05
