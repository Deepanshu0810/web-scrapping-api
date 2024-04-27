from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

# unique product view
class Product(Model):
    __keyspace__='scrapper_app'
    asin = columns.Text(primary_key=True, required=True)
    title = columns.Text()
    price_str = columns.Text(default='-1')

# detailed scrape event
class ProductScrapeEvent(Model):
    __keyspace__='scrapper_app'
    uuid = columns.UUID(primary_key=True)
    asin = columns.Text(required=True)
    title = columns.Text()
    price_str = columns.Text(default='-1')