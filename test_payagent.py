"""
Unit tests for PayAgent PayPal AI Engine
"""

import unittest
from payagent import (
    OrderRequest,
    InvoiceItem,
    DisputeDefenseCase,
    PayPalClientMockable,
    DisputeDefenseEngine
)

class TestPayAgent(unittest.TestCase):
    def setUp(self):
        self.client = PayPalClientMockable()

    def test_create_order(self):
        req = OrderRequest(
            intent="CAPTURE",
            currency_code="USD",
            amount=50.0,
            reference_id="TEST_REF_01",
            description="Unit Test Order"
        )
        resp = self.client.create_order(req)
        self.assertEqual(resp["status"], "CREATED")
        self.assertIn("links", resp)
        self.assertTrue(resp["id"].startswith("PAY-"))

    def test_generate_invoice(self):
        items = [
            InvoiceItem("Service A", 2, 25.0, "Description A"),
            InvoiceItem("Service B", 1, 50.0, "Description B")
        ]
        resp = self.client.generate_invoice("client@test.com", items)
        self.assertEqual(resp["status"], "DRAFT")
        self.assertEqual(resp["amount"]["value"], "100.00")
        self.assertEqual(len(resp["items"]), 2)

    def test_batch_payout(self):
        payouts = [
            {"recipient_email": "agent1@test.com", "amount": 20.0},
            {"recipient_email": "agent2@test.com", "amount": 30.0}
        ]
        resp = self.client.batch_payout(payouts)
        self.assertEqual(resp["batch_header"]["batch_status"], "SUCCESS")
        self.assertEqual(len(resp["items"]), 2)

    def test_dispute_defense_packet(self):
        case = DisputeDefenseCase(
            dispute_id="DISP-12345",
            transaction_id="TX-9999",
            buyer_email="buyer@test.com",
            dispute_reason="UNAUTHORISED",
            disputed_amount=100.0,
            evidence_proof_urls=["https://test.com/log.txt"],
            delivery_timestamp="2026-11-02T10:00:00Z",
            service_delivery_summary="Delivered with verified digital signature"
        )
        defense = DisputeDefenseEngine.build_defense_packet(case)
        self.assertEqual(defense["dispute_id"], "DISP-12345")
        self.assertIn("Delivered with verified digital signature", defense["rebuttal_statement"])
        self.assertEqual(defense["recommended_action"], "SUBMIT_EVIDENCE_TO_PAYPAL_RESOLUTION_CENTER")

if __name__ == "__main__":
    unittest.main()
