CREATE DATABASE  IF NOT EXISTS `universidad` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `universidad`;
-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: universidad
-- ------------------------------------------------------
-- Server version	8.0.46

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
-- Table structure for table `asignatura`
--

DROP TABLE IF EXISTS `asignatura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asignatura` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `creditos` float unsigned NOT NULL,
  `tipo` enum('básica','obligatoria','optativa') NOT NULL,
  `curso` tinyint unsigned NOT NULL,
  `cuatrimestre` tinyint unsigned NOT NULL,
  `id_profesor` int unsigned DEFAULT NULL,
  `id_grado` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_profesor` (`id_profesor`),
  KEY `id_grado` (`id_grado`),
  CONSTRAINT `asignatura_ibfk_1` FOREIGN KEY (`id_profesor`) REFERENCES `profesor` (`id_profesor`),
  CONSTRAINT `asignatura_ibfk_2` FOREIGN KEY (`id_grado`) REFERENCES `grado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=204 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asignatura`
--

LOCK TABLES `asignatura` WRITE;
/*!40000 ALTER TABLE `asignatura` DISABLE KEYS */;
INSERT INTO `asignatura` VALUES (1,'Algebra lineal y matemática discreta',6,'básica',1,1,3,4),(2,'Cálculo',6,'básica',1,1,14,4),(3,'Física para informática',6,'básica',1,1,3,4),(4,'Introducción a la programación',6,'básica',1,1,14,4),(5,'Organización y gestión de empresas',6,'básica',1,1,3,4),(6,'Estadística',6,'básica',1,2,14,4),(7,'Estructura y tecnología de computadores',6,'básica',1,2,3,4),(8,'Fundamentos de electrónica',6,'básica',1,2,14,4),(9,'Lógica y algorítmica',6,'básica',1,2,3,4),(10,'Metodología de la programación',6,'básica',1,2,14,4),(11,'Arquitectura de Computadores',6,'básica',2,1,3,4),(12,'Estructura de Datos y Algoritmos I',6,'obligatoria',2,1,3,4),(13,'Ingeniería del Software',6,'obligatoria',2,1,14,4),(14,'Sistemas Inteligentes',6,'obligatoria',2,1,3,4),(15,'Sistemas Operativos',6,'obligatoria',2,1,14,4),(16,'Bases de Datos',6,'básica',2,2,14,4),(17,'Estructura de Datos y Algoritmos II',6,'obligatoria',2,2,14,4),(18,'Fundamentos de Redes de Computadores',6,'obligatoria',2,2,3,4),(19,'Planificación y Gestión de Proyectos Informáticos',6,'obligatoria',2,2,3,4),(20,'Programación de Servicios Software',6,'obligatoria',2,2,14,4),(21,'Desarrollo de interfaces de usuario',6,'obligatoria',3,1,14,4),(22,'Ingeniería de Requisitos',6,'optativa',3,1,25,4),(23,'Integración de las Tecnologías de la Información en las Organizaciones',6,'optativa',3,1,NULL,4),(24,'Modelado y Diseño del Software 1',6,'optativa',3,1,26,4),(25,'Multiprocesadores',6,'optativa',3,1,NULL,4),(26,'Seguridad y cumplimiento normativo',6,'optativa',3,1,NULL,4),(27,'Sistema de Información para las Organizaciones',6,'optativa',3,1,NULL,4),(28,'Tecnologías web',6,'optativa',3,1,25,4),(29,'Teoría de códigos y criptografía',6,'optativa',3,1,NULL,4),(30,'Administración de bases de datos',6,'optativa',3,2,26,4),(31,'Herramientas y Métodos de Ingeniería del Software',6,'optativa',3,2,26,4),(32,'Informática industrial y robótica',6,'optativa',3,2,NULL,4),(33,'Ingeniería de Sistemas de Información',6,'optativa',3,2,NULL,4),(34,'Modelado y Diseño del Software 2',6,'optativa',3,2,26,4),(35,'Negocio Electrónico',6,'optativa',3,2,NULL,4),(36,'Periféricos e interfaces',6,'optativa',3,2,NULL,4),(37,'Sistemas de tiempo real',6,'optativa',3,2,NULL,4),(38,'Tecnologías de acceso a red',6,'optativa',3,2,NULL,4),(39,'Tratamiento digital de imágenes',6,'optativa',3,2,NULL,4),(40,'Administración de redes y sistemas operativos',6,'optativa',4,1,NULL,4),(41,'Almacenes de Datos',6,'optativa',4,1,25,4),(42,'Fiabilidad y Gestión de Riesgos',6,'optativa',4,1,NULL,4),(43,'Líneas de Productos Software',6,'optativa',4,1,NULL,4),(44,'Procesos de Ingeniería del Software 1',6,'optativa',4,1,26,4),(45,'Tecnologías multimedia',6,'optativa',4,1,NULL,4),(46,'Análisis y planificación de las TI',6,'optativa',4,2,NULL,4),(47,'Desarrollo Rápido de Aplicaciones',6,'optativa',4,2,NULL,4),(48,'Gestión de la Calidad y de la Innovación Tecnológica',6,'optativa',4,2,NULL,4),(49,'Inteligencia del Negocio',6,'optativa',4,2,25,4),(50,'Procesos de Ingeniería del Software 2',6,'optativa',4,2,NULL,4),(51,'Seguridad Informática',6,'optativa',4,2,25,4),(52,'Biologia celular',6,'básica',1,1,27,7),(53,'Física',6,'básica',1,1,13,7),(54,'Matemáticas I',6,'básica',1,1,32,7),(55,'Química general',6,'básica',1,1,30,7),(56,'Química orgánica',6,'básica',1,1,31,7),(57,'Biología vegetal y animal',6,'básica',1,2,28,7),(58,'Bioquímica',6,'básica',1,2,29,7),(59,'Genética',6,'básica',1,2,27,7),(60,'Matemáticas II',6,'básica',1,2,33,7),(61,'Microbiología',6,'básica',1,2,28,7),(62,'Botánica agrícola',6,'obligatoria',2,1,28,7),(63,'Fisiología vegetal',6,'obligatoria',2,1,28,7),(64,'Genética molecular',6,'obligatoria',2,1,27,7),(65,'Ingeniería bioquímica',6,'obligatoria',2,1,30,7),(66,'Termodinámica y cinética química aplicada',6,'obligatoria',2,1,20,7),(67,'Biorreactores',6,'obligatoria',2,2,31,7),(68,'Biotecnología microbiana',6,'obligatoria',2,2,29,7),(69,'Ingeniería genética',6,'obligatoria',2,2,27,7),(70,'Inmunología',6,'obligatoria',2,2,29,7),(71,'Virología',6,'obligatoria',2,2,NULL,7),(72,'Bases moleculares del desarrollo vegetal',4.5,'obligatoria',3,1,NULL,7),(73,'Fisiología animal',4.5,'obligatoria',3,1,NULL,7),(74,'Metabolismo y biosíntesis de biomoléculas',6,'obligatoria',3,1,29,7),(75,'Operaciones de separación',6,'obligatoria',3,1,NULL,7),(76,'Patología molecular de plantas',4.5,'obligatoria',3,1,NULL,7),(77,'Técnicas instrumentales básicas',4.5,'obligatoria',3,1,NULL,7),(78,'Bioinformática',4.5,'obligatoria',3,2,NULL,7),(79,'Biotecnología de los productos hortofrutículas',4.5,'obligatoria',3,2,NULL,7),(80,'Biotecnología vegetal',6,'obligatoria',3,2,28,7),(81,'Genómica y proteómica',4.5,'obligatoria',3,2,NULL,7),(82,'Procesos biotecnológicos',6,'obligatoria',3,2,30,7),(83,'Técnicas instrumentales avanzadas',4.5,'obligatoria',3,2,NULL,7),(84,'Álgebra lineal I',7.5,'básica',1,1,5,9),(85,'Análisis matemático I',7.5,'básica',1,1,32,9),(86,'Fundamentos de matemática',6,'básica',1,1,15,9),(87,'Programación para matemáticos',6,'básica',1,1,14,9),(88,'Álgebra lineal II',7.5,'básica',1,2,5,9),(89,'Análisis matemático II',7.5,'básica',1,2,32,9),(90,'Geometría',6,'básica',1,2,33,9),(91,'Probabilidad',6,'básica',1,2,15,9),(92,'Análisis matemático III',7.5,'obligatoria',2,1,32,9),(93,'Estructuras algebraicas',7.5,'obligatoria',2,1,5,9),(94,'Topología',6,'obligatoria',2,1,33,9),(95,'Ecuaciones diferenciales',7.5,'obligatoria',2,2,15,9),(96,'Estadística matemática',6,'obligatoria',2,2,NULL,9),(97,'Métodos numéricos',6,'obligatoria',2,2,33,9),(98,'Química general I',9,'básica',1,1,30,10),(99,'Matemática para químicos',6,'básica',1,1,33,10),(100,'Física general',6,'básica',1,1,13,10),(101,'Química general II',9,'básica',1,2,31,10),(102,'Química inorgánica',6,'básica',1,2,20,10),(103,'Laboratorio de química',4.5,'básica',1,2,NULL,10),(104,'Química analítica',9,'obligatoria',2,1,30,10),(105,'Fisicoquímica',6,'obligatoria',2,1,13,10),(106,'Química orgánica I',9,'obligatoria',2,2,31,10),(107,'Seguridad en el laboratorio',4.5,'optativa',2,2,NULL,10),(108,'Matemáticas I',6,'básica',1,1,5,1),(109,'Física I',6,'básica',1,1,30,1),(110,'Química',6,'básica',1,1,31,1),(111,'Expresión gráfica',6,'básica',1,1,73,1),(112,'Biología vegetal',6,'básica',1,1,28,1),(113,'Matemáticas II',6,'básica',1,2,32,1),(114,'Física II',6,'básica',1,2,13,1),(115,'Edafología',6,'básica',1,2,18,1),(116,'Estadística',6,'básica',1,2,33,1),(117,'Economía agraria',6,'básica',1,2,16,1),(118,'Topografía',6,'obligatoria',2,1,34,1),(119,'Fitotecnia',6,'obligatoria',2,1,18,1),(120,'Hidráulica',4.5,'obligatoria',2,1,74,1),(121,'Maquinaria agrícola',6,'obligatoria',2,2,75,1),(122,'Riegos y drenajes',4.5,'obligatoria',2,2,34,1),(123,'Protección de cultivos',4.5,'optativa',2,2,NULL,1),(124,'Cálculo I',6,'básica',1,1,32,2),(125,'Álgebra lineal',6,'básica',1,1,5,2),(126,'Física I',6,'básica',1,1,13,2),(127,'Expresión gráfica',6,'básica',1,1,73,2),(128,'Fundamentos de informática',6,'básica',1,1,25,2),(129,'Cálculo II',6,'básica',1,2,15,2),(130,'Física II',6,'básica',1,2,20,2),(131,'Química',6,'básica',1,2,30,2),(132,'Estadística',6,'básica',1,2,33,2),(133,'Empresa',6,'básica',1,2,16,2),(134,'Teoría de circuitos',7.5,'obligatoria',2,1,74,2),(135,'Electrotecnia',7.5,'obligatoria',2,1,74,2),(136,'Mecánica',6,'obligatoria',2,1,75,2),(137,'Máquinas eléctricas I',7.5,'obligatoria',2,2,76,2),(138,'Instalaciones eléctricas',6,'obligatoria',2,2,76,2),(139,'Energías renovables',4.5,'optativa',2,2,NULL,2),(140,'Cálculo I',6,'básica',1,1,32,3),(141,'Álgebra lineal',6,'básica',1,1,5,3),(142,'Física I',6,'básica',1,1,13,3),(143,'Expresión gráfica',6,'básica',1,1,73,3),(144,'Fundamentos de informática',6,'básica',1,1,26,3),(145,'Cálculo II',6,'básica',1,2,15,3),(146,'Física II',6,'básica',1,2,20,3),(147,'Química',6,'básica',1,2,31,3),(148,'Estadística',6,'básica',1,2,33,3),(149,'Empresa',6,'básica',1,2,16,3),(150,'Electrónica analógica',7.5,'obligatoria',2,1,76,3),(151,'Electrónica digital',7.5,'obligatoria',2,1,14,3),(152,'Teoría de circuitos',6,'obligatoria',2,1,74,3),(153,'Automatización industrial',6,'obligatoria',2,2,76,3),(154,'Instrumentación electrónica',6,'obligatoria',2,2,NULL,3),(155,'Robótica',4.5,'optativa',2,2,NULL,3),(156,'Cálculo I',6,'básica',1,1,32,5),(157,'Álgebra lineal',6,'básica',1,1,5,5),(158,'Física I',6,'básica',1,1,30,5),(159,'Expresión gráfica',6,'básica',1,1,73,5),(160,'Fundamentos de informática',6,'básica',1,1,3,5),(161,'Cálculo II',6,'básica',1,2,15,5),(162,'Física II',6,'básica',1,2,13,5),(163,'Química',6,'básica',1,2,78,5),(164,'Estadística',6,'básica',1,2,33,5),(165,'Empresa',6,'básica',1,2,16,5),(166,'Mecánica',7.5,'obligatoria',2,1,75,5),(167,'Resistencia de materiales',7.5,'obligatoria',2,1,75,5),(168,'Termodinámica técnica',6,'obligatoria',2,1,73,5),(169,'Mecánica de fluidos',6,'obligatoria',2,2,74,5),(170,'Diseño de máquinas',6,'obligatoria',2,2,75,5),(171,'Vehículos automóviles',4.5,'optativa',2,2,NULL,5),(172,'Cálculo I',6,'básica',1,1,5,6),(173,'Álgebra lineal',6,'básica',1,1,32,6),(174,'Física I',6,'básica',1,1,30,6),(175,'Expresión gráfica',6,'básica',1,1,73,6),(176,'Química general',6,'básica',1,1,78,6),(177,'Cálculo II',6,'básica',1,2,33,6),(178,'Física II',6,'básica',1,2,13,6),(179,'Química orgánica',6,'básica',1,2,31,6),(180,'Estadística',6,'básica',1,2,15,6),(181,'Empresa',6,'básica',1,2,16,6),(182,'Operaciones básicas',7.5,'obligatoria',2,1,78,6),(183,'Termodinámica química',6,'obligatoria',2,1,20,6),(184,'Ciencia de materiales',6,'obligatoria',2,1,75,6),(185,'Reactores químicos',7.5,'obligatoria',2,2,78,6),(186,'Control de procesos',6,'obligatoria',2,2,76,6),(187,'Tratamiento de aguas',4.5,'optativa',2,2,NULL,6),(188,'Matemáticas',6,'básica',1,1,33,8),(189,'Física',6,'básica',1,1,30,8),(190,'Química',6,'básica',1,1,31,8),(191,'Biología',6,'básica',1,1,27,8),(192,'Geología',6,'básica',1,1,77,8),(193,'Estadística',6,'básica',1,2,15,8),(194,'Ecología',6,'básica',1,2,29,8),(195,'Edafología',6,'básica',1,2,34,8),(196,'Economía ambiental',6,'básica',1,2,16,8),(197,'Cartografía',4.5,'básica',1,2,77,8),(198,'Contaminación atmosférica',6,'obligatoria',2,1,77,8),(199,'Hidrología',6,'obligatoria',2,1,77,8),(200,'Legislación ambiental',4.5,'obligatoria',2,1,NULL,8),(201,'Gestión de residuos',6,'obligatoria',2,2,29,8),(202,'Evaluación de impacto ambiental',6,'obligatoria',2,2,28,8),(203,'Educación ambiental',4.5,'optativa',2,2,NULL,8);
/*!40000 ALTER TABLE `asignatura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `curso`
--

