-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema motionai
-- -----------------------------------------------------
-- 모션 디퓨전 데이터베이스 

-- -----------------------------------------------------
-- Schema motionai
--
-- 모션 디퓨전 데이터베이스 
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `motionai` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;
USE `motionai` ;

-- -----------------------------------------------------
-- Table `motionai`.`mo_dataset`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `motionai`.`mo_dataset` (
  `idx` CHAR(6) NOT NULL,
  `kind` INT NOT NULL COMMENT '1: humanml\n2: kit \n3: custom ',
  `desceng` VARCHAR(2048) NOT NULL COMMENT '동작설명 영문 ',
  `deschan` VARCHAR(2048) NOT NULL COMMENT '동작설명 한글',
  `frame` INT NOT NULL COMMENT '프레임수',
  `time` VARCHAR(10) NOT NULL COMMENT '모션 프레임 시간, MM:SS 형식',
  PRIMARY KEY (`idx`, `kind`),
  UNIQUE INDEX `idx_UNIQUE` (`idx` ASC) )
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
