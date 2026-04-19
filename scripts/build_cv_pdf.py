"""Build a PDF version of the Alignerr CV with reportlab."""
from pathlib import Path
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable,
    ListFlowable,
    ListItem,
    KeepTogether,
)

OUT = Path(__file__).resolve().parent.parent / "cv-alignerr-ai-code-ranking.pdf"

NAVY = HexColor("#0B2B4E")
GREY = HexColor("#444B54")
LIGHT = HexColor("#6C757D")

styles = getSampleStyleSheet()

name_style = ParagraphStyle(
    "Name", parent=styles["Normal"],
    fontName="Helvetica-Bold", fontSize=22, leading=26,
    alignment=TA_CENTER, textColor=NAVY, spaceAfter=2,
)
sub_style = ParagraphStyle(
    "Sub", parent=styles["Normal"],
    fontName="Helvetica", fontSize=11, leading=14,
    alignment=TA_CENTER, textColor=GREY, spaceAfter=2,
)
contact_style = ParagraphStyle(
    "Contact", parent=styles["Normal"],
    fontName="Helvetica", fontSize=9.5, leading=12,
    alignment=TA_CENTER, textColor=GREY, spaceAfter=1,
)
heading_style = ParagraphStyle(
    "Heading", parent=styles["Normal"],
    fontName="Helvetica-Bold", fontSize=11.5, leading=14,
    textColor=NAVY, spaceBefore=10, spaceAfter=2,
)
body_style = ParagraphStyle(
    "Body", parent=styles["Normal"],
    fontName="Helvetica", fontSize=9.5, leading=12.5,
    textColor=HexColor("#1C1F23"), spaceAfter=3,
)
bullet_style = ParagraphStyle(
    "Bullet", parent=body_style,
    leftIndent=10, bulletIndent=0, spaceAfter=1.5,
)
role_title_style = ParagraphStyle(
    "RoleTitle", parent=styles["Normal"],
    fontName="Helvetica-Bold", fontSize=10.5, leading=12.5,
    textColor=HexColor("#111418"), spaceBefore=5, spaceAfter=0,
)
role_meta_style = ParagraphStyle(
    "RoleMeta", parent=styles["Normal"],
    fontName="Helvetica-Oblique", fontSize=9, leading=11,
    textColor=LIGHT, spaceAfter=2,
)

story = []


def h(text):
    story.append(Paragraph(text.upper(), heading_style))
    story.append(HRFlowable(width="100%", thickness=0.6, color=NAVY, spaceBefore=0, spaceAfter=3))


def p(text, style=body_style):
    story.append(Paragraph(text, style))


def bullets(items):
    flowables = [Paragraph(t, bullet_style) for t in items]
    story.append(
        ListFlowable(
            [ListItem(f, leftIndent=12, bulletColor=NAVY) for f in flowables],
            bulletType="bullet", start="•", bulletFontSize=8, leftIndent=10,
        )
    )
    story.append(Spacer(1, 2))


def role(title, org, dates):
    story.append(Paragraph(f"{title} &nbsp;—&nbsp; <font color='#444B54'>{org}</font>", role_title_style))
    story.append(Paragraph(dates, role_meta_style))


# -------- Header --------
story.append(Paragraph("ONIS EMEM", name_style))
story.append(Paragraph("Senior Software Engineer &nbsp;|&nbsp; AI Code Evaluation &amp; Productization", sub_style))
story.append(Paragraph("Tallinn, Estonia &nbsp;·&nbsp; onis.c.emem@gmail.com &nbsp;·&nbsp; +372 589 87 957", contact_style))
story.append(Paragraph(
    '<link href="https://linkedin.com/in/onis-emem/" color="#0B2B4E">linkedin.com/in/onis-emem</link> '
    '&nbsp;·&nbsp; '
    '<link href="https://onis-emem.com" color="#0B2B4E">onis-emem.com</link> '
    '&nbsp;·&nbsp; '
    '<link href="https://github.com/oniso20" color="#0B2B4E">github.com/oniso20</link>',
    contact_style,
))
story.append(Spacer(1, 6))

