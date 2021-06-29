class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        #         # Single hashmap solution

        #         restaurant_pairs = {}

        #         # For list 1
        #         for idx, restaurant in enumerate(list1):
        #             if(restaurant not in restaurant_pairs):
        #                 restaurant_pairs[restaurant] = [idx]
        #             else:
        #                 restaurant_pairs[restaurant].append(idx)

        #         # For list 2
        #         for idx, restaurant in enumerate(list2):
        #             if(restaurant not in restaurant_pairs):
        #                 restaurant_pairs[restaurant] = [idx]
        #             else:
        #                 restaurant_pairs[restaurant].append(idx)

        #         for restaurant, indices in list(restaurant_pairs.items()):
        #             if len(indices) != 2:
        #                 unrequired = restaurant_pairs.pop(restaurant)

        #         min_index_sum = math.inf

        #         for restaurant in restaurant_pairs.keys():
        #             restaurant_pairs[restaurant] = sum(restaurant_pairs[restaurant])

        #         for value in restaurant_pairs.values():
        #             if value < min_index_sum:
        #                 min_index_sum = value

        #         return_list = []

        #         for restaurant, index_sum in restaurant_pairs.items():
        #             if(index_sum == min_index_sum):
        #                 return_list.append(restaurant)

        #         return return_list

        # Improved Single hashmap solution while adding list 2 elements

        restaurant_pairs = {}

        # For list 1
        for idx, restaurant in enumerate(list1):
            if restaurant not in restaurant_pairs:
                restaurant_pairs[restaurant] = [idx]
            else:
                restaurant_pairs[restaurant].append(idx)

        # For list 2
        for idx, restaurant in enumerate(list2):
            if restaurant in restaurant_pairs:
                restaurant_pairs[restaurant].append(idx)

        for restaurant, indices in list(restaurant_pairs.items()):
            if len(indices) != 2:
                unrequired = restaurant_pairs.pop(restaurant)

        min_index_sum = math.inf

        for restaurant in restaurant_pairs.keys():
            restaurant_pairs[restaurant] = sum(restaurant_pairs[restaurant])

        for value in restaurant_pairs.values():
            if value < min_index_sum:
                min_index_sum = value

        return_list = []

        for restaurant, index_sum in restaurant_pairs.items():
            if index_sum == min_index_sum:
                return_list.append(restaurant)

        return return_list
