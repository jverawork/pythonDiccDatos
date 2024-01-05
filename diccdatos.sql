drop table cmdb_owner.CMD_BASESDATOS_T;

CREATE TABLE cmdb_owner.CMD_COMPSWXSISTEMA_T
(
  COD_COMPONENTE VARCHAR(250)
, ID_SISTEMA NUMERIC(38, 0)
, FEC_CREACION TIMESTAMP
, USU_CREACION VARCHAR(30)
, IP_EQUIPO VARCHAR(40)
)
;

SELECT 1
        FROM information_schema.tables 
        WHERE table_schema = 'cmdb_owner' -- Reemplaza 'esquema' con tu esquema específico
        AND table_name = 'CMD_LOGS_T'
        
select * from CMD_BASESDATOS_T;

select * from CMD_CATALOGOS_TP;

select * from CMD_CATALOGOSDET_TP;

select * from CMD_LOGS_T;

select * from CCMD_COMPSW_T;



