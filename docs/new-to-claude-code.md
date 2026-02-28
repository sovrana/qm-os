# New to Claude Code?

Quartermaster is built on top of [Claude Code](https://docs.anthropic.com/en/docs/claude-code), Anthropic's command-line AI assistant. If you're already using Claude Code, skip straight to the [Quickstart](quickstart.md).

If you're not, start here.

## What Claude Code actually is

Claude Code is an AI assistant that lives in your terminal. Unlike ChatGPT or the Claude web app, it can read your files, edit them, run commands, and interact with your computer directly. It's not a chat window you copy-paste from. It's a collaborator that works inside your actual environment.

Think of it as a very capable junior employee who sits next to you, can see your screen, and never forgets an instruction (within a single session).

The "within a single session" part is the limitation Quartermaster solves.

## Getting started with Claude Code

Chris Blattman, a professor at UChicago, has written the best beginner's guide to Claude Code I've found. He's not a programmer - everything on his site was built with AI tools - which makes his explanations particularly clear for non-technical users.

**Start here:** [claudeblattman.com](https://claudeblattman.com)

His **Essentials** section covers the fundamentals: which AI tools to use, prompt engineering basics, and how to think about AI assistants. His **Setup** section walks through installation on Mac and Windows.

## When you're ready for more

Once you have Claude Code installed and have run a few conversations, come back here. Quartermaster adds:

- **Persistent memory** across sessions (Claude remembers what you decided yesterday)
- **Automated workflows** that run on session start and end
- **Semantic search** over your entire document vault
- **Self-improving instructions** that get better every time you use the system
- **Published skills** for daily planning, document review, meeting prep, and more

The [Quickstart](quickstart.md) takes about 30 minutes and assumes Claude Code is already installed.

## Do I need to code?

No. The Quickstart involves running a few terminal commands (copy-paste), but everything after that is natural language. You tell Claude what you want. The system handles the rest.

The only technical prerequisite beyond Claude Code itself is Python 3.10+ for semantic search. If you don't want search, you can skip it entirely and still get 90% of the value.
