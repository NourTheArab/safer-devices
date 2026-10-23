"""Build a local-only, self-contained reading preview from repository content."""

import re
import shutil
from html import escape
from pathlib import Path
from urllib.parse import unquote, urlsplit, urlunsplit

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / ".private" / "preview"
MARKDOWN = MarkdownIt("commonmark", {"html": True}).enable("table")
ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>'
CHEVRON = '<svg class="chevron" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5"><path d="m6 9 6 6 6-6"/></svg>'
MARK = '<svg viewBox="0 0 42 46" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M5 41V21a16 16 0 0 1 32 0v20M12 41V22a9 9 0 0 1 18 0v19M21 13v28M5 30h32M2 41h38"/></svg>'
PAIRS = {"README.md": "README.ar.md", **{f"guides/{name}.md": f"ar/{name}.md" for name in ("accounts", "browsers", "mac", "windows", "phones", "developers", "getting-help", "why-this-matters")}, "prompts/AGENT-AUDIT.md": "ar/agent-audit.md", "prompts/APPROVE-ONE-CHANGE.md": "ar/approve-one-change.md", "sources/README.md": "ar/sources.md"}
TWINS = {**PAIRS, **{value: key for key, value in PAIRS.items()}}


def route(name):
    return {"README.md": "index.html", "README.ar.md": "ar.html", "LICENSE": "license.html"}.get(name, str(Path(name).with_suffix(".html")))


def href(name):
    return "/" + route(name)


def is_arabic(name):
    return name == "README.ar.md" or name.startswith("ar/")


def render_markdown(path):
    source = path.read_text(encoding="utf-8")
    source = re.sub(r"\A---\n(?=[A-Za-z][\w-]*:).*?\n---\n", "", source, count=1, flags=re.S)
    tokens = MARKDOWN.parse(source)
    headings = iter(heading_ids_in_order(source))
    for token in tokens:
        if token.type == "heading_open":
            token.attrSet("id", next(headings))
        for child in token.children or []:
            attribute = "href" if child.type == "link_open" else "src" if child.type == "image" else None
            if attribute is None:
                continue
            parsed = urlsplit(child.attrGet(attribute))
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(ROOT):
                raise ValueError("Preview link outside repository")
            name = str(target.relative_to(ROOT))
            destination = href(name) if target.suffix == ".md" or name == "LICENSE" else "/" + name
            fragment = parsed.fragment
            if name == "README.ar.md" and unquote(fragment) == "البداية-من-هنا":
                fragment = "start-here"
            child.attrSet(attribute, urlunsplit(("", "", destination, parsed.query, fragment)))
    return MARKDOWN.renderer.render(tokens, MARKDOWN.options, {})


def heading_ids_in_order(content):
    # Same heading convention as the repository checker, retaining document order.
    seen = set()
    for line in content.splitlines():
        if not re.match(r"^#{1,6}\s", line):
            continue
        title = re.sub(r"^#{1,6}\s+", "", line).strip()
        base = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        value, count = base, 0
        while value in seen:
            count += 1
            value = f"{base}-{count}"
        seen.add(value)
        yield value


def labels(arabic):
    if arabic:
        return {"name": "أمان رقمي", "twin": "Safer Devices", "home": "البداية", "guides": "الأدلة", "agent": "تعليمات المساعدة", "sources": "المصادر", "locale": "English", "draft": "معاينة محلية للمستودع.", "github": "معاينة غيت هب", "skip": "الانتقال للمحتوى", "copy": "نسخ النص", "verify": "علامة الإنجاز", "privacy": "الأسرار والتقارير تبقى خاصة.", "license": "الترخيص"}
    return {"name": "Safer Devices", "twin": "أمان رقمي", "home": "Start here", "guides": "Guides", "agent": "Agent prompt", "sources": "Sources", "locale": "العربية", "draft": "Local preview of the repository.", "github": "GitHub preview", "skip": "Skip to content", "copy": "Copy prompt", "verify": "What counts as finished", "privacy": "Keep secrets and reports private.", "license": "License"}


