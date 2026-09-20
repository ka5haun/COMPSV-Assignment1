from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.



# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""

while response != "N":
    print("Input a preference:")
    preference = input()

    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []

for product in products:
    converted_product = product.copy()
    converted_product["tags"] = set(product["tags"])
    converted_products.append(converted_product)


# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags.intersection(customer_tags))




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    matches = []

    for product in products:
        match_count = count_matches(product["tags"], customer_tags)

        if match_count > 0:
            matches.append({
                "name": product["name"],
                "matches": match_count
            })

    matches.sort(key=lambda item: item["matches"], reverse=True)

    return matches

# TODO: Step 7 - Call your function and print the results

recommendations = recommend_products(converted_products, customer_preferences)

print("\nRecommend Products:")

for product in recommendations:
    print(f'-{product["name"]} ({product["matches"]} match(es))')


# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. How might this code change if you had 1000+ products?

1. In this program I used lists, sets, loops, and set intersections to compare customer preferences with product tags. The customer's 
preferences are collected in a list since a makes it easy to add each preference as the customer enters it. After that, the preferences 
are converted into a set. Using a set removes duplicate preferences and makes it easier to compare the preferences with the tags that 
each product has. I converted each product's tags into a set too. The count_matches function uses the intersection operation to find tags
that appear in both the product's tags and the customer's preferences. The length of the intersection tells the program how many matches a
product has. A loop is used in the recommend_products function to check every product in the catalog. Products with at least one match are 
added to the recommendation list, and the list is sorted so products with more matching tags show up first

2. If there was more than 1000 products I would think about changing the way that the products are searched. Instead of checking every 
product every time a customer enters a new preference, the program could create an index that connects each tag to the products that have 
that tag. This would make getting recommendations faster and for a bigger scale, product info could be stored in a database instead of 
directly in a python list.





