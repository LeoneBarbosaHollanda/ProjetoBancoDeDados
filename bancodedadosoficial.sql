-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema bancodedadosoficial
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema bancodedadosoficial
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bancodedadosoficial` DEFAULT CHARACTER SET utf8mb3 ;
USE `bancodedadosoficial` ;

-- -----------------------------------------------------
-- Table `bancodedadosoficial`.`pessoa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bancodedadosoficial`.`pessoa` (
  `Conta` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `Agencia` INT NOT NULL,
  `RG` BIGINT NOT NULL,
  `SaldoConta` INT NOT NULL,
  `Senha` VARCHAR(45) NOT NULL,
  `CPF` BIGINT NOT NULL,
  PRIMARY KEY (`Conta`, `CPF`),
  UNIQUE INDEX `Conta_UNIQUE` (`Conta` ASC) VISIBLE,
  UNIQUE INDEX `CPF_UNIQUE` (`CPF` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 84
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `bancodedadosoficial`.`emprestimo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bancodedadosoficial`.`emprestimo` (
  `idEMPRESTIMO` INT NOT NULL AUTO_INCREMENT,
  `VALOR` FLOAT NOT NULL,
  `PARCELA` INT NOT NULL,
  `dataEmprestimo` DATE NOT NULL,
  `CPF` BIGINT NOT NULL,
  PRIMARY KEY (`idEMPRESTIMO`),
  INDEX `fk_emprestimo_pessoa_idx` (`CPF` ASC) VISIBLE,
  CONSTRAINT `fk_emprestimo_pessoa`
    FOREIGN KEY (`CPF`)
    REFERENCES `bancodedadosoficial`.`pessoa` (`CPF`))
ENGINE = InnoDB
AUTO_INCREMENT = 10
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `bancodedadosoficial`.`pagamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bancodedadosoficial`.`pagamento` (
  `idPAGAMENTO` INT NOT NULL AUTO_INCREMENT,
  `PREÇO` INT NOT NULL,
  `dataPagamento` DATE NULL DEFAULT NULL,
  `CPF` BIGINT NOT NULL,
  PRIMARY KEY (`idPAGAMENTO`),
  INDEX `fk_pagamento_pessoa1_idx` (`CPF` ASC) VISIBLE,
  CONSTRAINT `fk_pagamento_pessoa1`
    FOREIGN KEY (`CPF`)
    REFERENCES `bancodedadosoficial`.`pessoa` (`CPF`))
ENGINE = InnoDB
AUTO_INCREMENT = 16
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `bancodedadosoficial`.`recebimento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bancodedadosoficial`.`recebimento` (
  `idRECEBIMENTO` INT NOT NULL AUTO_INCREMENT,
  `PREÇO` INT NOT NULL,
  `dataRecebimento` DATE NOT NULL,
  `CPF` BIGINT NOT NULL,
  PRIMARY KEY (`idRECEBIMENTO`),
  INDEX `fk_recebimento_pessoa1_idx` (`CPF` ASC) VISIBLE,
  CONSTRAINT `fk_recebimento_pessoa1`
    FOREIGN KEY (`CPF`)
    REFERENCES `bancodedadosoficial`.`pessoa` (`CPF`))
ENGINE = InnoDB
AUTO_INCREMENT = 52
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
