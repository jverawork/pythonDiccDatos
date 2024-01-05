from datetime import datetime

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'




class CmdBasesdatosT(models.Model):
    TIPBDD = (
        ('1', 'Under 09s'),
        ('2', 'Under 10s'),
        ('3', 'Under 11s')
    )

    TIPESTADOS = (
        ('A', 'Activo'),
        ('I', 'Inactivo')
    )

    #id_bd = models.DecimalField(db_column='ID_BD', max_digits=38, decimal_places=0)  # Field name made lowercase.
    id_bd = models.AutoField(db_column='ID_BD',primary_key=True)
    cod_bd = models.TextField(db_column='COD_BD', help_text = "Codigo de la Bdd")  # Field name made lowercase. This field type is a guess.
    descripcion = models.TextField(db_column='DESCRIPCION')  # Field name made lowercase. This field type is a guess.
    estado = models.TextField(db_column='ESTADO', default = 'A', choices=TIPESTADOS)  # Field name made lowercase. This field type is a guess.
    tipo_bd = models.CharField(db_column='TIPO_BD', max_length=30, choices=TIPBDD)  # Field name made lowercase.
    bd_default = models.CharField(db_column='BD_DEFAULT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', default = datetime.now())  # Field name made lowercase.
    usu_creacion = models.CharField(db_column='USU_CREACION', max_length=30)  # Field name made lowercase.
    ip_equipo = models.CharField(db_column='IP_EQUIPO', max_length=40)  # Field name made lowercase.

    def __str__(self):
        return str(self.id_bd)
    
    def get_absolute_url(self):
        #Devuelve la url para acceder a una instancia particular del modelo.
        return reverse('model-detail-view', args=[str(self.id)])
    
    class Meta:
        managed = False
        db_table = 'CMD_BASESDATOS_T'


