/*
------------------------INFO---------------------------
1:Se deben borrar los archivos y carpetas de Migrations, exceptuando __init__.py  
en la Ruta:Process/core/migrations.
2:Crear el archivo de migración por consola con el comando:
python manage.py makemigrations
3:Crear base de datos arij con usuario SYS y otorgar privilegios.
4:Conectarse a la base de datos.
5:Migrar archivo de migrations a la base de datos utilizando el comando en consola django:
python manange.py migrations

**IMPORTANTE:Si modificamos el models.py y generamos un nuevo archivo de Migrations para
migrarlo a la base de datos y actualizarla, debemos Dropear todas las tablas de la BD con
el listado de comandos de abajo.

---------------------SYS-------------------------------
CREATE USER arij IDENTIFIED BY 123;
GRANT CONNECT, RESOURCE TO arij;
alter user arij default tablespace users quota unlimited on users;
commit;

---------------------CONEXIÓN--------------------------
NOMBRE: arij
'USER': arij
'PASSWORD':123
ROL:VALOR POR DEFECTO
SID: VACIO SIN TICKET
NOMBRE DEL SERVICIO: XEPDB1
*/ 

-------------------------DROPALL----------------------------
DROP TABLE "ARIJ"."AUTH_GROUP" CASCADE CONSTRAINTS;
DROP TABLE "ARIJ"."AUTH_GROUP_PERMISSIONS" CASCADE CONSTRAINTS;
DROP TABLE "ARIJ"."AUTH_PERMISSION" CASCADE CONSTRAINTS;
DROP TABLE "ARIJ"."AUTH_USER" CASCADE CONSTRAINTS;
DROP TABLE "ARIJ"."AUTH_USER_GROUPS" CASCADE CONSTRAINTS;
DROP TABLE "ARIJ"."AUTH_USER_USER_PERMISSIONS" CASCADE CONSTRAINTS;
DROP TABLE "ARIJ"."CORE_ROL" CASCADE CONSTRAINTS;
DROP TABLE "ARIJ"."CORE_USUARIO" CASCADE CONSTRAINTS;
DROP TABLE "ARIJ"."DJANGO_ADMIN_LOG" CASCADE CONSTRAINTS;
DROP TABLE "ARIJ"."DJANGO_CONTENT_TYPE" CASCADE CONSTRAINTS;
DROP TABLE "ARIJ"."DJANGO_MIGRATIONS" CASCADE CONSTRAINTS;
DROP TABLE "ARIJ"."DJANGO_SESSION" CASCADE CONSTRAINTS;
DROP TABLE "ARIJ"."CORE_COLUMNA" CASCADE CONSTRAINTS;
DROP TABLE "ARIJ"."CORE_COMENTARIO" CASCADE CONSTRAINTS;
DROP TABLE "ARIJ"."CORE_DOCUMENTO" CASCADE CONSTRAINTS;
DROP TABLE "ARIJ"."CORE_TABLERO" CASCADE CONSTRAINTS;
DROP TABLE "ARIJ"."CORE_TAREA" CASCADE CONSTRAINTS;
DROP TABLE "ARIJ"."CORE_TAREA_COLUMNA" CASCADE CONSTRAINTS;
DROP TABLE "ARIJ"."CORE_TAREA_TIPO" CASCADE CONSTRAINTS;
commit;
