# -*- coding: utf-8 -*-
import unittest

from gilded_rose import (
    Item, 
    Product,
    GildedRose,
    Sulfuras,
    AgedBrie,
)


_items = [
     dict(name="+5 Dexterity Vest", sell_in=10, quality=20),
     dict(name="Aged Brie", sell_in=2, quality=0),
     dict(name="Elixir of the Mongoose", sell_in=5, quality=7),
     dict(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
     dict(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
     dict(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
     dict(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
     dict(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
     dict(name="Conjured Mana Cake", sell_in=3, quality=6),
]


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_integration(self):
        items = [Item(**item) for item in _items]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        for orig, updated in zip(_items, gilded_rose.items):
            self.assertEqual(orig['name'], updated.name)
        

class ProductTest(unittest.TestCase):

    def test_equality(self):
        # import pdb; pdb.set_trace()
        self.assertEqual(
             Product(name="A", sell_in=2, quality=0),
             Product(name="A", sell_in=2, quality=0),
        )
        self.assertNotEqual(
             Product(name="A", sell_in=1, quality=0),
             Product(name="A", sell_in=2, quality=0),
        )


class ProductTest(unittest.TestCase):
    item = Item(name="A", sell_in=0, quality=80)
    klass = Product

    def test_to_and_from_item(self):
        as_product = Product.from_item(self.item)
        self.assertEqual(type(as_product), self.klass)
        self.assertEqual(
            # as Item doesn't support element wise equality we fall back on 
            # (somewhat brittle) repr comparison.
            str(Product.to_item(as_product)),
            str(self.item),
        )


class SulfurasTest(ProductTest):
    item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
    klass = Sulfuras

    def test_update(self):
        self.assertEqual(
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80).update(),
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        )
        self.assertEqual(
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=40, quality=80).update(),
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=40, quality=80),
        )
        self.assertNotEqual(
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=40, quality=80).update(),
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=39, quality=80),
        )


class AgedBrieTest(ProductTest):
    item = Item('Aged Brie', 10, 10)
    klass = AgedBrie

    def test_update(self):
        self.assertEqual(
            AgedBrie(name="Aged Brie", sell_in=10, quality=10).update(),
            AgedBrie(name="Aged Brie", sell_in=10, quality=11),
        )


if __name__ == '__main__':
    unittest.main()
