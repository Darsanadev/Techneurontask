def reordering_plan(items):
    reordering_item = []

    for item in items:
        item_id = int(item ["item_id"])
        current_stock = item["current_stock"]
        forecasted_demand = item["forecasted_demand"]
        batch_size = item["batch_size"]
        reorder_cost_per_unit = item['reorder_cost_per_unit']
        
        if current_stock >= forecasted_demand: # out of stock avunila cost of oreder umilaa
            print("no out of stock")
            continue
        
        required_units = forecasted_demand - current_stock # how many needed

        if current_stock < forecasted_demand: # out of stock 
            amount=batch_size * reorder_cost_per_unit
            units_to_order = required_units + amount
        reordering_item.append((item_id, units_to_order))

    return reordering_item if reordering_item else "No reordering_item"

items = [
    {"item_id": 101, "current_stock": 20, "forecasted_demand": 50, "batch_size": 10, "reorder_cost_per_unit": 5},
    {"item_id": 102, "current_stock": 30, "forecasted_demand": 60, "batch_size": 20, "reorder_cost_per_unit": 6},

]
print(reordering_plan(items))




