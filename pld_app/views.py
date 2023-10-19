from django.http import HttpResponse
from django.shortcuts import render
from pld_app.models import *
from pld_app.forms import *
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect 
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
from io import BytesIO
import io
from .utils import read_file_as_image
from django.core.files.storage import FileSystemStorage


MODEL_apple_Class_names = ['Apple Apple scab',
 'Apple Black rot',
 'Apple Cedar apple rust',
 'Apple Healthy',
 'Random Image / Data Not Available']


MODEL_cabbage_Class_names =  ['Random Image / Data Not Available', 'cabbage looper']

MODEL_cassava_Class_names = ['Cassava bacterial blight',
 'Cassava brown streak disease',
 'Cassava green mottle',
 'Cassava Healthy',
 'Cassava mosaic disease',
 'Random Image / Data Not Available']

MODEL_cherry_Class_names =  ['Cherry (including sour) Powdery mildew',
 'Cherry (including sour) Healthy',
 'Random Image / Data Not Available']

MODEL_chili_Class_names = ['Chili Healthy',
 'Chili leaf curl',
 'Chili leaf spot',
 'Chili whitefly',
 'Chili yellowish',
 'Random Image / Data Not Available']

MODEL_coffee_Class_names = ['Cercospora leaf spot',
 'Coffee Healthy',
 'Coffee red spider mite',
 'Coffee rust',
 'Random Image / Data Not Available']

MODEL_corn_Class_names = ['Blight in corn Leaf',
 'Common Rust in corn Leaf',
 'Corn (maize) Healthy',
 'Gray Leaf Spot in corn Leaf',
 'Random Image / Data Not Available']

MODEL_cucumber_Class_names =  ['Cucumber Diseased', 'Cucumber Healthy', 'Random Image / Data Not Available']

MODEL_garlic_Class_names =  ['Garlic Healthy', 'Random Image / Data Not Available']

MODEL_gauva_Class_names =  ['Gauva Diseased', 'Gauva Healthy', 'Random Image / Data Not Available']

MODEL_ginger_Class_names =  ['Ginger Healthy', 'Random Image / Data Not Available']

MODEL_grape_Class_names = ['Grape Esca Black Measles',
 'Grape Leaf blight Isariopsis Leaf Spot',
 'Grape black rot',
 'Grape Healthy',
 'Random Image / Data Not Available']

MODEL_jamun_Class_names =  ['Jamun Diseased', 'Jamun Healthy', 'Random Image / Data Not Available']

MODEL_lemon_Class_names =  ['Lemon Healthy', 'Lemon Diseased', 'Random Image / Data Not Available']

MODEL_mango_Class_names =  ['Mango Diseased', 'Mango Healthy', 'Random Image / Data Not Available']

MODEL_orange_Class_names =  ['Orange Haunglongbing Citrus Greening', 'Random Image / Data Not Available']

MODEL_peach_Class_names =  ['Peach Bacterial spot', 'Peach Healthy', 'Random Image / Data Not Available']

MODEL_pepper_Class_names =  ['Pepper Bell Bacterial Spot', 'Pepper Bell Healthy', 'Random Image / Data Not Available']

MODEL_pome_Class_names =  ['Pomegranate Diseased', 'Pomegranate Healthy', 'Random Image / Data Not Available']

MODEL_potatoes_Class_names = ['Potato Early blight',
 'Potato Late blight',
 'Potato Healthy',
 'Random Image / Data Not Available',
 'potato hollow heart']

MODEL_rice_Class_names = ['Random Image / Data Not Available',
 'Rice brown spot',
 'Rice Healthy',
 'Rice hispa',
 'Rice leaf blast',
 'Rice neck blast']

MODEL_soybean_Class_names = ['Random Image / Data Not Available',
 'Soybean bacterial blight',
 'Soybean caterpillar',
 'Soybean diabrotica speciosa',
 'Soybean downy mildew',
 'Soybean Healthy',
 'Soybean mosaic virus',
 'Soybean powdery mildew',
 'Soybean rust',
 'Soybean southern blight']

MODEL_strawberry_Class_names =  ['Random Image / Data Not Available', 'Strawberry Leaf scorch', 'Strawberry Healthy']

