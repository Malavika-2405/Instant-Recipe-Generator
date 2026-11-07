
# ==========================================
# INSTANT RECIPE GENERATOR
# Recipe Dataset
# ==========================================

RECIPES = [

    {
        "id": 1,
        "name": "Vegetable Fried Rice",
        "description": "A delicious Indo-Chinese rice dish loaded with fresh vegetables.",
        "cuisine": "Chinese",
        "diet": ["Vegetarian", "Vegan"],
        "prep_time": 10,
        "cook_time": 15,
        "difficulty": "Easy",
        "servings": 2,
        "ingredients": [
            {"name": "rice", "quantity": 2, "unit": "cups"},
            {"name": "carrot", "quantity": 1, "unit": "piece"},
            {"name": "onion", "quantity": 1, "unit": "piece"},
            {"name": "capsicum", "quantity": 1, "unit": "piece"},
            {"name": "soy sauce", "quantity": 2, "unit": "tbsp"},
            {"name": "garlic", "quantity": 3, "unit": "cloves"},
            {"name": "oil", "quantity": 2, "unit": "tbsp"}
        ],
        "instructions": [
            "Cook the rice and allow it to cool.",
            "Chop all the vegetables into small pieces.",
            "Heat oil in a pan and saute garlic and onion.",
            "Add carrot and capsicum and stir-fry for a few minutes.",
            "Add cooked rice and soy sauce.",
            "Mix everything well and serve hot."
        ],
        "nutrition": {
            "calories": 320,
            "protein": 7,
            "carbs": 58,
            "fat": 8
        }
    },

    {
        "id": 2,
        "name": "Paneer Butter Masala",
        "description": "Rich and creamy Indian paneer curry with aromatic spices.",
        "cuisine": "Indian",
        "diet": ["Vegetarian", "Gluten-Free"],
        "prep_time": 15,
        "cook_time": 25,
        "difficulty": "Medium",
        "servings": 2,
        "ingredients": [
            {"name": "paneer", "quantity": 200, "unit": "g"},
            {"name": "tomato", "quantity": 3, "unit": "pieces"},
            {"name": "onion", "quantity": 1, "unit": "piece"},
            {"name": "butter", "quantity": 2, "unit": "tbsp"},
            {"name": "cream", "quantity": 3, "unit": "tbsp"},
            {"name": "ginger garlic paste", "quantity": 1, "unit": "tbsp"},
            {"name": "garam masala", "quantity": 1, "unit": "tsp"}
        ],
        "instructions": [
            "Cut paneer into medium-sized cubes.",
            "Heat butter in a pan and saute onions.",
            "Add tomatoes and ginger garlic paste.",
            "Cook until soft and blend into a smooth paste.",
            "Add the paste back to the pan with spices.",
            "Add paneer cubes and cream.",
            "Simmer for 5 minutes and serve hot."
        ],
        "nutrition": {
            "calories": 380,
            "protein": 18,
            "carbs": 14,
            "fat": 28
        }
    },

    {
        "id": 3,
        "name": "Masala Dosa",
        "description": "Crispy South Indian dosa filled with flavorful potato masala.",
        "cuisine": "Indian",
        "diet": ["Vegetarian", "Vegan", "Gluten-Free"],
        "prep_time": 15,
        "cook_time": 20,
        "difficulty": "Medium",
        "servings": 2,
        "ingredients": [
            {"name": "dosa batter", "quantity": 2, "unit": "cups"},
            {"name": "potato", "quantity": 2, "unit": "pieces"},
            {"name": "onion", "quantity": 1, "unit": "piece"},
            {"name": "mustard seeds", "quantity": 1, "unit": "tsp"},
            {"name": "green chilli", "quantity": 2, "unit": "pieces"},
            {"name": "turmeric", "quantity": 0.5, "unit": "tsp"},
            {"name": "oil", "quantity": 2, "unit": "tbsp"}
        ],
        "instructions": [
            "Boil and mash the potatoes.",
            "Heat oil and add mustard seeds.",
            "Add onions, green chillies and turmeric.",
            "Add mashed potatoes and mix well.",
            "Heat a dosa pan and spread the batter.",
            "Cook until crispy and place potato masala inside.",
            "Fold and serve with chutney."
        ],
        "nutrition": {
            "calories": 290,
            "protein": 6,
            "carbs": 48,
            "fat": 8
        }
    },

    {
        "id": 4,
        "name": "Tomato Pasta",
        "description": "Italian-style pasta with a fresh and flavorful tomato sauce.",
        "cuisine": "Italian",
        "diet": ["Vegetarian", "Vegan"],
        "prep_time": 10,
        "cook_time": 20,
        "difficulty": "Easy",
        "servings": 2,
        "ingredients": [
            {"name": "pasta", "quantity": 200, "unit": "g"},
            {"name": "tomato", "quantity": 3, "unit": "pieces"},
            {"name": "garlic", "quantity": 3, "unit": "cloves"},
            {"name": "onion", "quantity": 1, "unit": "piece"},
            {"name": "olive oil", "quantity": 2, "unit": "tbsp"},
            {"name": "oregano", "quantity": 1, "unit": "tsp"},
            {"name": "chilli flakes", "quantity": 0.5, "unit": "tsp"}
        ],
        "instructions": [
            "Boil pasta in salted water until cooked.",
            "Heat olive oil in a pan.",
            "Add chopped garlic and onion.",
            "Add tomatoes and cook until soft.",
            "Season with oregano and chilli flakes.",
            "Add cooked pasta and mix thoroughly.",
            "Serve warm."
        ],
        "nutrition": {
            "calories": 350,
            "protein": 11,
            "carbs": 55,
            "fat": 10
        }
    },

    {
        "id": 5,
        "name": "Chicken Biryani",
        "description": "Aromatic Indian rice dish cooked with spiced chicken.",
        "cuisine": "Indian",
        "diet": ["Non-Vegetarian", "Gluten-Free"],
        "prep_time": 20,
        "cook_time": 40,
        "difficulty": "Hard",
        "servings": 2,
        "ingredients": [
            {"name": "chicken", "quantity": 300, "unit": "g"},
            {"name": "basmati rice", "quantity": 1.5, "unit": "cups"},
            {"name": "onion", "quantity": 2, "unit": "pieces"},
            {"name": "tomato", "quantity": 1, "unit": "piece"},
            {"name": "yogurt", "quantity": 0.5, "unit": "cup"},
            {"name": "ginger garlic paste", "quantity": 1, "unit": "tbsp"},
            {"name": "biryani masala", "quantity": 2, "unit": "tbsp"}
        ],
        "instructions": [
            "Wash and soak basmati rice.",
            "Marinate chicken with yogurt and spices.",
            "Fry onions until golden brown.",
            "Add tomatoes and marinated chicken.",
            "Cook until the chicken is nearly done.",
            "Add partially cooked rice over the chicken.",
            "Cover and cook on low heat until rice and chicken are fully cooked.",
            "Garnish and serve hot."
        ],
        "nutrition": {
            "calories": 520,
            "protein": 32,
            "carbs": 62,
            "fat": 16
        }
    },

    {
        "id": 6,
        "name": "Vegetable Sandwich",
        "description": "A quick and healthy sandwich filled with fresh vegetables.",
        "cuisine": "Continental",
        "diet": ["Vegetarian"],
        "prep_time": 10,
        "cook_time": 5,
        "difficulty": "Easy",
        "servings": 2,
        "ingredients": [
            {"name": "bread", "quantity": 4, "unit": "slices"},
            {"name": "tomato", "quantity": 1, "unit": "piece"},
            {"name": "cucumber", "quantity": 1, "unit": "piece"},
            {"name": "onion", "quantity": 1, "unit": "piece"},
            {"name": "butter", "quantity": 2, "unit": "tbsp"},
            {"name": "cheese", "quantity": 2, "unit": "slices"}
        ],
        "instructions": [
            "Wash and slice all vegetables.",
            "Spread butter on bread slices.",
            "Arrange cucumber, tomato and onion.",
            "Add cheese slices.",
            "Cover with another bread slice.",
            "Toast until golden brown and serve."
        ],
        "nutrition": {
            "calories": 280,
            "protein": 10,
            "carbs": 34,
            "fat": 12
        }
    },

    {
        "id": 7,
        "name": "Chickpea Salad",
        "description": "A refreshing protein-rich salad with chickpeas and vegetables.",
        "cuisine": "Mediterranean",
        "diet": ["Vegetarian", "Vegan", "Gluten-Free"],
        "prep_time": 15,
        "cook_time": 0,
        "difficulty": "Easy",
        "servings": 2,
        "ingredients": [
            {"name": "chickpeas", "quantity": 1, "unit": "cup"},
            {"name": "cucumber", "quantity": 1, "unit": "piece"},
            {"name": "tomato", "quantity": 1, "unit": "piece"},
            {"name": "onion", "quantity": 0.5, "unit": "piece"},
            {"name": "lemon", "quantity": 1, "unit": "piece"},
            {"name": "olive oil", "quantity": 1, "unit": "tbsp"}
        ],
        "instructions": [
            "Cook or drain the chickpeas.",
            "Chop cucumber, tomato and onion.",
            "Add all ingredients to a bowl.",
            "Squeeze fresh lemon juice.",
            "Add olive oil and mix well.",
            "Serve fresh."
        ],
        "nutrition": {
            "calories": 220,
            "protein": 10,
            "carbs": 32,
            "fat": 7
        }
    },

    {
        "id": 8,
        "name": "Vegetable Noodles",
        "description": "Quick stir-fried noodles with colorful vegetables.",
        "cuisine": "Chinese",
        "diet": ["Vegetarian", "Vegan"],
        "prep_time": 10,
        "cook_time": 15,
        "difficulty": "Easy",
        "servings": 2,
        "ingredients": [
            {"name": "noodles", "quantity": 200, "unit": "g"},
            {"name": "carrot", "quantity": 1, "unit": "piece"},
            {"name": "cabbage", "quantity": 1, "unit": "cup"},
            {"name": "capsicum", "quantity": 1, "unit": "piece"},
            {"name": "soy sauce", "quantity": 2, "unit": "tbsp"},
            {"name": "garlic", "quantity": 3, "unit": "cloves"}
        ],
        "instructions": [
            "Boil noodles according to package instructions.",
            "Drain and keep aside.",
            "Heat oil in a wok.",
            "Add garlic and chopped vegetables.",
            "Stir-fry on high heat.",
            "Add noodles and soy sauce.",
            "Toss well and serve."
        ],
        "nutrition": {
            "calories": 330,
            "protein": 9,
            "carbs": 52,
            "fat": 10
        }
    },

    {
        "id": 9,
        "name": "Mushroom Soup",
        "description": "A warm and creamy mushroom soup for a comforting meal.",
        "cuisine": "Continental",
        "diet": ["Vegetarian", "Gluten-Free"],
        "prep_time": 10,
        "cook_time": 20,
        "difficulty": "Easy",
        "servings": 2,
        "ingredients": [
            {"name": "mushroom", "quantity": 200, "unit": "g"},
            {"name": "onion", "quantity": 1, "unit": "piece"},
            {"name": "garlic", "quantity": 2, "unit": "cloves"},
            {"name": "milk", "quantity": 1, "unit": "cup"},
            {"name": "butter", "quantity": 1, "unit": "tbsp"},
            {"name": "black pepper", "quantity": 0.5, "unit": "tsp"}
        ],
        "instructions": [
            "Wash and slice the mushrooms.",
            "Melt butter in a pan.",
            "Add garlic and onion and saute.",
            "Add mushrooms and cook until soft.",
            "Pour in milk and simmer.",
            "Blend partially for a creamy texture.",
            "Add black pepper and serve warm."
        ],
        "nutrition": {
            "calories": 180,
            "protein": 7,
            "carbs": 14,
            "fat": 11
        }
    },

    {
        "id": 10,
        "name": "Egg Fried Rice",
        "description": "A simple and tasty fried rice with scrambled eggs.",
        "cuisine": "Chinese",
        "diet": ["Non-Vegetarian"],
        "prep_time": 10,
        "cook_time": 10,
        "difficulty": "Easy",
        "servings": 2,
        "ingredients": [
            {"name": "rice", "quantity": 2, "unit": "cups"},
            {"name": "egg", "quantity": 2, "unit": "pieces"},
            {"name": "carrot", "quantity": 1, "unit": "piece"},
            {"name": "spring onion", "quantity": 2, "unit": "stalks"},
            {"name": "soy sauce", "quantity": 1, "unit": "tbsp"},
            {"name": "oil", "quantity": 2, "unit": "tbsp"}
        ],
        "instructions": [
            "Cook rice and allow it to cool.",
            "Beat eggs in a bowl.",
            "Heat oil and scramble the eggs.",
            "Add chopped carrot and spring onion.",
            "Add cooked rice and soy sauce.",
            "Mix well and serve hot."
        ],
        "nutrition": {
            "calories": 360,
            "protein": 12,
            "carbs": 50,
            "fat": 11
        }
    },

    {
        "id": 11,
        "name": "Banana Pancakes",
        "description": "Soft and fluffy pancakes made with ripe bananas.",
        "cuisine": "Continental",
        "diet": ["Vegetarian"],
        "prep_time": 10,
        "cook_time": 15,
        "difficulty": "Easy",
        "servings": 2,
        "ingredients": [
            {"name": "banana", "quantity": 2, "unit": "pieces"},
            {"name": "flour", "quantity": 1, "unit": "cup"},
            {"name": "milk", "quantity": 0.5, "unit": "cup"},
            {"name": "egg", "quantity": 1, "unit": "piece"},
            {"name": "sugar", "quantity": 1, "unit": "tbsp"},
            {"name": "butter", "quantity": 1, "unit": "tbsp"}
        ],
        "instructions": [
            "Mash ripe bananas in a bowl.",
            "Add flour, milk, egg and sugar.",
            "Mix until a smooth batter forms.",
            "Heat a pan and add butter.",
            "Pour a small amount of batter.",
            "Cook both sides until golden brown.",
            "Serve with banana slices or honey."
        ],
        "nutrition": {
            "calories": 290,
            "protein": 8,
            "carbs": 48,
            "fat": 8
        }
    },

    {
        "id": 12,
        "name": "Chicken Pepper Fry",
        "description": "A spicy South Indian chicken dish with freshly ground black pepper.",
        "cuisine": "Indian",
        "diet": ["Non-Vegetarian", "Gluten-Free"],
        "prep_time": 15,
        "cook_time": 25,
        "difficulty": "Medium",
        "servings": 2,
        "ingredients": [
            {"name": "chicken", "quantity": 300, "unit": "g"},
            {"name": "onion", "quantity": 2, "unit": "pieces"},
            {"name": "tomato", "quantity": 1, "unit": "piece"},
            {"name": "black pepper", "quantity": 1, "unit": "tsp"},
            {"name": "ginger garlic paste", "quantity": 1, "unit": "tbsp"},
            {"name": "curry leaves", "quantity": 10, "unit": "leaves"},
            {"name": "oil", "quantity": 2, "unit": "tbsp"}
        ],
        "instructions": [
            "Clean and cut the chicken into small pieces.",
            "Heat oil in a pan and add curry leaves.",
            "Add onions and saute until golden.",
            "Add ginger garlic paste and tomatoes.",
            "Add chicken and cook with the spices.",
            "Add freshly ground black pepper.",
            "Cook until the chicken is fully cooked and serve hot."
        ],
        "nutrition": {
            "calories": 310,
            "protein": 30,
            "carbs": 10,
            "fat": 17
        }
    }

]
