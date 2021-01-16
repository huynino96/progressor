-- MySQL dump 10.13  Distrib 5.7.21, for osx10.13 (x86_64)
--
-- Host: localhost    Database: progressor
-- ------------------------------------------------------
-- Server version	5.7.21

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
-- Table structure for table `api_github`
--

DROP TABLE IF EXISTS `api_github`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `api_github` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `repository` varchar(99) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_github`
--

LOCK TABLES `api_github` WRITE;
/*!40000 ALTER TABLE `api_github` DISABLE KEYS */;
INSERT INTO `api_github` VALUES (1,'2020-12-01 08:58:15.076915','2020-12-01 08:58:15.076966','kagkarlsson/db-scheduler'),(2,'2020-12-01 08:59:21.489636','2020-12-01 08:59:21.489697','axios/axios'),(3,'2020-12-01 08:59:58.242921','2020-12-01 08:59:58.242970','Pylons/deform'),(4,'2020-12-01 09:01:35.986111','2020-12-01 09:01:35.986160','sebastianbergmann/php-timer');
/*!40000 ALTER TABLE `api_github` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_language`
--

DROP TABLE IF EXISTS `api_language`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `api_language` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `javascript` int(11) NOT NULL,
  `java` int(11) NOT NULL,
  `python` int(11) NOT NULL,
  `php` int(11) NOT NULL,
  `type` varchar(20) NOT NULL,
  `github_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_language_github_id_1c5f816e_fk_api_github_id` (`github_id`),
  CONSTRAINT `api_language_github_id_1c5f816e_fk_api_github_id` FOREIGN KEY (`github_id`) REFERENCES `api_github` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_language`
--

LOCK TABLES `api_language` WRITE;
/*!40000 ALTER TABLE `api_language` DISABLE KEYS */;
INSERT INTO `api_language` VALUES (1,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',0,116,0,0,'class',1),(2,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',0,114,0,0,'comment',1),(3,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',0,0,0,0,'library',1),(4,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',0,10808,0,0,'line_of_code',1),(5,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',0,28,0,0,'method',1),(6,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',0,31,0,0,'testing',1),(7,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',4,0,0,0,'class',2),(8,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',257,0,0,0,'comment',2),(9,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',36,0,0,0,'library',2),(10,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',8543,0,0,0,'line_of_code',2),(11,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',80,0,0,0,'method',2),(12,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',2,0,0,0,'testing',2),(13,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',29,0,22,0,'class',3),(14,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',169,0,0,0,'comment',3),(15,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',0,0,0,0,'library',3),(16,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',22486,0,8760,0,'line_of_code',3),(17,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',105,0,20,0,'method',3),(18,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',1,0,13,0,'testing',3),(19,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',1,0,0,5,'class',4),(20,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',0,0,0,27,'comment',4),(21,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',0,0,0,2,'library',4),(22,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',43,0,0,705,'line_of_code',4),(23,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',0,0,0,7,'method',4),(24,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',0,0,0,3,'testing',4),(25,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',0,117,0,0,'class',1),(26,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',0,116,0,0,'comment',1),(27,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',0,0,0,0,'library',1),(28,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',0,10811,0,0,'line_of_code',1),(29,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',0,30,0,0,'method',1),(30,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',0,30,0,0,'testing',1),(31,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',4,0,0,0,'class',2),(32,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',261,0,0,0,'comment',2),(33,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',35,0,0,0,'library',2),(34,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',8541,0,0,0,'line_of_code',2),(35,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',80,0,0,0,'method',2),(36,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',2,0,0,0,'testing',2),(37,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',29,0,18,0,'class',3),(38,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',169,0,0,0,'comment',3),(39,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',0,0,0,0,'library',3),(40,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',22485,0,8759,0,'line_of_code',3),(41,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',103,0,23,0,'method',3),(42,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',1,0,13,0,'testing',3),(43,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',1,0,0,5,'class',4),(44,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',0,0,0,26,'comment',4),(45,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',0,0,0,2,'library',4),(46,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',46,0,0,701,'line_of_code',4),(47,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',0,0,0,4,'method',4),(48,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',0,0,0,3,'testing',4),(49,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',0,114,0,0,'class',1),(50,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',0,115,0,0,'comment',1),(51,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',0,0,0,0,'library',1),(52,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',0,10810,0,0,'line_of_code',1),(53,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',0,28,0,0,'method',1),(54,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',0,32,0,0,'testing',1),(55,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',4,0,0,0,'class',2),(56,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',259,0,0,0,'comment',2),(57,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',33,0,0,0,'library',2),(58,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',8543,0,0,0,'line_of_code',2),(59,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',80,0,0,0,'method',2),(60,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',2,0,0,0,'testing',2),(61,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',29,0,20,0,'class',3),(62,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',169,0,0,0,'comment',3),(63,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',0,0,0,0,'library',3),(64,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',22486,0,8759,0,'line_of_code',3),(65,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',106,0,25,0,'method',3),(66,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',1,0,11,0,'testing',3),(67,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',1,0,0,6,'class',4),(68,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',0,0,0,25,'comment',4),(69,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',0,0,0,2,'library',4),(70,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',43,0,0,703,'line_of_code',4),(71,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',0,0,0,7,'method',4),(72,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',0,0,0,3,'testing',4),(73,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',0,117,0,0,'class',1),(74,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',0,117,0,0,'comment',1),(75,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',0,0,0,0,'library',1),(76,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',0,10812,0,0,'line_of_code',1),(77,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',0,28,0,0,'method',1),(78,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',0,31,0,0,'testing',1),(79,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',4,0,0,0,'class',2),(80,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',261,0,0,0,'comment',2),(81,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',35,0,0,0,'library',2),(82,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',8541,0,0,0,'line_of_code',2),(83,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',82,0,0,0,'method',2),(84,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',2,0,0,0,'testing',2),(85,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',30,0,21,0,'class',3),(86,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',169,0,0,0,'comment',3),(87,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',0,0,0,0,'library',3),(88,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',22486,0,8758,0,'line_of_code',3),(89,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',106,0,25,0,'method',3),(90,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',1,0,11,0,'testing',3),(91,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',1,0,0,8,'class',4),(92,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',0,0,0,26,'comment',4),(93,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',0,0,0,2,'library',4),(94,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',45,0,0,705,'line_of_code',4),(95,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',0,0,0,5,'method',4),(96,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',0,0,0,3,'testing',4);
/*!40000 ALTER TABLE `api_language` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_media`
--

