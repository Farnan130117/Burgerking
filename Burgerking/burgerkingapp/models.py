from django.db import models

# Create your models here.

class Product(models.Model):     #product_class

	name = models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=400, null=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)    
	  #pip install pillow
	  #Pillow is a Python Imaging Library which deals with different image files. 
	  #We won’t be using pillow directly but Django is using it. Therefore, we need pillow library.
	price	=	models.DecimalField(max_digits=10,	decimal_places=2)				
	available	=	models.BooleanField(default=True)
	created	=	models.DateTimeField(auto_now_add=True)				
	updated	=	models.DateTimeField(auto_now=True)
	#date_created = models.DateTimeField(default=datetime.now(), null=True,  editable=False)
	#date_created = models.DateTimeField(auto_now_add=True, null=True)
     
	def __str__(self):
		return self.name