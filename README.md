# Meta Ads MCP for Claude

> **Empire Amplify** - Model Context Protocol (MCP) server for Claude AI to interact with Meta Ads.

## Overview

This MCP server enables Claude to:
- **Analyze Campaigns** - Get AI-powered insights
- **Generate Recommendations** - Optimization suggestions
- **Create Reports** - Natural language reporting
- **Automate Tasks** - AI-driven campaign management

## What is MCP?

Model Context Protocol (MCP) allows AI assistants like Claude to securely interact with external tools and APIs. This server provides Claude with access to your Meta Ads data.

## Quick Start

### 1. Install

```bash
git clone https://github.com/gordongeraghty/meta-ads-mcp-claude.git
cd meta-ads-mcp-claude
pip install -r requirements.txt
```

### 2. Configure

```bash
cp .env.example .env
# Add your Meta API credentials
```

### 3. Run MCP Server

```bash
python mcp_server.py
```

### 4. Connect to Claude

Add to your Claude Desktop config:
```json
{
  "mcpServers": {
    "meta-ads": {
      "command": "python",
      "args": ["path/to/mcp_server.py"]
    }
  }
}
```

## Available Tools

| Tool | Description |
|------|-------------|
| `list_campaigns` | Get all campaigns with metrics |
| `analyze_performance` | AI analysis of campaign performance |
| `get_recommendations` | Optimization suggestions |
| `generate_report` | Create performance report |

## Example Prompts

Ask Claude:
- "Analyze my Meta Ads campaigns and identify underperformers"
- "What campaigns should I increase budget on?"
- "Generate a weekly performance report"
- "Which ad sets have the highest CPA?"

## Scripts

| Script | Description |
|--------|-------------|
| `mcp_server.py` | Main MCP server |
| `analyze_campaigns.py` | Campaign analysis tools |
| `generate_insights.py` | AI insight generation |
| `optimize_suggestions.py` | Optimization recommendations |

## Security

- Uses OAuth2 for Meta API authentication
- Credentials stored in environment variables
- Read-only access by default
- Audit logging enabled

## Related Projects

- [pipeboard-co/meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) - Reference implementation
- [meta-ads-automation](../meta-ads-automation) - Python scripts

## License

MIT License - Empire Amplify 2025
