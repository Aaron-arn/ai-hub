# AIHub

![AIHub banner](assets/banner.png)

![Registry health](https://img.shields.io/github/actions/workflow/status/Aaron-arn/ai-hub/health.yml?label=registry%20health)

Open ecosystem for discovering, installing and managing AI skills, tools, MCP servers and agents.

## Structure

```text
aihub/
├── registry/     # registry.json - index of all available packages
├── skills/       # AI skills: guidance loaded into an agent's context
│   ├── code-management/
│   ├── code-review/
│   └── organization/
├── tools/        # AI tools: executable programs for agents
│   ├── web-search/    # DuckDuckGo search
│   ├── calculator/    # safe arithmetic evaluation
│   └── filesystem/    # sandboxed file access
├── prompts/      # AI prompts: copy-paste prompt templates (not installable)
│   ├── sql-query-optimizer/
│   └── code-reviewer/
├── mcp/          # MCP servers: model-context-protocol servers for assistants
│   ├── sqlite-mcp/    # read-only SQLite queries over stdio
│   └── filesystem-mcp/ # sandboxed file access over stdio
├── agents/       # Agents: instructions + optional bundled tools
│   ├── code-review-agent/
│   └── research-agent/
└── packages/     # Bundles (coming soon)
```

## Packages

Each package contains a `manifest.json` (the AIHub contract) plus its content.

- **Skills** are instructions (`skill.md`) loaded into an agent's context. They require no permissions.
- **Tools** are executable programs (`main.py`) with declared permissions.
- **Prompts** are copy-paste templates (`prompt.md`) shared by the community. They are not installable — copy them with `aihub copy <name>`.
- **MCP servers** are Model Context Protocol servers (`main.py`, stdio transport) that expose tools to assistants: `aihub install sqlite-mcp` then register in your MCP client.
- **Agents** are instruction sets (`agent.md`) that turn an assistant into a specialist, optionally bundling AIHub tools via `aihub:<name>` references (installed automatically).

See `registry/registry.json` for the full index.

## Contributing a prompt

Share a prompt with the community from the CLI:

```bash
pip install aihub-cli
gh auth login        # or: aihub config set github_token <token>
aihub contribute prompt
```

`aihub contribute prompt` asks for the title, description, author, language,
2-4 tags and the prompt text, then forks this repository, pushes a
`prompt/<slug>` branch and opens a pull request. The
[Prompt PR auto-merge](.github/workflows/prompt-pr.yml) workflow validates
the package against the AIHub contract and merges it automatically — no
manual approval needed.

Contributions to tools, skills, MCP servers and agents are not open yet;
they will require a manual review.

## Roadmap

- [x] Define manifest.json contract
- [x] Create registry.json
- [x] Add test packages (3 tools + 3 skills)
- [x] AIHub CLI: search, info, install, uninstall, list, update
- [x] Prompt contributions (CLI -> PRs with automatic validation and merge)
- [x] Website with automatic registry sync
- [x] GitHub Actions validation for PRs
- [x] Download counts (see `docs/COUNTS-API.md`)
- [x] Browser contributions on the website (prompts -> PRs, `GITHUB_TOKEN`-gated)
- [x] MCP servers and agents (manifest contract, CLI install, website filters)
- [x] Registry health check (workflow + badge)
- [ ] Contributions for tools, skills, MCP servers and agents (manual review)

## Related repositories

- [ai-hub-site](https://github.com/Aaron-arn/ai-hub-site) — the catalog website: <https://ai-hub-fr.vercel.app>
- [ai-hub-cli](https://github.com/Aaron-arn/ai-hub-cli) — the `aihub` command line tool

## License

MIT — see [LICENSE](LICENSE).
