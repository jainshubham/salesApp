from django.db import models

class ReportingManager(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SalesRepresentative(models.Model):
    GENDER_CHOICES = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    REPORTING_BIZ_UNIT = (
        ('OTC','OTC'),
        ('IVD','IVD'),
        ('HTP','HTP'),
    )
    ZONES = (
        ('East','East'),
        ('West','West'),
        ('South','South'),
        ('North','North'),
    )
   # email = models.EmailField(unique=True)
    mylab_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    # password = models.CharField(max_length=255)
    gender = models.CharField(max_length=100,choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    address = models.CharField(max_length=100)
    reporting_manager = models.ForeignKey(ReportingManager, on_delete=models.CASCADE)
    reporting_business_unit = models.CharField(max_length=10,choices=REPORTING_BIZ_UNIT)
    zone = models.CharField(max_length=6, choices= ZONES, null=True)

    def __str__(self):
        return self.name
    
    
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    specialization = models.CharField(max_length=100)
    is_clinic_owner = models.BooleanField(default=False) 
    clinic_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    registration_council = models.CharField(max_length=100)
    registration_no = models.CharField(max_length=100)
    yor = models.IntegerField()
    photo_id_proof = models.URLField()  
    registration_proof = models.URLField()
    clinic_registration_proof = models.URLField()


class Inventory(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    units = models.IntegerField()
    pack_size = models.IntegerField()
    
    def __str__(self):
        return self.product.name


class Pharmacy(models.Model):
    TYPES = (
        ('Small','Small'),
        ('Medium','Medium'),
        ('Large','Large'),
    )
    IS_OWNER = (
        ('Yes','Yes'),
        ('No','No'),
    )
    IS_ONLINE_FRIENDLY = (
        ('Yes','Yes'),
        ('No','No'),
    )
    name = models.CharField(max_length=100)
    drug_license_number = models.CharField(max_length=100)
    p_type = models.CharField(max_length=10, choices=TYPES) 
    location = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    is_owner = models.CharField(max_length=5, choices=IS_OWNER)
    contact_person_designation = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    whatsapp_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    is_online_friendly = models.CharField(max_length=4, choices=IS_ONLINE_FRIENDLY)
    inventories = models.ManyToManyField(Inventory)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    logo = models.URLField()
    sales_rep = models.ForeignKey(SalesRepresentative, on_delete=models.CASCADE, related_name='stores')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CompetitorProduct(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)

    def __str__(self):
        return self.name


class Distributor(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    master_d = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Order(models.Model):
    # store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='orders')
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    sales_rep = models.ForeignKey(SalesRepresentative, on_delete=models.CASCADE, related_name='orders')
    order_book_image = models.URLField()
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, null=True, blank=True)
    # payment_terms = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    # notes = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.pharmacy.name}"



class Working(models.Model):
    GOT_ORDERS = (
        ('Yes','Yes'),
        ('No','No'),
    )
    IS_NEW_MARKETING_MATERIAL = (
        ('Yes','Yes'),
        ('No','No'),
    )
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    is_new_marketing_material = models.CharField(max_length=5, choices=IS_NEW_MARKETING_MATERIAL)
    marketing_material_image = models.URLField(null=True)
    got_orders = models.CharField(max_length=5, choices=GOT_ORDERS)
    order_book_image = models.URLField(null=True)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, null=True, blank=True)
    pharmacy_image = models.URLField(null=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items', null=True)
    working = models.ForeignKey(Working, on_delete=models.CASCADE, related_name='order_items', null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    units = models.IntegerField()
    pack_size = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
