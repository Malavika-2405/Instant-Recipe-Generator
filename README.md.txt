# 🍃 Instant Recipe Generator – RecipeCraft

**Turn Your Ingredients Into Delicious Meals!**

An AI-powered recipe recommendation web application that helps users discover recipes using available ingredients or by uploading a photo of their fridge. Powered by Google Gemini AI.

## 🌐 Live Demo

**[Open RecipeCraft](https://instant-recipe-generator.onrender.com)**

## 📌 About the Project

Instant Recipe Generator is a smart kitchen assistant designed to make cooking easier and reduce food waste. Users can enter ingredients manually or upload a fridge/ingredient image. The application uses Gemini AI to identify ingredients and helps users discover suitable recipes.

## ✨ Features

- 🔍 **Ingredient-Based Recipe Search** – Find recipes using available ingredients.
- 🤖 **AI Ingredient Detection** – Identify ingredients from fridge images using Google Gemini AI.
- 🥗 **Dietary Preferences** – Filter vegetarian, vegan, and non-vegetarian recipes.
- 🌎 **Cuisine Filters** – Explore recipes from different cuisines.
- ⏱️ **Cooking Time Filters** – Find recipes based on available time.
- 🛒 **Missing Ingredients** – View ingredients needed to complete a recipe.
- 📖 **Recipe Details** – Get ingredients and step-by-step cooking instructions.
- 📊 **Nutrition Information** – View approximate nutritional values.
- ❤️ **Favourites** – Save and manage favourite recipes.
- ⭐ **Recipe Ratings** – Rate recipes based on your experience.
- 🍽️ **Serving Adjustment** – Adjust ingredient quantities based on servings.
- 🎲 **Surprise Me** – Discover a random recipe.
- 🛍️ **Shopping List** – Manage ingredients you need to purchase.

## 📸 Screenshots

### Homepage
![Homepage](screenshots/homepage.png)

### Recipe Results
![Recipe Results](screenshots/recipe-results.png)

### Recipe Details
![Recipe Details](screenshots/recipe-details.png)

### AI Fridge Ingredient Detection
![Fridge Detection](screenshots/fridge-detection.png)

### Favourites
![Favourites](screenshots/favorites.png)

### Shopping List
![Shopping List](screenshots/shopping-list.png)

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Flask | Web framework |
| Google Gemini AI | Image-based ingredient recognition |
| SQLite | Database |
| HTML5 | Webpage structure |
| CSS3 | Styling and responsive design |
| JavaScript | Frontend interactions |

## 📂 Project Structure

```text
Instant-Recipe-Generator/
│
├── app.py
├── recipes.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── database/
│   └── recipes.db
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── results.html
│   ├── recipe_details.html
│   ├── ingredient_review.html
│   ├── favorites.html
│   └── shopping_list.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│
└── utils/
    ├── __init__.py
    ├── recipe_engine.py
    └── image_detector.py
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Malavika-2405/Instant-Recipe-Generator.git
```

### 2. Navigate to the project directory

```bash
cd Instant-Recipe-Generator
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure the Gemini API key

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your own Gemini API key.

### 7. Run the application

```bash
python app.py
```

### 8. Open in your browser

```text
http://127.0.0.1:5000
```

## 🤖 How It Works

1. Users enter available ingredients or upload a fridge image.
2. Gemini AI identifies ingredients from the uploaded image.
3. Users can review and edit the detected ingredients.
4. The recipe engine searches for matching recipes.
5. Users can apply cuisine, dietary, and cooking-time filters.
6. Users can explore recipe instructions, nutrition information, favourites, and shopping lists.

## 🚀 Future Enhancements

- Expand the recipe database.
- Add multilingual recipe support.
- Improve personalized recipe recommendations.
- Introduce more advanced nutritional analysis.

## 👩‍💻 Developed By

**Malavika P**

B.E. Computer Science and Engineering

GitHub: [Malavika-2405](https://github.com/Malavika-2405)

---

⭐ If you find this project interesting, consider giving it a star on GitHub!

**RecipeCraft – Smart Recipes. Smarter Cooking!**
