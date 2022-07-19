### Size of your array is the size of your menu
# here: 2 of item 3, 15 of item 4 etc 
my_order=[0,0,2,15,0,3,0]
# sanity check:
#my_order=[1,1,1,1,1,1,1]
## sanity check should respond with
## 1, base, base^2, base^3, etc

base=5 # free parameter

# initialization values
order_number=0
menu_size=len(my_order)

item_orders=list()
for menu_item,item_qty in enumerate(my_order):
    ui=item_qty//(base-1) # this is how many times do we need to repeat (base-1)
    item_number=0
    for i in range(0,ui):
        ith=(base-1)*base**(menu_size*i+menu_item)
        item_number+=ith
    item_number+=item_qty % (base-1) *base**(menu_size*ui+menu_item)
    item_orders.append(item_number)
    order_number+=item_number
print(f"Order with classical quantities: {my_order} ")
print(f"Base chosen: {base}")
print(f"Order with computed quantities and item index for each item: {item_orders}")
print(f"Final order: {order_number}")