from cassandra.cqlengine.management import sync_table
import uuid
from .models import Product, ProductScrapeEvent
from .db import get_cassandra_session

session = get_cassandra_session()
sync_table(Product)
sync_table(ProductScrapeEvent)

def create_entry(data:dict):
    Product.create(**data)

# data = {
#     'asin': 'B07JGTVTWN',
#     'title': 'title'
# }

def create_scrape_entry(data:dict):
    data['uuid'] = uuid.uuid1()
    ProductScrapeEvent.create(**data)