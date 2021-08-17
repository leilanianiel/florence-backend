import os
from app.models.fridge import Fridge
from app.models.customer import Customer
from flask import Blueprint, json, request, jsonify, make_response
from dotenv import load_dotenv
from app import db, app
from app.models.product import Product
from app.models.category import Category
import datetime
from flask_login import login_required, current_user
import requests
recipes_bp = Blueprint("recipes", __name__, url_prefix="/recipes")

# GET ALL PRODUCTS


@recipes_bp.route("/<id>", methods=["GET"], strict_slashes=False)
@login_required
def get_recipe_detail(id):
    
    if "development" in os.environ.get("FLASK_ENV"):
    
        testData = """{"aggregateLikes": 1, "analyzedInstructions": [{"name": "", "steps": [{"equipment": [{"id": 404784, "image": "oven.jpg", "localizedName": "oven", "name": "oven"}], "ingredients": [{"id": 10018137, "image": "", "localizedName": "cake mix", "name": "cake mix"}, {"id": 9236, "image": "peach.png", "localizedName": "peach", "name": "peach"}, {"id": 1019016, "image": "apple-juice.jpg", "localizedName": "juice", "name": "juice"}], "number": 1, "step": "When oven is preheated, pour the whole can of peaches and juice into oven. Then add the dry cake mix on top of the peaches."}, {"equipment": [], "ingredients": [{"id": 2010, "image": "cinnamon.jpg", "localizedName": "cinnamon", "name": "cinnamon"}, {"id": 1001, "image": "butter-sliced.jpg", "localizedName": "butter", "name": "butter"}], "number": 2, "step": "Place several pieces of butter on top, and sprinkle cinnamon over all."}, {"equipment": [{"id": 404784, "image": "oven.jpg", "localizedName": "oven", "name": "oven"}], "ingredients": [{"id": 9236, "image": "peach.png", "localizedName": "peach", "name": "peach"}], "length": {"number": 45, "unit": "minutes"}, "number": 3, "step": "Place lid on oven and bake about 45 minutes. Recipe will give a layer of peaches with a cake covering."}, {"equipment": [], "ingredients": [], "number": 4, "step": "Serves 8.Variations"}, {"equipment": [{"id": 404784, "image": "oven.jpg", "localizedName": "oven", "name": "oven"}], "ingredients": [{"id": 10018137, "image": "", "localizedName": "cake mix", "name": "cake mix"}, {"id": 9236, "image": "peach.png", "localizedName": "peach", "name": "peach"}], "number": 5, "step": "Stir the cake mix and peaches when placed in oven to provide a more spongy layer of cake."}, {"equipment": [], "ingredients": [{"id": 2001, "image": "allspice-ground.jpg", "localizedName": "allspice", "name": "allspice"}, {"id": 2010, "image": "cinnamon.jpg", "localizedName": "cinnamon", "name": "cinnamon"}, {"id": 9236, "image": "peach.png", "localizedName": "peach", "name": "peach"}, {"id": 9003, "image": "apple.jpg", "localizedName": "apple", "name": "apple"}], "number": 6, "step": "Use canned apples instead of peaches, and add 1 Tbsp. cinnamon and 1 tsp. allspice to the apples."}, {"equipment": [], "ingredients": [{"id": 9070, "image": "cherries.jpg", "localizedName": "cherries", "name": "cherries"}, {"id": 9236, "image": "peach.png", "localizedName": "peach", "name": "peach"}, {"id": 19335, "image": "sugar-in-bowl.png", "localizedName": "sugar", "name": "sugar"}], "number": 7, "step": "Use canned cherries instead of peaches, and add more sugar with the cherries."}, {"equipment": [], "ingredients": [{"id": 18114, "image": "spice-cake.jpg", "localizedName": "spice cake mix", "name": "spice cake mix"}, {"id": 10118137, "image": "white-cake-mix.png", "localizedName": "white cake mix", "name": "white cake mix"}], "number": 8, "step": "Instead of the white cake mix, use a yellow or spice cake mix."}]}], "cheap": false, "creditsText": "Foodista.com \u2013 The Cooking Encyclopedia Everyone Can Edit", "cuisines": ["Southern"], "dairyFree": false, "diets": [], "dishTypes": ["side dish"], "extendedIngredients": [{"aisle": "Milk, Eggs, Other Dairy", "amount": 8.0, "consistency": "solid", "id": 1001, "image": "butter-sliced.jpg", "measures": {"metric": {"amount": 8.0, "unitLong": "servings", "unitShort": "servings"}, "us": {"amount": 8.0, "unitLong": "servings", "unitShort": "servings"}}, "meta": [], "metaInformation": [], "name": "butter", "nameClean": "butter", "original": "butter", "originalName": "butter", "originalString": "butter", "unit": "servings"}, {"aisle": "Spices and Seasonings", "amount": 0.5, "consistency": "solid", "id": 2010, "image": "cinnamon.jpg", "measures": {"metric": {"amount": 0.5, "unitLong": "teaspoons", "unitShort": "tsps"}, "us": {"amount": 0.5, "unitLong": "teaspoons", "unitShort": "tsps"}}, "meta": [], "metaInformation": [], "name": "cinnamon", "nameClean": "cinnamon", "original": "1/2 teaspoon cinnamon", "originalName": "cinnamon", "originalString": "1/2 teaspoon cinnamon", "unit": "teaspoon"}, {"aisle": "Produce", "amount": 1.0, "consistency": "solid", "id": 9236, "image": "peach.png", "measures": {"metric": {"amount": 1.0, "unitLong": "large can", "unitShort": "large can"}, "us": {"amount": 1.0, "unitLong": "large can", "unitShort": "large can"}}, "meta": ["sliced"], "metaInformation": ["sliced"], "name": "peaches", "nameClean": "peach", "original": "1 large can sliced peaches", "originalName": "sliced peaches", "originalString": "1 large can sliced peaches", "unit": "large can"}, {"aisle": "Baking", "amount": 1.0, "consistency": "solid", "id": 18137, "image": "white-cake-mix.jpg", "measures": {"metric": {"amount": 1.0, "unitLong": "", "unitShort": ""}, "us": {"amount": 1.0, "unitLong": "", "unitShort": ""}}, "meta": ["white"], "metaInformation": ["white"], "name": "white cake mix", "nameClean": "vanilla cake mix", "original": "1 pkt white cake mix", "originalName": "pkt white cake mix", "originalString": "1 pkt white cake mix", "unit": ""}], "gaps": "no", "glutenFree": false, "healthScore": 2.0, "id": 649381, "image": "https://spoonacular.com/recipeImages/649381-556x370.jpg", "imageType": "jpg", "instructions": "
When oven is preheated, pour the whole can of peaches and juice into oven. Then add the dry cake mix on top of the peaches. Place several pieces of butter on top, and sprinkle cinnamon over all. Place lid on oven and bake about 45 minutes. Recipe will give a layer of peaches with a cake covering.
Serves 8.
Variations
1. Stir the cake mix and peaches when placed in oven to provide a more spongy layer of cake.
2. Use canned apples instead of peaches, and add 1 Tbsp. cinnamon and 1 tsp. allspice to the apples.
3. Use canned cherries instead of peaches, and add more sugar with the cherries.
4. Instead of the white cake mix, use a yellow or spice cake mix.
", "license": "CC BY 3.0", "lowFodmap": false, "occasions": [], "originalId": null, "pricePerServing": 51.76, "readyInMinutes": 45, "servings": 8, "sourceName": "Foodista", "sourceUrl": "http://www.foodista.com/recipe/YH2LR73V/lazy-cobbler", "spoonacularScore": 22.0, "spoonacularSourceUrl": "https://spoonacular.com/lazy-cobbler-649381", "summary": "The recipe Lazy Cobbler could satisfy your Southern craving in about 45 minutes. For 52 cents per serving, this recipe covers 6% of your daily requirements of vitamins and minerals. This recipe makes 8 servings with 298 calories, 3g of protein, and 7g of fat each. Not a lot of people made this recipe, and 1 would say it hit the spot. A mixture of pkt cake mix, cinnamon, peaches, and a handful of other ingredients are all it takes to make this recipe so yummy. It works well as a dessert. All things considered, we decided this recipe deserves a spoonacular score of 24%. This score is rather bad. Similar recipes include Jiffy Peach Cobbler \u2013 A cobbler you can make anytime, with either fresh or store bought peaches, The Lazy Boy, and Lazy Pierogi.", "sustainable": false, "title": "Lazy Cobbler", "vegan": false, "vegetarian": false, "veryHealthy": false, "veryPopular": false, "weightWatcherSmartPoints": 12, "winePairing": {"pairedWines": ["riesling", "sparkling wine", "zinfandel"], "pairingText": "Riesling, Sparkling Wine, and Zinfandel are great choices for Southern. In general, there are a few rules that will help you pair wine with southern food. Food-friendly riesling or sparkling white wine will work with many fried foods, while zinfandel is great with barbecued fare. The Fess Parker Santa Barbara Riesling with a 4 out of 5 star rating seems like a good match. It costs about 9 dollars per bottle.", "productMatches": [{"averageRating": 0.8, "description": "Floral notes and orange blossoms, commingle with scents of citrus, peach, honeysuckle and light apricot on the nose. On the palate you will find flavors of peach, apricot and citrus. These flavors combine to produce an off-dry, yet well-balanced Riesling.", "id": 433832, "imageUrl": "https://spoonacular.com/productImages/433832-312x231.jpg", "link": "https://click.linksynergy.com/deeplink?id=*QCiIS6t4gA&mid=2025&murl=https%3A%2F%2Fwww.wine.com%2Fproduct%2Ffess-parker-santa-barbara-riesling-1999%2F13667", "price": "$8.98", "ratingCount": 8.0, "score": 0.76, "title": "Fess Parker Santa Barbara Riesling"}]}}"""
        return testData, 200

    r = requests.get(url=f'https://api.spoonacular.com/recipes/{id}/information', params={
        "apiKey": app.config["SPOONACULAR"]})
    print(r)
    # extracting data in json format
    data = r.json()
    return json.dumps(data), 200

