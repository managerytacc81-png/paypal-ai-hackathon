# PayPal AI Hackathon Devpost Submission: PayAgent
## Project Name: PayAgent — Autonomous Agentic Commerce, Invoicing & Dispute Defense Engine
## Elevator Pitch
An autonomous commerce middleware connecting AI agents to PayPal's Orders, Invoicing, Payouts, and Dispute Resolution APIs—enabling AI agents to sell services, invoice clients, and defend against chargebacks completely hands-free.

---

## Inspiration
As AI agents increasingly run autonomous tasks—from scraping market intelligence to code audits—they hit a payment wall. Agents cannot easily carry credit cards or navigate legacy banking portals.
PayPal's robust developer infrastructure (v2 Orders, Invoicing, and Payouts) provides the ideal institutional settlement rail. We built **PayAgent** to turn PayPal into the economic nervous system for autonomous AI agents.

---

## What It Does
1. **Agent-to-Human Dynamic Checkout:** Agents dynamically spin up PayPal v2 Orders when human users request premium tasks or dataset exports.
2. **Smart Milestone Invoicing:** Generates itemized, professional PayPal Invoices upon completed agent workflows.
3. **AI Dispute Defense Concierge:** Automatically scans server execution logs and API telemetry to draft legally rigorous chargeback defense packages for PayPal Resolution Center.
4. **Multi-Agent Revenue Splitting:** Automatically calculates affiliate and contributor shares, dispatching instant payouts via PayPal Payouts.

---

## How We Built It
- **PayPal Developer Platform:** Integrated PayPal Orders v2, Invoicing v2, Payouts v1, and Disputes API.
- **Agent Tool Protocol:** Packaged as native MCP (Model Context Protocol) tool definitions for immediate integration with Anthropic Claude, Google Gemini, and open-source agent runtimes.
- **Automated Verification:** Comprehensive test suite validating payment authorizations, invoice generation, and dispute evidence compilation.

---

## Try It Out / Build Instructions
```bash
cd /home/user/revenue-eval/submissions/paypal-ai-hackathon
python3 -m unittest test_payagent.py
python3 payagent.py demo
```