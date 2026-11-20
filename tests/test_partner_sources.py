import csv
import json
from pathlib import Path
import unittest


RECORDS = Path(__file__).resolve().parents[1] / 'records'
SCHEMAS = {'anchor_registry.csv': ['anchor', 'script', 'origin_school', 'location', 'purpose', 'paper_a', 'paper_b', 'score_a', 'score_b'], 'travel_roster.csv': ['person', 'school', 'age_group', 'travel', 'unfunded'], 'office_exchange.json': 'dict'}


class PartnerSourceTests(unittest.TestCase):
    def test_format(self):
        for name, shape in SCHEMAS.items():
            with self.subTest(name=name), (RECORDS / name).open(encoding='utf-8', newline='') as source:
                if isinstance(shape, list):
                    rows = csv.DictReader(source)
                    self.assertEqual(rows.fieldnames, shape)
                    records = list(rows)
                    self.assertTrue(records)
                    self.assertTrue(all(None not in row and None not in row.values() for row in records))
                else:
                    records = json.load(source)
                    self.assertIsInstance(records, list if shape == 'list' else dict)
                    self.assertTrue(records)