# -------- Summary --------
h("Summary")
p(
    "Senior engineer with 7+ years shipping production code across full-stack web, payments, "
    "and AI systems, now operating as a PM who still writes and reviews code daily. Deep "
    "experience with LLM evaluation in production — built eval-gated AI features using Langfuse "
    "and LLM-as-judge, defined response-quality rubrics, and closed feedback loops that cut "
    "hallucinations. Fluent in JavaScript/TypeScript, Python, and Node.js; comfortable reading "
    "and reviewing Java, Go, and C-family code. Known for small PRs, sharp code review, and "
    "articulating exactly what makes one solution better than another."
)

# -------- Relevant Strengths --------
h("Relevant Strengths for AI Code Ranking")
bullets([
    "<b>Code review at scale:</b> Review PRs across Next.js, Node, and Python stacks for "
    "Inktrail, TechSynergy, and Laferla. Consistently catch logic errors, missing edge cases, "
    "security issues (auth, injection, secret handling), and readability regressions before merge.",
    "<b>LLM output evaluation:</b> Shipped Langfuse + LLM-as-judge on Hub AI; wrote rubrics "
    "for correctness, factuality, and tone; +20% response quality in production. Round-trip "
    "server-side validation errors back to the model so it self-corrects in 1–2 turns.",
    "<b>Multi-language fluency:</b> JavaScript/TypeScript, Python, Node.js daily. Java/C++ "
    "from academic work and competitive problem solving; Go and Rust read-fluent for review.",
    "<b>Algorithms &amp; complexity:</b> M.Sc. Industrial Ecology with ML modelling "
    "(supervised learning on PV waste forecasting, ACS-published). Built real-time tracking, "
    "funnel analytics, and cost-reconciliation pipelines from scratch.",
    "<b>RLHF &amp; preference data awareness:</b> Productized LLM features that depend on "
    "preference signals; designed feedback capture and evaluation loops that inform model- "
    "and prompt-level improvements.",
])

# -------- Core Skills --------
h("Core Skills")
bullets([
    "<b>Languages:</b> JavaScript, TypeScript, Python, Node.js, SQL &nbsp;·&nbsp; Reading: Java, Go, C++, Rust",
    "<b>AI / ML:</b> LLM evaluation (RAG, LLM-as-judge), prompt engineering, Langfuse, eval-gated release, cost reconciliation, RLHF concepts",
    "<b>Engineering:</b> React, Next.js, Express, REST/GraphQL API design, BFF patterns, Azure/AWS, Git, CI/CD, testing &amp; TDD, performance profiling",
    "<b>Quality:</b> Code review, design patterns, refactoring, security (OWASP, secret hygiene, input validation), observability",
    "<b>Domains:</b> Payments (Wise), insurance, iGaming integrations, KYC/KYB, marketplaces",
])

# -------- Experience --------
h("Experience")

role("Senior Product Manager (with hands-on AI/eng ownership)",
     "Hub88 / Yolo Group · Tallinn", "2023 – Present")
p("Own HubConnect (B2B integration platform) and Hub AI (internal LLM assistant). Still in "
  "the codebase — review PRs, write specs at code level, pair on integration and evaluation logic.")
bullets([
    "<b>Hub AI — eval-gated LLM productization.</b> Built evaluation harness with Langfuse "
    "+ LLM-as-judge before widening access. Defined response-quality rubric (correctness, "
    "groundedness, tone), shipped fast feedback loops, <b>improved response quality by 20%</b> "
    "and reduced hallucinations in production. 100+ users, 350+ sessions in six weeks.",
    "<b>HubConnect — engineering reviewer for integration code.</b> Review API contracts, "
    "schema migrations, and integration code between suppliers and operators. Catch edge "
    "cases, auth and replay issues, and idempotency bugs before rollout.",
    "<b>1-Click Onboarding — workflow replatforming.</b> Replaced manual onboarding with "
    "a self-service flow; <b>+80%</b> partners integrating within two weeks, <b>+140%</b> "
    "production-ready integrations the following quarter.",
    "<b>Promotions marketplace.</b> Shipped two-sided marketplace — <b>60%</b> supplier "
    "adoption, <b>70%</b> operator opt-in in month one.",
])

