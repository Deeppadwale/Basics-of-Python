
def calculate(a,b):
    mean=(a*b)/2
    return (mean)


output=calculate(10,20)
print(output)




def largestNNumber(a,b):
    if a>b :
        print("a is greter then b ")
    else:
        print("a less than b")
     

largestNNumber(10,20)




# 1. Check if a number is even or odd

def isEven(number):
    return number % 2==0

out=isEven(10)
out1=isEven(5)
out2=isEven(30)
out3=isEven(40)
out4=isEven(50)

print(out)
print(out1)
print(out2)
print(out3)
print(out4)


# find the largest of tree numbers

def max_largest_numbe(a,b,c):
    return max(a,b,c)

print(max_largest_numbe(10,20,30))
print(max_largest_numbe(555,550,330))
print(max_largest_numbe(1022,2033,3033))
print(max_largest_numbe(1012,2012,3012))




# Create a calculator for a grocery shop
def calculator(items):
    total = 0
    for item in items:
        name = item['name']
        price = item['price']
        quantity = item['quntity']  # Keep 'quntity' if matching input key
        subtotal = price * quantity

        print(f"{name}: {quantity} x ${price:.2f} = ${subtotal:.2f}")
        total += subtotal

    print(f"Total Bill: ${total:.2f}")
    return total

# List of items in the cart
cart = []

# Loop to input multiple products
while True:
    name = input("Enter a product name (or type 'done' to finish): ")
    if name.lower() == 'done':
        break
    price = float(input("Enter a price: "))
    quantity = int(input("Enter a quantity: "))

    # ✅ Correct dictionary: keys are strings, values are variables
    cart.append({'name': name, 'price': price, 'quntity': quantity})

# Run the calculator with the complete cart
calculator(cart)

