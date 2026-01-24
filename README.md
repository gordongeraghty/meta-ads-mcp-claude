# Meta Ads Claude AI Integration

AI-powered campaign analysis and strategic recommendations using Claude API for Meta advertising intelligence.

## 🎯 Features

- **AI Campaign Analysis** - Deep analysis of campaign performance with Claude insights
- **Strategic Recommendations** - AI-generated optimization strategies
- **Metric Benchmarking** - Compare performance against industry benchmarks
- **Optimization Suggestions** - Context-aware tactical recommendations
- **Multi-metric Support** - Analyze ROAS, CPA, CTR, and more
- **Business Context Awareness** - Industry-specific insights (ecommerce, SaaS, services)

---

## 📋 Prerequisites

### Required

- **Python 3.11+**
- **pip** (Python package manager)
- **Anthropic API Key** (for Claude access)
  - Get from [Anthropic Console](https://console.anthropic.com/)
- **Meta Business Account** with Ads Manager access
- **Facebook Access Token** with `ads_read` permission

### API Access

1. **Anthropic Claude API**:
   - Go to [Anthropic Console](https://console.anthropic.com/)
   - Create API key in settings
   - Store in `.env` file

2. **Meta Credentials**:
   - Access Token: [Meta Apps Dashboard](https://developers.facebook.com/apps/)
   - Business Account ID: [Ads Manager](https://adsmanager.facebook.com/)

---

## 🚀 Setup Steps

### 1. Clone the Repository

```bash
git clone https://github.com/gordongeraghty/meta-ads-mcp-claude.git
cd meta-ads-mcp-claude
```

### 2. Create Virtual Environment

```bash
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Create `.env` file:

```bash
cp .env.example .env
```

Edit `.env`:

```env
FACEBOOK_ACCESS_TOKEN=your_access_token
FACEBOOK_BUSINESS_ACCOUNT_ID=ACT_1234567890
ANTHROPIC_API_KEY=your_claude_api_key
```

### 5. Verify Installation

```bash
python scripts/analyze_campaigns.py --account-id ACT_1234567890
```

---

## 📖 Per-Script Usage Examples

### Script 1: `analyze_campaigns.py` - AI Campaign Analysis

**Purpose**: Analyze campaign performance with AI-powered insights and recommendations.

**Command**:

```bash
python scripts/analyze_campaigns.py --account-id ACT_1234567890 --lookback 7
```

**Parameters**:

- `--account-id` (required): Meta Business Account ID
- `--lookback` (optional): Days of data to analyze (default: 7)

**Example Commands**:

```bash
# Analyze last 7 days of campaign data
python scripts/analyze_campaigns.py --account-id ACT_1234567890 --lookback 7

# Analyze last 30 days
python scripts/analyze_campaigns.py --account-id ACT_1234567890 --lookback 30

# Analyze last 14 days
python scripts/analyze_campaigns.py --account-id ACT_1234567890 --lookback 14
```

**Expected Output**:

```
Analyzing campaigns for account: ACT_1234567890
Lookback period: 7 days
================================================================================

Campaign Performance Summary (2024-01-15 to 2024-01-22):

Campaign: Q1_Brand_Awareness
  ID: 123456789012345
  Spend: $2,500.50
  Impressions: 125,000
  Clicks: 3,500
  CTR: 2.80%
  CPC: $0.71
  Conversions: 85
  CPA: $29.41
  Conv Value: $2,550.00
  ROAS: 1.02x
--------------------------------------------------------------------------------

Aggregate Metrics:
  Total Spend: $7,903.50
  Total Conversions: 270
  Overall CPA: $29.27
  Best Performer: Q1_Conversions_Mobile (ROAS: 1.33x)

AI Analysis:
  • Best performer: Q1_Conversions_Mobile with 1.33x ROAS
  • Mobile conversion campaign driving strong ROI at 1.33x ROAS
  • Retargeting showing highest CTR at 3.33%, indicating engaged audience
  • Overall account ROAS: 1.19x (healthy range)
  • CPA relatively stable across campaigns ($26-$30)

Recommendations:
  • Increase budget allocation to Q1_Conversions_Mobile (best ROAS)
  • Test audience expansion for Retargeting_Website (high CTR signals)
  • Review creative in Brand Awareness campaign (below 1x ROAS)
  • Implement A/B testing on landing pages (potential CPA improvement)
  • Scale winning creatives by 15-20% week-over-week
```

**Output Metrics**:

| Metric | Description |
|--------|-------------|
| **ROAS** | Return on Ad Spend (Revenue / Spend) |
| **CPA** | Cost Per Acquisition (Spend / Conversions) |
| **CPC** | Cost Per Click (Spend / Clicks) |
| **CTR** | Click-Through Rate (Clicks / Impressions) |
| **ROAS** | Return on Ad Spend |

---

### Script 2: `generate_insights.py` - Generate Strategic Insights

**Purpose**: Generate AI-powered insights with industry-specific benchmarks and strategies.

**Command**:

```bash
python scripts/generate_insights.py --metric "roas" --target 1.5 --context "ecommerce"
```

**Parameters**:

- `--metric` (optional): Metric to optimize
  - `roas` - Return on Ad Spend (default)
  - `cpa` - Cost Per Acquisition
  - `ctr` - Click-Through Rate
- `--target` (optional): Target metric value (default: 1.5)
- `--context` (optional): Business context (default: ecommerce)
  - `ecommerce` - E-commerce/retail
  - `saas` - Software as a Service
  - `services` - Service-based business

**Example Commands**:

```bash
# Generate ROAS insights for ecommerce targeting 1.5x
python scripts/generate_insights.py --metric "roas" --target 1.5 --context "ecommerce"

# Generate CPA insights for SaaS targeting $20 CPA
python scripts/generate_insights.py --metric "cpa" --target 20 --context "saas"

# Generate CTR insights for ecommerce
python scripts/generate_insights.py --metric "ctr" --target 2.0 --context "ecommerce"
```

**Expected Output**:

```
Generating AI Insights
Metric: ROAS
Target: 1.5
Context: ECOMMERCE
================================================================================

Benchmarking:
  Current Benchmark: 1.2x
  Industry Average: 1.5x
  Top Performers: 2.0x+
  Your Target: 1.5

Recommended Strategies:
  1. Implement dynamic product ads showing personalized recommendations
  2. Use lookback windows for retargeting (7-30 days based on product type)
  3. A/B test bidding strategies (CPA vs ROAS optimization)
  4. Segment audiences by purchase history and value
  5. Test seasonal messaging and urgency tactics
```

**Supported Benchmarks**:

| Context | Metric | Current | Average | Top Performer |
|---------|--------|---------|---------|---------------|
| **Ecommerce** | ROAS | 1.2x | 1.5x | 2.0x+ |
| **Ecommerce** | CPA | $30 | $20 | $10 |
| **Ecommerce** | CTR | 1.5% | 0.9% | 3.0%+ |
| **SaaS** | ROAS | 1.5x | 2.0x | 3.0x+ |

---

### Script 3: `optimize_suggestions.py` - Optimization Recommendations

**Purpose**: Generate AI-driven optimization suggestions for campaigns.

**Command**:

```bash
python scripts/optimize_suggestions.py --account-id ACT_1234567890 --campaign-name "Q1_Brand"
```

**Parameters**:

- `--account-id` (required): Meta Business Account ID
- `--campaign-name` (optional): Specific campaign to analyze

**Example Commands**:

```bash
# Get general optimization suggestions for account
python scripts/optimize_suggestions.py --account-id ACT_1234567890

# Get suggestions for specific campaign
python scripts/optimize_suggestions.py --account-id ACT_1234567890 --campaign-name "Q1_Brand_Awareness"
```

**Expected Output**:

```
AI Optimization Suggestions
Account: ACT_1234567890
Campaign: Q1_Brand_Awareness
================================================================================

================================ HIGH PRIORITY ACTIONS ================================

[HIGH] Pause underperforming ad sets (CTR < 0.8%)
  Expected Impact: Reduce wasted spend by 5-10%
  Implementation Time: 5 minutes

[HIGH] Increase budget to top-performing ad sets by 15%
  Expected Impact: Improve ROAS by 0.1-0.2x
  Implementation Time: 2 minutes

[MEDIUM] Update targeting to exclude high-cost audiences
  Expected Impact: Reduce CPA by 5-15%
  Implementation Time: 15 minutes

================================= CREATIVE OPTIMIZATIONS ==================================

Test: A/B test 3 new headline variations
  Rationale: Current headlines underperforming vs competitors
  Estimated Lift: 10-20% CTR improvement
  Duration: 7 days

Test: Switch image format from static to carousel
  Rationale: Carousel ads averaging 25% higher engagement
  Estimated Lift: 5-15% CTR improvement
  Duration: 7 days

Test: Test new CTA button text: "Shop Now" vs "Explore"
  Rationale: Different CTAs resonate differently by audience
  Estimated Lift: 3-8% conversion improvement
  Duration: 5 days

========================== BIDDING STRATEGY RECOMMENDATIONS ==========================

Current: CPA Optimization at $30
  Recommendation: Switch to ROAS at 1.5x for next 7 days
  Reason: Account has sufficient conversion data
  Expected: Better scaling and budget utilization

================================================================================
```

**Recommendation Categories**:

1. **HIGH PRIORITY ACTIONS** - Immediate optimizations (quick wins)
2. **CREATIVE OPTIMIZATIONS** - Testing recommendations
3. **BIDDING STRATEGY RECOMMENDATIONS** - Optimization strategy changes
4. **AUDIENCE RECOMMENDATIONS** - Targeting improvements

---

## ⚙️ Configuration

### Environment Variables

Create `.env`:

```env
# Meta Credentials
FACEBOOK_ACCESS_TOKEN=your_access_token
FACEBOOK_BUSINESS_ACCOUNT_ID=ACT_1234567890

# Claude API
ANTHROPIC_API_KEY=your_api_key
CLAUDE_MODEL=claude-3-sonnet-20240229

# Optional
LOG_LEVEL=INFO
```

---

## 🔧 Troubleshooting

### Error: `ANTHROPIC_API_KEY not found`

**Solution**: Add API key to `.env`:

```bash
echo 'ANTHROPIC_API_KEY=your_key' >> .env
```

### Error: `Invalid API key`

**Solution**:
1. Go to [Anthropic Console](https://console.anthropic.com/)
2. Create/regenerate API key
3. Update `.env`

### Error: `Rate limit exceeded`

**Solution**: Claude API has usage limits
- Check [Anthropic Console](https://console.anthropic.com/) for usage
- Implement request caching
- Batch requests when possible

---

## 📚 Links to Official Documentation

- **[Anthropic Claude API](https://docs.anthropic.com/)** - Claude API documentation
- **[Claude Models](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)** - Available models
- **[Prompt Engineering](https://docs.anthropic.com/claude/docs/prompt-engineering)** - Best practices
- **[Facebook Business SDK](https://developers.facebook.com/docs/business-sdk)** - Meta SDK docs
- **[Marketing API](https://developers.facebook.com/docs/marketing-api)** - Meta API reference

---

## 🤝 Related Repositories

- **[meta-campaign-management](https://github.com/gordongeraghty/meta-campaign-management)** - Campaign CRUD
- **[meta-creative-ai-generation](https://github.com/gordongeraghty/meta-creative-ai-generation)** - AI creatives
- **[meta-competitor-intelligence](https://github.com/gordongeraghty/meta-competitor-intelligence)** - Competitor tracking
- **[empire-amplify-ads-automation](https://github.com/gordongeraghty/empire-amplify-ads-automation)** - Master hub

---

## 📝 License

MIT License - See LICENSE file

## 👥 Author

Gordon Geraghty - Head of Performance Media, Empire Amplify