DROP TABLE IF EXISTS `curso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `curso` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `anyo_inicio` year NOT NULL,
  `anyo_fin` year NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `curso`
--

LOCK TABLES `curso` WRITE;
/*!40000 ALTER TABLE `curso` DISABLE KEYS */;
INSERT INTO `curso` VALUES (1,2021,2022),(2,2022,2023),(3,2023,2024),(4,2024,2025),(5,2025,2026),(6,2026,2027);
/*!40000 ALTER TABLE `curso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departamento`
--

DROP TABLE IF EXISTS `departamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departamento` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departamento`
--

LOCK TABLES `departamento` WRITE;
/*!40000 ALTER TABLE `departamento` DISABLE KEYS */;
INSERT INTO `departamento` VALUES (1,'Informática'),(2,'Matemáticas'),(3,'Economía y Empresa'),(4,'Educación'),(5,'Agronomía'),(6,'Química y Física'),(7,'Arquitectura'),(8,'Derecho'),(9,'Biología y Geología'),(10,'Ingeniería Industrial');
/*!40000 ALTER TABLE `departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grado`
--

DROP TABLE IF EXISTS `grado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grado` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grado`
--

LOCK TABLES `grado` WRITE;
/*!40000 ALTER TABLE `grado` DISABLE KEYS */;
INSERT INTO `grado` VALUES (1,'Ingeniería Agrícola (Plan 2015)'),(2,'Ingeniería Eléctrica (Plan 2014)'),(3,'Ingeniería Electrónica Industrial (Plan 2010)'),(4,'Ingeniería Informática (Plan 2015)'),(5,'Ingeniería Mecánica (Plan 2010)'),(6,'Ingeniería Química Industrial (Plan 2010)'),(7,'Biotecnología (Plan 2015)'),(8,'Ciencias Ambientales (Plan 2009)'),(9,'Matemáticas (Plan 2010)'),(10,'Química (Plan 2009)');
/*!40000 ALTER TABLE `grado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `matricula_asignatura`
--

DROP TABLE IF EXISTS `matricula_asignatura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `matricula_asignatura` (
  `id_persona` int unsigned NOT NULL,
  `id_asignatura` int unsigned NOT NULL,
  `id_curso` int unsigned NOT NULL,
  PRIMARY KEY (`id_persona`,`id_asignatura`,`id_curso`),
  KEY `id_asignatura` (`id_asignatura`),
  KEY `id_curso` (`id_curso`),
  CONSTRAINT `matricula_asignatura_ibfk_1` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id`),
  CONSTRAINT `matricula_asignatura_ibfk_2` FOREIGN KEY (`id_asignatura`) REFERENCES `asignatura` (`id`),
  CONSTRAINT `matricula_asignatura_ibfk_3` FOREIGN KEY (`id_curso`) REFERENCES `curso` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matricula_asignatura`
--

LOCK TABLES `matricula_asignatura` WRITE;
/*!40000 ALTER TABLE `matricula_asignatura` DISABLE KEYS */;
INSERT INTO `matricula_asignatura` VALUES (1,1,1),(2,1,1),(4,1,1),(19,1,5),(21,1,4),(23,1,5),(24,1,5),(35,1,1),(37,1,3),(38,1,4),(39,1,5),(39,1,6),(40,1,6),(41,1,2),(42,1,3),(43,1,4),(44,1,6),(63,1,5),(66,1,1),(69,1,6),(1,2,1),(2,2,1),(4,2,1),(19,2,5),(21,2,4),(23,2,5),(24,2,5),(38,2,4),(39,2,5),(41,2,2),(42,2,3),(43,2,4),(44,2,6),(63,2,5),(66,2,1),(66,2,2),(69,2,6),(1,3,1),(2,3,1),(4,3,1),(19,3,5),(21,3,4),(23,3,5),(24,3,5),(36,3,2),(37,3,3),(38,3,4),(39,3,5),(40,3,6),(41,3,2),(41,3,3),(42,3,3),(42,3,4),(43,3,4),(43,3,5),(44,3,6),(63,3,5),(66,3,1),(69,3,6),(1,4,2),(19,4,5),(21,4,4),(23,4,5),(24,4,5),(36,4,2),(37,4,3),(39,4,5),(40,4,6),(41,4,2),(42,4,3),(43,4,4),(43,4,5),(44,4,6),(63,4,5),(66,4,1),(69,4,6),(1,5,2),(19,5,5),(21,5,4),(23,5,5),(24,5,5),(35,5,1),(35,5,2),(36,5,2),(37,5,3),(39,5,5),(40,5,6),(42,5,3),(42,5,4),(43,5,4),(44,5,6),(69,5,6),(1,6,2),(19,6,5),(21,6,4),(23,6,5),(24,6,5),(35,6,1),(38,6,4),(39,6,5),(39,6,6),(40,6,6),(41,6,2),(42,6,3),(44,6,6),(66,6,1),(66,6,2),(1,7,2),(19,7,5),(21,7,4),(23,7,5),(24,7,5),(35,7,1),(35,7,2),(36,7,2),(37,7,3),(38,7,4),(39,7,5),(40,7,6),(41,7,2),(42,7,3),(44,7,6),(63,7,5),(63,7,6),(69,7,6),(1,8,2),(19,8,5),(21,8,4),(23,8,5),(24,8,5),(35,8,1),(36,8,2),(37,8,3),(37,8,4),(38,8,4),(40,8,6),(41,8,2),(42,8,3),(43,8,4),(44,8,6),(63,8,5),(66,8,1),(69,8,6),(1,9,2),(19,9,5),(21,9,4),(23,9,5),(24,9,5),(35,9,1),(37,9,3),(39,9,5),(40,9,6),(41,9,2),(42,9,3),(43,9,4),(44,9,6),(63,9,5),(66,9,1),(66,9,2),(69,9,6),(1,10,2),(19,10,5),(21,10,4),(21,10,5),(23,10,5),(24,10,5),(36,10,2),(37,10,3),(38,10,4),(39,10,5),(40,10,6),(41,10,2),(42,10,3),(44,10,6),(66,10,1),(69,10,6),(21,11,5),(35,11,2),(36,11,3),(37,11,4),(42,11,4),(43,11,5),(63,11,6),(66,11,2),(21,12,5),(21,12,6),(35,12,2),(36,12,3),(37,12,4),(38,12,5),(39,12,6),(41,12,3),(42,12,4),(43,12,5),(66,12,2),(21,13,5),(35,13,2),(36,13,3),(37,13,4),(38,13,5),(39,13,6),(41,13,3),(42,13,4),(43,13,5),(43,13,6),(63,13,6),(21,14,5),(35,14,2),(36,14,3),(37,14,4),(38,14,5),(38,14,6),(39,14,6),(42,14,4),(43,14,5),(63,14,6),(66,14,2),(66,14,3),(21,15,5),(35,15,2),(36,15,3),(37,15,4),(38,15,5),(39,15,6),(42,15,4),(66,15,2),(21,16,5),(35,16,2),(35,16,3),(36,16,3),(37,16,4),(38,16,5),(41,16,3),(42,16,4),(63,16,6),(21,17,5),(35,17,2),(36,17,3),(37,17,4),(38,17,5),(39,17,6),(41,17,3),(42,17,4),(43,17,5),(63,17,6),(66,17,2),(21,18,5),(35,18,2),(36,18,3),(37,18,4),(38,18,5),(39,18,6),(41,18,3),(41,18,4),(42,18,4),(43,18,5),(63,18,6),(66,18,2),(21,19,5),(35,19,2),(36,19,3),(37,19,4),(38,19,5),(39,19,6),(43,19,5),(63,19,6),(66,19,2),(35,20,2),(36,20,3),(38,20,5),(39,20,6),(43,20,5),(66,20,2),(21,21,6),(35,21,3),(36,21,4),(38,21,6),(41,21,4),(42,21,5),(43,21,6),(66,21,3),(41,22,4),(38,23,6),(21,24,6),(35,24,3),(38,24,6),(41,24,4),(42,24,5),(37,25,5),(66,25,3),(36,26,4),(66,26,3),(35,27,3),(36,27,4),(21,28,6),(37,28,5),(41,28,4),(43,29,6),(21,30,6),(38,30,6),(41,30,4),(36,32,4),(42,32,5),(43,32,6),(21,33,6),(66,33,3),(35,34,3),(37,34,5),(42,34,5),(43,34,6),(36,35,4),(43,36,6),(66,36,3),(42,37,5),(35,39,3),(37,39,5),(38,39,6),(36,40,5),(41,40,5),(35,41,4),(37,41,6),(37,42,6),(66,42,4),(36,43,5),(66,43,4),(36,44,5),(41,44,5),(37,45,6),(42,45,6),(35,46,4),(41,47,5),(35,48,4),(36,48,5),(42,48,6),(66,48,4),(37,49,6),(42,49,6),(41,50,5),(42,50,6),(35,51,4),(66,51,4),(7,52,2),(45,52,1),(46,52,2),(47,52,3),(49,52,5),(64,52,5),(7,53,2),(45,53,1),(46,53,2),(47,53,3),(48,53,4),(48,53,5),(49,53,5),(50,53,6),(51,53,4),(64,53,5),(67,53,3),(7,54,2),(45,54,1),(46,54,2),(47,54,3),(48,54,4),(49,54,5),(49,54,6),(50,54,6),(51,54,4),(64,54,5),(67,54,3),(7,55,2),(45,55,1),(46,55,2),(46,55,3),(47,55,3),(47,55,4),(48,55,4),(49,55,5),(50,55,6),(51,55,4),(64,55,5),(67,55,3),(7,56,2),(45,56,1),(46,56,2),(46,56,3),(47,56,3),(48,56,4),(49,56,5),(49,56,6),(64,56,5),(7,57,2),(45,57,1),(45,57,2),(46,57,2),(47,57,3),(48,57,4),(49,57,5),(50,57,6),(51,57,4),(64,57,5),(67,57,3),(7,58,2),(45,58,1),(46,58,2),(49,58,5),(51,58,4),(67,58,3),(7,59,2),(45,59,1),(46,59,2),(48,59,4),(49,59,5),(50,59,6),(51,59,4),(64,59,5),(67,59,3),(45,60,1),(47,60,3),(48,60,4),(49,60,5),(51,60,4),(64,60,5),(67,60,3),(7,61,2),(46,61,2),(46,61,3),(47,61,3),(48,61,4),(49,61,5),(50,61,6),(64,61,5),(67,61,3),(7,62,3),(45,62,2),(46,62,3),(48,62,5),(49,62,6),(64,62,6),(67,62,4),(7,63,3),(45,63,2),(46,63,3),(46,63,4),(47,63,4),(48,63,5),(49,63,6),(51,63,5),(64,63,6),(45,64,2),(48,64,5),(49,64,6),(64,64,6),(67,64,4),(7,65,3),(45,65,2),(46,65,3),(47,65,4),(48,65,5),(49,65,6),(51,65,5),(64,65,6),(67,65,4),(7,66,3),(45,66,2),(46,66,3),(47,66,4),(48,66,5),(49,66,6),(51,66,5),(51,66,6),(64,66,6),(67,66,4),(7,67,3),(7,67,4),(45,67,2),(46,67,3),(47,67,4),(48,67,5),(49,67,6),(51,67,5),(64,67,6),(67,67,4),(67,67,5),(7,68,3),(45,68,2),(46,68,3),(47,68,4),(49,68,6),(51,68,5),(7,69,3),(45,69,2),(46,69,3),(46,69,4),(49,69,6),(64,69,6),(67,69,4),(7,70,3),(45,70,2),(46,70,3),(47,70,4),(48,70,5),(48,70,6),(49,70,6),(51,70,5),(64,70,6),(67,70,4),(7,71,3),(45,71,2),(46,71,3),(48,71,5),(49,71,6),(51,71,5),(64,71,6),(67,71,4),(67,71,5),(7,72,4),(45,72,3),(47,72,5),(48,72,6),(51,72,6),(67,72,5),(7,73,4),(45,73,3),(46,73,4),(47,73,5),(51,73,6),(67,73,5),(7,74,4),(45,74,3),(46,74,4),(47,74,5),(48,74,6),(51,74,6),(67,74,5),(7,75,4),(45,75,3),(46,75,4),(47,75,5),(48,75,6),(67,75,5),(7,76,4),(45,76,3),(46,76,4),(47,76,5),(48,76,6),(51,76,6),(67,76,5),(7,77,4),(45,77,3),(47,77,5),(67,77,5),(7,78,4),(45,78,3),(46,78,4),(47,78,5),(48,78,6),(51,78,6),(67,78,5),(7,79,4),(45,79,3),(46,79,4),(47,79,5),(48,79,6),(51,79,6),(67,79,5),(7,80,4),(46,80,4),(47,80,5),(48,80,6),(51,80,6),(67,80,5),(7,81,4),(46,81,4),(47,81,5),(51,81,6),(67,81,5),(7,82,4),(45,82,3),(46,82,4),(47,82,5),(48,82,6),(51,82,6),(67,82,5),(7,83,4),(45,83,3),(46,83,4),(47,83,5),(48,83,6),(51,83,6),(11,84,3),(53,84,3),(55,84,5),(56,84,6),(65,84,4),(11,85,3),(53,85,3),(55,85,5),(56,85,6),(57,85,5),(53,86,3),(54,86,4),(56,86,6),(57,86,5),(11,87,3),(52,87,2),(53,87,3),(54,87,4),(55,87,5),(56,87,6),(57,87,5),(65,87,4),(11,88,3),(52,88,2),(53,88,3),(54,88,4),(55,88,5),(57,88,5),(57,88,6),(65,88,4),(11,89,3),(52,89,2),(53,89,3),(54,89,4),(55,89,5),(56,89,6),(57,89,5),(57,89,6),(11,90,3),(52,90,2),(53,90,3),(54,90,4),(55,90,5),(56,90,6),(57,90,5),(57,90,6),(65,90,4),(11,91,3),(53,91,3),(54,91,4),(55,91,5),(56,91,6),(65,91,4),(11,92,4),(52,92,3),(53,92,4),(54,92,5),(57,92,6),(11,93,4),(52,93,3),(53,93,4),(54,93,5),(55,93,6),(65,93,5),(11,94,4),(52,94,3),(53,94,4),(54,94,5),(55,94,6),(57,94,6),(11,95,4),(52,95,3),(53,95,4),(54,95,5),(55,95,6),(57,95,6),(65,95,5),(11,96,4),(52,96,3),(53,96,4),(55,96,6),(57,96,6),(65,96,5),(11,97,4),(52,97,3),(53,97,4),(54,97,5),(55,97,6),(57,97,6),(65,97,5),(58,98,3),(58,98,4),(59,98,4),(61,98,6),(62,98,6),(68,98,5),(22,99,4),(58,99,3),(59,99,4),(60,99,5),(61,99,6),(68,99,5),(59,100,4),(61,100,6),(58,101,3),(59,101,4),(59,101,5),(61,101,6),(68,101,5),(22,102,4),(22,102,5),(58,102,3),(58,102,4),(59,102,4),(61,102,6),(62,102,6),(68,102,5),(22,103,4),(59,103,4),(60,103,5),(62,103,6),(68,103,5),(22,104,5),(58,104,4),(60,104,6),(22,105,5),(58,105,4),(59,105,5),(68,105,6),(22,106,5),(58,106,4),(59,106,5),(60,106,6),(68,106,6),(22,107,5),(58,107,4),(59,107,5),(60,107,6),(68,107,6);
/*!40000 ALTER TABLE `matricula_asignatura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `persona`
--

DROP TABLE IF EXISTS `persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `persona` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nif` varchar(9) DEFAULT NULL,
  `primer_nombre` varchar(25) NOT NULL,
  `segundo_nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(50) NOT NULL,
  `ciudad` varchar(25) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `telefono` varchar(9) DEFAULT NULL,
  `fecha_nacimiento` date NOT NULL,
  `sexo` enum('H','M') NOT NULL,
  `tipo` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nif` (`nif`),
  KEY `APENOM1NOM2` (`apellido`,`primer_nombre`,`segundo_nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persona`
--

LOCK TABLES `persona` WRITE;
/*!40000 ALTER TABLE `persona` DISABLE KEYS */;
INSERT INTO `persona` VALUES (1,'26902806M','Carlos','Salvador','Pérez','C.A.B.A.','C/ Real del barrio alto','950254837','1998-03-28','H','alumno'),(2,'89542419S','Juan','José','Vega','Avellaneda','C/ Mercurio','618253876','1999-08-08','H','alumno'),(3,'11105554G','Zoe','Zara','Gea','Vicente Lopez','C/ Marte','618223876','1986-08-19','M','profesor'),(4,'17105885A','Pedro','Pablo','Pagac','La Plata','C/ Estrella fugaz',NULL,'2007-10-05','H','alumno'),(5,'38223286T','David','Schmidt','Fisher','Merlo','C/ Venus','678516294','1985-01-19','H','profesor'),(6,'04233869Y','José','Juan','Bayer','Avellaneda','C/ Júpiter','628349590','2005-01-28','H','alumno'),(7,'97258166K','Ismael','Saul','Turcotte','C.A.B.A.','C/ Neptuno',NULL,'2006-05-24','H','alumno'),(8,'79503962T','Cristina','Carolina','Rutherford','C.A.B.A.','C/ Saturno','669162534','1984-08-21','M','profesor'),(9,'82842571K','Ramón','','Tremblay','Olivos','C/ Urano','626351429','2003-11-21','H','alumno'),(10,'61142000L','Esther','Lorena','Lakin','Campana','C/ Plutón',NULL,'1984-05-19','M','profesor'),(11,'46900725E','Daniel','Damian','Pacocha','C.A.B.A.','C/ Andarax','679837625','2004-04-26','H','alumno'),(12,'85366986W','Carmen','Carla','Hirthe','Quilmes','C/ Almanzora',NULL,'1978-04-29','M','profesor'),(13,'73571384L','Alfredo','Alberto','Morissette','C.A.B.A.','C/ Guadalquivir','950896725','1987-02-01','H','profesor'),(14,'82937751G','Manolo','Pedro','Kozey','Avellaneda','C/ Duero','950263514','1984-01-02','H','profesor'),(15,'80502866Z','Alejandro','Martin ','Schoen','San Isidro','C/ Tajo','668726354','1987-03-14','H','profesor'),(16,'10485008K','Antonio','Adrian','Considine','Quilmes','C/ Sierra de los Filabres',NULL,'1989-03-18','H','profesor'),(17,'85869555K','Guillermo','Roberto','Upton','Berazategui','C/ Sierra de Gádor',NULL,'1980-05-05','H','profesor'),(18,'04326833G','Micaela','Laura','Murray','San Isidro','C/ Veleta','662765413','1983-02-25','H','profesor'),(19,'11578526G','Inma','','Yundt','C.A.B.A.','C/ Picos de Europa','678652431','2005-09-01','M','alumno'),(20,'79221403L','Francesca','','Muller','C.A.B.A.','C/ Quinto pino',NULL,'1987-10-31','H','profesor'),(21,'79089577Y','Juan','Maria','López','C.A.B.A.','C/ Los pinos','678652431','2005-01-01','H','alumno'),(22,'41491230N','Antonio','Marcos','Guerrero','La Plata','C/ Cabo de Gata','626652498','2006-02-11','H','alumno'),(23,'64753215G','Irene','','Martínez','San Isidro','C/ Zapillo','628452384','2003-03-12','M','alumno'),(24,'85135690V','Sonia','','Ruiz','Lanus','C/ Mercurio','678812017','2002-04-13','M','alumno'),(25,'25988000R','Lucía','Belén','Fernández','Campana','C/ Hipólito Yrigoyen 4292','114746093','1989-08-04','M','profesor'),(26,'86848884X','Martín','Ezequiel','Sosa','Moron','C/ Paraná 3713',NULL,'1974-02-26','H','profesor'),(27,'48552728G','Valeria','Inés','Romero','Avellaneda','C/ Italia 194','236271957','1978-07-23','M','profesor'),(28,'43757517V','Gustavo','Ariel','Benítez','Vicente Lopez','C/ Güemes 3183','116710873','1974-10-13','H','profesor'),(29,'82217824T','Paula',NULL,'Acosta','Merlo','C/ Pueyrredón 3847',NULL,'1990-06-08','M','profesor'),(30,'13320452W','Hernán','Darío','Medina','Vicente Lopez','C/ Güemes 3877','239362688','1975-08-06','H','profesor'),(31,'77962320W','Natalia','Soledad','Herrera','Moron','C/ Brown 4397','239039473','1988-09-22','M','profesor'),(32,'13405927D','Diego','Alejandro','Castro','Olivos','C/ Sarmiento 500','118204296','1987-03-14','H','profesor'),(33,'74708126D','Romina',NULL,'Giménez','Olivos','C/ Mitre 3842','227745788','1981-10-08','M','profesor'),(34,'96820486P','Fernando','José','Ríos','Moron','C/ Brown 3647',NULL,'1980-01-05','H','profesor'),(35,'14443850B','Sofía','Valentina','Gómez','La Plata','C/ Uruguay 3853','237038721','2003-05-14','M','alumno'),(36,'75171986M','Mateo',NULL,'Rodríguez','Pilar','C/ Hipólito Yrigoyen 4172','115866552','2004-08-22','H','alumno'),(37,'23203533Y','Valentina','Abril','González','Pilar','C/ Hipólito Yrigoyen 2220','158143344','2004-02-02','M','alumno'),(38,'97046671B','Benjamín','Tomás','Fernández','Lanus','C/ España 3132',NULL,'2005-03-16','H','alumno'),(39,'70316750T','Martina',NULL,'López','C.A.B.A.','C/ San Martín 101','114335171','2007-03-03','M','alumno'),(40,'93359230E','Thiago','Nicolás','Díaz','C.A.B.A.','C/ Alvear 2299','223596457','2008-06-09','H','alumno'),(41,'99198595D','Camila','Agustina','Martínez','Moron','C/ Sarmiento 4571','159467819','2004-02-13','M','alumno'),(42,'66073339C','Santiago',NULL,'Pérez','Quilmes','C/ Sarmiento 2606','233492025','2003-04-11','H','alumno'),(43,'60466696H','Emma','Luz','Sánchez','C.A.B.A.','C/ Mitre 3289','116821993','2006-01-14','M','alumno'),(44,'13433596D','Joaquín','Ignacio','Romero','Moron','C/ Las Heras 2587','119347833','2007-10-20','H','alumno'),(45,'93027895W','Catalina',NULL,'Sosa','Quilmes','C/ Sarmiento 4356','228697676','2001-04-30','M','alumno'),(46,'19329269T','Lautaro','Gabriel','Álvarez','Berazategui','C/ Rivadavia 1701','151758944','2002-01-25','H','alumno'),(47,'70642368F','Mía','Julieta','Torres','San Isidro','C/ España 267',NULL,'2003-04-22','M','alumno'),(48,'79370789C','Bautista',NULL,'Ruiz','La Plata','C/ Moreno 1623','239942439','2005-02-10','H','alumno'),(49,'61430266A','Delfina','Rocío','Ramírez','Merlo','C/ Moreno 2918',NULL,'2006-09-12','M','alumno'),(50,'65799328P','Felipe','Andrés','Flores','Merlo','C/ Italia 1549','238458863','2008-09-26','H','alumno'),(51,'80423899Y','Lucía',NULL,'Acosta','Lanus','C/ Mitre 1855','118618762','2006-07-28','M','alumno'),(52,'83156735M','Tomás','Agustín','Benítez','Quilmes','C/ Belgrano 2983','224632979','2004-11-13','H','alumno'),(53,'47644351N','Isabella','Victoria','Medina','San Isidro','C/ Paraná 2514','152702144','2005-02-19','M','alumno'),(54,'68526026X','Facundo',NULL,'Suárez','Quilmes','C/ Mitre 595','152783754','2004-06-09','H','alumno'),(55,'47149597B','Julieta','Milagros','Herrera','C.A.B.A.','C/ Pueyrredón 2677',NULL,'2007-02-02','M','alumno'),(56,'11861671L','Agustín','Federico','Aguirre','Tigre','C/ Corrientes 3495','112618161','2008-01-12','H','alumno'),(57,'51596580J','Renata',NULL,'Pereyra','Avellaneda','C/ Mitre 4697','226284394','2006-11-07','M','alumno'),(58,'93983744V','Nicolás','Matías','Gutiérrez','C.A.B.A.','C/ Brown 2689','238149173','2005-12-18','H','alumno'),(59,'60217143S','Abril','Antonella','Giménez','Lanus','C/ Brown 2491','221966882','2005-01-13','M','alumno'),(60,'47773020L','Gonzalo',NULL,'Molina','Campana','C/ Pueyrredón 1102','236349960','2005-01-11','H','alumno'),(61,'82767058V','Florencia','Ayelén','Silva','Campana','C/ Alsina 4694',NULL,'2008-03-24','M','alumno'),(62,'93076786H','Franco','Emanuel','Castro','Avellaneda','C/ Mitre 405',NULL,'2008-11-01','H','alumno'),(63,'96958788B','Micaela',NULL,'Rojas','Merlo','C/ Belgrano 3579','227967545','2006-07-13','M','alumno'),(64,'42119104D','Ignacio','Leandro','Ortiz','Tigre','C/ Lavalle 1125',NULL,'2007-12-05','H','alumno'),(65,'82656183W','Agustina','Belén','Núñez','Berazategui','C/ Corrientes 1309','115644462','2004-09-02','M','alumno'),(66,'66086873F','Maximiliano',NULL,'Luna','Lanus','C/ Las Heras 1235','114008192','2001-01-20','H','alumno'),(67,'97270142Z','Candela','Sol','Juárez','Lanus','C/ Las Heras 4363','221943814','2005-11-18','M','alumno'),(68,'42588937K','Tobías','Ramiro','Cabrera','Moron','C/ Rivadavia 1917','157695356','2007-04-30','H','alumno'),(69,'85375365D','Pilar',NULL,'Ríos','Lanus','C/ Las Heras 1746','238676586','2006-08-31','M','alumno'),(70,'87924088X','Lucas','Sebastián','Morales','Merlo','C/ Alsina 1396','159134545','2008-06-30','H','alumno'),(71,'64804706K','Antonella','Celeste','Ferreyra','C.A.B.A.','C/ Moreno 789','223314594','2007-01-10','M','alumno'),(72,'39141699T','Ezequiel',NULL,'Godoy','Merlo','C/ Paraná 465','239667041','2007-09-18','H','alumno'),(73,'53464097E','Ricardo','Omar','Paz','Avellaneda','C/ Pellegrini 1250','145209871','1979-04-17','H','profesor'),(74,'30246633T','Laura','Andrea','Vázquez','Quilmes','C/ Mitre 845','153367102','1983-09-02','M','profesor'),(75,'62992312G','Sergio',NULL,'Domínguez','La Plata','C/ 7 1532',NULL,'1976-12-11','H','profesor'),(76,'97366946B','Gabriela','Noemí','Ledesma','Tigre','C/ Cazón 410','162248835','1987-06-28','M','profesor'),(77,'16480894Z','Marcelo','Hugo','Quiroga','Pilar','C/ Tucumán 677','140985521','1981-02-14','H','profesor'),(78,'19722233D','Silvina',NULL,'Ojeda','Merlo','C/ Libertad 2210',NULL,'1985-10-09','M','profesor');
/*!40000 ALTER TABLE `persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profesor`
--

DROP TABLE IF EXISTS `profesor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profesor` (
  `id_profesor` int unsigned NOT NULL,
  `id_departamento` int unsigned NOT NULL,
  PRIMARY KEY (`id_profesor`),
  KEY `id_departamento` (`id_departamento`),
  CONSTRAINT `profesor_ibfk_1` FOREIGN KEY (`id_profesor`) REFERENCES `persona` (`id`),
  CONSTRAINT `profesor_ibfk_2` FOREIGN KEY (`id_departamento`) REFERENCES `departamento` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profesor`
--

LOCK TABLES `profesor` WRITE;
/*!40000 ALTER TABLE `profesor` DISABLE KEYS */;
INSERT INTO `profesor` VALUES (3,1),(14,1),(25,1),(26,1),(5,2),(15,2),(32,2),(33,2),(8,3),(16,3),(10,4),(12,4),(17,4),(18,5),(34,5),(13,6),(20,6),(30,6),(31,6),(78,6),(27,9),(28,9),(29,9),(77,9),(73,10),(74,10),(75,10),(76,10);
/*!40000 ALTER TABLE `profesor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-11-06 16:32:56
