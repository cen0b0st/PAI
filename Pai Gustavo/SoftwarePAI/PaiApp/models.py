from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cargo(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    nombre_cargo = models.CharField(max_length=50)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cargo'


class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categoria'


class CierreMensual(models.Model):
    id_cierre_mensual = models.IntegerField(primary_key=True)
    fecha_cierre_mensual = models.DateField()
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cierre_mensual'


class CierreMensualInsumo(models.Model):
    id_cierre_mensual_insumo = models.IntegerField(primary_key=True)
    saldo = models.IntegerField()
    precio = models.FloatField()
    estado = models.IntegerField()
    fk_id_cierre_mensual = models.ForeignKey(CierreMensual, models.DO_NOTHING, db_column='fk_id_cierre_mensual')
    fk_id_insumos = models.ForeignKey('Insumos', models.DO_NOTHING, db_column='fk_id_insumos')
    fk_id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='fk_id_categoria')

    class Meta:
        managed = False
        db_table = 'cierre_mensual_insumo'


class Compra(models.Model):
    id_compra = models.IntegerField(primary_key=True)
    fecha_compra = models.DateField()
    guia = models.CharField(max_length=50)
    orden_de_compra = models.CharField(max_length=50)
    rut_proveedor = models.CharField(max_length=50)
    nombre_proveedor = models.CharField(max_length=50)
    total_compra = models.IntegerField()
    descuento = models.IntegerField()
    fecha_omgresp_compra = models.DateField()
    rut_responsable = models.CharField(max_length=50)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'compra'


class CompraInsumo(models.Model):
    id_compra_insumo = models.IntegerField(primary_key=True)
    cantidad = models.IntegerField()
    precio_unitario = models.FloatField()
    precio_promedio = models.FloatField()
    precio_con_iva = models.FloatField()
    activo = models.IntegerField()
    compra_insumocol = models.CharField(db_column='Compra_Insumocol', max_length=45)  # Field name made lowercase.
    fk_id_compra = models.ForeignKey(Compra, models.DO_NOTHING, db_column='fk_id_compra')
    fk_id_insumos = models.ForeignKey('Insumos', models.DO_NOTHING, db_column='fk_id_insumos')

    class Meta:
        managed = False
        db_table = 'compra_insumo'


class Departamento(models.Model):
    id_dpto = models.AutoField(primary_key=True)
    nombre_dpto = models.CharField(max_length=50)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'departamento'


class DepartamentoUsuario(models.Model):
    id_dpto_user = models.AutoField(primary_key=True)
    fk_id_dpto = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='fk_id_dpto')
    fk_id_user = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_id_user')

    class Meta:
        managed = False
        db_table = 'departamento/usuario'
        unique_together = (('id_dpto_user', 'fk_id_dpto', 'fk_id_user'),)


class Derivacion(models.Model):
    id_derivacion = models.IntegerField(primary_key=True)
    rut_derivado = models.CharField(max_length=50)
    fecha_derivado = models.DateTimeField()
    activo = models.IntegerField()
    fk_id_formulariosr = models.ForeignKey('Formulariosr', models.DO_NOTHING, db_column='fk_id_formularioSR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'derivacion'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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
    id = models.BigAutoField(primary_key=True)
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


class Formulario(models.Model):
    id_formulario = models.IntegerField(primary_key=True)
    pk_folio = models.CharField(max_length=50)
    fecha_creacion = models.DateField()
    rut_solicitante = models.CharField(max_length=50)
    rut_jefe_aprobador = models.CharField(max_length=50)
    rut_admin_interna = models.CharField(max_length=50)
    estado = models.IntegerField()
    fk_id_dpto = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='fk_id_dpto')
    fk_id_sub_dpto = models.ForeignKey('SubDepartamento', models.DO_NOTHING, db_column='fk_id_sub_dpto')
    fk_id_seccion = models.ForeignKey('Seccion', models.DO_NOTHING, db_column='fk_id_seccion')

    class Meta:
        managed = False
        db_table = 'formulario'


class FormularioHistorial(models.Model):
    id_formulario_historial = models.IntegerField(primary_key=True)
    fecha = models.DateTimeField()
    estado = models.IntegerField()
    rut_gestor = models.CharField(max_length=50)
    activo = models.IntegerField()
    fk_id_formulario = models.ForeignKey(Formulario, models.DO_NOTHING, db_column='fk_id_formulario')

    class Meta:
        managed = False
        db_table = 'formulario_historial'


class FormularioInsumo(models.Model):
    id_formulario_insumo = models.IntegerField(db_column='id_formulario_Insumo', primary_key=True)  # Field name made lowercase.
    fk_id_formulario = models.ForeignKey(Formulario, models.DO_NOTHING, db_column='fk_id_formulario')
    fk_id_insumos = models.ForeignKey('Insumos', models.DO_NOTHING, db_column='fk_id_insumos')
    cantidad = models.IntegerField()
    precio = models.FloatField()
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'formulario_insumo'
        unique_together = (('id_formulario_insumo', 'fk_id_formulario', 'fk_id_insumos'),)


