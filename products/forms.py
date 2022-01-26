from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Brand, ProductReview


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label="image", required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        brands = Brand.objects.all()
        friendly_names_categories = [
            (c.id, c.get_friendly_name()) for c in categories]
        friendly_names_brands = [(b.id, b.get_friendly_name()) for b in brands]

        self.fields['category'].choices = friendly_names_categories
        self.fields['brand'].choices = friendly_names_brands
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'radius-10'


# Add review form
class ProductReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        fields = ('review_rating', 'review_text', )
