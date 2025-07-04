-- MySQL dump 10.13  Distrib 9.3.0, for macos15.2 (arm64)
--
-- Host: localhost    Database: blood_alcohol
-- ------------------------------------------------------
-- Server version	9.3.0

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
-- Table structure for table `bac_levels`
--

DROP TABLE IF EXISTS `bac_levels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bac_levels` (
  `id` int NOT NULL AUTO_INCREMENT,
  `bac_range` varchar(20) DEFAULT NULL,
  `g_per_l_range` varchar(20) DEFAULT NULL,
  `symptoms` text,
  `legal_implications` text,
  `recommendation` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bac_levels`
--

LOCK TABLES `bac_levels` WRITE;
/*!40000 ALTER TABLE `bac_levels` DISABLE KEYS */;
INSERT INTO `bac_levels` VALUES (1,'0.00–0.02','0–0.2','Mild relaxation, emotional easing, slight motor or cognitive impairment','Legally regarded as “sober”','Generally safe, but avoid driving when fatigued'),(2,'0.03–0.05','0.3–0.5','Judgment begins to decline, attention distracts easily, slight visual blurring','Violates law in some countries or for new drivers','Recommend stopping further drinking, hydrate and eat'),(3,'0.06–0.079','0.6–0.79','Noticeably slower reactions, slurred speech, impaired balance','Legal DUI limit ≈ 0.08% in most regions','Driving prohibited; take full rest'),(4,'0.08–0.149','0.8–1.49','Uncoordinated behavior, emotional instability, severe judgment impairment','Legally defined “drunk driving”; accident risk ×10','Must be accompanied by a sober person; ensure a safe environment'),(5,'0.15–0.199','1.5–1.99','Vomiting, loss of coordination, short-term memory blackouts (amnesia)','Acute alcohol intoxication; vomiting and high error risk','Hospital observation advised; no driving; fall prevention'),(6,'0.20–0.299','2.0–2.99','Drowsiness, poor stimulus response; body temperature drops','Severe intoxication, hypothermia risk ↑','Emergency medical evaluation; side-lying position; monitor vitals'),(7,'0.30–0.399','3.0–3.99','Deep coma; abnormal breathing rhythm','Critical condition; death rate increases','Immediate diagnosis; potential need for ventilator'),(8,'0.40–0.499','4.0–4.99','Respiratory depression, possible cardiac arrest','Potentially fatal zone','Advanced Cardiovascular Life Support (ACLS); ICU monitoring'),(9,'≥ 0.50','≥ 5.0','Multi-organ failure, extremely high fatality rate','Normal rescue success rate < 50%','Comprehensive treatment, blood purification, and organ support');
/*!40000 ALTER TABLE `bac_levels` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-04 15:26:37