MODEL_sugarcane_Class_names = ['Random Image / Data Not Available',
 'Sugarcane bacterial blight',
 'Sugarcane Healthy',
 'Sugarcane red rot',
 'Sugarcane red stripe',
 'Sugarcane rust']

MODEL_tea_Class_names = ['Random Image / Data Not Available',
 'Tea algal leaf',
 'Tea anthracnose',
 'Tea brown blight',
 'Tea Healthy',
 'Tea red leaf spot']

MODEL_tomato_Class_names = ['Random Image / Data Not Available',
 'Tomato Bacterial spot',
 'Tomato Early blight',
 'Tomato Late blight',
 'Tomato Leaf Mold',
 'Tomato Septoria leaf spot',
 'Tomato Spider mites Two spotted spider mite',
 'Tomato Target Spot',
 'Tomato Tomato mosaic virus',
 'Tomato Healthy',
 'Tomato yellow leaf curl virus']
 
MODEL_wheat_Class_names = ['Random Image / Data Not Available',
 'Wheat brown rust',
 'Wheat Healthy',
 'Wheat septoria',
 'Wheat yellow rust']


try:
	MODEL_apple = load_model("pld_app/saved_models/apple.h5")
	MODEL_cabbage = load_model("pld_app/saved_models/cabbage.h5")
	MODEL_cassava = load_model("pld_app/saved_models/cassava.h5")
	MODEL_cherry = load_model("pld_app/saved_models/cherry.h5")
	MODEL_chili = load_model("pld_app/saved_models/chili.h5")
	MODEL_coffee = load_model("pld_app/saved_models/coffee.h5")
	MODEL_corn = load_model("pld_app/saved_models/corn.h5")
	MODEL_cucumber = load_model("pld_app/saved_models/cucumber.h5")
	MODEL_garlic = load_model("pld_app/saved_models/garlic.h5")
	MODEL_gauva = load_model("pld_app/saved_models/gauva.h5")
	MODEL_ginger = load_model("pld_app/saved_models/ginger.h5")
	MODEL_grape = load_model("pld_app/saved_models/grape.h5")
	MODEL_jamun = load_model("pld_app/saved_models/jamun.h5")
	MODEL_lemon = load_model("pld_app/saved_models/lemon.h5")
	MODEL_mango = load_model("pld_app/saved_models/mango.h5")
	MODEL_orange = load_model("pld_app/saved_models/orange.h5")
	MODEL_peach = load_model("pld_app/saved_models/peach.h5")
	MODEL_pepper = load_model("pld_app/saved_models/pepper.h5")
	MODEL_pome = load_model("pld_app/saved_models/pome.h5")
	MODEL_potatoes = load_model("pld_app/saved_models/potatoes.h5")
	MODEL_rice = load_model("pld_app/saved_models/rice.h5")
	MODEL_soybean = load_model("pld_app/saved_models/soybean.h5")
	MODEL_strawberry = load_model("pld_app/saved_models/strawberry.h5")
	MODEL_sugarcane = load_model("pld_app/saved_models/sugarcane.h5")
	MODEL_tea = load_model("pld_app/saved_models/tea.h5")
	MODEL_tomato = load_model("pld_app/saved_models/tomato.h5")
	MODEL_wheat = load_model("pld_app/saved_models/wheat.h5")
except FileNotFoundError:
	print("Error: Some 'plants models' file was not found.")
	MODEL = None




def health(request):
	return HttpResponse(Plant.objects.count())


