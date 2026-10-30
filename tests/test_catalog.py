import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import ai_engineer

class CatalogTests(unittest.TestCase):
    def test_scenario_search(self):
        self.assertTrue(any(x["id"]=="fincrime-graphrag" for x in ai_engineer.discover("fincrime")))
    def test_unique(self):
        data=ai_engineer.catalog()
        ids=[x["id"] for x in data["scenarios"]]
        self.assertEqual(len(ids),len(set(ids)))
    def test_dry_run_no_write(self):
        with tempfile.TemporaryDirectory() as td:
            result=ai_engineer.install(td,"graphrag",dry_run=True)
            self.assertTrue(result["dry_run"])
            self.assertFalse((Path(td)/".ai-engineer-install.json").exists())
    def test_reject_unknown_pack(self):
        with tempfile.TemporaryDirectory() as td:
            with self.assertRaises(ValueError):
                ai_engineer.install(td,"unknown")
if __name__=="__main__":
    unittest.main()
