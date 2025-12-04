DROP DATABASE IF EXISTS pokemon_db;
CREATE DATABASE IF NOT EXISTS pokemon_db DEFAULT CHARACTER SET utf8 ;
USE pokemon_db ;


-- -----------------------------------------------------
-- Table `pokemon`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pokemon` (
  `codigo_pokemon` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(200) NOT NULL,
  `descripcion` TEXT NULL,
  `nivel` INT NULL DEFAULT 1,
  `fecha_creacion` DATE NOT NULL,
  PRIMARY KEY (`codigo_pokemon`)
);


-- -----------------------------------------------------
-- Table `tipo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tipo` (
  `codigo_tipo` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`codigo_tipo`)
);


-- -----------------------------------------------------
-- Table `pokemon_x_tipo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pokemon_x_tipo` (
  `codigo_pokemon` INT NOT NULL,
  `codigo_tipo` INT NOT NULL,
  PRIMARY KEY (`codigo_pokemon`, `codigo_tipo`),
  INDEX `fk_pokemon_has_tipo_tipo1_idx` (`codigo_tipo` ASC) VISIBLE,
  INDEX `fk_pokemon_has_tipo_pokemon_idx` (`codigo_pokemon` ASC) VISIBLE,
  CONSTRAINT `fk_pokemon_has_tipo_pokemon`
    FOREIGN KEY (`codigo_pokemon`)
    REFERENCES `pokemon` (`codigo_pokemon`),
  CONSTRAINT `fk_pokemon_has_tipo_tipo1`
    FOREIGN KEY (`codigo_tipo`)
    REFERENCES `tipo` (`codigo_tipo`)
);