@csrf_exempt
def plants_collection(request):

	plants_collection = Plant.objects.all()



	data = [
		{"name": "Apple", "classes": "Apple scab, Black rot, Cedar apple rust, healthy"},
		{"name": "Cabbage", "classes": "looper"},
		{"name": "Cassava", "classes": "Bacterial blight, brown streak disease, green mottle, healthy, mosaic disease"},
		{"name": "Cherry", "classes": "(including sour) healthy, (including sour) Powdery mildew"},
		{"name": "Chilli", "classes": "Healthy, leaf curl, leaf spot, whitefly, yellowish (including sour) healthy, (including sour) Powdery mildew"},
		{"name": "Coffee", "classes": "Cercospora leaf spot, healthy, red spider mite, rust"},
		{"name": "Corn", "classes": "Blight in corn Leaf, Common Rust in corn Leaf, Corn (maize) healthy, Gray Leaf Spot in corn Leaf"},
		{"name": "Cucumber", "classes": "Diseased, healthy"},
		{"name": "Garlic", "classes": "Diseased, healthy"},
		{"name": "Gauva", "classes": "Diseased, healthy"},
		{"name": "Ginger", "classes": "Diseased, healthy"},
		{"name": "Grape", "classes": "Black rot, Esca Black Measles, healthy, Leaf blight Isariopsis Leaf Spot"},
		{"name": "Jamun", "classes": "Diseased, healthy"},
		{"name": "Lemon", "classes": "Diseased, healthy"},
		{"name": "Mango", "classes": "Diseased, healthy"},
		{"name": "Orange", "classes": "Haunglongbing Citrus greening"},
		{"name": "Peach", "classes": "Bacterial spot, healthy"},
		{"name": "Pepper", "classes": "Bacterial spot, healthy"},
		{"name": "Pomegrante", "classes": "Diseased, healthy"},
		{"name": "Potato", "classes": "Early blight, healthy, hollow heart, Late blight"},
		{"name": "Random Images", "classes": "Random Images"},
		{"name": "Rice", "classes": "Brown spot, healthy, hispa, leaf blast, neck blast"},
		{"name": "Soybean", "classes": "Bacterial blight, caterpillar, diabrotica speciosa, downy mildew, healthy, mosaic virus, powdery mildew, rust, southern blight"},
		{"name": "Strawberry", "classes": "Healthy, Leaf scorch"},
		{"name": "Sugarcane", "classes": "Bacterial blight, healthy, red rot, red stripe, rust"},
		{"name": "Tea", "classes": "Algal leaf, anthracnose, brown blight, healthy, red leaf spot"},
		{"name": "Tomato", "classes": "Bacterial spot, Early blight, healthy, Late blight, Leaf Mold, Septoria leaf spot, Spider mites Two spotted spider mite, Target Spot, mosaic virus, yellow leaf curl virus"},
		{"name": "Wheat", "classes": "Brown rust, healthy, septoria, yellow rust"}
	]
	
	context = {
		'plants_collection':plants_collection,
		'data':data,
	}
	
	return render(request, 'pld_app/main/plants-collection.html',context)


@csrf_exempt
def about_us(request):
	return render(request, 'pld_app/main/about-us.html')


@csrf_exempt
def contact_us(request):
	if request.method == 'POST':
		try:
			result_to_show = Contact.objects.create(
				name = str(request.POST['name']),
				number = str(request.POST['number']),
				email = str(request.POST['email']),
				message = str(request.POST['message']),
			)

			return redirect("/")
		except:
			pass
	return render(request, 'pld_app/main/contact-us.html')


@csrf_exempt
def prediction_result(request):

	print(request)
	print(request)
	print(request.method)

	if request.method == "GET":
		return render(request, 'pld_app/main/prediction-result.html')
		# return redirect('/')
	if request.method == 'POST':
		return render(request, 'pld_app/main/prediction-result.html')


