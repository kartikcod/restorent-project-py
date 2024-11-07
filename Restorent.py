Menu={
    'pasta':20,
    'pizza':50,
    'rasgulla':44,
    'samosa':70,
    'chat':30
}
print("Welcome to python restorent--")
print("pizza Rs:50\npasta Rs:50\nrasgulla Rs:44\nsamosa Rs:70\nchat Rs:30\n")

total_amount=0

item_1=input ("Enter the name of item you want to order you =")

if item_1 in Menu:
          total_amount+=Menu[item_1]
          print(f"your item {item_1} Has been added to you order")

else:
    print("ordered item {item_1} are not available")

another_item=input("Do you want another item yes/no:")
if another_item =="yes":
   item_2=  input("Enter the name of second item Name:")
   if item_2 in Menu:
       total_amount+=Menu[item_2]
       print(f"Your second item {item_2} has been added to you order")

   else:
       print(f"item {item_2} are not available")


print(f"your total amount is :{total_amount}")
print("Thank You! visit again!")