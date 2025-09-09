# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adventureworksdwbuildversion(models.Model):
    dbversion = models.CharField(db_column='DBVersion', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    versiondate = models.DateTimeField(db_column='VersionDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdventureWorksDWBuildVersion'


class Databaselog(models.Model):
    databaselogid = models.AutoField(db_column='DatabaseLogID', primary_key=True)  # Field name made lowercase.
    posttime = models.DateTimeField(db_column='PostTime')  # Field name made lowercase.
    databaseuser = models.CharField(db_column='DatabaseUser', max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    event = models.CharField(db_column='Event', max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    schema = models.CharField(db_column='Schema', max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    object = models.CharField(db_column='Object', max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tsql = models.TextField(db_column='TSQL', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    xmlevent = models.TextField(db_column='XmlEvent')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'DatabaseLog'


class Dimaccount(models.Model):
    accountkey = models.AutoField(db_column='AccountKey', primary_key=True)  # Field name made lowercase.
    parentaccountkey = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentAccountKey', blank=True, null=True)  # Field name made lowercase.
    accountcodealternatekey = models.IntegerField(db_column='AccountCodeAlternateKey', blank=True, null=True)  # Field name made lowercase.
    parentaccountcodealternatekey = models.IntegerField(db_column='ParentAccountCodeAlternateKey', blank=True, null=True)  # Field name made lowercase.
    accountdescription = models.CharField(db_column='AccountDescription', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    accounttype = models.CharField(db_column='AccountType', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(db_column='Operator', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    custommembers = models.CharField(db_column='CustomMembers', max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    valuetype = models.CharField(db_column='ValueType', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    custommemberoptions = models.CharField(db_column='CustomMemberOptions', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimAccount'


class Dimcurrency(models.Model):
    currencykey = models.AutoField(db_column='CurrencyKey', primary_key=True)  # Field name made lowercase.
    currencyalternatekey = models.CharField(db_column='CurrencyAlternateKey', unique=True, max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    currencyname = models.CharField(db_column='CurrencyName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimCurrency'


class Dimcustomer(models.Model):
    customerkey = models.AutoField(db_column='CustomerKey', primary_key=True)  # Field name made lowercase.
    geographykey = models.ForeignKey('Dimgeography', models.DO_NOTHING, db_column='GeographyKey', blank=True, null=True)  # Field name made lowercase.
    customeralternatekey = models.CharField(db_column='CustomerAlternateKey', unique=True, max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    namestyle = models.BooleanField(db_column='NameStyle', blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    maritalstatus = models.CharField(db_column='MaritalStatus', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    suffix = models.CharField(db_column='Suffix', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    yearlyincome = models.DecimalField(db_column='YearlyIncome', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalchildren = models.SmallIntegerField(db_column='TotalChildren', blank=True, null=True)  # Field name made lowercase.
    numberchildrenathome = models.SmallIntegerField(db_column='NumberChildrenAtHome', blank=True, null=True)  # Field name made lowercase.
    englisheducation = models.CharField(db_column='EnglishEducation', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    spanisheducation = models.CharField(db_column='SpanishEducation', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    frencheducation = models.CharField(db_column='FrenchEducation', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    englishoccupation = models.CharField(db_column='EnglishOccupation', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    spanishoccupation = models.CharField(db_column='SpanishOccupation', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    frenchoccupation = models.CharField(db_column='FrenchOccupation', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    houseownerflag = models.CharField(db_column='HouseOwnerFlag', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    numbercarsowned = models.SmallIntegerField(db_column='NumberCarsOwned', blank=True, null=True)  # Field name made lowercase.
    addressline1 = models.CharField(db_column='AddressLine1', max_length=120, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    addressline2 = models.CharField(db_column='AddressLine2', max_length=120, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    datefirstpurchase = models.DateField(db_column='DateFirstPurchase', blank=True, null=True)  # Field name made lowercase.
    commutedistance = models.CharField(db_column='CommuteDistance', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimCustomer'


class Dimdate(models.Model):
    datekey = models.IntegerField(db_column='DateKey', primary_key=True)  # Field name made lowercase.
    fulldatealternatekey = models.DateField(db_column='FullDateAlternateKey', unique=True)  # Field name made lowercase.
    daynumberofweek = models.SmallIntegerField(db_column='DayNumberOfWeek')  # Field name made lowercase.
    englishdaynameofweek = models.CharField(db_column='EnglishDayNameOfWeek', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    spanishdaynameofweek = models.CharField(db_column='SpanishDayNameOfWeek', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    frenchdaynameofweek = models.CharField(db_column='FrenchDayNameOfWeek', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    daynumberofmonth = models.SmallIntegerField(db_column='DayNumberOfMonth')  # Field name made lowercase.
    daynumberofyear = models.SmallIntegerField(db_column='DayNumberOfYear')  # Field name made lowercase.
    weeknumberofyear = models.SmallIntegerField(db_column='WeekNumberOfYear')  # Field name made lowercase.
    englishmonthname = models.CharField(db_column='EnglishMonthName', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    spanishmonthname = models.CharField(db_column='SpanishMonthName', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    frenchmonthname = models.CharField(db_column='FrenchMonthName', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    monthnumberofyear = models.SmallIntegerField(db_column='MonthNumberOfYear')  # Field name made lowercase.
    calendarquarter = models.SmallIntegerField(db_column='CalendarQuarter')  # Field name made lowercase.
    calendaryear = models.SmallIntegerField(db_column='CalendarYear')  # Field name made lowercase.
    calendarsemester = models.SmallIntegerField(db_column='CalendarSemester')  # Field name made lowercase.
    fiscalquarter = models.SmallIntegerField(db_column='FiscalQuarter')  # Field name made lowercase.
    fiscalyear = models.SmallIntegerField(db_column='FiscalYear')  # Field name made lowercase.
    fiscalsemester = models.SmallIntegerField(db_column='FiscalSemester')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimDate'


class Dimdepartmentgroup(models.Model):
    departmentgroupkey = models.AutoField(db_column='DepartmentGroupKey', primary_key=True)  # Field name made lowercase.
    parentdepartmentgroupkey = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentDepartmentGroupKey', blank=True, null=True)  # Field name made lowercase.
    departmentgroupname = models.CharField(db_column='DepartmentGroupName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimDepartmentGroup'


class Dimemployee(models.Model):
    employeekey = models.AutoField(db_column='EmployeeKey', primary_key=True)  # Field name made lowercase.
    parentemployeekey = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentEmployeeKey', blank=True, null=True)  # Field name made lowercase.
    employeenationalidalternatekey = models.CharField(db_column='EmployeeNationalIDAlternateKey', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    parentemployeenationalidalternatekey = models.CharField(db_column='ParentEmployeeNationalIDAlternateKey', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesterritorykey = models.ForeignKey('Dimsalesterritory', models.DO_NOTHING, db_column='SalesTerritoryKey', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    namestyle = models.BooleanField(db_column='NameStyle')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hiredate = models.DateField(db_column='HireDate', blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=256, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    maritalstatus = models.CharField(db_column='MaritalStatus', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emergencycontactname = models.CharField(db_column='EmergencyContactName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emergencycontactphone = models.CharField(db_column='EmergencyContactPhone', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salariedflag = models.BooleanField(db_column='SalariedFlag', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    payfrequency = models.SmallIntegerField(db_column='PayFrequency', blank=True, null=True)  # Field name made lowercase.
    baserate = models.DecimalField(db_column='BaseRate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vacationhours = models.SmallIntegerField(db_column='VacationHours', blank=True, null=True)  # Field name made lowercase.
    sickleavehours = models.SmallIntegerField(db_column='SickLeaveHours', blank=True, null=True)  # Field name made lowercase.
    currentflag = models.BooleanField(db_column='CurrentFlag')  # Field name made lowercase.
    salespersonflag = models.BooleanField(db_column='SalesPersonFlag')  # Field name made lowercase.
    departmentname = models.CharField(db_column='DepartmentName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    employeephoto = models.BinaryField(db_column='EmployeePhoto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimEmployee'


class Dimgeography(models.Model):
    geographykey = models.AutoField(db_column='GeographyKey', primary_key=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    stateprovincecode = models.CharField(db_column='StateProvinceCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    stateprovincename = models.CharField(db_column='StateProvinceName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    countryregioncode = models.CharField(db_column='CountryRegionCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    englishcountryregionname = models.CharField(db_column='EnglishCountryRegionName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    spanishcountryregionname = models.CharField(db_column='SpanishCountryRegionName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    frenchcountryregionname = models.CharField(db_column='FrenchCountryRegionName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesterritorykey = models.ForeignKey('Dimsalesterritory', models.DO_NOTHING, db_column='SalesTerritoryKey', blank=True, null=True)  # Field name made lowercase.
    ipaddresslocator = models.CharField(db_column='IpAddressLocator', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimGeography'


class Dimorganization(models.Model):
    organizationkey = models.AutoField(db_column='OrganizationKey', primary_key=True)  # Field name made lowercase.
    parentorganizationkey = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentOrganizationKey', blank=True, null=True)  # Field name made lowercase.
    percentageofownership = models.CharField(db_column='PercentageOfOwnership', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    organizationname = models.CharField(db_column='OrganizationName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    currencykey = models.ForeignKey(Dimcurrency, models.DO_NOTHING, db_column='CurrencyKey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimOrganization'


class Dimproduct(models.Model):
    productkey = models.AutoField(db_column='ProductKey', primary_key=True)  # Field name made lowercase.
    productalternatekey = models.CharField(db_column='ProductAlternateKey', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    productsubcategorykey = models.ForeignKey('Dimproductsubcategory', models.DO_NOTHING, db_column='ProductSubcategoryKey', blank=True, null=True)  # Field name made lowercase.
    weightunitmeasurecode = models.CharField(db_column='WeightUnitMeasureCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sizeunitmeasurecode = models.CharField(db_column='SizeUnitMeasureCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    englishproductname = models.CharField(db_column='EnglishProductName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    spanishproductname = models.CharField(db_column='SpanishProductName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    frenchproductname = models.CharField(db_column='FrenchProductName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    standardcost = models.DecimalField(db_column='StandardCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    finishedgoodsflag = models.BooleanField(db_column='FinishedGoodsFlag')  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    safetystocklevel = models.SmallIntegerField(db_column='SafetyStockLevel', blank=True, null=True)  # Field name made lowercase.
    reorderpoint = models.SmallIntegerField(db_column='ReorderPoint', blank=True, null=True)  # Field name made lowercase.
    listprice = models.DecimalField(db_column='ListPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sizerange = models.CharField(db_column='SizeRange', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    daystomanufacture = models.IntegerField(db_column='DaysToManufacture', blank=True, null=True)  # Field name made lowercase.
    productline = models.CharField(db_column='ProductLine', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dealerprice = models.DecimalField(db_column='DealerPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    style = models.CharField(db_column='Style', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    modelname = models.CharField(db_column='ModelName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    largephoto = models.BinaryField(db_column='LargePhoto', blank=True, null=True)  # Field name made lowercase.
    englishdescription = models.CharField(db_column='EnglishDescription', max_length=400, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    frenchdescription = models.CharField(db_column='FrenchDescription', max_length=400, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    chinesedescription = models.CharField(db_column='ChineseDescription', max_length=400, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    arabicdescription = models.CharField(db_column='ArabicDescription', max_length=400, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hebrewdescription = models.CharField(db_column='HebrewDescription', max_length=400, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    thaidescription = models.CharField(db_column='ThaiDescription', max_length=400, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    germandescription = models.CharField(db_column='GermanDescription', max_length=400, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    japanesedescription = models.CharField(db_column='JapaneseDescription', max_length=400, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    turkishdescription = models.CharField(db_column='TurkishDescription', max_length=400, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimProduct'
        unique_together = (('productalternatekey', 'startdate'),)


class Dimproductcategory(models.Model):
    productcategorykey = models.AutoField(db_column='ProductCategoryKey', primary_key=True)  # Field name made lowercase.
    productcategoryalternatekey = models.IntegerField(db_column='ProductCategoryAlternateKey', unique=True, blank=True, null=True)  # Field name made lowercase.
    englishproductcategoryname = models.CharField(db_column='EnglishProductCategoryName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    spanishproductcategoryname = models.CharField(db_column='SpanishProductCategoryName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    frenchproductcategoryname = models.CharField(db_column='FrenchProductCategoryName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimProductCategory'