class CmdCatalogosdetTp(models.Model):
    cod_item = models.CharField(db_column='COD_ITEM', max_length=30)  # Field name made lowercase.
    cod_catalogo = models.CharField(db_column='COD_CATALOGO', max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=1000)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=1)  # Field name made lowercase.
    usu_creacion = models.CharField(db_column='USU_CREACION', max_length=30)  # Field name made lowercase.
    fec_creacion = models.TimeField(db_column='FEC_CREACION')  # Field name made lowercase.
    ip_equipo = models.CharField(db_column='IP_EQUIPO', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CMD_CATALOGOSDET_TP'


class CmdCatalogosTp(models.Model):
    cod_catalogo = models.CharField(db_column='COD_CATALOGO', max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=120)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=1)  # Field name made lowercase.
    usu_creacion = models.CharField(db_column='USU_CREACION', max_length=30)  # Field name made lowercase.
    fec_creacion = models.TimeField(db_column='FEC_CREACION', primary_key=True)  # Field name made lowercase.
    ip_equipo = models.CharField(db_column='IP_EQUIPO', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CMD_CATALOGOS_TP'


class CmdCompswxsistemaT(models.Model):
    cod_componente = models.CharField(db_column='COD_COMPONENTE', max_length=250)  # Field name made lowercase.
    id_sistema = models.DecimalField(db_column='ID_SISTEMA', max_digits=38, decimal_places=0)  # Field name made lowercase.
    fec_creacion = models.TimeField(db_column='FEC_CREACION')  # Field name made lowercase.
    usu_creacion = models.CharField(db_column='USU_CREACION', max_length=30)  # Field name made lowercase.
    ip_equipo = models.CharField(db_column='IP_EQUIPO', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CMD_COMPSWXSISTEMA_T'


class CmdCompswT(models.Model):
    cod_componente = models.CharField(db_column='COD_COMPONENTE', max_length=250)  # Field name made lowercase.
    estado_dd = models.CharField(db_column='ESTADO_DD', max_length=3)  # Field name made lowercase.
    nombre_componente = models.CharField(db_column='NOMBRE_COMPONENTE', max_length=250)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=3000)  # Field name made lowercase.
    version = models.CharField(db_column='VERSION', max_length=20)  # Field name made lowercase.
    usu_creacion = models.CharField(db_column='USU_CREACION', max_length=30)  # Field name made lowercase.
    fec_creacion = models.TimeField(db_column='FEC_CREACION')  # Field name made lowercase.
    ip_equipo = models.CharField(db_column='IP_EQUIPO', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CMD_COMPSW_T'


class CmdDasobjxsistemaT(models.Model):
    id_objxsis = models.DecimalField(db_column='ID_OBJXSIS', max_digits=38, decimal_places=0)  # Field name made lowercase.
    id_sistema = models.DecimalField(db_column='ID_SISTEMA', max_digits=38, decimal_places=0)  # Field name made lowercase.
    id_bd = models.DecimalField(db_column='ID_BD', max_digits=38, decimal_places=0)  # Field name made lowercase.
    cod_esquema = models.CharField(db_column='COD_ESQUEMA', max_length=60)  # Field name made lowercase.
    cod_objeto = models.CharField(db_column='COD_OBJETO', max_length=500)  # Field name made lowercase.
    tipo_objeto = models.CharField(db_column='TIPO_OBJETO', max_length=60)  # Field name made lowercase.
    desc_objeto = models.CharField(db_column='DESC_OBJETO', max_length=500)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=1)  # Field name made lowercase.
    fuente = models.CharField(db_column='FUENTE', max_length=5)  # Field name made lowercase.
    estado_dd = models.CharField(db_column='ESTADO_DD', max_length=3)  # Field name made lowercase.
    fec_creacion = models.TimeField(db_column='FEC_CREACION')  # Field name made lowercase.
    usu_creacion = models.CharField(db_column='USU_CREACION', max_length=30)  # Field name made lowercase.
    ip_equipo = models.CharField(db_column='IP_EQUIPO', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CMD_DASOBJXSISTEMA_T'


class CmdDasusrxsistemaT(models.Model):
    id_usr = models.CharField(db_column='ID_USR', max_length=20)  # Field name made lowercase.
    id_sistema = models.DecimalField(db_column='ID_SISTEMA', max_digits=38, decimal_places=0)  # Field name made lowercase.
    id_instancia = models.DecimalField(db_column='ID_INSTANCIA', max_digits=38, decimal_places=0)  # Field name made lowercase.
    cod_esquema = models.CharField(db_column='COD_ESQUEMA', max_length=60)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=1)  # Field name made lowercase.
    fec_creacion = models.TimeField(db_column='FEC_CREACION')  # Field name made lowercase.
    usu_creacion = models.CharField(db_column='USU_CREACION', max_length=30)  # Field name made lowercase.
    ip_equipo = models.CharField(db_column='IP_EQUIPO', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CMD_DASUSRXSISTEMA_T'


class CmdEsquemasT(models.Model):
    id_bd = models.DecimalField(db_column='ID_BD', max_digits=38, decimal_places=0)  # Field name made lowercase.
    cod_esquema = models.CharField(db_column='COD_ESQUEMA', max_length=60)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=500)  # Field name made lowercase.
    tipo_esquema = models.CharField(db_column='TIPO_ESQUEMA', max_length=10)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=1)  # Field name made lowercase.
    usu_creacion = models.CharField(db_column='USU_CREACION', max_length=30)  # Field name made lowercase.
    fec_creacion = models.TimeField(db_column='FEC_CREACION')  # Field name made lowercase.
    ip_equipo = models.CharField(db_column='IP_EQUIPO', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CMD_ESQUEMAS_T'


class CmdObjbddetT(models.Model):
    id_bd = models.DecimalField(db_column='ID_BD', max_digits=38, decimal_places=0)  # Field name made lowercase.
    cod_esquema_det = models.CharField(db_column='COD_ESQUEMA_DET', max_length=60)  # Field name made lowercase.
    cod_objeto_det = models.CharField(db_column='COD_OBJETO_DET', max_length=500)  # Field name made lowercase.
    cod_esquema_padre = models.CharField(db_column='COD_ESQUEMA_PADRE', max_length=60)  # Field name made lowercase.
    cod_objeto_padre = models.CharField(db_column='COD_OBJETO_PADRE', max_length=500)  # Field name made lowercase.
    tipo_objeto = models.CharField(db_column='TIPO_OBJETO', max_length=60)  # Field name made lowercase.
    estado_dd = models.CharField(db_column='ESTADO_DD', max_length=1)  # Field name made lowercase.
    fec_ultimo_ddl = models.TimeField(db_column='FEC_ULTIMO_DDL', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=1)  # Field name made lowercase.
    usu_creacion = models.CharField(db_column='USU_CREACION', max_length=30)  # Field name made lowercase.
    fec_creacion = models.TimeField(db_column='FEC_CREACION')  # Field name made lowercase.
    ip_equipo = models.CharField(db_column='IP_EQUIPO', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CMD_OBJBDDET_T'


class CmdObjbdT(models.Model):
    id_bd = models.DecimalField(db_column='ID_BD', max_digits=38, decimal_places=0)  # Field name made lowercase.
    cod_esquema = models.CharField(db_column='COD_ESQUEMA', max_length=60)  # Field name made lowercase.
    cod_objeto = models.CharField(db_column='COD_OBJETO', max_length=500)  # Field name made lowercase.
    tipo_objeto = models.CharField(db_column='TIPO_OBJETO', max_length=60)  # Field name made lowercase.
    estado_dd = models.CharField(db_column='ESTADO_DD', max_length=1)  # Field name made lowercase.
    fec_ultimo_ddl = models.TimeField(db_column='FEC_ULTIMO_DDL')  # Field name made lowercase.
    usu_creacion = models.CharField(db_column='USU_CREACION', max_length=30)  # Field name made lowercase.
    fec_creacion = models.TimeField(db_column='FEC_CREACION')  # Field name made lowercase.
    ip_equipo = models.CharField(db_column='IP_EQUIPO', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CMD_OBJBD_T'


class CmdObjxcompswT(models.Model):
    id_objxcompsw = models.DecimalField(db_column='ID_OBJXCOMPSW', max_digits=38, decimal_places=0)  # Field name made lowercase.
    cod_componente = models.CharField(db_column='COD_COMPONENTE', max_length=250)  # Field name made lowercase.
    id_bd = models.DecimalField(db_column='ID_BD', max_digits=38, decimal_places=0)  # Field name made lowercase.
    cod_esquema = models.CharField(db_column='COD_ESQUEMA', max_length=60)  # Field name made lowercase.
    cod_objeto = models.CharField(db_column='COD_OBJETO', max_length=500)  # Field name made lowercase.
    tipo_objeto = models.CharField(db_column='TIPO_OBJETO', max_length=60)  # Field name made lowercase.
    desc_objeto = models.CharField(db_column='DESC_OBJETO', max_length=500)  # Field name made lowercase.
    est_obj_sist = models.CharField(db_column='EST_OBJ_SIST', max_length=1)  # Field name made lowercase.
    fuente = models.CharField(db_column='FUENTE', max_length=5)  # Field name made lowercase.
    estado_dd = models.CharField(db_column='ESTADO_DD', max_length=3)  # Field name made lowercase.
    usu_creacion = models.CharField(db_column='USU_CREACION', max_length=30)  # Field name made lowercase.
    fec_creacion = models.TimeField(db_column='FEC_CREACION')  # Field name made lowercase.
    ip_equipo = models.CharField(db_column='IP_EQUIPO', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CMD_OBJXCOMPSW_T'


class CmdParametrosTp(models.Model):
    id_parametro = models.DecimalField(db_column='ID_PARAMETRO', max_digits=38, decimal_places=0)  # Field name made lowercase.
    cod_parametro = models.CharField(db_column='COD_PARAMETRO', max_length=10)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=100)  # Field name made lowercase.
    valor1 = models.CharField(db_column='VALOR1', max_length=300)  # Field name made lowercase.
    valor2 = models.CharField(db_column='VALOR2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    ejecucion = models.CharField(db_column='EJECUCION', max_length=1)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=1)  # Field name made lowercase.
    usu_creacion = models.CharField(db_column='USU_CREACION', max_length=30)  # Field name made lowercase.
    fec_creacion = models.TimeField(db_column='FEC_CREACION')  # Field name made lowercase.
    ip_equipo = models.CharField(db_column='IP_EQUIPO', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CMD_PARAMETROS_TP'


class CmdSistemasT(models.Model):
    id_sistema = models.DecimalField(db_column='ID_SISTEMA', max_digits=38, decimal_places=0)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=500)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=1000)  # Field name made lowercase.
    codapli = models.CharField(db_column='CODAPLI', max_length=60, blank=True, null=True)  # Field name made lowercase.
    estado_sistema = models.CharField(db_column='ESTADO_SISTEMA', max_length=1)  # Field name made lowercase.
    cod_cat_modulo = models.CharField(db_column='COD_CAT_MODULO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cod_modulo = models.CharField(db_column='COD_MODULO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    modulo_web = models.CharField(db_column='MODULO_WEB', max_length=250, blank=True, null=True)  # Field name made lowercase.
    usu_creacion = models.CharField(db_column='USU_CREACION', max_length=30)  # Field name made lowercase.
    fec_creacion = models.TimeField(db_column='FEC_CREACION')  # Field name made lowercase.
    ip_equipo = models.CharField(db_column='IP_EQUIPO', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CMD_SISTEMAS_T'


class CmdUsuxcompswT(models.Model):
    id_usu = models.CharField(db_column='ID_USU', max_length=38, blank=True, null=True)  # Field name made lowercase.
    id_bd = models.CharField(db_column='ID_BD', max_length=38, blank=True, null=True)  # Field name made lowercase.
    cod_esquema = models.CharField(db_column='COD_ESQUEMA', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_componente = models.CharField(db_column='COD_COMPONENTE', max_length=250, blank=True, null=True)  # Field name made lowercase.
    jndi = models.CharField(db_column='JNDI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pool_name = models.CharField(db_column='POOL_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fec_creacion = models.TimeField(db_column='FEC_CREACION', blank=True, null=True)  # Field name made lowercase.
    usu_creacion = models.CharField(db_column='USU_CREACION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_equipo = models.CharField(db_column='IP_EQUIPO', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CMD_USUXCOMPSW_T'




