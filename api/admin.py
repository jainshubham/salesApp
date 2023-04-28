from django.contrib import admin
from api.models import Pharmacy, ReportingManager, SalesRepresentative, Doctor, Store, Product, CompetitorProduct, Category, Distributor, Order, OrderItem, Working

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(CompetitorProduct)
class CompetitorProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(ReportingManager)
class ReportingManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(SalesRepresentative)
class SalesRepresentativeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'phone_number', 'email', 'sales_rep')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'category')

@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = ('name','location','master_d', 'category')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'pharmacy', 'sales_rep', 'shipping_address')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'units', 'pack_size')

@admin.register(Working)
class WorkingAdmin(admin.ModelAdmin):
    list_display = ('id',)
