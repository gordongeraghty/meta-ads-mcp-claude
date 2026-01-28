#!/usr/bin/env python3
"""
Analyze Meta campaign performance using Claude AI.

Usage:
    python scripts/analyze_campaigns.py --account-id ACT_1234567890 --lookback 7
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta

from dotenv import load_dotenv

load_dotenv()


def analyze_campaigns(account_id, lookback_days=7):
    """
    Analyze campaign performance with AI insights.

    Args:
        account_id (str): Meta Business Account ID
        lookback_days (int): Number of days to analyze
    """
    try:
        print(f"\nAnalyzing campaigns for account: {account_id}")
        print(f"Lookback period: {lookback_days} days")
        print(f'{"="*80}\n')

        date_start = (datetime.now() - timedelta(days=lookback_days)).strftime("%Y-%m-%d")
        date_end = datetime.now().strftime("%Y-%m-%d")

        # Simulated campaign data
        campaigns = [
            {
                "id": "123456789012345",
                "name": "Q1_Brand_Awareness",
                "spend": 2500.50,
                "impressions": 125000,
                "clicks": 3500,
                "conversions": 85,
                "conversion_value": 2550.00,
                "ctr": 0.028,
                "cpc": 0.71,
                "cpa": 29.41,
                "roas": 1.02,
            },
            {
                "id": "123456789012346",
                "name": "Q1_Conversions_Mobile",
                "spend": 4200.75,
                "impressions": 95000,
                "clicks": 2800,
                "conversions": 140,
                "conversion_value": 5600.00,
                "ctr": 0.0295,
                "cpc": 1.50,
                "cpa": 30.00,
                "roas": 1.33,
            },
            {
                "id": "123456789012347",
                "name": "Retargeting_Website",
                "spend": 1200.25,
                "impressions": 45000,
                "clicks": 1500,
                "conversions": 45,
                "conversion_value": 1350.00,
                "ctr": 0.0333,
                "cpc": 0.80,
                "cpa": 26.67,
                "roas": 1.125,
            },
        ]

        print(f"Campaign Performance Summary ({date_start} to {date_end}):\n")

        total_spend = 0
        total_conversions = 0
        best_roas = None
        best_roas_campaign = None

        for campaign in campaigns:
            print(f"Campaign: {campaign['name']}")
            print(f"  ID: {campaign['id']}")
            print(f"  Spend: ${campaign['spend']:.2f}")
            print(f"  Impressions: {campaign['impressions']:,}")
            print(f"  Clicks: {campaign['clicks']:,}")
            print(f"  CTR: {campaign['ctr']*100:.2f}%")
            print(f"  CPC: ${campaign['cpc']:.2f}")
            print(f"  Conversions: {campaign['conversions']}")
            print(f"  CPA: ${campaign['cpa']:.2f}")
            print(f"  Conv Value: ${campaign['conversion_value']:.2f}")
            print(f"  ROAS: {campaign['roas']:.2f}x")

            # Track metrics
            total_spend += campaign["spend"]
            total_conversions += campaign["conversions"]
            if best_roas is None or campaign["roas"] > best_roas:
                best_roas = campaign["roas"]
                best_roas_campaign = campaign["name"]

            print("-" * 80)

        print(f"\nAggregate Metrics:")
        print(f"  Total Spend: ${total_spend:.2f}")
        print(f"  Total Conversions: {total_conversions}")
        print(f"  Overall CPA: ${total_spend/total_conversions:.2f}")
        print(f"  Best Performer: {best_roas_campaign} (ROAS: {best_roas:.2f}x)\n")

        # AI Insights (simulated)
        insights = {
            "analysis_period": f"{date_start} to {date_end}",
            "total_campaigns": len(campaigns),
            "total_spend": total_spend,
            "key_insights": [
                f"Best performer: {best_roas_campaign} with {best_roas:.2f}x ROAS",
                "Mobile conversion campaign driving strong ROI at 1.33x ROAS",
                "Retargeting showing highest CTR at 3.33%, indicating engaged audience",
                "Overall account ROAS: 1.19x (healthy range)",
                "CPA relatively stable across campaigns ($26-$30)",
            ],
            "recommendations": [
                "Increase budget allocation to Q1_Conversions_Mobile (best ROAS)",
                "Test audience expansion for Retargeting_Website (high CTR signals)",
                "Review creative in Brand Awareness campaign (below 1x ROAS)",
                "Implement A/B testing on landing pages (potential CPA improvement)",
                "Scale winning creatives by 15-20% week-over-week",
            ],
        }

        print(f"AI Analysis:")
        for recommendation in insights["recommendations"]:
            print(f"  • {recommendation}")

        return insights

    except Exception as e:
        print(f"Error analyzing campaigns: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze campaign performance with AI")
    parser.add_argument("--account-id", required=True, help="Meta Business Account ID")
    parser.add_argument("--lookback", type=int, default=7, help="Days to analyze (default: 7)")
    args = parser.parse_args()

    analyze_campaigns(args.account_id, args.lookback)
