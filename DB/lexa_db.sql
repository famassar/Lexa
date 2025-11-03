-- MariaDB dump 10.19  Distrib 10.5.22-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: lexa
-- ------------------------------------------------------
-- Server version	10.5.22-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alldata`
--

DROP TABLE IF EXISTS `alldata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alldata` (
  `hostid` bigint(20) unsigned NOT NULL DEFAULT 0,
  `host_name` varchar(100) NOT NULL,
  `visible_name` varchar(100) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `disabled` smallint(5) unsigned DEFAULT NULL,
  `interface_type` smallint(5) unsigned DEFAULT 1,
  `interface_id` smallint(5) unsigned DEFAULT NULL,
  `interface_ip_address` varchar(32) DEFAULT NULL,
  `interface_dns` varchar(100) DEFAULT NULL,
  `interface_use_ip` smallint(5) unsigned DEFAULT NULL,
  `interface_port` varchar(32) DEFAULT NULL,
  `interface_default` smallint(5) unsigned DEFAULT 1,
  `inserted` smallint(5) unsigned DEFAULT 0,
  `updated` smallint(5) unsigned DEFAULT 0,
  `deleted` smallint(5) unsigned DEFAULT 0,
  `type` varchar(256) DEFAULT NULL,
  `type_full` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `alias` varchar(100) DEFAULT NULL,
  `os` varchar(100) DEFAULT NULL,
  `os_full` varchar(100) DEFAULT NULL,
  `os_short` varchar(100) DEFAULT NULL,
  `serialno_a` varchar(100) DEFAULT NULL,
  `serialno_b` varchar(100) DEFAULT NULL,
  `tag` varchar(100) DEFAULT NULL,
  `asset_tag` varchar(100) DEFAULT NULL,
  `macaddress_a` varchar(100) DEFAULT NULL,
  `macaddress_b` varchar(100) DEFAULT NULL,
  `hardware` varchar(256) DEFAULT NULL,
  `hardware_full` varchar(100) DEFAULT NULL,
  `software` varchar(100) DEFAULT NULL,
  `software_full` varchar(100) DEFAULT NULL,
  `software_app_a` varchar(100) DEFAULT NULL,
  `software_app_b` varchar(100) DEFAULT NULL,
  `software_app_c` varchar(100) DEFAULT NULL,
  `software_app_d` varchar(100) DEFAULT NULL,
  `software_app_e` varchar(100) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `location_lat` varchar(100) DEFAULT NULL,
  `location_lon` varchar(100) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL,
  `chassis` varchar(100) DEFAULT NULL,
  `model` varchar(100) DEFAULT NULL,
  `hw_arch` varchar(100) DEFAULT NULL,
  `vendor` varchar(100) DEFAULT NULL,
  `contract_number` varchar(100) DEFAULT NULL,
  `installer_name` varchar(100) DEFAULT NULL,
  `deployment_status` varchar(100) DEFAULT NULL,
  `url_a` varchar(100) DEFAULT NULL,
  `url_b` varchar(100) DEFAULT NULL,
  `url_c` varchar(100) DEFAULT NULL,
  `host_networks` varchar(100) DEFAULT NULL,
  `host_netmask` varchar(100) DEFAULT NULL,
  `host_router` varchar(100) DEFAULT NULL,
  `oob_ip` varchar(100) DEFAULT NULL,
  `oob_netmask` varchar(100) DEFAULT NULL,
  `oob_router` varchar(100) DEFAULT NULL,
  `date_hw_purchase` varchar(100) DEFAULT NULL,
  `date_hw_install` varchar(100) DEFAULT NULL,
  `date_hw_expiry` varchar(100) DEFAULT NULL,
  `date_hw_decomm` varchar(100) DEFAULT NULL,
  `site_address_a` varchar(100) DEFAULT NULL,
  `site_address_b` varchar(100) DEFAULT NULL,
  `site_address_c` varchar(100) DEFAULT NULL,
  `site_city` varchar(100) DEFAULT NULL,
  `site_state` varchar(100) DEFAULT NULL,
  `site_country` varchar(100) DEFAULT NULL,
  `site_zip` varchar(100) DEFAULT NULL,
  `site_rack` varchar(100) DEFAULT NULL,
  `site_notes` varchar(100) DEFAULT NULL,
  `poc_1_name` varchar(100) DEFAULT NULL,
  `poc_1_email` varchar(100) DEFAULT NULL,
  `poc_1_phone_a` varchar(100) DEFAULT NULL,
  `poc_1_phone_b` varchar(100) DEFAULT NULL,
  `poc_1_cell` varchar(100) DEFAULT NULL,
  `poc_1_screen` varchar(100) DEFAULT NULL,
  `poc_1_notes` varchar(100) DEFAULT NULL,
  `poc_2_name` varchar(100) DEFAULT NULL,
  `poc_2_email` varchar(100) DEFAULT NULL,
  `poc_2_phone_a` varchar(100) DEFAULT NULL,
  `poc_2_phone_b` varchar(100) DEFAULT NULL,
  `poc_2_cell` varchar(100) DEFAULT NULL,
  `poc_2_screen` varchar(100) DEFAULT NULL,
  `poc_2_notes` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `datacheck`
--

DROP TABLE IF EXISTS `datacheck`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datacheck` (
  `hostid` bigint(20) unsigned NOT NULL DEFAULT 0,
  `host_name` varchar(100) NOT NULL,
  `visible_name` varchar(100) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `disabled` smallint(5) unsigned DEFAULT NULL,
  `interface_type` smallint(5) unsigned DEFAULT 1,
  `interface_id` smallint(5) DEFAULT NULL,
  `interface_ip_address` varchar(32) DEFAULT NULL,
  `interface_dns` varchar(100) DEFAULT NULL,
  `interface_use_ip` smallint(5) unsigned DEFAULT NULL,
  `interface_port` varchar(32) DEFAULT NULL,
  `interface_default` smallint(5) unsigned DEFAULT 1,
  `inserted` smallint(5) unsigned DEFAULT 0,
  `updated` smallint(5) unsigned DEFAULT 0,
  `deleted` smallint(5) unsigned DEFAULT 0,
  `type` varchar(100) DEFAULT NULL,
  `type_full` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `alias` varchar(100) DEFAULT NULL,
  `os` varchar(100) DEFAULT NULL,
  `os_full` varchar(100) DEFAULT NULL,
  `os_short` varchar(100) DEFAULT NULL,
  `serialno_a` varchar(100) DEFAULT NULL,
  `serialno_b` varchar(100) DEFAULT NULL,
  `tag` varchar(100) DEFAULT NULL,
  `asset_tag` varchar(100) DEFAULT NULL,
  `macaddress_a` varchar(100) DEFAULT NULL,
  `macaddress_b` varchar(100) DEFAULT NULL,
  `hardware` varchar(100) DEFAULT NULL,
  `hardware_full` varchar(100) DEFAULT NULL,
  `software` varchar(100) DEFAULT NULL,
  `software_full` varchar(100) DEFAULT NULL,
  `software_app_a` varchar(100) DEFAULT NULL,
  `software_app_b` varchar(100) DEFAULT NULL,
  `software_app_c` varchar(100) DEFAULT NULL,
  `software_app_d` varchar(100) DEFAULT NULL,
  `software_app_e` varchar(100) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `location_lat` varchar(100) DEFAULT NULL,
  `location_lon` varchar(100) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL,
  `chassis` varchar(100) DEFAULT NULL,
  `model` varchar(100) DEFAULT NULL,
  `hw_arch` varchar(100) DEFAULT NULL,
  `vendor` varchar(100) DEFAULT NULL,
  `contract_number` varchar(100) DEFAULT NULL,
  `installer_name` varchar(100) DEFAULT NULL,
  `deployment_status` varchar(100) DEFAULT NULL,
  `url_a` varchar(100) DEFAULT NULL,
  `url_b` varchar(100) DEFAULT NULL,
  `url_c` varchar(100) DEFAULT NULL,
  `host_networks` varchar(100) DEFAULT NULL,
  `host_netmask` varchar(100) DEFAULT NULL,
  `host_router` varchar(100) DEFAULT NULL,
  `oob_ip` varchar(100) DEFAULT NULL,
  `oob_netmask` varchar(100) DEFAULT NULL,
  `oob_router` varchar(100) DEFAULT NULL,
  `date_hw_purchase` varchar(100) DEFAULT NULL,
  `date_hw_install` varchar(100) DEFAULT NULL,
  `date_hw_expiry` varchar(100) DEFAULT NULL,
  `date_hw_decomm` varchar(100) DEFAULT NULL,
  `site_address_a` varchar(100) DEFAULT NULL,
  `site_address_b` varchar(100) DEFAULT NULL,
  `site_address_c` varchar(100) DEFAULT NULL,
  `site_city` varchar(100) DEFAULT NULL,
  `site_state` varchar(100) DEFAULT NULL,
  `site_country` varchar(100) DEFAULT NULL,
  `site_zip` varchar(100) DEFAULT NULL,
  `site_rack` varchar(100) DEFAULT NULL,
  `site_notes` varchar(100) DEFAULT NULL,
  `poc_1_name` varchar(100) DEFAULT NULL,
  `poc_1_email` varchar(100) DEFAULT NULL,
  `poc_1_phone_a` varchar(100) DEFAULT NULL,
  `poc_1_phone_b` varchar(100) DEFAULT NULL,
  `poc_1_cell` varchar(100) DEFAULT NULL,
  `poc_1_screen` varchar(100) DEFAULT NULL,
  `poc_1_notes` varchar(100) DEFAULT NULL,
  `poc_2_name` varchar(100) DEFAULT NULL,
  `poc_2_email` varchar(100) DEFAULT NULL,
  `poc_2_phone_a` varchar(100) DEFAULT NULL,
  `poc_2_phone_b` varchar(100) DEFAULT NULL,
  `poc_2_cell` varchar(100) DEFAULT NULL,
  `poc_2_screen` varchar(100) DEFAULT NULL,
  `poc_2_notes` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inventory` (
  `hostid` bigint(20) unsigned NOT NULL DEFAULT 0,
  `type` varchar(100) DEFAULT NULL,
  `type_full` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `alias` varchar(100) DEFAULT NULL,
  `os` varchar(100) DEFAULT NULL,
  `os_full` varchar(100) DEFAULT NULL,
  `os_short` varchar(100) DEFAULT NULL,
  `serialno_a` varchar(100) DEFAULT NULL,
  `serialno_b` varchar(100) DEFAULT NULL,
  `tag` varchar(100) DEFAULT NULL,
  `asset_tag` varchar(100) DEFAULT NULL,
  `macaddress_a` varchar(100) DEFAULT NULL,
  `macaddress_b` varchar(100) DEFAULT NULL,
  `hardware` varchar(100) DEFAULT NULL,
  `hardware_full` varchar(100) DEFAULT NULL,
  `software` varchar(100) DEFAULT NULL,
  `software_full` varchar(100) DEFAULT NULL,
  `software_app_a` varchar(100) DEFAULT NULL,
  `software_app_b` varchar(100) DEFAULT NULL,
  `software_app_c` varchar(100) DEFAULT NULL,
  `software_app_d` varchar(100) DEFAULT NULL,
  `software_app_e` varchar(100) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `location_lat` varchar(100) DEFAULT NULL,
  `location_lon` varchar(100) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL,
  `chassis` varchar(100) DEFAULT NULL,
  `model` varchar(100) DEFAULT NULL,
  `hw_arch` varchar(100) DEFAULT NULL,
  `vendor` varchar(100) DEFAULT NULL,
  `contract_number` varchar(100) DEFAULT NULL,
  `installer_name` varchar(100) DEFAULT NULL,
  `deployment_status` varchar(100) DEFAULT NULL,
  `url_a` varchar(100) DEFAULT NULL,
  `url_b` varchar(100) DEFAULT NULL,
  `url_c` varchar(100) DEFAULT NULL,
  `host_networks` varchar(100) DEFAULT NULL,
  `host_netmask` varchar(100) DEFAULT NULL,
  `host_router` varchar(100) DEFAULT NULL,
  `oob_ip` varchar(100) DEFAULT NULL,
  `oob_netmask` varchar(100) DEFAULT NULL,
  `oob_router` varchar(100) DEFAULT NULL,
  `date_hw_purchase` varchar(100) DEFAULT NULL,
  `date_hw_install` varchar(100) DEFAULT NULL,
  `date_hw_expiry` varchar(100) DEFAULT NULL,
  `date_hw_decomm` varchar(100) DEFAULT NULL,
  `site_address_a` varchar(100) DEFAULT NULL,
  `site_address_b` varchar(100) DEFAULT NULL,
  `site_address_c` varchar(100) DEFAULT NULL,
  `site_city` varchar(100) DEFAULT NULL,
  `site_state` varchar(100) DEFAULT NULL,
  `site_country` varchar(100) DEFAULT NULL,
  `site_zip` varchar(100) DEFAULT NULL,
  `site_rack` varchar(100) DEFAULT NULL,
  `site_notes` varchar(100) DEFAULT NULL,
  `poc_1_name` varchar(100) DEFAULT NULL,
  `poc_1_email` varchar(100) DEFAULT NULL,
  `poc_1_phone_a` varchar(100) DEFAULT NULL,
  `poc_1_phone_b` varchar(100) DEFAULT NULL,
  `poc_1_cell` varchar(100) DEFAULT NULL,
  `poc_1_screen` varchar(100) DEFAULT NULL,
  `poc_1_notes` varchar(100) DEFAULT NULL,
  `poc_2_name` varchar(100) DEFAULT NULL,
  `poc_2_email` varchar(100) DEFAULT NULL,
  `poc_2_phone_a` varchar(100) DEFAULT NULL,
  `poc_2_phone_b` varchar(100) DEFAULT NULL,
  `poc_2_cell` varchar(100) DEFAULT NULL,
  `poc_2_screen` varchar(100) DEFAULT NULL,
  `poc_2_notes` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary table structure for view `v_deleted`
--

DROP TABLE IF EXISTS `v_deleted`;
/*!50001 DROP VIEW IF EXISTS `v_deleted`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `v_deleted` AS SELECT
 1 AS `hostid`,
  1 AS `host_name`,
  1 AS `visible_name`,
  1 AS `description`,
  1 AS `disabled`,
  1 AS `interface_type`,
  1 AS `interface_ip_address`,
  1 AS `interface_dns`,
  1 AS `interface_use_ip`,
  1 AS `interface_port`,
  1 AS `interface_default`,
  1 AS `type`,
  1 AS `type_full`,
  1 AS `name`,
  1 AS `alias`,
  1 AS `os`,
  1 AS `os_full`,
  1 AS `os_short`,
  1 AS `serialno_a`,
  1 AS `serialno_b`,
  1 AS `tag`,
  1 AS `asset_tag`,
  1 AS `macaddress_a`,
  1 AS `macaddress_b`,
  1 AS `hardware`,
  1 AS `hardware_full`,
  1 AS `software`,
  1 AS `software_full`,
  1 AS `software_app_a`,
  1 AS `software_app_b`,
  1 AS `software_app_c`,
  1 AS `software_app_d`,
  1 AS `software_app_e`,
  1 AS `contact`,
  1 AS `location`,
  1 AS `location_lat`,
  1 AS `location_lon`,
  1 AS `notes`,
  1 AS `chassis`,
  1 AS `model`,
  1 AS `hw_arch`,
  1 AS `vendor`,
  1 AS `contract_number`,
  1 AS `installer_name`,
  1 AS `deployment_status`,
  1 AS `url_a`,
  1 AS `url_b`,
  1 AS `url_c`,
  1 AS `host_networks`,
  1 AS `host_netmask`,
  1 AS `host_router`,
  1 AS `oob_ip`,
  1 AS `oob_netmask`,
  1 AS `oob_router`,
  1 AS `date_hw_purchase`,
  1 AS `date_hw_install`,
  1 AS `date_hw_expiry`,
  1 AS `date_hw_decomm`,
  1 AS `site_address_a`,
  1 AS `site_address_b`,
  1 AS `site_address_c`,
  1 AS `site_city`,
  1 AS `site_state`,
  1 AS `site_country`,
  1 AS `site_zip`,
  1 AS `site_rack`,
  1 AS `site_notes`,
  1 AS `poc_1_name`,
  1 AS `poc_1_email`,
  1 AS `poc_1_phone_a`,
  1 AS `poc_1_phone_b`,
  1 AS `poc_1_cell`,
  1 AS `poc_1_screen`,
  1 AS `poc_1_notes`,
  1 AS `poc_2_name`,
  1 AS `poc_2_email`,
  1 AS `poc_2_phone_a`,
  1 AS `poc_2_phone_b`,
  1 AS `poc_2_cell`,
  1 AS `poc_2_screen`,
  1 AS `poc_2_notes` */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_differences`
--

DROP TABLE IF EXISTS `v_differences`;
/*!50001 DROP VIEW IF EXISTS `v_differences`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `v_differences` AS SELECT
 1 AS `hostid`,
  1 AS `host_name`,
  1 AS `visible_name`,
  1 AS `description`,
  1 AS `disabled`,
  1 AS `interface_type`,
  1 AS `interface_ip_address`,
  1 AS `interface_dns`,
  1 AS `interface_use_ip`,
  1 AS `interface_port`,
  1 AS `interface_default`,
  1 AS `inserted`,
  1 AS `updated`,
  1 AS `deleted`,
  1 AS `type`,
  1 AS `type_full`,
  1 AS `name`,
  1 AS `alias`,
  1 AS `os`,
  1 AS `os_full`,
  1 AS `os_short`,
  1 AS `serialno_a`,
  1 AS `serialno_b`,
  1 AS `tag`,
  1 AS `asset_tag`,
  1 AS `macaddress_a`,
  1 AS `macaddress_b`,
  1 AS `hardware`,
  1 AS `hardware_full`,
  1 AS `software`,
  1 AS `software_full`,
  1 AS `software_app_a`,
  1 AS `software_app_b`,
  1 AS `software_app_c`,
  1 AS `software_app_d`,
  1 AS `software_app_e`,
  1 AS `contact`,
  1 AS `location`,
  1 AS `location_lat`,
  1 AS `location_lon`,
  1 AS `notes`,
  1 AS `chassis`,
  1 AS `model`,
  1 AS `hw_arch`,
  1 AS `vendor`,
  1 AS `contract_number`,
  1 AS `installer_name`,
  1 AS `deployment_status`,
  1 AS `url_a`,
  1 AS `url_b`,
  1 AS `url_c`,
  1 AS `host_networks`,
  1 AS `host_netmask`,
  1 AS `host_router`,
  1 AS `oob_ip`,
  1 AS `oob_netmask`,
  1 AS `oob_router`,
  1 AS `date_hw_purchase`,
  1 AS `date_hw_install`,
  1 AS `date_hw_expiry`,
  1 AS `date_hw_decomm`,
  1 AS `site_address_a`,
  1 AS `site_address_b`,
  1 AS `site_address_c`,
  1 AS `site_city`,
  1 AS `site_state`,
  1 AS `site_country`,
  1 AS `site_zip`,
  1 AS `site_rack`,
  1 AS `site_notes`,
  1 AS `poc_1_name`,
  1 AS `poc_1_email`,
  1 AS `poc_1_phone_a`,
  1 AS `poc_1_phone_b`,
  1 AS `poc_1_cell`,
  1 AS `poc_1_screen`,
  1 AS `poc_1_notes`,
  1 AS `poc_2_name`,
  1 AS `poc_2_email`,
  1 AS `poc_2_phone_a`,
  1 AS `poc_2_phone_b`,
  1 AS `poc_2_cell`,
  1 AS `poc_2_screen`,
  1 AS `poc_2_notes` */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_inserted`
--

DROP TABLE IF EXISTS `v_inserted`;
/*!50001 DROP VIEW IF EXISTS `v_inserted`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `v_inserted` AS SELECT
 1 AS `hostid`,
  1 AS `host_name`,
  1 AS `visible_name`,
  1 AS `description`,
  1 AS `disabled`,
  1 AS `interface_type`,
  1 AS `interface_ip_address`,
  1 AS `interface_dns`,
  1 AS `interface_use_ip`,
  1 AS `interface_port`,
  1 AS `interface_default`,
  1 AS `type`,
  1 AS `type_full`,
  1 AS `name`,
  1 AS `alias`,
  1 AS `os`,
  1 AS `os_full`,
  1 AS `os_short`,
  1 AS `serialno_a`,
  1 AS `serialno_b`,
  1 AS `tag`,
  1 AS `asset_tag`,
  1 AS `macaddress_a`,
  1 AS `macaddress_b`,
  1 AS `hardware`,
  1 AS `hardware_full`,
  1 AS `software`,
  1 AS `software_full`,
  1 AS `software_app_a`,
  1 AS `software_app_b`,
  1 AS `software_app_c`,
  1 AS `software_app_d`,
  1 AS `software_app_e`,
  1 AS `contact`,
  1 AS `location`,
  1 AS `location_lat`,
  1 AS `location_lon`,
  1 AS `notes`,
  1 AS `chassis`,
  1 AS `model`,
  1 AS `hw_arch`,
  1 AS `vendor`,
  1 AS `contract_number`,
  1 AS `installer_name`,
  1 AS `deployment_status`,
  1 AS `url_a`,
  1 AS `url_b`,
  1 AS `url_c`,
  1 AS `host_networks`,
  1 AS `host_netmask`,
  1 AS `host_router`,
  1 AS `oob_ip`,
  1 AS `oob_netmask`,
  1 AS `oob_router`,
  1 AS `date_hw_purchase`,
  1 AS `date_hw_install`,
  1 AS `date_hw_expiry`,
  1 AS `date_hw_decomm`,
  1 AS `site_address_a`,
  1 AS `site_address_b`,
  1 AS `site_address_c`,
  1 AS `site_city`,
  1 AS `site_state`,
  1 AS `site_country`,
  1 AS `site_zip`,
  1 AS `site_rack`,
  1 AS `site_notes`,
  1 AS `poc_1_name`,
  1 AS `poc_1_email`,
  1 AS `poc_1_phone_a`,
  1 AS `poc_1_phone_b`,
  1 AS `poc_1_cell`,
  1 AS `poc_1_screen`,
  1 AS `poc_1_notes`,
  1 AS `poc_2_name`,
  1 AS `poc_2_email`,
  1 AS `poc_2_phone_a`,
  1 AS `poc_2_phone_b`,
  1 AS `poc_2_cell`,
  1 AS `poc_2_screen`,
  1 AS `poc_2_notes` */;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `v_deleted`
--

/*!50001 DROP VIEW IF EXISTS `v_deleted`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_deleted` AS select `t1`.`hostid` AS `hostid`,`t1`.`host_name` AS `host_name`,`t1`.`visible_name` AS `visible_name`,`t1`.`description` AS `description`,`t1`.`disabled` AS `disabled`,`t1`.`interface_type` AS `interface_type`,`t1`.`interface_ip_address` AS `interface_ip_address`,`t1`.`interface_dns` AS `interface_dns`,`t1`.`interface_use_ip` AS `interface_use_ip`,`t1`.`interface_port` AS `interface_port`,`t1`.`interface_default` AS `interface_default`,`t1`.`type` AS `type`,`t1`.`type_full` AS `type_full`,`t1`.`name` AS `name`,`t1`.`alias` AS `alias`,`t1`.`os` AS `os`,`t1`.`os_full` AS `os_full`,`t1`.`os_short` AS `os_short`,`t1`.`serialno_a` AS `serialno_a`,`t1`.`serialno_b` AS `serialno_b`,`t1`.`tag` AS `tag`,`t1`.`asset_tag` AS `asset_tag`,`t1`.`macaddress_a` AS `macaddress_a`,`t1`.`macaddress_b` AS `macaddress_b`,`t1`.`hardware` AS `hardware`,`t1`.`hardware_full` AS `hardware_full`,`t1`.`software` AS `software`,`t1`.`software_full` AS `software_full`,`t1`.`software_app_a` AS `software_app_a`,`t1`.`software_app_b` AS `software_app_b`,`t1`.`software_app_c` AS `software_app_c`,`t1`.`software_app_d` AS `software_app_d`,`t1`.`software_app_e` AS `software_app_e`,`t1`.`contact` AS `contact`,`t1`.`location` AS `location`,`t1`.`location_lat` AS `location_lat`,`t1`.`location_lon` AS `location_lon`,`t1`.`notes` AS `notes`,`t1`.`chassis` AS `chassis`,`t1`.`model` AS `model`,`t1`.`hw_arch` AS `hw_arch`,`t1`.`vendor` AS `vendor`,`t1`.`contract_number` AS `contract_number`,`t1`.`installer_name` AS `installer_name`,`t1`.`deployment_status` AS `deployment_status`,`t1`.`url_a` AS `url_a`,`t1`.`url_b` AS `url_b`,`t1`.`url_c` AS `url_c`,`t1`.`host_networks` AS `host_networks`,`t1`.`host_netmask` AS `host_netmask`,`t1`.`host_router` AS `host_router`,`t1`.`oob_ip` AS `oob_ip`,`t1`.`oob_netmask` AS `oob_netmask`,`t1`.`oob_router` AS `oob_router`,`t1`.`date_hw_purchase` AS `date_hw_purchase`,`t1`.`date_hw_install` AS `date_hw_install`,`t1`.`date_hw_expiry` AS `date_hw_expiry`,`t1`.`date_hw_decomm` AS `date_hw_decomm`,`t1`.`site_address_a` AS `site_address_a`,`t1`.`site_address_b` AS `site_address_b`,`t1`.`site_address_c` AS `site_address_c`,`t1`.`site_city` AS `site_city`,`t1`.`site_state` AS `site_state`,`t1`.`site_country` AS `site_country`,`t1`.`site_zip` AS `site_zip`,`t1`.`site_rack` AS `site_rack`,`t1`.`site_notes` AS `site_notes`,`t1`.`poc_1_name` AS `poc_1_name`,`t1`.`poc_1_email` AS `poc_1_email`,`t1`.`poc_1_phone_a` AS `poc_1_phone_a`,`t1`.`poc_1_phone_b` AS `poc_1_phone_b`,`t1`.`poc_1_cell` AS `poc_1_cell`,`t1`.`poc_1_screen` AS `poc_1_screen`,`t1`.`poc_1_notes` AS `poc_1_notes`,`t1`.`poc_2_name` AS `poc_2_name`,`t1`.`poc_2_email` AS `poc_2_email`,`t1`.`poc_2_phone_a` AS `poc_2_phone_a`,`t1`.`poc_2_phone_b` AS `poc_2_phone_b`,`t1`.`poc_2_cell` AS `poc_2_cell`,`t1`.`poc_2_screen` AS `poc_2_screen`,`t1`.`poc_2_notes` AS `poc_2_notes` from (`alldata` `t1` left join `datacheck` `t2` on(`t1`.`hostid` = `t2`.`hostid`)) where `t2`.`hostid` is null */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_differences`
--

/*!50001 DROP VIEW IF EXISTS `v_differences`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_differences` AS select `alldata`.`hostid` AS `hostid`,`alldata`.`host_name` AS `host_name`,`alldata`.`visible_name` AS `visible_name`,`alldata`.`description` AS `description`,`alldata`.`disabled` AS `disabled`,`alldata`.`interface_type` AS `interface_type`,`alldata`.`interface_ip_address` AS `interface_ip_address`,`alldata`.`interface_dns` AS `interface_dns`,`alldata`.`interface_use_ip` AS `interface_use_ip`,`alldata`.`interface_port` AS `interface_port`,`alldata`.`interface_default` AS `interface_default`,`alldata`.`inserted` AS `inserted`,`alldata`.`updated` AS `updated`,`alldata`.`deleted` AS `deleted`,`alldata`.`type` AS `type`,`alldata`.`type_full` AS `type_full`,`alldata`.`name` AS `name`,`alldata`.`alias` AS `alias`,`alldata`.`os` AS `os`,`alldata`.`os_full` AS `os_full`,`alldata`.`os_short` AS `os_short`,`alldata`.`serialno_a` AS `serialno_a`,`alldata`.`serialno_b` AS `serialno_b`,`alldata`.`tag` AS `tag`,`alldata`.`asset_tag` AS `asset_tag`,`alldata`.`macaddress_a` AS `macaddress_a`,`alldata`.`macaddress_b` AS `macaddress_b`,`alldata`.`hardware` AS `hardware`,`alldata`.`hardware_full` AS `hardware_full`,`alldata`.`software` AS `software`,`alldata`.`software_full` AS `software_full`,`alldata`.`software_app_a` AS `software_app_a`,`alldata`.`software_app_b` AS `software_app_b`,`alldata`.`software_app_c` AS `software_app_c`,`alldata`.`software_app_d` AS `software_app_d`,`alldata`.`software_app_e` AS `software_app_e`,`alldata`.`contact` AS `contact`,`alldata`.`location` AS `location`,`alldata`.`location_lat` AS `location_lat`,`alldata`.`location_lon` AS `location_lon`,`alldata`.`notes` AS `notes`,`alldata`.`chassis` AS `chassis`,`alldata`.`model` AS `model`,`alldata`.`hw_arch` AS `hw_arch`,`alldata`.`vendor` AS `vendor`,`alldata`.`contract_number` AS `contract_number`,`alldata`.`installer_name` AS `installer_name`,`alldata`.`deployment_status` AS `deployment_status`,`alldata`.`url_a` AS `url_a`,`alldata`.`url_b` AS `url_b`,`alldata`.`url_c` AS `url_c`,`alldata`.`host_networks` AS `host_networks`,`alldata`.`host_netmask` AS `host_netmask`,`alldata`.`host_router` AS `host_router`,`alldata`.`oob_ip` AS `oob_ip`,`alldata`.`oob_netmask` AS `oob_netmask`,`alldata`.`oob_router` AS `oob_router`,`alldata`.`date_hw_purchase` AS `date_hw_purchase`,`alldata`.`date_hw_install` AS `date_hw_install`,`alldata`.`date_hw_expiry` AS `date_hw_expiry`,`alldata`.`date_hw_decomm` AS `date_hw_decomm`,`alldata`.`site_address_a` AS `site_address_a`,`alldata`.`site_address_b` AS `site_address_b`,`alldata`.`site_address_c` AS `site_address_c`,`alldata`.`site_city` AS `site_city`,`alldata`.`site_state` AS `site_state`,`alldata`.`site_country` AS `site_country`,`alldata`.`site_zip` AS `site_zip`,`alldata`.`site_rack` AS `site_rack`,`alldata`.`site_notes` AS `site_notes`,`alldata`.`poc_1_name` AS `poc_1_name`,`alldata`.`poc_1_email` AS `poc_1_email`,`alldata`.`poc_1_phone_a` AS `poc_1_phone_a`,`alldata`.`poc_1_phone_b` AS `poc_1_phone_b`,`alldata`.`poc_1_cell` AS `poc_1_cell`,`alldata`.`poc_1_screen` AS `poc_1_screen`,`alldata`.`poc_1_notes` AS `poc_1_notes`,`alldata`.`poc_2_name` AS `poc_2_name`,`alldata`.`poc_2_email` AS `poc_2_email`,`alldata`.`poc_2_phone_a` AS `poc_2_phone_a`,`alldata`.`poc_2_phone_b` AS `poc_2_phone_b`,`alldata`.`poc_2_cell` AS `poc_2_cell`,`alldata`.`poc_2_screen` AS `poc_2_screen`,`alldata`.`poc_2_notes` AS `poc_2_notes` from `alldata` where !exists(select 1 from `datacheck` where lcase(`alldata`.`host_name`) = lcase(`datacheck`.`host_name`) limit 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_inserted`
--

/*!50001 DROP VIEW IF EXISTS `v_inserted`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_inserted` AS select `t1`.`hostid` AS `hostid`,`t1`.`host_name` AS `host_name`,`t1`.`visible_name` AS `visible_name`,`t1`.`description` AS `description`,`t1`.`disabled` AS `disabled`,`t1`.`interface_type` AS `interface_type`,`t1`.`interface_ip_address` AS `interface_ip_address`,`t1`.`interface_dns` AS `interface_dns`,`t1`.`interface_use_ip` AS `interface_use_ip`,`t1`.`interface_port` AS `interface_port`,`t1`.`interface_default` AS `interface_default`,`t1`.`type` AS `type`,`t1`.`type_full` AS `type_full`,`t1`.`name` AS `name`,`t1`.`alias` AS `alias`,`t1`.`os` AS `os`,`t1`.`os_full` AS `os_full`,`t1`.`os_short` AS `os_short`,`t1`.`serialno_a` AS `serialno_a`,`t1`.`serialno_b` AS `serialno_b`,`t1`.`tag` AS `tag`,`t1`.`asset_tag` AS `asset_tag`,`t1`.`macaddress_a` AS `macaddress_a`,`t1`.`macaddress_b` AS `macaddress_b`,`t1`.`hardware` AS `hardware`,`t1`.`hardware_full` AS `hardware_full`,`t1`.`software` AS `software`,`t1`.`software_full` AS `software_full`,`t1`.`software_app_a` AS `software_app_a`,`t1`.`software_app_b` AS `software_app_b`,`t1`.`software_app_c` AS `software_app_c`,`t1`.`software_app_d` AS `software_app_d`,`t1`.`software_app_e` AS `software_app_e`,`t1`.`contact` AS `contact`,`t1`.`location` AS `location`,`t1`.`location_lat` AS `location_lat`,`t1`.`location_lon` AS `location_lon`,`t1`.`notes` AS `notes`,`t1`.`chassis` AS `chassis`,`t1`.`model` AS `model`,`t1`.`hw_arch` AS `hw_arch`,`t1`.`vendor` AS `vendor`,`t1`.`contract_number` AS `contract_number`,`t1`.`installer_name` AS `installer_name`,`t1`.`deployment_status` AS `deployment_status`,`t1`.`url_a` AS `url_a`,`t1`.`url_b` AS `url_b`,`t1`.`url_c` AS `url_c`,`t1`.`host_networks` AS `host_networks`,`t1`.`host_netmask` AS `host_netmask`,`t1`.`host_router` AS `host_router`,`t1`.`oob_ip` AS `oob_ip`,`t1`.`oob_netmask` AS `oob_netmask`,`t1`.`oob_router` AS `oob_router`,`t1`.`date_hw_purchase` AS `date_hw_purchase`,`t1`.`date_hw_install` AS `date_hw_install`,`t1`.`date_hw_expiry` AS `date_hw_expiry`,`t1`.`date_hw_decomm` AS `date_hw_decomm`,`t1`.`site_address_a` AS `site_address_a`,`t1`.`site_address_b` AS `site_address_b`,`t1`.`site_address_c` AS `site_address_c`,`t1`.`site_city` AS `site_city`,`t1`.`site_state` AS `site_state`,`t1`.`site_country` AS `site_country`,`t1`.`site_zip` AS `site_zip`,`t1`.`site_rack` AS `site_rack`,`t1`.`site_notes` AS `site_notes`,`t1`.`poc_1_name` AS `poc_1_name`,`t1`.`poc_1_email` AS `poc_1_email`,`t1`.`poc_1_phone_a` AS `poc_1_phone_a`,`t1`.`poc_1_phone_b` AS `poc_1_phone_b`,`t1`.`poc_1_cell` AS `poc_1_cell`,`t1`.`poc_1_screen` AS `poc_1_screen`,`t1`.`poc_1_notes` AS `poc_1_notes`,`t1`.`poc_2_name` AS `poc_2_name`,`t1`.`poc_2_email` AS `poc_2_email`,`t1`.`poc_2_phone_a` AS `poc_2_phone_a`,`t1`.`poc_2_phone_b` AS `poc_2_phone_b`,`t1`.`poc_2_cell` AS `poc_2_cell`,`t1`.`poc_2_screen` AS `poc_2_screen`,`t1`.`poc_2_notes` AS `poc_2_notes` from (`datacheck` `t1` left join `alldata` `t2` on(`t1`.`hostid` = `t2`.`hostid`)) where `t2`.`hostid` is null */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-12 14:19:56
