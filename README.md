# Meta Ads MCP for Claude

> **Empire Amplify** - Planned Model Context Protocol (MCP) server for Claude AI to interact with Meta Ads.

## Status

> **This repository is a scaffold/template.** The MCP server (`mcp_server.py`) has not been built yet. The existing scripts output hardcoded sample data to demonstrate what the tool structure would look like. No actual Meta API calls or AI analysis is performed.

### What exists:
- `scripts/analyze_campaigns.py` - Prints hardcoded sample campaign data
- `scripts/generate_insights.py` - Returns pre-written strategy templates
- `scripts/optimize_suggestions.py` - Outputs generic optimization tips

### What does NOT exist yet:
- `mcp_server.py` - The actual MCP server implementation
- Any real Meta API integration
- Any real AI/Claude integration
- OAuth2 authentication
- Audit logging

## Overview

When implemented, this MCP server would enable Claude to:
- **Analyse Campaigns** - Get AI-powered insights from real Meta data
- **Generate Recommendations** - Data-driven optimisation suggestions
- **Create Reports** - Natural language reporting
- **Automate Tasks** - AI-driven campaign management

## What is MCP?

Model Context Protocol (MCP) allows AI assistants like Claude to securely interact with external tools and APIs. This server would provide Claude with access to your Meta Ads data.

## Planned Tools

| Tool | Description | Status |
|------|-------------|--------|
| `list_campaigns` | Get all campaigns with metrics | Not built |
| `analyze_performance` | AI analysis of campaign performance | Not built |
| `get_recommendations` | Optimisation suggestions | Not built |
| `generate_report` | Create performance report | Not built |

## Example Prompts (Once Implemented)

Ask Claude:
- "Analyse my Meta Ads campaigns and identify underperformers"
- "What campaigns should I increase budget on?"
- "Generate a weekly performance report"
- "Which ad sets have the highest CPA?"

## Related Projects

- [pipeboard-co/meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) - Reference MCP implementation for Meta Ads

## License

MIT License - Empire Amplify 2025
