# -*- coding: utf-8 -*-
from dataclasses import dataclass

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        self.items = [
            Product.to_item(
                Product.from_item(item)
                .update()
            )
           for item in self.items
        ]
        return self


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


@dataclass
class Product:
    name: str
    sell_in: int
    quality: int

    max_quality: int = 50

    _class_name_to_class = None

    @classmethod
    def _get_class(cls, item: Item):
        if cls._class_name_to_class is None:
            cls._class_name_to_class = {P.name: P for P in Product.__subclasses__()}
        if item.name in cls._class_name_to_class:
            return cls._class_name_to_class[item.name]
        return cls

    @classmethod
    def from_item(cls, item):
        """Dispatches an Item object to its specialised Product if found else to 
        a generic Product.
        """
        return cls._get_class(item)(
            name=item.name,
            sell_in=item.sell_in,
            quality=item.quality,
        )

    def to_item(self):
        return Item(
            name=self.name,
            sell_in=self.sell_in,
            quality=self.quality,
        )

    def update(self):
        """The generic case
        """
        if self.quality > 0:
            self.quality = self.quality - 1

        self.sell_in = self.sell_in - 1

        if self.sell_in < 0:
            if self.quality > 0:
                if self.name != "Sulfuras, Hand of Ragnaros":
                    self.quality = self.quality - 1


        return self


class Sulfuras(Product):
    name = "Sulfuras, Hand of Ragnaros"
    quality = 80   # constant

    max_quality: int = 80

    def update(self) -> None:
        """
        Sulfuras, being a legendary item, never has to be sold or decreases in Quality
        """
        return self


class AgedBrie(Product):
    name = 'Aged Brie'

    def update(self) -> None:
        """
        "Aged Brie" actually increases in Quality the older it gets
        """
        if self.quality < 50:
            self.quality = self.quality + 1

        self.sell_in = self.sell_in - 1

        if self.sell_in < 0:
            if self.quality < 50:
                self.quality = self.quality + 1

        return self


class BackstagePass(Product):
    name = "Backstage passes to a TAFKAL80ETC concert"

    def update(self) -> None:

        if self.quality < 50:
            self.quality = self.quality + 1
            if self.sell_in < 11:
                if self.quality < 50:
                    self.quality = self.quality + 1
            if self.sell_in < 6:
                if self.quality < 50:
                    self.quality = self.quality + 1

        self.sell_in = self.sell_in - 1

        if self.sell_in < 0:
            if self.quality > 0:
                self.quality = self.quality - 1

        return self
