from rest_framework import serializers
from api.models import Pharmacy, Category, CompetitorProduct, ReportingManager, Doctor, SalesRepresentative, Store, Distributor, Product, Order, OrderItem, Inventory,Working

class DistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'
        
class ReportingManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportingManager
        fields = '__all__'

class SalesRepresentativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesRepresentative
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CompetitorProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitorProduct
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    sales_rep_id = serializers.PrimaryKeyRelatedField(
                queryset=SalesRepresentative.objects.all(),
                write_only=True,
                required=False
                )
    pharmacy_id = serializers.PrimaryKeyRelatedField(
                queryset=Pharmacy.objects.all(),
                write_only=True,
                required=False
                )
    
    distributor_id = serializers.PrimaryKeyRelatedField(
                queryset=Distributor.objects.all(),
                write_only=True,
                required=False
                )
    
    class Meta:
        model = Order
        fields = ('order_book_image', 'shipping_address', 'id', 'order_items', 'pharmacy', 'sales_rep',  'distributor', 'distributor_id', 'sales_rep_id', 'pharmacy_id') 
        extra_kwargs = {
                'shipping_address': {'write_only':True},
                'order_book_image': {'write_only':True},
                }
        depth = 1

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        validated_data['sales_rep_id'] = validated_data['sales_rep_id'].id
        validated_data['distributor_id'] = validated_data['distributor_id'].id
        validated_data['pharmacy_id'] = validated_data['pharmacy_id'].id
        order = Order.objects.create(**validated_data)
        print(order_items_data)
        for item in order_items_data:
             OrderItem.objects.create(order=order, units=item.get('units'), pack_size=item.get('pack_size'), product=item.get('product'))
        return order

    # def update(self, instance, validated_data):
    #     order_items_data = validated_data.pop('order_items')
    #     order_items = (instance.order_items).all()
    #     order_items = list(order_items)
    #     # instance.store = validated_data.get('store', instance.store)
    #     instance.pharmacy = validated_data.get('pharmacy', instance.pharmacy)
    #     instance.product_name = validated_data.get('product_name', instance.product_name)
    #     instance.sales_rep = validated_data.get('sales_rep', instance.sales_rep)
    #     instance.order_image = validated_data.get('order_image', instance.order_book_image)
    #     instance.distributer = validated_data.get('distributer', instance.distributer)
    #     instance.delivery_date = validated_data.get('delivery_date', instance.delivery_date)
    #     # instance.payment_terms = validated_data.get('payment_terms', instance.payment_terms)
    #     instance.shipping_address = validated_data.get('shipping_address', instance.shipping_address)
    #     # instance.notes = validated_data.get('notes', instance.notes)
    #     instance.order_date = validated_data.get('order_date',instance.order_date)
    #     instance.save()
    #     for item in order_items_data:
    #         order_item = order_items.pop(0)
    #         order_item.product = item.get('product', order_item.product)
    #     instance.order_date = validated_data.get('order_date',instance.order_date)
    #     instance.save()
    #     for item in order_items_data:

class WorkingSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    pharmacy_id = serializers.PrimaryKeyRelatedField(
                queryset=Pharmacy.objects.all(),
                write_only=True,
                required=False
                )
    
    distributor_id = serializers.PrimaryKeyRelatedField(
                queryset=Distributor.objects.all(),
                write_only=True,
                required=False
                )
    
    class Meta:
        model = Working
        fields = ('pharmacy', 'product', 'is_new_marketing_material', 'marketing_material_image', 'got_orders','order_items','order_book_image', 'distributor' , 'pharmacy_image', 'distributor_id', 'pharmacy_id')
        extra_kwargs = {
                'order_book_image': {'write_only':True},
                }
        depth = 1
   
    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        validated_data['distributor_id'] = validated_data['distributor_id'].id
        validated_data['pharmacy_id'] = validated_data['pharmacy_id'].id
        working = Working.objects.create(**validated_data)
        print(order_items_data)
        for item in order_items_data:
             OrderItem.objects.create(working=working, units=item.get('units'), pack_size=item.get('pack_size'), product=item.get('product'))
        return working
