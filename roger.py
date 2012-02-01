# tested for python 3.0
import json
from collections import defaultdict

#read products
products_file = open('products.txt', 'r')
p_by_m  = defaultdict(list) # p[manufacturer] = [p1, p2,...pn]
for p in products_file:
    product = json.loads(p)
    manufacturer = product['manufacturer'].lower()
    product['model'] = product['model'].lower().replace('-', '').replace(' ', '')
    if manufacturer not in p_by_m:
        p_by_m[manufacturer] = []
    p_by_m[manufacturer].append(product)

manufacturers = list(p_by_m.keys())
#read listings
listings_file = open('listings.txt', 'r')
match_results = defaultdict(list)
cnt = 0
for l in listings_file:
    listing = json.loads(l)
    manufacturer = ''
    for m in manufacturers:
        if m in listing['manufacturer'].lower():
            manufacturer = m
            break
    if not manufacturer:
        continue
    search_title = listing['title'].lower().replace('-', '').replace(' ', '')
    for p in p_by_m[m]:
        if p['model'] in search_title:
            match_results[p['product_name']].append(listing)
            cnt += 1
            break

#print ("%d products matched"%len(match_results))
#print ("%d listings matched"%cnt)
result_file = open('result.txt', 'w')
for product, listings in match_results.items():
    result_file.write(json.dumps({
        'product_name':product,
        'listings':listings,
        })+"\n")
    