DROP TABLE IF EXISTS `api_media`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `api_media` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `file` int(11) NOT NULL,
  `folder` int(11) NOT NULL,
  `github_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_media_github_id_2bed6c39_fk_api_github_id` (`github_id`),
  CONSTRAINT `api_media_github_id_2bed6c39_fk_api_github_id` FOREIGN KEY (`github_id`) REFERENCES `api_github` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_media`
--

LOCK TABLES `api_media` WRITE;
/*!40000 ALTER TABLE `api_media` DISABLE KEYS */;
INSERT INTO `api_media` VALUES (1,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',155,81,1),(2,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',119,25,2),(3,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',364,104,3),(4,'2020-11-26 08:58:15.076915','2020-11-26 08:58:15.076915',23,4,4),(5,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',159,80,1),(6,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',122,27,2),(7,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',365,107,3),(8,'2020-11-27 08:58:15.076915','2020-11-27 08:58:15.076915',25,7,4),(9,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',158,78,1),(10,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',122,26,2),(11,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',365,108,3),(12,'2020-11-28 08:58:15.076915','2020-11-28 08:58:15.076915',24,8,4),(13,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',159,79,1),(14,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',122,26,2),(15,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',363,108,3),(16,'2020-11-29 08:58:15.076915','2020-11-29 08:58:15.076915',25,6,4);
/*!40000 ALTER TABLE `api_media` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add file and folder',7,'add_fileandfolder'),(26,'Can change file and folder',7,'change_fileandfolder'),(27,'Can delete file and folder',7,'delete_fileandfolder'),(28,'Can view file and folder',7,'view_fileandfolder'),(29,'Can add programming',8,'add_programming'),(30,'Can change programming',8,'change_programming'),(31,'Can delete programming',8,'delete_programming'),(32,'Can view programming',8,'view_programming'),(33,'Can add github',9,'add_github'),(34,'Can change github',9,'change_github'),(35,'Can delete github',9,'delete_github'),(36,'Can view github',9,'view_github'),(37,'Can add language',10,'add_language'),(38,'Can change language',10,'change_language'),(39,'Can delete language',10,'delete_language'),(40,'Can view language',10,'view_language'),(41,'Can add media',11,'add_media'),(42,'Can change media',11,'change_media'),(43,'Can delete media',11,'delete_media'),(44,'Can view media',11,'view_media');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(7,'api','fileandfolder'),(9,'api','github'),(10,'api','language'),(11,'api','media'),(8,'api','programming'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-11-26 08:14:31.916480'),(2,'auth','0001_initial','2020-11-26 08:14:32.239465'),(3,'admin','0001_initial','2020-11-26 08:14:32.702034'),(4,'admin','0002_logentry_remove_auto_add','2020-11-26 08:14:32.789351'),(5,'admin','0003_logentry_add_action_flag_choices','2020-11-26 08:14:32.800400'),(6,'api','0001_initial','2020-11-26 08:14:32.911349'),(7,'contenttypes','0002_remove_content_type_name','2020-11-26 08:14:33.003776'),(8,'auth','0002_alter_permission_name_max_length','2020-11-26 08:14:33.057669'),(9,'auth','0003_alter_user_email_max_length','2020-11-26 08:14:33.103612'),(10,'auth','0004_alter_user_username_opts','2020-11-26 08:14:33.118541'),(11,'auth','0005_alter_user_last_login_null','2020-11-26 08:14:33.166403'),(12,'auth','0006_require_contenttypes_0002','2020-11-26 08:14:33.209614'),(13,'auth','0007_alter_validators_add_error_messages','2020-11-26 08:14:33.219146'),(14,'auth','0008_alter_user_username_max_length','2020-11-26 08:14:33.311019'),(15,'auth','0009_alter_user_last_name_max_length','2020-11-26 08:14:33.361869'),(16,'auth','0010_alter_group_name_max_length','2020-11-26 08:14:33.410100'),(17,'auth','0011_update_proxy_permissions','2020-11-26 08:14:33.422043'),(18,'auth','0012_alter_user_first_name_max_length','2020-11-26 08:14:33.515211'),(19,'sessions','0001_initial','2020-11-26 08:14:33.544833'),(20,'api','0002_auto_20201126_0817','2020-11-26 08:20:07.331472'),(21,'api','0003_auto_20201126_0818','2020-11-26 08:20:07.426283'),(22,'api','0004_auto_20201126_0819','2020-11-26 08:20:07.519629');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-02 14:12:21
