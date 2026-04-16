# Onis Emem

**Product Manager & Engineer · Tallinn, Estonia**
**Building at the agent‑native frontier — [inktrail.ai](https://inktrail.ai) · [printeasy.io](https://printeasy.io) · [techsynergy.io](https://techsynergy.io)**

I lead platform and AI products at [Yolo Group](https://www.yologroup.com/) ([Hub88](https://hub88.io), the B2B iGaming aggregator), founded [TechSynergy](https://techsynergy.io), and ship [Inktrail](https://inktrail.ai) on the side — a real‑time collaborative workspace where agents ship.

Ten years in, I still merge code every week. The gap between *shipping with agents* and *managing shipping with agents* is closing fast, and the PMs who understand the build are the PMs who win the next decade. I'm betting my career on that.

---

## What I'm building now

### [Inktrail](https://inktrail.ai) — the workspace where agents ship
A real‑time collaborative workspace. Five tools replaced (docs · canvas · presentations · transcription · publishing). Repositioned Q2 2026 from "AI workspace" to **agent‑native workspace**: every agent action is diffable, reversible, and leaves a trail.

**Stack.** Elixir/Phoenix + MongoDB for real‑time collab (Phoenix channels + prosemirror‑collab + WAL canvas ops) · React + TypeScript + Vite + PixiJS (GPU‑rendered canvas with a validation pipeline of 50 tests + WCAG AA contrast) · Tauri desktop · Clerk · Stripe · OpenRouter · Cloudflare R2 · Fly.io. Private repos live under [`inktrail-ai/*`](https://github.com/inktrail-ai).

**What shipped recently.**

- **Collaboration** — a sharing model with organisation workspaces, access requests, and role attribution ("via project / via org / via file share"); threaded comments on documents and canvases with reactions
- **Content creation** — inline charts (6 types, CSV import, AI‑generated from plain language); presentation mode on canvas; a 178‑template library for screens and diagrams; bidirectional embedding between documents and canvases
- **Publishing** — Medium‑quality public pages with serif typography, RSS feeds, and public profiles at `/u/:username`; cover images, social share previews, custom domains for knowledge bases
- **Admin & billing** — standalone [admin.inktrail.ai](https://admin.inktrail.ai) with Google OAuth and role‑based access; credit metering with real cost reconciliation against OpenRouter; referral system with ROI analytics
- **Files & platform** — native support for Word, PowerPoint, and Excel attachments across every chat surface; Google Drive connector; desktop app via Tauri

### [PrintEasy](https://printeasy.io) — a creator marketplace for African artists
Pivoting from a B2B print‑on‑demand vendor platform to a B2C creator marketplace (the "Redbubble of Africa"). Full backend rewrite in April 2026 — 58k+ lines across ~280 files, **230+ API endpoints**, 210 tests, zero TypeScript errors.

**Stack.** NestJS + Prisma + PostgreSQL + BullMQ + Redis on Hetzner · Paystack payments with HMAC‑SHA‑512 webhook verification · KWIK delivery · Dojah BVN/CAC KYC · Cloudflare R2 · self‑hosted Grafana + Prometheus + Tempo + Loki for observability.

Separately, `merch-enhance` — a Python + FastAPI + Celery service that generates realistic product mockups using a model‑template library, Gemini Flash (photo‑ref editing), Imagen Fast (text‑to‑image), OpenAI fallback, and Claude for zone detection.

Primitives built: auto‑review (30‑second instant publish via sharp image validation, replaces manual admin queue) · partner payouts with batched Paystack Transfers · permission‑based RBAC (SUPPORT/FINANCE/CONTENT) · Redbubble‑style ProductGroup → Style → Variant hierarchy ("design once, toggle styles") · 12 SendGrid email templates · FCM push · full order‑to‑delivery state machine · v1→v2 ETL with dry‑run.

### [conductor](https://github.com/inktrail-ai/conductor) — a DAG engine for Claude agents *(private)*
A Bun + TypeScript CLI orchestrator that runs multi‑stage agent workflows defined in YAML as DAGs, built on the Claude Agent SDK + MCP. Bounded concurrency · artifact passing via template interpolation · persistent memory (an LLM extracts learnings categorised as decision/pattern/gotcha/fact/error, stored in SQLite FTS5) · git worktree isolation · cost/budget controls · retry logic. 16 example workflows power real Inktrail feature rollouts (`sharing-phase-a.yaml` → `-d.yaml`, `publishing-sprint-1/2/3.yaml`, `comments-redesign.yaml`).

### [TechSynergy](https://techsynergy.io) — career platform for African tech talent
The company I founded in 2023. TechSynergy connects African talent with global opportunities through a mentorship and project marketplace — **$7K MRR in year one**, **1,000+ job placements**, **$50K+ in salaries facilitated** across a 1,000‑member community.

In 2026 we're rebuilding the whole platform on a modern TypeScript stack: a new web app, a consolidated API, and a **dedicated payment service** that runs as its own deployment so mentorship fees, project milestones, and freelancer payouts never compete with core request traffic. PrintEasy (above) sits under the same umbrella as our commerce product.

Operational tooling we run in‑house:
- Self‑hosted help centre — 53 articles across 9 categories, content in Git, a TipTap‑based CMS using GitHub as the database so edits happen as PRs. Public code: [`techsynergy-help-admin`](https://github.com/techsynergy-io/techsynergy-help-admin) · [`techsynergy-help-center`](https://github.com/techsynergy-io/techsynergy-help-center)
- Shared observability stack (Grafana + Prometheus + Tempo + Loki) across all TechSynergy products

---

## How I work

- **Ship small, iterate hot.** Three active companies — PM at Yolo Group by day, TechSynergy and Inktrail by night — force ruthless scope discipline. I favour one bundled PR over churn, revert publicly when I'm wrong (Inktrail has a 9‑commit wireframe revert to prove it), and capture the *why* in memory rather than comments.
- **Agents, not assistants.** I build systems where agents do real work with guardrails: strict server‑side validators that round‑trip errors back to the model so it self‑corrects in 1–2 turns, hard surface splits (`/canvas` prototyping vs `/design` polished) enforced at four layers (schema · dispatch · prompt · tests), skill registries with `applicable?` callbacks, and cost reconciliation loops on every LLM call.
- **Real‑time internals are a first‑class skill.** Collaborative editors that don't lose your work under concurrent edits; canvases that stay in sync when the network blinks; agents that can co‑edit alongside humans without trashing each other's state. I've shipped all three in production and know where the sharp edges are.
- **Code taste before dependency.** shadcn/ui + CSS variables + HugeIcons religiously. Mobile‑first by default. Design‑token before dependency. Pure‑Elixir `:zip.unzip` + regex over Office Open XML when a library would add maintenance debt.

---

## Stack I reach for

**Frontend**
Next.js 16 · React 19 · TypeScript (strict) · Tailwind 4 · shadcn/ui · HugeIcons

**Canvas & editor**
TipTap · PixiJS · Excalidraw · ELK · ECharts

**Backend**
NestJS + Prisma · Elixir / Phoenix · Node.js · Python / FastAPI

**AI**
Claude Agent SDK · Model Context Protocol (MCP) · OpenRouter as a single gateway for Claude, GPT‑5, Gemini, DeepSeek and Nemotron · rembg · sharp

**Data**
PostgreSQL · MongoDB · Turso / libSQL · Redis + BullMQ · Prisma · Drizzle

**Infra & observability**
Fly.io · Vercel · Cloudflare Workers · Hetzner · Cloudflare R2 · PostHog · Grafana + Prometheus + Tempo + Loki

**Payments & auth**
Clerk · Stripe · Paystack · Google OAuth · JWT (jose + HMAC session)

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
