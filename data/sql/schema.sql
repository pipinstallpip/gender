-- MySQL Script generated by MySQL Workbench
-- mar 10 mar 2020 23:18:04 CET
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema Gender
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Gender
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Gender` DEFAULT CHARACTER SET utf8 ;
USE `Gender` ;

-- -----------------------------------------------------
-- Table `Gender`.`country`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gender`.`country` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `value` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Gender`.`name`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gender`.`name` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `value` VARCHAR(45) NULL,
  `gender` BIT NOT NULL DEFAULT 0->male 1->female,
  `country_id` INT NOT NULL,
  PRIMARY KEY (`id`, `country_id`),
  INDEX `fk_name_country_idx` (`country_id` ASC),
  UNIQUE INDEX `unique_fields` (`value` ASC, `gender` ASC, `country_id` ASC),
  CONSTRAINT `fk_name_country`
    FOREIGN KEY (`country_id`)
    REFERENCES `Gender`.`country` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
