from django import forms
from .models import product,Cart
from django.core.exceptions import ValidationError



class Login_user(forms.Form):
    email_user=forms.EmailField()
    password_user=forms.CharField()
    # def clean(self):
    #     if wrong_credentiels():
    #         raise ValidationError("username pwd didn't match")        


class Product(forms.ModelForm):
    class Meta:
        model = product
        fields = "__all__"

    
    
    def clean_Product_Name(self):
        return self.cleaned_data["Product_Name"].upper()        


    
    def clean(self):
        super(Product,self).clean()
        Product_Name = self.cleaned_data.get('Product_Name')
    
        Product_Price = self.cleaned_data.get('Product_Price')
        print("Product Name",Product_Name,)
        print("Product_Price",Product_Price)

        if Product_Price < 100:
            # raise forms.ValidationError("Product price should not be less than 100 ")
            self.add_error('Product_Price', 'Product price should not be less than 100 ')
      
        return self.cleaned_data


class OrderForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = "__all__"
    
    def clean_product_id(self):
        return self.cleaned_data["Product_Name"].upper()  
       



    




    # def form_valid(self, form):
    #     self.object = form.save(commit=False)

    #     # Do any custom stuff here

    #     self.object.save()

    #     return render_to_response(self.template_name, self.get_context_data())

    





        










