import itertools
from src import split_data


class Day15(object):
    @split_data
    def cookies(self, instructions, only500cal=False):
        ingredients = self._handle_ingredients(instructions)
        ingredient_names = [ingredient['name'] for ingredient in ingredients]
        all_recipes = itertools.combinations_with_replacement(ingredient_names, 100)
        attributes = ['capacity', 'durability', 'flavor', 'texture', 'calories']
        recipes = {}
        for recipe in all_recipes:
            fact = self._build_sum(attributes)
            for name in ingredient_names:
                ingredient = [ingredient for ingredient in ingredients if ingredient['name'] == name][0]
                for attr in attributes:
                    fact[attr] += ingredient[attr] * recipe.count(name)

            if self._legal_cooking(fact, only500cal):
                total = fact['capacity'] * fact['durability'] * fact['flavor'] * fact['texture']
                recipes[total] = recipe
        return max(recipes.keys())

    def _build_sum(self, attributes):
        ingredients_sum = {}
        for attr in attributes:
            ingredients_sum[attr] = 0
        return ingredients_sum

    def _handle_ingredients(self, instructions):
        return [self._handle_ingredient(instruction.split(' ')) for instruction in instructions]

    def _handle_ingredient(self, result):
        return {
            'name': result[0],
            result[1]: int(result[2][:-1]),
            result[3]: int(result[4][:-1]),
            result[5]: int(result[6][:-1]),
            result[7]: int(result[8][:-1]),
            result[9]: int(result[10][:1]),
        }

    def _legal_cooking(self, fact, only500cal):
        legal = fact['capacity'] >= 0 and fact['durability'] >= 0 and fact['flavor'] >= 0 and fact['texture'] >= 0
        if only500cal and fact['calories'] != 500:
            legal = False
        return legal
