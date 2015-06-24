-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-06-2015 a las 18:52:52
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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `smartphonefixes`
--

CREATE TABLE IF NOT EXISTS `smartphonefixes` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `idTrajectory` int(5) NOT NULL,
  `obtained` tinyint(1) NOT NULL,
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
  PRIMARY KEY (`id`),
  KEY `fk_PerTrajectories` (`idTrajectory`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=13497 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `trajectories`
--

CREATE TABLE IF NOT EXISTS `trajectories` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `idUser` int(5) NOT NULL,
  `startTime` datetime NOT NULL,
  `endTime` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=21 ;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `smartphonefixes`
--
ALTER TABLE `smartphonefixes`
  ADD CONSTRAINT `fk_PerTrajectories` FOREIGN KEY (`idTrajectory`) REFERENCES `trajectories` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
