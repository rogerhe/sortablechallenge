# tested for python 3.0
import json
from collections import defaultdict

#read products
products_file = open('products.txt', 'r')
p_by_m  = defaultdict(list) # p[manufacturer] = [p1, p2,...pn]
for p in products_file:
    product = json.loads(p)
    manufacturer = product['manufacturer']
    if manufacturer not in p_by_m:
        p_by_m[manufacturer] = []
    p_by_m[manufacturer].append(product)

#read listings
listings_file = open('listings.txt', 'r')
match_results = defaultdict(list)
for l in listings_file:
    listing = json.loads(l)
    for p in p_by_m[listing['manufacturer']]:
        if p['model'] in listing['title'] and \
            ('family' not in p or \
            'family' in p and p['family'] in listing['title']):
            match_results[p['product_name']].append(listing)
            break

result_file = open('result.txt', 'w')
for product, listings in match_results.items():
    result_file.write(json.dumps({
        'product_name':product,
        'listings':listings,
        })+"\n")
    