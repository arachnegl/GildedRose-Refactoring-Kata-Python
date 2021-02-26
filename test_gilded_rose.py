# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


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
        

class ItemTest(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(
             Item(name="A", sell_in=2, quality=0),
             Item(name="A", sell_in=2, quality=0),
        )

if __name__ == '__main__':
    unittest.main()
