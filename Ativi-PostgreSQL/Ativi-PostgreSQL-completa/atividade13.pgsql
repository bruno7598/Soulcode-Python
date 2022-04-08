-- ---------------------------------------------------
-- CRIANDO AS TABELAS PARA A ATIVIDADE 13
-- --------------------------------------------------
CREATE TABLE informa (
    id_dados serial not NULL,
    DATA VARCHAR(100),
    valor NUMERIC
);


SELECT * from informa;
insert into informa (data, valor) VALUES ('11/23/2021', -314);
-- ---------------------------------------------------
-- CRIANDO A TABELA LOG PARA REGISTRAR AS INFORMAÇÕES SOLICITADAS
-- ---------------------------------------------------
CREATE OR REPLACE FUNCTION TGR_trabalho()
    RETURNS TRIGGER AS $$
        BEGIN
            IF (TG_OP = 'INSERT') THEN
            INSERT INTO LOG_trabalho(usuario, dia, dados_registro) VALUES (CURRENT_USER, CURRENT_TIMESTAMP, 'Inclusão realizada. ' || NEW.* || ' .' );
            RETURN NEW;
            ELSIF (TG_OP = 'UPDATE') THEN
            INSERT INTO LOG_trabalho(usuario, dia, dados_registro) VALUES (CURRENT_USER, CURRENT_TIMESTAMP, 'Alteração realizada. Operação antiga: ' || OLD.* || ' para nova operação ' || NEW.* || ' .' );
            RETURN NEW;
            ELSIF (TG_OP = 'DELETE') THEN
            INSERT INTO LOG_trabalho(usuario, dia, dados_registro) VALUES (CURRENT_USER, CURRENT_TIMESTAMP, 'Deleção realizada. Operação deletada: ' || OLD.* || ' .' );
            RETURN OLD;
            END IF;
        RETURN NULL;
    END;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER log_trabalho
AFTER INSERT OR UPDATE OR DELETE ON informa
FOR EACH ROW
EXECUTE PROCEDURE TGR_trabalho();



CREATE TABLE log_trabalho (
    id_log serial,
    usuario varchar,
    dia varchar,
    dados_registro varchar
);


SELECT * FROM log_trabalho;
SELECT dados_registro from log_trabalho WHERE id_log BETWEEN 1 and 10;

-- ---------------------------------------------------
-- CRIANDO AS TABELAS PARA SEPARAR OS BLOCOS POR ELA COM O TYPE
-- ---------------------------------------------------
CREATE OR REPLACE FUNCTION TGR_dados()
    RETURNS TRIGGER AS $$
        BEGIN
            IF (TG_OP = 'INSERT') THEN
            INSERT INTO LOG_trabalho(usuario, dia, dados_registro) VALUES (CURRENT_USER, CURRENT_TIMESTAMP, 'Inclusão realizada. ' || NEW.* || ' .' );
            RETURN NEW;
            ELSIF (TG_OP = 'UPDATE') THEN
            INSERT INTO LOG_trabalho(usuario, dia, dados_registro) VALUES (CURRENT_USER, CURRENT_TIMESTAMP, 'Alteração realizada. Operação antiga: ' || OLD.* || ' para nova operação ' || NEW.* || ' .' );
            RETURN NEW;
            ELSIF (TG_OP = 'DELETE') THEN
            INSERT INTO LOG_trabalho(usuario, dia, dados_registro) VALUES (CURRENT_USER, CURRENT_TIMESTAMP, 'Deleção realizada. Operação deletada: ' || OLD.* || ' .' );
            RETURN OLD;
            END IF;
        RETURN NULL;
    END;
$$
LANGUAGE 'plpgsql';


CREATE TRIGGER log_dados
AFTER INSERT OR UPDATE OR DELETE ON dados
FOR EACH ROW
EXECUTE PROCEDURE TGR_dados();




CREATE TABLE dados (
    data_final varchar,
    calculos operacoes
);

CREATE TYPE operacoes as (
    media integer,
    mediana integer,
    moda varchar,
    desvio_prad integer,
    maior integer,
    menor integer
);



SELECT * from dados;

SELECT data_final, (calculos).media, (calculos).mediana, (calculos).moda,(calculos).desvio_prad,(calculos).maior, (calculos).menor  from dados order by data;