role("Product Manager &amp; Engineer",
     "Laferla Insurance Group · Tallinn", "2022 – Present")
p("Rebuilt a 40-year-old insurer's customer platform on Next.js + Node with a BFF to the "
  "internal CRM. Hands-on engineering lead on quoting, KYC/KYB, and admin tooling.")
bullets([
    "Rewrote quote engine: <b>3–7 days → instant</b> turnaround while preserving underwriting rules.",
    "KYC automation: <b>days → 1–2 minutes</b> (SumSub integration, re-engineered review).",
    "KYB: <b>3–7 days → 24 hours</b>.",
    "Admin BFF + Azure SSO: <b>−40% internal workload, +50% NPS</b>.",
    "Owned code review, release process, and on-call for the platform.",
])

role("Software Developer &amp; Scrum Master", "100Devs · Boston (Remote)", "2021 – 2022")
p("Shipped full-stack React/Node.js apps for multiple clients. Translated ambiguous goals "
  "into MVPs; <b>−30% time-to-market</b> via tight feedback loops and code-review-led development.")

role("Payment Operations Specialist", "Wise (TransferWise) · Tallinn", "2021 – 2022")
p("Analysed large transaction datasets (SQL/Python) to find refund-logic bottlenecks; "
  "partnered with Treasury, Compliance, and Product engineers to implement fixes. "
  "<b>+32% workflow throughput</b>.")

role("Software Developer &amp; Scrum Master", "Dado Food · Enugu, Nigeria (Remote)", "2019 – 2021")
p("Built real-time order tracking on Node.js — <b>−15% support inquiries</b>. Frontend "
  "and asset optimisation: <b>+30% app performance</b>.")

role("Python Data Scientist / ML Researcher",
     "ITMO University × University of Southern Denmark",
     "2018 – 2025 (fractional post-grad)")
p("Co-authored ACS-published research using supervised ML to forecast solar PV waste across "
  "15 West African countries. Python, scikit-learn, time-series modelling, uncertainty "
  "quantification. Publication: <i>Environmental Science &amp; Technology, 2025</i>.")

# -------- Side Projects --------
h("Side Projects &amp; Open Source")
bullets([
    "<b>Inktrail (inktrail.ai) —</b> Collaborative workspace (docs, canvas, publishing) "
    "experimenting with AI + human co-editing. Real-time sync, per-call cost reconciliation, "
    "eval-gated AI features, server-side validation round-tripped back to the model for "
    "self-correction. Solo-built.",
    "<b>oniso20/conductor —</b> Open-source CLI for running multi-stage Claude agent workflows.",
    "<b>TechSynergy (Co-founder, CPO) —</b> Africa-first hiring &amp; payments platform. "
    "AI-assisted talent matching, multi-currency wallets. <b>€7K MRR, €100K+ revenue, "
    "50+ projects shipped, 900+ talent community.</b>",
])

# -------- Education --------
h("Education")
bullets([
    "Vocational Diploma, ICT — Helsinki Business College, 2022–2023",
    "M.Sc. Exchange, Life Cycle Engineering — University of Southern Denmark, 2019–2020",
    "M.Sc. Industrial Ecology — ITMO University, 2018–2020",
    "B.Tech. Environmental Engineering — Rivers State University, 2004–2010",
])

# -------- Certifications --------
h("Certifications")
bullets([
    "Software Architecture — Global Dev Experts, 2024",
    "Agile Project &amp; Delivery Management — ICAgile, 2023",
    "Power BI Data Analyst Associate — Microsoft, 2021",
])

doc = SimpleDocTemplate(
    str(OUT), pagesize=LETTER,
    leftMargin=0.65 * inch, rightMargin=0.65 * inch,
    topMargin=0.55 * inch, bottomMargin=0.55 * inch,
    title="Onis Emem — Senior Software Engineer — AI Code Ranking",
    author="Onis Emem",
)
doc.build(story)
print(f"Wrote {OUT}")
