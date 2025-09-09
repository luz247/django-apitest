# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class NewEmailSvia(models.Model):
    lead_id = models.IntegerField(blank=True, null=True)
    rut = models.CharField(max_length=12, blank=True, null=True)
    ruteje = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.CharField(max_length=25, null=True, blank=True)

    class Meta:

        db_table = "new_table"
        app_label = "core"


class CarteraTotales(models.Model):
    rut = models.CharField(max_length=11, null=True, blank=True)
    CtaCto = models.CharField(max_length=16, null=True, blank=True)
    boletas = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:

        db_table = "other_Table"
        app_label = "core"


class AllContacts(models.Model):
    id = models.BigAutoField(primary_key=True)
    lead_id = models.IntegerField(blank=True, null=True)
    rut = models.CharField(
        max_length=20, db_collation="Modern_Spanish_CI_AS", blank=True, null=True
    )
    ruteje = models.CharField(
        max_length=11, db_collation="Modern_Spanish_CI_AS", blank=True, null=True
    )
    telefono = models.CharField(
        max_length=20, db_collation="Modern_Spanish_CI_AS", blank=True, null=True
    )
    glosa = models.CharField(
        max_length=255, db_collation="Modern_Spanish_CI_AS", blank=True, null=True
    )
    feccomp = models.DateField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    respuesta = models.CharField(
        max_length=150, db_collation="Modern_Spanish_CI_AS", blank=True, null=True
    )
    tipo = models.CharField(
        max_length=2, db_collation="Modern_Spanish_CI_AS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "All_contacts"


class Cheque(models.Model):
    n_cheque = models.CharField(
        db_column="N_cheque",
        max_length=50,
        db_collation="Modern_Spanish_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    fecha_ven_cheque = models.DateField(
        db_column="Fecha_ven_cheque", blank=True, null=True
    )  # Field name made lowercase.
    importe_pago = models.DecimalField(
        db_column="Importe_pago", max_digits=18, decimal_places=0, blank=True, null=True
    )  # Field name made lowercase.
    doc_pago = models.DecimalField(
        db_column="Doc_Pago", max_digits=18, decimal_places=0, blank=True, null=True
    )  # Field name made lowercase.
    rut_cli = models.CharField(
        db_column="Rut_Cli",
        max_length=50,
        db_collation="Modern_Spanish_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    socio_comercial = models.IntegerField(
        db_column="Socio_comercial", blank=True, null=True
    )  # Field name made lowercase.
    fecha_contabiliza = models.DateField(
        db_column="Fecha_Contabiliza", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Cheque"


class Descuento(models.Model):
    id = models.BigAutoField(primary_key=True)
    origen = models.CharField(
        max_length=10, db_collation="Modern_Spanish_CI_AS", blank=True, null=True
    )
    rut = models.CharField(
        max_length=50, db_collation="Modern_Spanish_CI_AS", blank=True, null=True
    )
    ic = models.IntegerField(blank=True, null=True)
    cc = models.IntegerField(blank=True, null=True)
    deuda_total = models.CharField(
        max_length=20, db_collation="Modern_Spanish_CI_AS", blank=True, null=True
    )
    descuento_total = models.CharField(
        max_length=20, db_collation="Modern_Spanish_CI_AS", blank=True, null=True
    )
    tipo_descuento = models.CharField(
        max_length=20, db_collation="Modern_Spanish_CI_AS", blank=True, null=True
    )
    tp_dcto = models.CharField(
        db_column="Tp_Dcto",
        max_length=20,
        db_collation="Modern_Spanish_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    nombre_camp = models.CharField(
        db_column="Nombre_Camp",
        max_length=50,
        db_collation="Modern_Spanish_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    dcto_extraordinario = models.CharField(
        db_column="Dcto_Extraordinario",
        max_length=20,
        db_collation="Modern_Spanish_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Descuento"


class Deuda(models.Model):
    id = models.BigAutoField(primary_key=True)
    ic = models.IntegerField(blank=True, null=True)
    monto = models.IntegerField(blank=True, null=True)
    contador = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Deuda"
