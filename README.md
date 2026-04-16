# Onis Emem

**Product Manager & Engineer · Tallinn, Estonia**
**Building at the agent‑native frontier — [inktrail.ai](https://inktrail.ai) · [printeasy.io](https://printeasy.io) · [techsynergy.io](https://techsynergy.io)**

In a world where anyone can ship code with AI, output stops being scarce. **Taste becomes the scarce thing** — knowing what to ship, when to ship it, what to cut, and what to protect.

I sit at the intersection of product judgment and builder hands because that's where leverage lives now. Three companies. One operator. Agents as force multipliers, not replacements. I lead platform and AI products at [Yolo Group](https://www.yologroup.com/) / [Hub88](https://hub88.io), I founded [TechSynergy](https://techsynergy.io), and I ship [Inktrail](https://inktrail.ai) on the side — the workspace where agents ship.

---

## What I bring

Six things a pure coder or a traditional PM will miss.

1. **Restraint over output.** I know when to revert, when to cut scope, when to ship small. Multi‑product operation at solo scale builds the muscle; AI making output cheap makes the muscle matter more.
2. **Repositioning as a PM discipline.** Moving a brand from commodity ("AI workspace") to owned ("agent‑native workspace") is a sentence that ships before a single feature does. Traditional PMs don't do this work. Coders can't.
3. **Agent‑era product craft.** Building *for* agents, *with* agents, *alongside* agents — while keeping humans in control. Guardrails, cost loops, defence‑in‑depth. This isn't "adding AI to a product." This is shipping products where agents do real work.
4. **Frameworks over features.** Sacred Seven review lens. The artefact pipeline. The monthly report template. A 16‑week PM curriculum. Systems that survive personnel changes and scale past me.
5. **Taste across surfaces.** I can write a PRD engineering wants to build, a marketing brief sales wants to sell, and a commit a reviewer would approve. The gap between those three documents is where most products fail.
6. **Judgment about exposure.** I know what to keep internal and what to publish. This portfolio was scrubbed with that instinct — and if you're reading it, that *is* the signal.

---

## What I'm building now

### [Inktrail](https://inktrail.ai) — the workspace where agents ship
A real‑time collaborative workspace. Five tools replaced (docs · canvas · presentations · transcription · publishing). Repositioned Q2 2026 from "AI workspace" to **agent‑native workspace**: every agent action is diffable, reversible, and leaves a trail.

**Stack.** Elixir/Phoenix on the backend with real‑time channels; React + TypeScript + Vite on the web with a GPU‑rendered canvas; Tauri for desktop. Multi‑provider AI routing, usage‑based billing, cloud‑native storage.

**What shipped recently.**

- **Collaboration** — organisation workspaces with granular sharing, access requests with approval flow, threaded comments on documents and canvases with reactions
- **Content creation** — inline charts generated from plain language or CSV; presentation mode on canvas; a template library for screens and diagrams; bidirectional embedding between documents and canvases
- **Publishing** — Medium‑quality public pages with serif typography, RSS feeds, and public creator profiles; cover images, social share previews, custom domains for knowledge bases
- **Admin & billing** — internal operator tooling with role‑based access; usage metering with real cost reconciliation against the AI gateway; referral programme with ROI analytics
- **Files & platform** — native support for Word, PowerPoint, and Excel attachments across every chat surface; Google Drive connector; desktop app

### [Conductor](https://github.com/oniso20/conductor) — a DAG engine for Claude agents
A Bun + TypeScript CLI orchestrator that runs multi‑stage agent workflows defined in YAML as directed acyclic graphs. Built on the [Claude Agent SDK](https://www.npmjs.com/package/@anthropic-ai/claude-agent-sdk) + [Model Context Protocol](https://modelcontextprotocol.io).

Bounded concurrency, artifact passing between stages, persistent memory with searchable learnings (SQLite + FTS5), git worktree isolation for parallel branches, cost and budget controls, retry logic, MCP server attachment, and a web dashboard. Originally built to orchestrate real multi‑phase feature rollouts — parallel backend and frontend work that would otherwise be serial.

### [PrintEasy](https://printeasy.io) — a creator marketplace for African artists
Pivoting from a B2B print‑on‑demand vendor platform to a B2C creator marketplace.

**Stack.** NestJS + Prisma + PostgreSQL on a cost‑efficient EU provider · Redis‑backed async jobs · Nigeria‑local payments and delivery partners · automated KYC / KYB · cloud‑native storage · self‑hosted observability.

Separately, `merch-enhance` — a Python + FastAPI + Celery service that generates realistic product mockups from a model‑template library, using a multi‑provider AI routing strategy for photo‑reference editing, text‑to‑image generation, and automated design placement.

Primitives built: auto‑review (30‑second instant publish via automated image validation, replaces manual admin queue) · creator and partner payouts with batched transfers · permission‑based RBAC across staff roles · Redbubble‑style ProductGroup → Style → Variant hierarchy ("design once, toggle styles") · transactional email + push notifications · full order‑to‑delivery state machine · safe v1 → v2 data migration with dry‑run mode.

### [TechSynergy](https://techsynergy.io) — career platform for African tech talent
The company I founded in 2023. TechSynergy connects African talent with global opportunities through a mentorship and project marketplace — **$7K MRR in year one**, **1,000+ job placements**, **$50K+ in salaries facilitated** across a 1,000‑member community.

In 2026 we're rebuilding the whole platform on a modern TypeScript stack: a new web app, a consolidated API, and a **dedicated payment service** that runs as its own deployment so mentorship fees, project milestones, and freelancer payouts never compete with core request traffic. PrintEasy (above) sits under the same umbrella as our commerce product.

Operational tooling we run in‑house: a self‑hosted help centre with content in Git and a TipTap‑based CMS that uses GitHub as the database, so content edits happen as PRs — no GitBook fees, no vendor lock‑in.

---

## How I build

- **Ship small, iterate hot.** Three active companies — PM at Yolo Group by day, TechSynergy and Inktrail by night — force ruthless scope discipline. I favour one bundled PR over churn, revert publicly when I'm wrong (Inktrail has a 9‑commit wireframe revert to prove it), and capture the *why* in memory rather than comments.
- **Agents, not assistants.** I build systems where agents do real work with guardrails: strict server‑side validation that round‑trips errors back to the model so it self‑corrects in 1–2 turns, clear separation between prototyping and polished output surfaces enforced from schema to prompts, and cost reconciliation loops on every LLM call.
- **Real‑time internals are a first‑class skill.** Collaborative editors that don't lose work under concurrent edits; canvases that stay in sync when the network blinks; agents that co‑edit alongside humans without trashing each other's state. I've shipped all three in production and know where the sharp edges are.
- **Code taste before dependency.** Design tokens before dependencies. Mobile‑first by default. The smaller primitive over the heavier library when it means less maintenance debt.

---

## How I do product

- **Problem first, numbers second, scope third.** Every PRD opens with the diagnosis before the prescription — what's failing, by how much, and why now. If the data isn't there, the spec isn't ready.
- **Positioning before building.** Who it's for, who it's *not* for, what success looks like — written before a single feature gets scoped. Repositioning work starts with the sentence that replaces the tagline, not the components that replace the screens.
- **Phased shipping with rationale.** Phase 1 → Phase 1.5 → Phase 2 isn't arbitrary; the order comes from where leverage compounds fastest. I can defend every sequence decision against "can't we just do it all now."
- **A pipeline, not a pile of docs.** Strategy → PRD → user story map → design brief → launch brief → release‑day retro → monthly report. Each artefact is written for a different audience and pulls only what's needed from the one before it. Nothing is written twice.
- **Release day is a data event.** Every release ships with a feedback capture and an issue log. Retros happen within days, not weeks, and feed the next monthly report. Metrics are always diffed against the previous period.
- **I teach what I build.** A 16‑week product management curriculum. A custom PM productivity toolkit built on the Claude Agent SDK — seven skills that run from the command line, dogfooded on my own product work.

---

## Stack I reach for

**Frontend**
Next.js 16 · React 19 · TypeScript (strict) · Tailwind 4 · shadcn/ui · HugeIcons

**Canvas & editor**
TipTap · PixiJS · Excalidraw · ELK · ECharts

**Backend**
NestJS + Prisma · Elixir / Phoenix · Node.js · Python / FastAPI

**AI**
Claude Agent SDK · Model Context Protocol (MCP) · multi‑model routing via a single LLM gateway · computer‑vision pipelines for image validation

**Data**
PostgreSQL · MongoDB · libSQL · Redis with job queues · modern ORMs (Prisma, Drizzle)

**Infra & observability**
Fly.io · Vercel · Cloudflare Workers · EU bare‑metal · cloud‑native object storage · PostHog · self‑hosted Grafana + Prometheus + Tempo + Loki

**Payments & auth**
Clerk · Stripe · regional payment gateways · Google OAuth · JWT

---

## Impact at work

**Yolo Group / Hub88** (Product Manager, 2023–present)

- Grew partner integrations completed in 2 weeks by **80%** by replacing Google‑Doc onboarding with self‑service one‑click onboarding
- Expanded active onboarding pipeline by **25%** and scaled production‑ready integrations by **140%** in one quarter
- Drove **991% growth** in unique product requests by centralising fragmented docs into a searchable catalogue embedded in sales workflows
- Launched Hub AI — **100+ users and 350+ sessions in six weeks**, **+20%** response quality via Langfuse + LLM‑as‑judge evals
- **60% supplier adoption** and **70% operator opt‑in** for the promotions marketplace in month one

**TechSynergy** (founder, 2023–present) — $7K MRR in year one · 1,000+ talent placements · $50K+ in salaries facilitated across a 1,000‑member community.

**Laferla Insurance Group** (developer + PM, 2022–present) — full‑stack rebuild cut insurance quote turnaround from 3–7 days to instant; automated KYB from 3–7 days to 24 hours; **+50% NPS**; **−40% internal workload** via BFF + Azure SSO.

**Before that** · 100Devs (Boston) · Dado Food (Enugu) real‑time delivery tracking on Node · co‑authored a peer‑reviewed ACS paper at ITMO × University of Southern Denmark modelling 2.3–7.8M tons of West African solar PV e‑waste — the first quantitative baseline for regional policy.

---

## Elsewhere

- **Long‑form** · [onis-emem.notion.site](https://onis-emem.notion.site/hello)
- **LinkedIn** · [/in/onis-emem](https://www.linkedin.com/in/onis-emem/)
- **Email** · onis.c.emem@gmail.com

<sub>Open to conversations about agent‑native platform product, DevEx, internal developer platforms, and applied AI.</sub>