def get_recipe_url(recipe_id):
    r = requests.get(url=f'https://api.spoonacular.com/recipes/{recipe_id}/information', params={
        "apiKey": app.config["SPOONACULAR"]})
    data = r.json()

    return data['sourceUrl']

    
@recipes_bp.route("", methods=["GET"], strict_slashes=False)
@login_required
def get_recipes():
    
    if "development" in os.environ.get("FLASK_ENV"):
        testingData = [{"id": 649381, "image": "https://spoonacular.com/recipeImages/649381-312x231.jpg", "imageType": "jpg", "likes": 1, "missedIngredientCount": 2, "missedIngredients": [{"aisle": "Spices and Seasonings", "amount": 0.5, "id": 2010, "image": "https://spoonacular.com/cdn/ingredients_100x100/cinnamon.jpg", "meta": [], "metaInformation": [], "name": "cinnamon", "original": "1/2 teaspoon cinnamon", "originalName": "cinnamon", "originalString": "1/2 teaspoon cinnamon", "unit": "teaspoon", "unitLong": "teaspoons", "unitShort": "tsp"}, {"aisle": "Baking", "amount": 1.0, "id": 18137, "image": "https://spoonacular.com/cdn/ingredients_100x100/white-cake-mix.jpg", "meta": ["white"], "metaInformation": ["white"], "name": "white cake mix", "original": "1 pkt white cake mix", "originalName": "pkt white cake mix", "originalString": "1 pkt white cake mix", "unit": "", "unitLong": "", "unitShort": ""}], "title": "Lazy Cobbler", "unusedIngredients": [{"aisle": "Produce", "amount": 1.0, "id": 11135, "image": "https://spoonacular.com/cdn/ingredients_100x100/cauliflower.jpg", "meta": [], "metaInformation": [], "name": "cauliflower", "original": "Cauliflower", "originalName": "Cauliflower", "originalString": "Cauliflower", "unit": "serving", "unitLong": "serving", "unitShort": "serving"}, {"aisle": "Produce", "amount": 1.0, "id": 9200, "image": "https://spoonacular.com/cdn/ingredients_100x100/orange.png", "meta": [], "metaInformation": [], "name": "oranges", "original": "Oranges", "originalName": "Oranges", "originalString": "Oranges", "unit": "serving", "unitLong": "serving", "unitShort": "serving"}], "usedIngredientCount": 2, "usedIngredients": [{"aisle": "Milk, Eggs, Other Dairy", "amount": 8.0, "id": 1001, "image": "https://spoonacular.com/cdn/ingredients_100x100/butter-sliced.jpg", "meta": [], "metaInformation": [], "name": "butter", "original": "butter", "originalName": "butter", "originalString": "butter", "unit": "servings", "unitLong": "servings", "unitShort": "servings"}, {"aisle": "Produce", "amount": 1.0, "extendedName": "canned peaches", "id": 9236, "image": "https://spoonacular.com/cdn/ingredients_100x100/peach.png", "meta": ["sliced"], "metaInformation": ["sliced"], "name": "peaches", "original": "1 large can sliced peaches", "originalName": "sliced peaches", "originalString": "1 large can sliced peaches", "unit": "large can", "unitLong": "large can", "unitShort": "large can"}]}, {"id": 157473, "image": "https://spoonacular.com/recipeImages/157473-312x231.jpg", "imageType": "jpg", "likes": 0, "missedIngredientCount": 2, "missedIngredients": [{"aisle": "Produce", "amount": 1.0, "id": 11215, "image": "https://spoonacular.com/cdn/ingredients_100x100/garlic.png", "meta": [], "metaInformation": [], "name": "garlic", "original": "1 head of garlic, roasted", "originalName": "garlic, roasted", "originalString": "1 head of garlic, roasted", "unit": "head", "unitLong": "head", "unitShort": "head"}, {"aisle": "Milk, Eggs, Other Dairy", "amount": 0.5, "id": 1077, "image": "https://spoonacular.com/cdn/ingredients_100x100/milk.png", "meta": ["2%", "(I used )"], "metaInformation": ["2%", "(I used )"], "name": "milk", "original": "1/2 cup milk (I used 2%)", "originalName": "milk (I used 2%)", "originalString": "1/2 cup milk (I used 2%)", "unit": "cup", "unitLong": "cups", "unitShort": "cup"}], "title": "Cauliflower Mash with Roasted Garlic", "unusedIngredients": [{"aisle": "Produce", "amount": 1.0, "id": 9236, "image": "https://spoonacular.com/cdn/ingredients_100x100/peach.png", "meta": [], "metaInformation": [], "name": "peaches", "original": "Peaches", "originalName": "Peaches", "originalString": "Peaches", "unit": "serving", "unitLong": "serving", "unitShort": "serving"}, {"aisle": "Produce", "amount": 1.0, "id": 9200, "image": "https://spoonacular.com/cdn/ingredients_100x100/orange.png", "meta": [], "metaInformation": [], "name": "oranges", "original": "Oranges", "originalName": "Oranges", "originalString": "Oranges", "unit": "serving", "unitLong": "serving", "unitShort": "serving"}], "usedIngredientCount": 2, "usedIngredients": [{"aisle": "Milk, Eggs, Other Dairy", "amount": 3.0, "id": 1001, "image": "https://spoonacular.com/cdn/ingredients_100x100/butter-sliced.jpg", "meta": [], "metaInformation": [], "name": "butter", "original": "3 tablespoons butter", "originalName": "butter", "originalString": "3 tablespoons butter", "unit": "tablespoons", "unitLong": "tablespoons", "unitShort": "Tbsp"}, {"aisle": "Produce", "amount": 1.0, "id": 11135, "image": "https://spoonacular.com/cdn/ingredients_100x100/cauliflower.jpg", "meta": ["cut into florets"], "metaInformation": ["cut into florets"], "name": "cauliflower", "original": "1 large head of cauliflower, cut into florets", "originalName": "cauliflower, cut into florets", "originalString": "1 large head of cauliflower, cut into florets", "unit": "large head", "unitLong": "large head", "unitShort": "large head"}]}]
        recipe_response = []
        
        for recipe in testingData:
            print(recipe)
            recipe_id = recipe['id']
            title = recipe['title']
            image = recipe["image"] #put into image tag
            url = get_recipe_url(recipe_id)

            recipe_dict = {
                "name" : title,
                "url" : url,
                "image" : image
            }
            recipe_response.append(recipe_dict)

        


        return jsonify(recipe_response), 200
    
    if current_user.is_authenticated:
        customer_id = current_user.id

        customer = Customer.query.get(customer_id)
        fridge = Fridge.query.get(customer.fridge_id)

        productNames = {}
        for item in fridge.items:
            product = Product.query.get(item.product_id)
            if product is None:
                continue

            productNames[product.name] = 1

        ingredientList = ''
        for name in productNames.keys():
            ingredientList += name + ","
        
        
        print(ingredientList)

        response = requests.get(url='https://api.spoonacular.com/recipes/findByIngredients', params={
            "ingredients": ingredientList,
            "apiKey": app.config["SPOONACULAR"], "number": 3})
        print(response)
        # extracting data in json format
        data = response.json()

        recipe_response = []
        
        for recipe in data:
            recipe_id = recipe['id']
            title = recipe['title']
            image = recipe['image']
            url = get_recipe_url(recipe_id)

            recipe_dict = {
                "name" : title,
                "url" : url,
                "image" : image,
                
            }
            recipe_response.append(recipe_dict)

        


        return jsonify(recipe_response), 200



# path = "https://us1.locationiq.com/v1/search.php"

# LOCATIONIQ_API_KEY = "...ec6a8368a..."

# query_params = {
#     "key": LOCATIONIQ_API_KEY,
#     "q": "Great Wall of China",
#     "format": "json"
# }

# response = requests.get(path, params=query_params)
