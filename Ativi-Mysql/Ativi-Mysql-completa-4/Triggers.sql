-- --------------------------------------------------------------------------------------
-- Atividade 10 - CRUD com Triggers - Alterando estoque do produto na tabela produtos
--
-- Bruno Miranda
-- Daniele Nogueira
-- Diego Alves
-- Eduardo de Souza D'Antona
-- Robson Motta
-- Tais de Assis Santos
--
-- --------------------------------------------------------------------------------------

-- -------------------------------------------------------
-- 1. Criacao da base de dados atividade10
-- -------------------------------------------------------

create database if not exists atividade10;
use atividade10;

-- -------------------------------------------------------
-- 2. Criacao das tabelas
-- -------------------------------------------------------

create table if not exists produtos (
	id integer auto_increment primary key,
    descricao varchar(60) unique comment 'Descrição do produto',
    estoque integer not null comment 'Quantidade em estoque do produto' default 0
);

create table if not exists itensvenda (
	id integer auto_increment primary key,
    venda integer comment 'Permite repetir ID de venda em mais de um produto',
	produto integer comment 'Identificador do produto na tabela produto',
	quantidade integer comment 'Quantidade de itens vendidos'
);

-- -------------------------------------------------------
-- 3. Inserts nas tabelas
-- -------------------------------------------------------

insert into produtos(descricao, estoque) values
("Arroz", 30), 			# id 1
("Feijão", 22), 		# id 2
("Tomate", 41), 		# id 3
("Cebola", 33), 		# id 4
("Alface", 53), 		# id 5
("Beterraba", 40), 		# id 6
("Melão", 22), 			# id 7
("Banana",20), 			# id 8
("Limão", 30), 			# id 9
("Melancia", 30); 		# id 10

-- -------------------------------------------------------
-- 4. Triggers
-- -------------------------------------------------------

-- 4.1 Trigger Insert

DELIMITER $
			CREATE TRIGGER tgr_itensvenda_insert AFTER INSERT ON itensvenda
			FOR EACH ROW
				BEGIN
					UPDATE produtos SET estoque = estoque - New.quantidade 
						WHERE id = New.produto;
				END
$

DELIMITER ;

-- 4.2 Trigger Update

DELIMITER $
			CREATE TRIGGER tgr_itensvenda_update AFTER UPDATE ON itensvenda
			FOR EACH ROW
				BEGIN
							
					IF (OLD.quantidade > NEW.quantidade) THEN
						UPDATE produtos SET estoque = estoque - (NEW.quantidade - OLD.quantidade)
							WHERE id = OLD.produto;
					ELSE
						UPDATE produtos SET estoque = estoque + (NEW.quantidade - OLD.quantidade)
							WHERE id = OLD.produto;						
					END IF;

				END

$

DELIMITER ;


-- 4.3 Trigger Delete

DELIMITER $
			CREATE TRIGGER tgr_itensvenda_delete AFTER DELETE ON itensvenda
			FOR EACH ROW
				BEGIN
					UPDATE produtos SET estoque = estoque + OLD.quantidade 
						WHERE id = OLD.produto;
				END
$

DELIMITER ;

SHOW TRIGGERS;
-- -------------------------------------------------------
-- 5. CrUD
-- -------------------------------------------------------

-- 5.1 Insert

# Venda de 5 melancias
insert into itensvenda (venda, produto, quantidade) values (1, 10, 5);

# Venda de 2 limões
insert into itensvenda (venda, produto, quantidade) values (1, 9, 5);

# Venda de 5 arrozes (kkkk)
insert into itensvenda (venda, produto, quantidade) values (1, 1, 5);

-- 5.2 Select

select * from produtos;

-- 5.3 Update

# Decrementando o estoque na linha 107
update itensvenda set quantidade = 15 where id = 3;

-- 5.4 Delete

# Venda de 5 melancias
delete from itensvenda where id = 1;

# Venda de 2 limões
delete from itensvenda where id = 2;
