# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exceptions import DropItem


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
