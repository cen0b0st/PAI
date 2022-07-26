# Generated by Django 4.0.6 on 2022-08-16 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id_cargo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cargo', models.CharField(max_length=50)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'cargo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=50)),
                ('estado', models.IntegerField()),
            ],
            options={
                'db_table': 'categoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CierreMensual',
            fields=[
                ('id_cierre_mensual', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_cierre_mensual', models.DateField()),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'cierre_mensual',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CierreMensualInsumo',
            fields=[
                ('id_cierre_mensual_insumo', models.IntegerField(primary_key=True, serialize=False)),
                ('saldo', models.IntegerField()),
                ('precio', models.FloatField()),
                ('estado', models.IntegerField()),
            ],
            options={
                'db_table': 'cierre_mensual_insumo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id_compra', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_compra', models.DateField()),
                ('guia', models.CharField(max_length=50)),
                ('orden_de_compra', models.CharField(max_length=50)),
                ('rut_proveedor', models.CharField(max_length=50)),
                ('nombre_proveedor', models.CharField(max_length=50)),
                ('total_compra', models.IntegerField()),
                ('descuento', models.IntegerField()),
                ('fecha_omgresp_compra', models.DateField()),
                ('rut_responsable', models.CharField(max_length=50)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'compra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CompraInsumo',
            fields=[
                ('id_compra_insumo', models.IntegerField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.FloatField()),
                ('precio_promedio', models.FloatField()),
                ('precio_con_iva', models.FloatField()),
                ('activo', models.IntegerField()),
                ('compra_insumocol', models.CharField(db_column='Compra_Insumocol', max_length=45)),
            ],
            options={
                'db_table': 'compra_insumo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_dpto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_dpto', models.CharField(max_length=50)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'departamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DepartamentoUsuario',
            fields=[
                ('id_dpto_user', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'departamento/usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Derivacion',
            fields=[
                ('id_derivacion', models.IntegerField(primary_key=True, serialize=False)),
                ('rut_derivado', models.CharField(max_length=50)),
                ('fecha_derivado', models.DateTimeField()),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'derivacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id_formulario', models.IntegerField(primary_key=True, serialize=False)),
                ('pk_folio', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateField()),
                ('rut_solicitante', models.CharField(max_length=50)),
                ('rut_jefe_aprobador', models.CharField(max_length=50)),
                ('rut_admin_interna', models.CharField(max_length=50)),
                ('estado', models.IntegerField()),
            ],
            options={
                'db_table': 'formulario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormularioHistorial',
            fields=[
                ('id_formulario_historial', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('estado', models.IntegerField()),
                ('rut_gestor', models.CharField(max_length=50)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'formulario_historial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormularioInsumo',
            fields=[
                ('id_formulario_insumo', models.IntegerField(db_column='id_formulario_Insumo', primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio', models.FloatField()),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'formulario_insumo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Formulariosr',
            fields=[
                ('id_formulariosr', models.AutoField(db_column='id_formularioSR', primary_key=True, serialize=False)),
                ('pk_foliosr', models.CharField(db_column='pk_folioSR', max_length=50)),
                ('tipo_formulario', models.CharField(max_length=50)),
                ('fecha_ingreso', models.DateTimeField()),
                ('fecha_respuesta', models.DateTimeField(blank=True, null=True)),
                ('anexo', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('comentario', models.TextField()),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'formulariosr',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormulariosrHistorial',
            fields=[
                ('id_formulariosr_historial', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_ingreso', models.DateTimeField()),
                ('indicaciones', models.TextField()),
                ('estado', models.IntegerField()),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'formulariosr_historial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Insumos',
            fields=[
                ('id_insumos', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo_insumo', models.CharField(max_length=50)),
                ('denominacion', models.CharField(max_length=255)),
                ('saldo', models.IntegerField()),
                ('precio', models.FloatField()),
                ('stock_critico', models.IntegerField()),
                ('estado', models.IntegerField()),
            ],
            options={
                'db_table': 'insumos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('id_perfiles', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_perfil', models.CharField(max_length=50)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'perfiles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PresupuestoDepartamento',
            fields=[
                ('id_presupuesto_dpto', models.IntegerField(primary_key=True, serialize=False)),
                ('presupuesto', models.FloatField()),
                ('presupuesto_total', models.FloatField()),
                ('fecha', models.DateField()),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'presupuesto_departamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PresupuestoSeccion',
            fields=[
                ('id_presupuesto_seccion', models.IntegerField(primary_key=True, serialize=False)),
                ('presupuesto', models.FloatField()),
                ('fecha', models.DateField()),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'presupuesto_seccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PresupuestoSubDepartamento',
            fields=[
                ('id_presupuesto_sub_dpto', models.IntegerField(primary_key=True, serialize=False)),
                ('presupuesto', models.FloatField()),
                ('fecha', models.DateField()),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'presupuesto_sub_departamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id_seccion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_seccion', models.CharField(max_length=50)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'seccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubDepartamento',
            fields=[
                ('id_sub_dpto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_sub_dpto', models.CharField(max_length=50)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'sub_departamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id_unidad_medida', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_unidad_medida', models.CharField(max_length=50)),
                ('estado', models.IntegerField()),
            ],
            options={
                'db_table': 'unidad_medida',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
                ('activo', models.IntegerField()),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('anexo', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsuarioCargo',
            fields=[
                ('id_usuario_cargo', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_activacion', models.DateTimeField()),
                ('fecha_desactivacion', models.DateTimeField()),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'usuario/cargo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsuariosPerfiles',
            fields=[
                ('id_usuarios_perfiles', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'usuarios_perfiles',
                'managed': False,
            },
        ),
    ]
