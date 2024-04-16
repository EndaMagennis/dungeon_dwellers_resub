from django.forms import ModelForm

from .models import Product, Category, Tag, ProductImage


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        self.fields['tag'].queryset = Tag.objects.all()
        self.fields['image'].queryset = ProductImage.objects.all()

    def disable_fields_based_on_category(self, category):
        if category.name == 'board_game':
            self.fields['has_dimensions'] = False
            self.fields['has_quantity']= False
            self.fields['dimensions'].disabled = True
            self.fields['quantity'].disabled = True
        else:
            self.fields['has_dimensions'] = True
            self.fields['has_quantity'] = True
            self.fields['dimensions'].disabled = False
            self.fields['quantity'].disabled = False
