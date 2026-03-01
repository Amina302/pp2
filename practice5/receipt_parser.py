import re

# RegEx Tasks
text = input("Input text: ")

# 1
print(re.findall(r"ab*", text))

# 2
print(re.findall(r"ab{2,3}", text))

# 3
print(re.findall(r"[a-z]+_[a-z]+", text))

# 4
print(re.findall(r"[A-Z][a-z]+", text))

# 5
print(re.findall(r"a.*b", text))

# 6
text2 = input("Input text to replace: ")
print(re.sub(r"[ ,\.]", ":", text2))

# 7
snake = input("Input snake_case: ")
print(re.sub(r"_([a-z])", lambda x: x.group(1).upper(), snake))

# 8
camel = input("Input CamelCase: ")
print(re.split(r"(?=[A-Z])", camel))

# 9
print(re.sub(r"([A-Z])", r" \1", camel).strip())

# 10
print(re.sub(r"(?<!^)([A-Z])", r"_\1", camel).lower())

print()

# Receipt Parsing


with open("raw.txt", encoding="utf-8") as f:
    receipt = f.read()

# Products
products = re.findall(r"\d+\.\n([^\n]+)", receipt)
print("Products:")
print(products)
print()

# Prices
prices = re.findall(r"\d[\d\s]*,\d{2}", receipt)
print("Prices:")
print(prices)
print()

# Total
total = re.search(r"ИТОГО:\s*([\d\s]+,\d{2})", receipt)
print("Total:")
print(total.group(1))
print()

# Date & Time
date = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4}\s*\d{2}:\d{2}:\d{2})", receipt)
print("Date and time:")
print(date.group(1))
print()

# Payment method
payment = re.search(r"(Банковская карта|Наличные):", receipt)
print("Payment method:")
print(payment.group(1))
print()