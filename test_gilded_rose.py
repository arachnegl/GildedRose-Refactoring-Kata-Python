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
    Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
    Item(name="Aged Brie", sell_in=2, quality=0),
    Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
    Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
    Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
    Item(name="Conjured Mana Cake", sell_in=3, quality=6),
]


class GildedRoseTest(unittest.TestCase):
    def test_integration(self):
        gilded_rose = GildedRose(_items)
        gilded_rose.update_quality()

        expected = [
            "+5 Dexterity Vest, 9, 19",
            "Aged Brie, 1, 1",
            "Elixir of the Mongoose, 4, 6",
            "Sulfuras, Hand of Ragnaros, 0, 80",
            "Sulfuras, Hand of Ragnaros, -1, 80",
            "Backstage passes to a TAFKAL80ETC concert, 14, 21",
            "Backstage passes to a TAFKAL80ETC concert, 9, 50",
            "Backstage passes to a TAFKAL80ETC concert, 4, 50",
            "Conjured Mana Cake, 2, 5",
        ]

        self.assertListEqual(
            list(map(str, gilded_rose.items)),
            expected,
        )


class ProductTest(unittest.TestCase):
    item = Item(name="A", sell_in=0, quality=80)
    klass = Product

    def test_equality(self):
        self.assertEqual(
            Product(name="A", sell_in=2, quality=0),
            Product(name="A", sell_in=2, quality=0),
        )
        self.assertNotEqual(
            Product(name="A", sell_in=1, quality=0),
            Product(name="A", sell_in=2, quality=0),
        )

    def test_to_and_from_item(self):
        as_product = Product.from_item(self.item)
        self.assertEqual(type(as_product), self.klass)
        self.assertEqual(
            # as Item doesn't support element wise equality we fall back on
            # (somewhat brittle) repr comparison.
            str(Product.to_item(as_product)),
            str(self.item),
        )

    def test_update(self):
        self.assertEqual(
            Product(name="+5 Dexterity Vest", sell_in=10, quality=20).update(),
            Product(name="+5 Dexterity Vest", sell_in=9, quality=19),
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
            Sulfuras(
                name="Sulfuras, Hand of Ragnaros", sell_in=40, quality=80
            ).update(),
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=40, quality=80),
        )
        self.assertNotEqual(
            Sulfuras(
                name="Sulfuras, Hand of Ragnaros", sell_in=40, quality=80
            ).update(),
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=39, quality=80),
        )


class AgedBrieTest(ProductTest):
    item = Item("Aged Brie", 10, 10)
    klass = AgedBrie

    def test_update(self):
        self.assertEqual(
            AgedBrie(name="Aged Brie", sell_in=10, quality=10).update(),
            AgedBrie(name="Aged Brie", sell_in=9, quality=11),
        )


if __name__ == "__main__":
    unittest.main()