def frame(body, name, title, github=False):
    arabic = is_arabic(name)
    text = labels(arabic)
    home = "/ar.html" if arabic else "/index.html"
    opposite = href(TWINS.get(name, "README.md" if arabic else "README.ar.md"))
    source = href("ar/sources.md" if arabic else "sources/README.md")
    github_url = "/github-ar.html" if arabic else "/github.html"
    strip = f'<div class="draft-strip"><div class="shell"><span>{text["draft"]}</span><a href="{home if github else github_url}">{text["home"] if github else text["github"]}</a></div></div>'
    brand = f'<a class="brand" href="{home}" aria-label="{text["name"]}">{MARK}<div class="brand-name">{text["name"]}<span lang="{"en" if arabic else "ar"}" dir="{"ltr" if arabic else "rtl"}">{text["twin"]}</span></div></a>'
    nav = f'<nav aria-label="{"التنقل الرئيسي" if arabic else "Main navigation"}"><a class="desktop-nav" href="{home}#guides">{text["guides"]}</a><a href="{source}">{text["sources"]}</a><a class="locale" href="{opposite}" lang="{"en" if arabic else "ar"}" hreflang="{"en" if arabic else "ar"}">{text["locale"]}</a></nav>'
    footer = f'<footer><p>{text["privacy"]}</p><div><a href="/license.html">{text["license"]}</a><a href="{source}">{text["sources"]}</a></div></footer>'
    content = strip + body if github else f'{strip}<div class="shell"><header class="masthead">{brand}{nav}</header>{body}{footer}</div>'
    return f'''<!doctype html><html lang="{"ar" if arabic else "en"}" dir="{"rtl" if arabic else "ltr"}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'self'; script-src 'self'; img-src 'self'; font-src 'self'; connect-src 'none'; base-uri 'none'; form-action 'none'"><meta name="description" content="Practical bilingual security guidance for people and their agents. Local preview."><title>{escape(title)} | Safer Devices preview</title><link rel="icon" href="/assets/mark.svg" type="image/svg+xml"><link rel="alternate" hreflang="{"en" if arabic else "ar"}" href="{opposite}"><link rel="stylesheet" href="/site/preview.css"><script defer src="/site/preview.js"></script></head><body class="{"github-preview" if github else "reading-preview"}"><a class="skip" href="#main">{text["skip"]}</a>{content}</body></html>'''


def checklist_rows(content):
    # The opening checklist comes from the same table shown on GitHub.
    rows = []
    started = False
    for line in content.splitlines():
        if line.startswith("|---"):
            if started:
                break
            started = True
            continue
        if started:
            if not line.startswith("|"):
                break
            rows.append([cell.strip() for cell in line.strip("|").split("|")])
    if len(rows) != 6 or any(len(row) != 3 for row in rows):
        raise ValueError("The opening checklist must contain six three-column rows")
    return rows


