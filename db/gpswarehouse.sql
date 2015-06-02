-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 02-06-2015 a las 01:25:20
-- Versión del servidor: 5.6.17
-- Versión de PHP: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `gpswarehouse`
--
CREATE DATABASE IF NOT EXISTS `gpswarehouse` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `gpswarehouse`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `smartphonefixes`
--

DROP TABLE IF EXISTS `smartphonefixes`;
CREATE TABLE IF NOT EXISTS `smartphonefixes` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `idTrajectory` int(5) NOT NULL,
  `latitude` decimal(18,15) NOT NULL,
  `longitude` decimal(18,15) NOT NULL,
  `height` decimal(7,2) DEFAULT NULL,
  `accuracy` decimal(6,2) NOT NULL,
  `speed` decimal(5,2) DEFAULT NULL,
  `timestamp` datetime NOT NULL,
  `batteryLevel` decimal(5,2) NOT NULL,
  `voltage` decimal(7,2) NOT NULL,
  `status` varchar(12) NOT NULL,
  `temperature` decimal(5,2) NOT NULL,
  `plugged` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `trajectories`
--

DROP TABLE IF EXISTS `trajectories`;
CREATE TABLE IF NOT EXISTS `trajectories` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `idUser` int(5) NOT NULL,
  `startTime` datetime NOT NULL,
  `endTime` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Volcado de datos para la tabla `trajectories`
--

INSERT INTO `trajectories` (`id`, `idUser`, `startTime`, `endTime`) VALUES
(1, 1, '2015-06-01 16:00:00', '2015-06-01 17:30:30');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
