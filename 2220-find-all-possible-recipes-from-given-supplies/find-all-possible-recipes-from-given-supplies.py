class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Graph to keep track of dependencies
        graph = defaultdict(list)
        # In-degrees to count required ingredients for each recipe
        in_degrees = defaultdict(int)
        # Initial set of supplies
        available = set(supplies)
        # Queue for processing available ingredients/recipes
        queue = deque(supplies)
        # Set to collect the result recipes that can be made
        result = []

        # Build the graph and in-degree count
        for recipe, ingredient_list in zip(recipes, ingredients):
            in_degrees[recipe] = len(ingredient_list)
            for ingredient in ingredient_list:
                graph[ingredient].append(recipe)
        
        # Process the queue
        while queue:
            current = queue.popleft()
            
            for recipe in graph[current]:
                in_degrees[recipe] -= 1
                if in_degrees[recipe] == 0:
                    queue.append(recipe)
                    result.append(recipe)
        
        return result