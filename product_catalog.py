from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
print(products)


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences = set(customer_preferences)



# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
append_converted = converted_products.append
for product in products:
    append_converted({"name": product["name"], "tags": set(product["tags"])})



# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags & customer_tags)




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommendations = []
    
    # Loop over each product
    for product in products:
        match_count = count_matches(product["tags"], customer_tags)
        
        # Store only products with at least one match
        if match_count > 0:
            recommendations.append({
                "name": product["name"],
                "matches": match_count
            })
    
    # Sort the recommendations by number of matches in descending order
    recommendations.sort(key=lambda x: x["matches"], reverse=True)
    
    return recommendations





# TODO: Step 7 - Call your function and print the results
recommendations = recommend_products(converted_products, customer_preferences)
print(recommendations)



# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. How might this code change if you had 1000+ products?
# 1. Core ops: list → set conversion to dedupe preferences; set intersection to count matches; loop over products to score; sort by match count to rank results.
# 2. For 1000+ products: precompute/ cache tag sets, avoid per-run conversions, and consider indexing tags to products to reduce full scans; possibly use a heap/partial sort to return top N.
#A tool which goes together with what customer are fond of with product tags in primitive python data structur and no harmonic operations. It is interested primarily in scoring and ranking products depending on the amount of tags they share. It receive inputs in the form of customers and items they like and lists them first. Having done this, we change that list into set whereby as duplicates move out and to do comparisons faster. The sets are effective as it is easy to check with it whether something is there and common things can be easily found with it. Its turned into sets of product tags also. That gets the ability to get matches by intersection of the two sets. The countmatches function is used to count out the number of tags overlapping the other by giving the size of that overlap. It's easy to read and fast. The recommendproducts feature performs a scan of the entire products and takes a look at the number of tags that they have in common and only products that have one or more hits are kept. It then ranks these products according to the highest to least score such that the best matches are displayed first. When the catalog hits beyond 1000 entries we can either accelerate it by pre-computing sets of tags (Done), creating indexes to connect tags to products or by just giving the N highest ranking records back in a heap rather than sorting them all. All in all, the system both remains to be clean, fast and scalable but at the same time remains simple.