@csrf_exempt
def home(request):

	if request.method == "GET":
		plants_collection = Plant.objects.all()
		context = {
			'plants_collection':plants_collection,
		}
		return render(request, 'pld_app/main/index.html',context)

	if request.method == 'POST' and request.FILES.get('plant_leaf_image') and request.POST['plant_type']:

		plant_type = request.POST['plant_type']

		# Define the mapping of plant types to models
		plant_type_to_model = {
			"Apple": MODEL_apple,
			"Cabbage": MODEL_cabbage,
			"Cassava": MODEL_cassava,
			"Cherry": MODEL_cherry,
			"Chilli": MODEL_chili,
			"Coffee": MODEL_coffee,
			"Corn": MODEL_corn,
			"Cucumber": MODEL_cucumber,
			"Garlic": MODEL_garlic,
			"Gauva": MODEL_gauva,
			"Ginger": MODEL_ginger,
			"Grape": MODEL_grape,
			"Jamun": MODEL_jamun,
			"Lemon": MODEL_lemon,
			"Mango": MODEL_mango,
			"Orange": MODEL_orange,
			"Peach": MODEL_peach,
			"Pepper": MODEL_pepper,
			"Pomegrante": MODEL_pome,
			"Potato": MODEL_potatoes,
			"Rice": MODEL_rice,
			"Soybean": MODEL_soybean,
			"Strawberry": MODEL_strawberry,
			"Sugarcane": MODEL_sugarcane,
			"Tea": MODEL_tea,
			"Tomato": MODEL_tomato,
			"Wheat": MODEL_wheat,
			# Add more plant types and their corresponding models here
		}

		# Check if the selected plant type exists in the mapping
		if plant_type in plant_type_to_model:
			MODEL = plant_type_to_model[plant_type]
		else:
			# Handle the case where the selected plant type is not found
			MODEL = None  # You can set a default model or raise an error as needed



		# Define the mapping of plant types to models
		plant_type_to_class_names = {
			"Apple": MODEL_apple_Class_names,
			"Cabbage": MODEL_cabbage_Class_names,
			"Cassava": MODEL_cassava_Class_names,
			"Cherry": MODEL_cherry_Class_names,
			"Chilli": MODEL_chili_Class_names ,
			"Coffee": MODEL_coffee_Class_names,
			"Corn": MODEL_corn_Class_names,
			"Cucumber": MODEL_cucumber_Class_names,
			"Garlic": MODEL_garlic_Class_names,
			"Gauva": MODEL_gauva_Class_names,
			"Ginger": MODEL_ginger_Class_names,
			"Grape": MODEL_grape_Class_names,
			"Jamun": MODEL_jamun_Class_names,
			"Lemon": MODEL_lemon_Class_names,
			"Mango": MODEL_mango_Class_names,
			"Orange": MODEL_orange_Class_names,
			"Peach": MODEL_peach_Class_names,
			"Pepper": MODEL_pepper_Class_names,
			"Pomegrante": MODEL_pome_Class_names,
			"Potato": MODEL_potatoes_Class_names,
			"Rice": MODEL_rice_Class_names,
			"Soybean": MODEL_soybean_Class_names,
			"Strawberry": MODEL_strawberry_Class_names,
			"Sugarcane": MODEL_sugarcane_Class_names,
			"Tea": MODEL_tea_Class_names,
			"Tomato": MODEL_tomato_Class_names,
			"Wheat": MODEL_wheat_Class_names,
			# Add more plant types and their corresponding models here
		}

		# Check if the selected plant type exists in the mapping
		if plant_type in plant_type_to_class_names:
			CLASS_NAMES = plant_type_to_class_names[plant_type]
		else:
			# Handle the case where the selected plant type is not found
			CLASS_NAMES = None  # You can set a default model or raise an error as needed

		if MODEL != None:
			if CLASS_NAMES != None:
				image_file = request.FILES.get('plant_leaf_image')
				image = read_file_as_image(image_file.read())
				try:
					image = image/255
					img_batch = tf.expand_dims(image, 0)
					# print(MODEL)
					# print(img_batch)
					# print(MODEL.summary())
					if MODEL != None:
						predictions = MODEL.predict(img_batch)
						# print(predictions)
						# print(np.argmax(predictions[0]))
						predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
						confidence = round(100* (np.max(predictions[0])),2)
						response_data = {
							'class': predicted_class,
							'confidence': float(confidence)
						}

						fs = FileSystemStorage()
						filename = fs.save(image_file.name, image_file)
						uploaded_file_url = fs.url(filename)
						url = uploaded_file_url

						result_to_show = Prediction.objects.create(
							predictions = str(response_data)
						)

						plant_type_cures = {
							"Apple": [
								{"title": "Fungicide Treatment", "subtitle": "Apply fungicides with myclobutanil or captan."},
								{"title": "Pruning", "subtitle": "Remove infected branches and leaves."},
								{"title": "Sanitation", "subtitle": "Collect and dispose of fallen leaves."},
							],
							"Cabbage": [
								{"title": "Pesticide Application", "subtitle": "Apply pesticides to control cabbage looper."},
								{"title": "Crop Rotation", "subtitle": "Practice crop rotation to reduce pest buildup."},
								{"title": "Companion Planting", "subtitle": "Plant companion crops that deter pests."},
							],
							"Cassava": [
								{"title": "Fungicide Treatment", "subtitle": "Apply fungicides to control bacterial blight and brown streak disease."},
								{"title": "Sanitation", "subtitle": "Remove and destroy infected plants."},
								{"title": "Plant Resistant Varieties", "subtitle": "Choose cassava varieties with disease resistance."},
							],
							"Cherry": [
								{"title": "Pruning", "subtitle": "Prune infected branches to reduce disease spread."},
								{"title": "Fungicide Application", "subtitle": "Apply fungicides for powdery mildew control."},
								{"title": "Sanitation", "subtitle": "Remove fallen leaves and fruit mummies."},
							],
							"Chilli": [
								{"title": "Pest Control", "subtitle": "Use organic or chemical methods to control pests."},
								{"title": "Foliar Spray", "subtitle": "Apply foliar sprays for leaf diseases."},
								{"title": "Companion Planting", "subtitle": "Plant basil or marigold as companions for pest control."},
							],
							"Coffee": [
								{"title": "Fungicide Treatment", "subtitle": "Apply fungicides for leaf spot control."},
								{"title": "Pruning", "subtitle": "Prune infected branches."},
								{"title": "Integrated Pest Management", "subtitle": "Use IPM techniques to control pests."},
							],
							"Corn": [
								{"title": "Fungicide Application", "subtitle": "Apply fungicides for leaf diseases."},
								{"title": "Crop Rotation", "subtitle": "Rotate corn crops to reduce disease pressure."},
								{"title": "Plant Resistant Varieties", "subtitle": "Choose corn varieties with disease resistance."},
							],
							"Cucumber": [
								{"title": "Pesticide Application", "subtitle": "Apply pesticides for pest control."},
								{"title": "Companion Planting", "subtitle": "Plant nasturtium or marigold as companions for pest deterrence."},
								{"title": "Hand-Picking Pests", "subtitle": "Hand-pick and destroy pests like cucumber beetles."},
							],
							"Garlic": [
								{"title": "Fungicide Treatment", "subtitle": "Apply fungicides for leaf diseases."},
								{"title": "Sanitation", "subtitle": "Remove infected leaves and plant debris."},
								{"title": "Plant Resistant Varieties", "subtitle": "Choose garlic varieties with disease resistance."},
							],
							"Gauva": [
								{"title": "Pesticide Application", "subtitle": "Apply pesticides for pest control."},
								{"title": "Fruit Bagging", "subtitle": "Use fruit bags to protect guava from pests."},
								{"title": "Pruning", "subtitle": "Prune infected branches and leaves."},
							],
							"Ginger": [
								{"title": "Fungicide Treatment", "subtitle": "Apply fungicides for leaf spot control."},
								{"title": "Sanitation", "subtitle": "Remove and destroy infected plants."},
								{"title": "Plant Resistant Varieties", "subtitle": "Choose ginger varieties with disease resistance."},
							],
							"Grape": [
								{"title": "Fungicide Application", "subtitle": "Apply fungicides for disease control."},
								{"title": "Pruning", "subtitle": "Prune grapevines to improve air circulation."},
								{"title": "Sanitation", "subtitle": "Remove and destroy infected leaves and fruit clusters."},
							],
							"Jamun": [
								{"title": "Pesticide Application", "subtitle": "Apply pesticides for pest control."},
								{"title": "Fruit Bagging", "subtitle": "Use fruit bags to protect jamun from pests."},
								{"title": "Pruning", "subtitle": "Prune infected branches and leaves."},
							],
							"Lemon": [
								{"title": "Pesticide Application", "subtitle": "Apply pesticides for pest control."},
								{"title": "Pruning", "subtitle": "Prune infected branches and leaves."},
								{"title": "Sanitation", "subtitle": "Remove and destroy infected fruit and leaves."},
							],
							"Mango": [
								{"title": "Fungicide Treatment", "subtitle": "Apply fungicides for disease control."},
								{"title": "Pruning", "subtitle": "Prune infected branches and leaves."},
								{"title": "Sanitation", "subtitle": "Collect and destroy fallen leaves and fruit mummies."},
							],
							"Orange": [
								{"title": "Fungicide Application", "subtitle": "Apply fungicides for disease control."},
								{"title": "Pruning", "subtitle": "Prune infected branches."},
								{"title": "Sanitation", "subtitle": "Remove and destroy infected leaves and fruit."},
							],
							"Peach": [
								{"title": "Fungicide Treatment", "subtitle": "Apply fungicides for peach tree diseases."},
								{"title": "Pruning", "subtitle": "Prune infected branches and twigs."},
								{"title": "Sanitation", "subtitle": "Remove and destroy infected fruit and leaves."},
							],
							"Pepper": [
								{"title": "Pesticide Application", "subtitle": "Apply pesticides for pepper pest control."},
								{"title": "Companion Planting", "subtitle": "Plant basil or marigold as companions for pest deterrence."},
								{"title": "Pruning", "subtitle": "Prune infected branches and leaves."},
							],
							"Pomegrante": [
								{"title": "Fungicide Treatment", "subtitle": "Apply fungicides for leaf spot control."},
								{"title": "Pruning", "subtitle": "Prune infected branches and leaves."},
								{"title": "Sanitation", "subtitle": "Remove and destroy infected leaves and fruit."},
							],
							"Potato": [
								{"title": "Fungicide Application", "subtitle": "Apply fungicides for early and late blight control."},
								{"title": "Hilling", "subtitle": "Hill soil around potato plants to protect tubers."},
								{"title": "Sanitation", "subtitle": "Remove and destroy infected plants and tubers."},
							],
							"Rice": [
								{"title": "Fungicide Treatment", "subtitle": "Apply fungicides for rice diseases."},
								{"title": "Flood Irrigation", "subtitle": "Use flood irrigation to control pests and diseases."},
								{"title": "Crop Rotation", "subtitle": "Rotate rice crops to reduce disease pressure."},
							],
							"Soybean": [
								{"title": "Pesticide Application", "subtitle": "Apply pesticides for soybean pests."},
								{"title": "Crop Rotation", "subtitle": "Rotate soybean crops to reduce pests and diseases."},
								{"title": "Sanitation", "subtitle": "Remove and destroy infected soybean plants."},
							],
							"Strawberry": [
								{"title": "Pesticide Application", "subtitle": "Apply pesticides for strawberry pests."},
								{"title": "Mulching", "subtitle": "Use mulch to prevent soil-borne diseases."},
								{"title": "Pruning", "subtitle": "Prune strawberry plants to improve air circulation."},
							],
							"Sugarcane": [
								{"title": "Fungicide Treatment", "subtitle": "Apply fungicides for sugarcane diseases."},
								{"title": "Pesticide Application", "subtitle": "Apply pesticides for sugarcane pests."},
								{"title": "Sanitation", "subtitle": "Remove and destroy infected sugarcane plants."},
							],
							"Tea": [
								{"title": "Pesticide Application", "subtitle": "Apply pesticides for tea plant pests."},
								{"title": "Pruning", "subtitle": "Prune tea bushes for disease control."},
								{"title": "Companion Planting", "subtitle": "Plant companion crops to deter pests."},
							],
							"Tomato": [
								{"title": "Fungicide Application", "subtitle": "Apply fungicides for tomato diseases."},
								{"title": "Pesticide Application", "subtitle": "Apply pesticides for tomato pests."},
								{"title": "Pruning", "subtitle": "Prune tomato plants for better air circulation."},
							],
							"Wheat": [
								{"title": "Fungicide Treatment", "subtitle": "Apply fungicides for wheat diseases."},
								{"title": "Crop Rotation", "subtitle": "Rotate wheat crops to reduce disease pressure."},
								{"title": "Sanitation", "subtitle": "Remove and destroy infected wheat plants."},
							],
						}


						# Check if the selected plant type exists in the mapping
						if plant_type in plant_type_cures:
							cures = plant_type_cures[plant_type]
						else:
							# Handle the case where the selected plant type is not found
							cures = None  # You can set a default model or raise an error as needed


						context = {
							'class': predicted_class,
							'confidence': float(confidence),
							'result_to_show': url,
							'plant_type': plant_type,
							'cures': cures,
						}

						print(context)
						# return redirect("/prediction-result", context)
						return render(request, 'pld_app/main/prediction-result.html',context)
				except:
					pass
		return redirect("/")