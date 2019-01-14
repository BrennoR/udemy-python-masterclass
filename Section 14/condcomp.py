menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("A meal was skipped")
print(meals)

meals = [meal for meal in menu if "spam" not in meal]
print(meals)

# if is being used to filter meals, can't have an else clause in the comprehension

meals_2 = [meal for meal in menu if "spam" not in meal if "chicken" not in meal]
print(meals_2)

meals_3 = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
print(meals_3)

fussy_meals = [meal for meal in menu if "spam" in meal or "egg" in meal if not
               ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)

fussy_meals = [meal for meal in menu if
               ("spam" in meal or "egg" in meal) and not ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)
