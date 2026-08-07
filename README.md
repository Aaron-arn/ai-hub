# AIHub

![AIHub banner](assets/banner.png)

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
├── mcp/          # MCP servers (coming soon)
├── agents/       # Agents (coming soon)
├── packages/     # Bundles (coming soon)
├── cli/          # AIHub CLI (coming soon)
└── website/      # AIHub website (coming soon)
```

## Packages

Each package contains a `manifest.json` (the AIHub contract) plus its content.

- **Skills** are instructions (`skill.md`) loaded into an agent's context. They require no permissions.
- **Tools** are executable programs (`main.py`) with declared permissions.
- **Prompts** are copy-paste templates (`prompt.md`) shared by the community. They are not installable — copy them with `aihub copy <name>`.

See `registry/registry.json` for the full index.

## Contributing a prompt

Open an issue in this repository with the structured format below (the [AIHub website](https://aaron-arn.github.io/ai-hub-site/) "Submit a prompt" form builds it for you). A GitHub Action automatically creates a pull request from it:

```text
## AIHub Prompt Contribution

### Title
Your prompt title

### Description
One sentence about what it does

### Author
Your name

### Language
English

### Tags
coding, testing, thinking

### Prompt
The full prompt text you want to share
```

## Roadmap

- [x] Define manifest.json contract
- [x] Create registry.json
- [x] Add test packages (3 tools + 3 skills)
- [x] AIHub CLI: search, info, install, uninstall, list, update
- [x] Prompt contributions (GitHub issues -> automated PRs)
- [x] Website with automatic registry sync
- [ ] GitHub Actions validation for PRs
- [ ] Download counts (see `docs/COUNTS-API.md`)

## Related repositories

- [ai-hub-site](https://github.com/Aaron-arn/ai-hub-site) — the catalog website: <https://aaron-arn.github.io/ai-hub-site/>
- [ai-hub-cli](https://github.com/Aaron-arn/ai-hub-cli) — the `aihub` command line tool

## License

MIT — see [LICENSE](LICENSE).
