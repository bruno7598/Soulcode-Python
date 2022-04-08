-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema boasaude
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema boasaude
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `boasaude` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `boasaude` ;

-- -----------------------------------------------------
-- Table `boasaude`.`itensvenda`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `boasaude`.`itensvenda` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `venda` INT NULL DEFAULT NULL COMMENT 'Permite repetir ID de venda em mais de um produto',
  `produto` INT NULL DEFAULT NULL COMMENT 'Identificador do produto na tabela produto',
  `quantidade` INT NULL DEFAULT NULL COMMENT 'Quantidade de itens vendidos',
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 17
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `boasaude`.`produtos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `boasaude`.`produtos` (
  `referencia` VARCHAR(3) NOT NULL,
  `descricao` VARCHAR(60) NULL DEFAULT NULL,
  `Estoque` INT NOT NULL DEFAULT '0',
  PRIMARY KEY (`referencia`),
  UNIQUE INDEX `descricao` (`descricao` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


INSERT INTO produtos (referencia, descricao, Estoque) VALUES 
(1,	"Arroz", 35),
(2,	"alface" ,20);