def home_page(arabic):
    name = "README.ar.md" if arabic else "README.md"
    text = labels(arabic)
    content = (ROOT / name).read_text()
    prompt = re.search(r"```text\n(.*?)```", content, re.S).group(1).strip()
    if arabic:
        heading = 'أمان أكثر.<br><span>خطوة بخطوة.</span>'
        description = "خطوات عملية لحماية الأجهزة والحسابات، بشكل مباشر أو بمساعدة أدوات ذكية. البداية بالأساسيات، والتغيير بعد فهم الأثر والموافقة عليه."
        aside = 'A little more<br>secure.'
        note = "دليل للأصدقاء والعائلة، بلا برامج تثبيت تلقائية أو وعود بأمان مطلق."
        start, agent = "البداية بالفحوص", "نص لأداة المساعدة"
        checks_title, checks_note = "ستة فحوص للبداية", "كل بند يوضّح علامة الإنجاز."
        concern = '<strong>عند الشك في اختراق:</strong> <a href="/ar/getting-help.html">طلب المساعدة أولًا</a>. التنظيف قد يزيل أدلة مهمة.'
        agent_title, agent_description = "مساعدة ذكية، بصلاحيات واضحة.", "تعليمات تبدأ بالقراءة فقط، وتحافظ على كلمات المرور والمحافظ، وتتطلب موافقة محددة قبل أي تغيير."
        fine = "النص نقطة بداية للمساعدة، وليس تفويضًا مطلقًا. غياب الوصول يعني توضيح الحدّ، لا تجاوز الحماية."
        prompt_label, full = "نص جاهز للنسخ", "التعليمات الكاملة"
        guide_title = "الدليل المناسب لكل خطوة"
        guide_names = ["الحسابات", "المتصفحات", "ماك", "ويندوز", "الهواتف", "أدوات التطوير", "طلب المساعدة", "حوادث حديثة، بشرح واضح"]
        guide_descriptions = ["البريد والمصادقة والجلسات", "الإضافات وصلاحيات المواقع", "التحديث والتشفير والمشاركة", "الحماية والنسخ والاسترداد", "التحديث والصلاحيات والاسترداد", "بيئات التشغيل والحاويات", "الاختراق المحتمل والاستهداف", "الأثر الأوسع والذكاء الاصطناعي والاستعداد"]
        source_heading, source_description = "المصادر قبل الأدوات.", "التوثيق الرسمي هو المرجع، والأدوات اختيارية. نطاق كل فحص وحدوده مهمان بقدر نتيجته."
        limits_heading, limits_description = "ما تم التحقق منه. وما بقي مجهولًا.", "نتيجة فحص واحدة لا تثبت أن الجهاز لم يُخترق. تحديثات مكتملة وصلاحيات أقل ونسخ قابلة للاستعادة تقلل المخاطر، من دون وعود بأمان مطلق."
        source_link, date = "المصادر والأدوات وحدودها", "مراجعة المصادر: 23 تشرين الأول 2026"
    else:
        heading = 'A little more secure.<br><span>One step at a time.</span>'
        description = "Practical security for your devices and accounts. Follow the checks yourself, or give your agent clear instructions and keep control of every change."
        aside = 'أمان رقمي،<br>بخطوات واضحة.'
        note = "For friends, families and the agents helping them. No automatic fixes. No promises of perfect safety."
        start, agent = "Start with the checks", "Give this to your agent"
        checks_title, checks_note = "Your first six checks", "Open any check to see what finished means."
        concern = '<strong>Already worried about a compromise?</strong> <a href="/guides/getting-help.html">Start with getting help</a>. Cleanup can remove evidence.'
        agent_title, agent_description = "A helpful agent. Clear boundaries.", "A copyable request that starts read-only, protects your passwords and wallets, and asks before making changes."
        fine = "This prompt sets a scope. It doesn't grant unrestricted access. An unavailable check stays unknown."
        prompt_label, full = "Copyable starting prompt", "Read the full agent instructions"
        guide_title = "A guide for each next step"
        guide_names = ["Accounts", "Browsers", "Mac", "Windows", "Phones", "Developer tools", "Getting help", "Recent incidents, explained"]
        guide_descriptions = ["Email, MFA and signed-in sessions", "Extensions and website permissions", "Updates, encryption and sharing", "Protection, backups and recovery", "Updates, permissions and recovery", "Runtimes, agents and containers", "Account takeover and targeted concerns", "Wider impact, AI and preparation"]
        source_heading, source_description = "Sources before tools.", "Start with official guidance. Optional tools have a purpose, a scope and limits. Understand those before approving a download or fix."
        limits_heading, limits_description = "Verified where checked. Honest everywhere else.", "One clean scan doesn't establish that a device was never compromised. Finished updates, fewer unnecessary permissions and recoverable backups reduce risk. Unknowns stay visible."
        source_link, date = "Explore sources, tools and their limits", "Sources reviewed: 23 October 2026"
    links = {"agent": href("ar/agent-audit.md" if arabic else "prompts/AGENT-AUDIT.md"), "sources": href("ar/sources.md" if arabic else "sources/README.md")}
    context_url = href("ar/why-this-matters.md" if arabic else "guides/why-this-matters.md")
    context_label = "حوادث حديثة، بشرح واضح" if arabic else "Recent incidents, explained"
    concern += f' <a href="{context_url}">{context_label}</a>.'
    checks = "".join(f'<details class="check-row"><summary><span class="check-name">{escape(label)}</span><span class="check-description">{escape(step)}</span>{CHEVRON}</summary><div class="check-body"><span class="finish-label">{text["verify"]}</span><p>{escape(finish)}</p></div></details>' for label, step, finish in checklist_rows(content))
    slugs = ("accounts", "browsers", "mac", "windows", "phones", "developers", "getting-help", "why-this-matters")
    guides = "".join(f'<a class="guide-link" href="{href(("ar/" if arabic else "guides/") + slug + ".md")}"><div><strong>{title}</strong><span>{description}</span></div>{ARROW}</a>' for slug, title, description in zip(slugs, guide_names, guide_descriptions))
    body = f'''<main id="main"><section class="hero"><div><h1>{heading}</h1><p>{description}</p><div class="actions"><a class="primary" href="#start-here">{start}{ARROW}</a><a class="text-link" href="#agent">{agent}</a></div></div><aside class="hero-aside"><div class="arabic-plate" lang="{"en" if arabic else "ar"}" dir="{"ltr" if arabic else "rtl"}">{aside}</div><div class="aside-note"><div class="tiny-rule"></div><p>{note}</p></div></aside></section><div class="concern">{concern}</div><section class="section" id="start-here"><div class="section-head"><h2>{checks_title}</h2><p>{checks_note}</p></div><div class="checklist">{checks}</div></section><section class="section" id="agent"><div class="agent-grid"><div class="agent-intro"><h2>{agent_title}</h2><p>{agent_description}</p><p class="fine">{fine}</p><a href="{links["agent"]}">{full}</a></div><div><div class="prompt-wrap"><div class="prompt-toolbar"><span>{prompt_label}</span><button class="copy" data-copy aria-describedby="copy-status">{text["copy"]}</button></div><pre id="audit-prompt">{escape(prompt)}</pre></div><p class="copy-status" id="copy-status" role="status" aria-live="polite"></p></div></div></section><section class="section" id="guides"><div class="section-head"><h2>{guide_title}</h2></div><div class="guide-grid">{guides}</div></section><section class="section"><div class="sources-grid"><div><h2>{source_heading}</h2><p>{source_description}</p><div class="source-links"><a href="https://ssd.eff.org/module/your-security-plan">EFF</a><a href="https://github.com/deimos-hq/wardlatch">Wardlatch</a><a href="https://github.com/djadmin/fort">fort</a><a href="https://github.com/dominikmartn/black-october-check">Dom’s checklist</a></div><p><a href="{links["sources"]}">{source_link}</a></p></div><div><h2>{limits_heading}</h2><p>{limits_description}</p><p class="quiet-note">{date}</p></div></div></section></main>'''
    return frame(body, name, text["name"])


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copytree(ROOT / "assets", OUT / "assets", dirs_exist_ok=True)
    shutil.copytree(ROOT / "site", OUT / "site", dirs_exist_ok=True)
    shutil.copytree(ROOT / "scripts", OUT / "scripts", dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copy2(ROOT / "requirements-dev.txt", OUT / "requirements-dev.txt")
    documents = [path for path in ROOT.rglob("*.md") if not {".private", ".git", ".impeccable", "__pycache__"}.intersection(path.relative_to(ROOT).parts)]
    for path in documents:
        name = str(path.relative_to(ROOT))
        if name in ("README.md", "README.ar.md"):
            continue
        title = re.search(r"^# (.+)$", path.read_text(), re.M).group(1)
        text = labels(is_arabic(name))
        home = "/ar.html" if is_arabic(name) else "/index.html"
        body = f'<main id="main" class="article-layout"><aside class="toc" aria-label="{"الأدلة" if is_arabic(name) else "Guide navigation"}"><a href="{home}">{text["home"]}</a><a href="{home}#guides">{text["guides"]}</a><a href="{home}#agent">{text["agent"]}</a></aside><article class="article">{render_markdown(path)}</article></main>'
        target = OUT / route(name)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(frame(body, name, title))
    for arabic, name in ((False, "README.md"), (True, "README.ar.md")):
        (OUT / route(name)).write_text(home_page(arabic))
        description = "معاينة محلية تقريبية لتنسيق المستودع على غيت هب، وليست صفحة منشورة." if arabic else "Approximate local README preview. GitHub controls its final rendering."
        body = f'<main id="main" class="github-frame"><div class="github-repo-title">safer-devices<small>{description}</small></div><article class="github-body">{render_markdown(ROOT / name)}</article></main>'
        (OUT / ("github-ar.html" if arabic else "github.html")).write_text(frame(body, name, "Repository preview", github=True))
    (OUT / "license.html").write_text(frame('<main id="main" class="article-layout"><article class="article"><h1>MIT License</h1><pre>' + escape((ROOT / "LICENSE").read_text()) + '</pre></article></main>', "LICENSE", "License"))
    print(f"Built {len(documents)} documents, bilingual home pages and GitHub-style previews.")
    print("Output: .private/preview. Nothing was published; no device settings were inspected.")


if __name__ == "__main__":
    main()
