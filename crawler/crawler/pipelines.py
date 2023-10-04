# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exceptions import DropItem
import psycopg2


class DuplicatesPipeline:
    def __init__(self):
        self.unique_items = set()

    def process_item(self, item, spider):
        from_ = item.get("from_")
        to_ = item.get("to_")
        if (from_, to_) in self.unique_items:
            raise DropItem(f"Duplicate item found: from={from_}, to={to_}")
        else:
            self.unique_items.add((from_, to_))
            return item


class SaveToPostgresPipeline:
    def __init__(self, database_settings):
        self.database_settings = database_settings

    @classmethod
    def from_crawler(cls, crawler):
        return cls(database_settings=crawler.settings.get("DATABASE_SETTINGS"))

    def open_spider(self, spider):
        self.conn = psycopg2.connect(**self.database_settings)
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

    def process_item(self, item, spider):
        query_first = "INSERT INTO from_to_urls (from_, to_) VALUES (%s, %s)"
        values = (
            item["from_"],
            item["to_"],
        )
        self.cursor.execute(query_first, values)
        _values = (
            item["hash_from_"],
            item["hash_to_"],
        )
        query_second = "INSERT INTO from_to_hashes (from_, to_) VALUES (%s, %s)"
        self.cursor.execute(query_second, _values)
        self.conn.commit()
        return item
