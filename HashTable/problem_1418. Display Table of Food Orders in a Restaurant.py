class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food_set = set()
        table_orders = {}
        for cust, table, food in orders:
            food_set.add(food)
            if table in table_orders:
                if food in table_orders[table]:
                    table_orders[table][food] += 1
                else:
                    table_orders[table][food] = 1
            else:
                table_orders[table] = {food: 1}

        food_list = sorted(list(food_set))

        display = [["Table"] + food_list]

        for table_num, orders_dict in sorted(table_orders.items(), key=lambda t: int(t[0])):
            row = [str(table_num)] + [str(orders_dict[food])
                                      if food in orders_dict else '0' for food in food_list]
            display.append(row)

        return display
