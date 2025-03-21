class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        foodStore = {recipes[i]:i for i in range(len(recipes))}
        supplies = set(supplies)
        reminder = set()
        answer = set()
        
        def can_I_Make(food_ptr):
            if recipes[food_ptr] in reminder: return False
            reminder.add(recipes[food_ptr])

            tempo = 0
            for ingredient in ingredients[food_ptr]:
                if ingredient in supplies or ingredient in answer:
                    tempo += 1
                elif ingredient in foodStore and can_I_Make(foodStore[ingredient]):
                    tempo += 1
                if tempo == len(ingredients[food_ptr]):
                    answer.add(recipes[food_ptr])
                    return True

            return False





        for i in range(len(recipes)):

            can_I_Make(i)
            
        return list(answer)