# Onis Emem

**Product Manager & Engineer · Tallinn, Estonia**
**Building at the agent‑native frontier — [inktrail.ai](https://inktrail.ai) · [printeasy.io](https://printeasy.io) · [techsynergy.io](https://techsynergy.io)**

I lead platform and AI products at [Yolo Group](https://www.yologroup.com/) ([Hub88](https://hub88.io), the B2B iGaming aggregator), founded [TechSynergy](https://techsynergy.io), and ship [Inktrail](https://inktrail.ai) on the side — a real‑time collaborative workspace where agents ship.

Ten years in, I still merge code every week. The gap between *shipping with agents* and *managing shipping with agents* is closing fast, and the PMs who understand the build are the PMs who win the next decade. I'm betting my career on that.

---

## What I'm building now

### [Inktrail](https://inktrail.ai) — the workspace where agents ship
A real‑time collaborative workspace. Five tools replaced (docs · canvas · presentations · transcription · publishing). Repositioned Q2 2026 from "AI workspace" to **agent‑native workspace**: every agent action is diffable, reversible, and leaves a trail.

**Stack.** Elixir/Phoenix on the backend with real‑time channels; React + TypeScript + Vite on the web with a GPU‑rendered canvas; Tauri for desktop. Multi‑provider AI routing, usage‑based billing, cloud‑native storage.

**What shipped recently.**

- **Collaboration** — organisation workspaces with granular sharing, access requests with approval flow, threaded comments on documents and canvases with reactions
- **Content creation** — inline charts (6 types, CSV import, AI‑generated from plain language); presentation mode on canvas; a 178‑template library for screens and diagrams; bidirectional embedding between documents and canvases
- **Publishing** — Medium‑quality public pages with serif typography, RSS feeds, and public creator profiles; cover images, social share previews, custom domains for knowledge bases
- **Admin & billing** — internal operator tooling with role‑based access; usage metering with real cost reconciliation against the AI gateway; referral programme with ROI analytics
- **Files & platform** — native support for Word, PowerPoint, and Excel attachments across every chat surface; Google Drive connector; desktop app

### [PrintEasy](https://printeasy.io) — a creator marketplace for African artists
Pivoting from a B2B print‑on‑demand vendor platform to a B2C creator marketplace (the "Redbubble of Africa"). Full backend rewrite in April 2026 — 58k+ lines across ~280 files, **230+ API endpoints**, 210 tests, zero TypeScript errors.

**Stack.** NestJS + Prisma + PostgreSQL on a cost‑efficient EU provider · Redis‑backed async jobs · Nigeria‑local payments and delivery partners · automated KYC / KYB · cloud‑native storage · self‑hosted observability.

Separately, `merch-enhance` — a Python + FastAPI + Celery service that generates realistic product mockups from a model‑template library, using a multi‑provider AI routing strategy for photo‑reference editing, text‑to‑image generation, and automated design placement.

Primitives built: auto‑review (30‑second instant publish via automated image validation, replaces manual admin queue) · creator and partner payouts with batched transfers · permission‑based RBAC across staff roles · Redbubble‑style ProductGroup → Style → Variant hierarchy ("design once, toggle styles") · transactional email + push notifications · full order‑to‑delivery state machine · safe v1 → v2 data migration with dry‑run mode.

### conductor — a DAG engine for Claude agents *(private)*
A Bun + TypeScript CLI orchestrator that runs multi‑stage agent workflows defined in YAML as directed acyclic graphs, built on the Claude Agent SDK + MCP. Bounded concurrency, artifact passing between stages, persistent memory with searchable learnings, isolated execution per phase, cost and budget controls, retry logic. Used to orchestrate real multi‑phase feature rollouts — parallel backend and frontend work that would otherwise be serial.

### [TechSynergy](https://techsynergy.io) — career platform for African tech talent
The company I founded in 2023. TechSynergy connects African talent with global opportunities through a mentorship and project marketplace — **$7K MRR in year one**, **1,000+ job placements**, **$50K+ in salaries facilitated** across a 1,000‑member community.

In 2026 we're rebuilding the whole platform on a modern TypeScript stack: a new web app, a consolidated API, and a **dedicated payment service** that runs as its own deployment so mentorship fees, project milestones, and freelancer payouts never compete with core request traffic. PrintEasy (above) sits under the same umbrella as our commerce product.

Operational tooling we run in‑house:
- Self‑hosted help centre — 53 articles across 9 categories, content in Git, a TipTap‑based CMS using GitHub as the database so edits happen as PRs. Public code: [`techsynergy-help-admin`](https://github.com/techsynergy-io/techsynergy-help-admin) · [`techsynergy-help-center`](https://github.com/techsynergy-io/techsynergy-help-center)
- Shared observability stack (Grafana + Prometheus + Tempo + Loki) across all TechSynergy products

---

## How I work

- **Ship small, iterate hot.** Three active companies — PM at Yolo Group by day, TechSynergy and Inktrail by night — force ruthless scope discipline. I favour one bundled PR over churn, revert publicly when I'm wrong (Inktrail has a 9‑commit wireframe revert to prove it), and capture the *why* in memory rather than comments.
- **Agents, not assistants.** I build systems where agents do real work with guardrails: strict server‑side validation that round‑trips errors back to the model so it self‑corrects in 1–2 turns, clear separation between prototyping and polished output surfaces enforced from schema to prompts, and cost reconciliation loops on every LLM call.
- **Real‑time internals are a first‑class skill.** Collaborative editors that don't lose work under concurrent edits; canvases that stay in sync when the network blinks; agents that co‑edit alongside humans without trashing each other's state. I've shipped all three in production and know where the sharp edges are.
- **Code taste before dependency.** Design tokens before dependencies. Mobile‑first by default. The smaller primitive over the heavier library when it means less maintenance debt.

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