class Formulariosr(models.Model):
    id_formulariosr = models.AutoField(db_column='id_formularioSR', primary_key=True)  # Field name made lowercase.
    pk_foliosr = models.CharField(db_column='pk_folioSR', max_length=50)  # Field name made lowercase.
    tipo_formulario = models.CharField(max_length=50)
    fecha_ingreso = models.DateTimeField()
    fecha_respuesta = models.DateTimeField(blank=True, null=True)
    anexo = models.IntegerField()
    email = models.CharField(max_length=50)
    comentario = models.TextField()
    activo = models.IntegerField()
    fk_id_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='fk_id_cargo')
    fk_id_dpto = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='fk_id_dpto')
    fk_id_sub_dpto = models.ForeignKey('SubDepartamento', models.DO_NOTHING, db_column='fk_id_sub_dpto')
    fk_id_seccion = models.ForeignKey('Seccion', models.DO_NOTHING, db_column='fk_id_seccion')

    class Meta:
        managed = False
        db_table = 'formulariosr'


class FormulariosrHistorial(models.Model):
    id_formulariosr_historial = models.IntegerField(primary_key=True)
    fecha_ingreso = models.DateTimeField()
    indicaciones = models.TextField()
    estado = models.IntegerField()
    activo = models.IntegerField()
    fk_id_formulariosr = models.ForeignKey(Formulariosr, models.DO_NOTHING, db_column='fk_id_formularioSR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formulariosr_historial'


class Insumos(models.Model):
    id_insumos = models.IntegerField(primary_key=True)
    codigo_insumo = models.CharField(max_length=50)
    denominacion = models.CharField(max_length=255)
    saldo = models.IntegerField()
    precio = models.FloatField()
    stock_critico = models.IntegerField()
    estado = models.IntegerField()
    fk_id_unidad_medida = models.ForeignKey('UnidadMedida', models.DO_NOTHING, db_column='fk_id_unidad_medida')
    fk_id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='fk_id_categoria')

    class Meta:
        managed = False
        db_table = 'insumos'


class Perfiles(models.Model):
    id_perfiles = models.IntegerField(primary_key=True)
    nombre_perfil = models.CharField(max_length=50)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'perfiles'


class PresupuestoDepartamento(models.Model):
    id_presupuesto_dpto = models.IntegerField(primary_key=True)
    presupuesto = models.FloatField()
    presupuesto_total = models.FloatField()
    fecha = models.DateField()
    activo = models.IntegerField()
    fk_id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='fk_id_categoria')
    fk_id_dpto = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='fk_id_dpto')

    class Meta:
        managed = False
        db_table = 'presupuesto_departamento'


class PresupuestoSeccion(models.Model):
    id_presupuesto_seccion = models.IntegerField(primary_key=True)
    presupuesto = models.FloatField()
    fecha = models.DateField()
    activo = models.IntegerField()
    fk_id_presupuesto_sub_dpto = models.ForeignKey('PresupuestoSubDepartamento', models.DO_NOTHING, db_column='fk_id_presupuesto_sub_dpto')
    fk_id_seccion = models.ForeignKey('Seccion', models.DO_NOTHING, db_column='fk_id_seccion')

    class Meta:
        managed = False
        db_table = 'presupuesto_seccion'


class PresupuestoSubDepartamento(models.Model):
    id_presupuesto_sub_dpto = models.IntegerField(primary_key=True)
    presupuesto = models.FloatField()
    fecha = models.DateField()
    activo = models.IntegerField()
    fk_id_presupuesto_dpto = models.ForeignKey(PresupuestoDepartamento, models.DO_NOTHING, db_column='fk_id_presupuesto_dpto')
    fk_id_sub_dpto = models.ForeignKey('SubDepartamento', models.DO_NOTHING, db_column='fk_id_sub_dpto')

    class Meta:
        managed = False
        db_table = 'presupuesto_sub_departamento'


class Seccion(models.Model):
    id_seccion = models.AutoField(primary_key=True)
    nombre_seccion = models.CharField(max_length=50)
    activo = models.IntegerField()
    fk_id_sub_dpto = models.ForeignKey('SubDepartamento', models.DO_NOTHING, db_column='fk_id_sub_dpto')

    class Meta:
        managed = False
        db_table = 'seccion'


class SubDepartamento(models.Model):
    id_sub_dpto = models.AutoField(primary_key=True)
    nombre_sub_dpto = models.CharField(max_length=50)
    activo = models.IntegerField()
    fk_id_dpto = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='fk_id_dpto')

    class Meta:
        managed = False
        db_table = 'sub_departamento'


class UnidadMedida(models.Model):
    id_unidad_medida = models.IntegerField(primary_key=True)
    nombre_unidad_medida = models.CharField(max_length=50)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'unidad_medida'


class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    activo = models.IntegerField()
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    anexo = models.IntegerField()
    email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'usuario'


class UsuarioCargo(models.Model):
    id_usuario_cargo = models.IntegerField(primary_key=True)
    fecha_activacion = models.DateTimeField()
    fecha_desactivacion = models.DateTimeField()
    activo = models.IntegerField()
    fk_id_user = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='fk_id_user')
    fk_id_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='fk_id_cargo')

    class Meta:
        managed = False
        db_table = 'usuario/cargo'
        unique_together = (('id_usuario_cargo', 'fk_id_user', 'fk_id_cargo'),)


class UsuariosPerfiles(models.Model):
    id_usuarios_perfiles = models.IntegerField(primary_key=True)
    fk_id_user = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='fk_id_user')
    fk_id_perfiles = models.ForeignKey(Perfiles, models.DO_NOTHING, db_column='fk_id_perfiles')

    class Meta:
        managed = False
        db_table = 'usuarios_perfiles'
        unique_together = (('id_usuarios_perfiles', 'fk_id_user', 'fk_id_perfiles'),)