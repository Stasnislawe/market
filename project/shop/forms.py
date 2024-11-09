from django import forms
from .models import Product


# #category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.CharField(max_length=200, db_index=True, unique=True)
#     image = models.ImageField(upload_to='products/%Y/%m/%d')
#     description = models.TextField(verbose_name='Описание')
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.PositiveIntegerField()
#     available = models.BooleanField(default=True)

class NewProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Наименование'
        self.fields['slug'].label = 'Слаг'
        self.fields['description'].label = 'Описание'
        self.fields['image'].label = 'Изображение'
        self.fields['price'].label = 'Стоимость'
        self.fields['quantity'].label = 'Количество'
        self.fields['available'].label = 'В наличии'


    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'image', 'price', 'quantity', 'available', 'slug')