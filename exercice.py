#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        values = []
        for i in range(10):
            values.append(input("Donnez une valeur : "))

    return sorted(values)


def anagrams(words: list = None) -> bool:
    if words is None:
        words = []
        words.append(sorted(input("Input a word : ")))
        words.append(sorted(input("Input a word : ")))

    return words[0] == words[1]


def contains_doubles(items: list) -> bool:
    item_dict = {}
    for item in items:
        if item not in item_dict:
            item_dict.update({item: 0})
        else:
            return False

    return True


def best_grades(student_grades: dict) -> dict:
    student_grades = {key: value for key, value in sorted(student_grades.items(), key=lambda x: sum(x[1]) / len(x[1]), reverse=True)}

    best_student = list(student_grades.keys())[0]
    grade = sum(student_grades[best_student]) / len(student_grades[best_student])

    return {best_student: grade}


def frequence(sentence: str) -> dict:
    letter_dict = {}

    for char in sentence:
        if char == ' ' or char == ',' or char == '.' or char == ';' or char == ':':
            continue
        
        if char not in letter_dict:
            letter_dict.update({char: 1})
        else:
            letter_dict[char] += 1

    letter_dict = {key: value for key, value in sorted(letter_dict.items(), key=lambda x: x[1], reverse=True)}
    
    for key, value in letter_dict.items():
        if value > 5:
            print(key)

    return letter_dict

recipe_dict = {}

def get_recipes():
    recipe_name = input("What is the name of your recipe? : ")
    ingredient_list = []

    while True:
        ingredient = input("Enter an ingredient in the recipe or 'end' to stop the inputs : ")

        if ingredient == 'end':
            break

        ingredient_list.append(ingredient)

    recipe_dict.update({recipe_name : ingredient_list})

def print_recipe(ingredients) -> None:
    recipe_name = input("What is the name of your recipe? : ")
    
    if recipe_name in recipe_dict:
        for ingredient in recipe_dict[recipe_name]:
            print(ingredient)
    else:
        print("this recipe doesn't exist")


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
