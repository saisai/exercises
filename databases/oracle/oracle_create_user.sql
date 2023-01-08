--------------------------------------
----- CODENCURSOR YOUTUBE CHANNEL ----
--------------------------------------

-- SCRIPT TO GRANT PRIVILEGES TO USER 

-- USER SQL
CREATE USER user_name IDENTIFIED BY password DEFAULT TABLESPACE USERS QUOTA UNLIMITED ON USERS ;

-- ROLES
GRANT "IMP_FULL_DATABASE" TO user_name ;
GRANT "EXP_FULL_DATABASE" TO user_name ;
GRANT "OLAP_DBA" TO user_name ;
GRANT "CONNECT" TO user_name ;
GRANT "RESOURCE" TO user_name ;
GRANT "DATAPUMP_EXP_FULL_DATABASE" TO user_name ;
GRANT "DATAPUMP_IMP_FULL_DATABASE" TO user_name ;
GRANT "SPATIAL_CSW_ADMIN" TO user_name ;
GRANT "SPATIAL_WFS_ADMIN" TO user_name ;
GRANT "OLAP_USER" TO user_name ;
GRANT "AUTHENTICATEDUSER" TO user_name ;

-- SYSTEM PRIVILEGES
GRANT EXECUTE ANY EVALUATION CONTEXT TO user_name ;
GRANT ALTER ANY OPERATOR TO user_name ;
GRANT CREATE INDEXTYPE TO user_name ;
GRANT ALTER DATABASE TO user_name ;
GRANT UPDATE ANY TABLE TO user_name ;
GRANT CREATE MINING MODEL TO user_name ;
GRANT ALTER ANY OUTLINE TO user_name ;
GRANT SELECT ANY SEQUENCE TO user_name ;
GRANT DROP ANY CUBE DIMENSION TO user_name ;
GRANT EXECUTE ANY OPERATOR TO user_name ;
GRANT DROP ANY VIEW TO user_name ;
GRANT IMPORT FULL DATABASE TO user_name ;
GRANT DROP ANY INDEX TO user_name ;
GRANT CREATE ANY PROCEDURE TO user_name ;
GRANT EXECUTE ASSEMBLY TO user_name ;
GRANT ALTER ANY INDEX TO user_name ;
GRANT UPDATE ANY CUBE DIMENSION TO user_name ;
GRANT EXECUTE ANY LIBRARY TO user_name ;
GRANT DROP ANY MINING MODEL TO user_name ;
GRANT INSERT ANY TABLE TO user_name ;
GRANT EXECUTE ANY PROGRAM TO user_name ;
GRANT UNDER ANY VIEW TO user_name ;
GRANT ALTER ANY INDEXTYPE TO user_name ;
GRANT DELETE ANY TABLE TO user_name ;
GRANT ANALYZE ANY TO user_name ;
GRANT UPDATE ANY CUBE BUILD PROCESS TO user_name ;
GRANT DROP ANY CUBE BUILD PROCESS TO user_name ;
GRANT UPDATE ANY CUBE TO user_name ;
GRANT CREATE ANY CUBE TO user_name ;
GRANT DROP ANY OPERATOR TO user_name ;
GRANT CREATE ANY OUTLINE TO user_name ;
GRANT ALTER ANY PROCEDURE TO user_name ;
GRANT INSERT ANY CUBE DIMENSION TO user_name ;
GRANT SELECT ANY TABLE TO user_name ;
GRANT CREATE MATERIALIZED VIEW TO user_name ;
GRANT DELETE ANY CUBE DIMENSION TO user_name ;
GRANT QUERY REWRITE TO user_name ;
GRANT CREATE ROLLBACK SEGMENT TO user_name ;
GRANT CREATE CUBE TO user_name ;
GRANT DROP ANY TABLE TO user_name ;
GRANT EXECUTE ANY ASSEMBLY TO user_name ;
GRANT CREATE SEQUENCE TO user_name ;
GRANT FLASHBACK ANY TABLE TO user_name ;
GRANT SELECT ANY CUBE DIMENSION TO user_name ;
GRANT CREATE ANY MATERIALIZED VIEW TO user_name ;
GRANT DROP ANY TRIGGER TO user_name ;
GRANT ALTER ANY CUBE DIMENSION TO user_name ;
GRANT SELECT ANY CUBE TO user_name ;
GRANT CREATE ANY TABLE TO user_name ;
GRANT CREATE EVALUATION CONTEXT TO user_name ;
GRANT CREATE CUBE BUILD PROCESS TO user_name ;
GRANT FORCE TRANSACTION TO user_name ;
GRANT DROP ANY PROCEDURE TO user_name ;
GRANT CREATE DIMENSION TO user_name ;
GRANT CREATE ANY INDEXTYPE TO user_name ;
GRANT CREATE ANY TYPE TO user_name ;
GRANT BACKUP ANY TABLE TO user_name ;
GRANT ALTER ANY TYPE TO user_name ;
GRANT UNDER ANY TYPE TO user_name ;
GRANT SELECT ANY TRANSACTION TO user_name ;
GRANT CREATE CUBE DIMENSION TO user_name ;
GRANT CREATE ANY INDEX TO user_name ;
GRANT EXECUTE ANY INDEXTYPE TO user_name ;
GRANT CREATE TABLE TO user_name ;
GRANT EXECUTE ANY PROCEDURE TO user_name ;
GRANT DROP ANY CUBE TO user_name ;
GRANT INSERT ANY MEASURE FOLDER TO user_name ;
GRANT CREATE ANY MEASURE FOLDER TO user_name ;
GRANT COMMENT ANY TABLE TO user_name ;
GRANT CREATE ANY CUBE DIMENSION TO user_name ;
GRANT CREATE ANY EVALUATION CONTEXT TO user_name ;
GRANT ALTER ANY EVALUATION CONTEXT TO user_name ;
GRANT CREATE ANY MINING MODEL TO user_name ;
GRANT FORCE ANY TRANSACTION TO user_name ;
GRANT SELECT ANY DICTIONARY TO user_name ;
GRANT EXECUTE ANY CLASS TO user_name ;
GRANT EXECUTE ANY TYPE TO user_name ;
GRANT EXECUTE ANY RULE TO user_name ;
GRANT ALTER ANY DIMENSION TO user_name ;
GRANT EXECUTE ANY RULE SET TO user_name ;
GRANT ALTER ANY TABLE TO user_name ;
GRANT DROP ANY DIRECTORY TO user_name ;
GRANT DROP ANY DIMENSION TO user_name ;
GRANT EXPORT FULL DATABASE TO user_name ;
GRANT READ ANY FILE GROUP TO user_name ;
GRANT CREATE PUBLIC SYNONYM TO user_name ;
GRANT CREATE TABLESPACE TO user_name ;
GRANT DROP ANY OUTLINE TO user_name ;
GRANT ALTER ANY MATERIALIZED VIEW TO user_name ;
GRANT DROP ANY INDEXTYPE TO user_name ;
GRANT SELECT ANY MINING MODEL TO user_name ;
GRANT COMMENT ANY MINING MODEL TO user_name ;
GRANT CREATE ANY DIMENSION TO user_name ;
GRANT ALTER ANY MINING MODEL TO user_name ;
GRANT CREATE ANY VIEW TO user_name ;
GRANT CREATE VIEW TO user_name ;
GRANT DROP ANY MATERIALIZED VIEW TO user_name ;
GRANT CREATE ANY CUBE BUILD PROCESS TO user_name ;
GRANT UNDER ANY TABLE TO user_name ;
GRANT DROP ANY MEASURE FOLDER TO user_name ;
GRANT CREATE PROCEDURE TO user_name ;
GRANT ALTER ANY CUBE TO user_name ;

COMMIT;

-- from https://www.youtube.com/watch?v=s0Qmc9WwoEk&ab_channel=CodeNCursor