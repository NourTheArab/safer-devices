---
name: Safer Devices
description: Bilingual editorial device and account security guidance.
colors:
  paper: "#000"
  surface: "#0c0c0c"
  ink: "#fff"
  text: "#cfcfcb"
  mute: "#a4a49f"
  rule: "#303030"
  gold: "#b8954a"
  sand: "#cbb896"
  olive: "#7fae8d"
typography:
  display:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "min(clamp(3.2rem,6.5vw,5.8rem),5.125rem)"
    fontWeight: 400
    lineHeight: 1.04
    letterSpacing: "-.025em"
  headline:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(1.8rem,3.5vw,2.5rem)"
    fontWeight: 400
    lineHeight: 1.2
  body:
    fontFamily: "Plex, Arial, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.8
  body-ar:
    fontFamily: "Plex, Arial, sans-serif"
    fontSize: "1.08rem"
    fontWeight: 400
    lineHeight: 1.9
    letterSpacing: "0"
  display-ar:
    fontFamily: "Amiri, serif"
    fontSize: "clamp(3.1rem,6vw,5.3rem)"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0"
  label:
    fontFamily: "Plex, Arial, sans-serif"
    fontSize: ".82rem"
  lead:
    fontFamily: "Plex, Arial, sans-serif"
    fontSize: "1.2rem"
    lineHeight: 1.7
spacing:
  compact: "20px"
  regular: "24px"
  navigation: "28px"
  row-gap: "30px"
  column-gap: "65px"
components:
  action-primary:
    backgroundColor: "{colors.sand}"
    textColor: "{colors.paper}"
    padding: "11px 19px"
  action-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
  action-copy:
    backgroundColor: "transparent"
    textColor: "{colors.sand}"
    padding: "6px 13px"
  action-copy-hover:
    backgroundColor: "{colors.sand}"
    textColor: "{colors.paper}"
  prompt-container:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
  navigation:
    textColor: "{colors.sand}"
  checklist-row:
    textColor: "{colors.text}"
    padding: "23px 0"
  guide-link:
    textColor: "{colors.ink}"
    padding: "19px 0"
---

# Design System: Safer Devices

## Overview

**Creative North Star: "The Bilingual Editorial Register"**

A bilingual editorial register, extending the owner’s Nawafith reference through black surfaces, fine rules, serif headings and readable sans serif guidance. Dense information stays calm through clear columns, measured paragraphs and visible completion criteria.

The custom reading preview and the repository presentation share content and artwork. GitHub controls its own typography and layout; its local approximation is not the custom reading system. The repository is approved for public GitHub publication; the reading preview remains local. This document records the implemented system in `site/preview.css`, `site/preview.js` and `scripts/build_preview.py`.

**Key Characteristics:**
- Black reading surface with sand actions and olive verification cues.
- Newsreader Latin headings, Amiri Arabic headings and Plex body text.
- Fine ruled registers, native disclosures and square controls.
- English first, paired Arabic pages and logical RTL spacing.

## Colors

Sand and restrained gold warm a true black reading surface. Olive signals completion and accessible focus. The frontmatter records the colors actually used by the custom reading system.

### Primary

- **Sand:** links, primary action, alternate heading lines, Arabic plate and table headings.
- **Gold:** the small linework brand mark.

### Secondary

- **Olive:** finish labels, copy status, small editorial rules and keyboard focus outlines.

### Neutral

- **Paper:** true black page background and dark text on the sand action.
- **Surface:** near black prompt panels, code blocks and disclosure hover states.
- **Ink:** headings, strong text and link hover states.
- **Text:** reading paragraphs and checklist descriptions.
- **Mute:** notes, captions, navigation support and footer text.
- **Rule:** fine separators and panel outlines.

**The Ruled Register Rule.** Separate repeated checks and guide links with fine rules and open space. Reserve the filled surface for bounded text such as the copyable prompt.

## Typography

**Display Font:** Newsreader, with Georgia and serif fallbacks, for Latin headings. Amiri, with a serif fallback, for Arabic headings and Arabic display plates.

**Body Font:** IBM Plex Sans Arabic, registered as Plex, with Arial and sans serif fallbacks. The Latin prompt and technical code use the platform monospace stack; this is a functional code treatment.

The type ramp moves from quiet supporting text through comfortable body copy to large serif statements. Display headings use regular weight. Body emphasis uses medium weight. Local font files and the three SIL Open Font License texts live in `assets/fonts`; `assets/fonts/provenance.json` records their sources. No Thmanyah font files are redistributed.

### Hierarchy

- **Display:** frontmatter display role for the English home statement. At the phone breakpoint it becomes (3.45rem), with a (14ch) maximum measure.
- **Arabic display:** frontmatter Arabic display role, with a (15ch) maximum measure and (3.2rem) phone size. Arabic headings use (1.5) line height.
- **Headline:** frontmatter headline role for recurring section headings. Phone section headings use (1.9rem).
- **Article title:** fluid Latin title (clamp(2.3rem,5vw,3.9rem)), line height (1.1), tightening (-.02em); phone size (2.6rem). Arabic inherits Amiri and zero tracking.
- **Body:** frontmatter body roles, with reading articles limited to (70ch). English lead text uses the lead role; phone hero paragraphs use (1.04rem).
- **Label:** compact supporting text, without uppercase transformation or decorative eyebrow treatment.

**The Two Scripts Rule.** Use the appropriate display face for each script, preserve Arabic shaping and apply no Arabic tracking.

## Layout

The centered shell caps at (1192px). Desktop total outside space is (96px), reducing to (48px) at the (900px) breakpoint and (36px) at the (600px) breakpoint. Repeated desktop column gaps use the column-gap token; fine rules hold the page together.

The home statement has unequal columns (1.7fr / 1fr), with a slightly different Arabic ratio (1.6fr / 1fr). The agent section uses (1fr / 1.35fr); guides and sources use equal columns. Below (900px), the agent and article layouts stack. Below (600px), the home statement, guide register and sources stack; the companion language plate remains beside its short note within the stacked aside.

Desktop checklist summaries align a title (225px), description and chevron (24px), with the row-gap token. At (900px), the title becomes (175px). At (600px), title and description share one column, with the chevron beside both. Expanded finish text follows the same column alignment until mobile stacking.

Reading sections use vertical padding (53px), reduced to (35px) on phones. Articles have a (190px) sticky navigation column, gap (70px), and a reading measure (70ch). Below (900px), article navigation becomes a static wrapping row. Tables may scroll horizontally inside their own container; code wraps within its container.

English opens first. Paired language links lead to the corresponding guide where available. Arabic pages declare `lang="ar"` and `dir="rtl"`; logical inline borders and padding carry the reversed layout. Arabic wording uses neutral nominal and impersonal forms.

## Elevation & Depth

The custom reading system has no box shadows. Fine borders and the near black surface distinguish panels and hover states. No floating card elevation or backdrop treatment is implemented.

**The Flat Reading Rule.** Use borders, tone and spacing for hierarchy. The custom reading surface uses no shadows.

Links and primary actions transition over (.15s ease-out). Disclosure chevrons rotate over (.2s ease-out). Reduced motion removes transitions and animations and switches smooth scrolling to automatic scrolling.

## Shapes

The custom reading treatment uses square corners and thin strokes (1px). The mark is original arch linework; directional affordances are inline SVG arrows and chevrons. Glyph characters do not stand in for icons. The rounded (6px) containers in the GitHub approximation belong to that host simulation, not to this reading system.

## Components

### Primary action

A sand rectangle with dark text, medium weight and a matching border. Desktop padding is the primary component token; phones use (10px 15px). Hover turns the fill white. Keyboard focus uses an olive outline (2px) with offset (6px), shared by links, buttons and summaries.

### Copy action and prompt container

A transparent outlined control sits in the toolbar of a square near black bordered panel. Hover inverts the copy control to sand. The toolbar and prompt are separated by a fine rule. The prompt wraps, including long content, and reserves a polite live status line beneath it.

`site/preview.js` copies only the prompt text to the clipboard. Success changes the label and announces status. If clipboard access fails, it selects the prompt for manual copying. It does not run the prompt or inspect a device. The CSS defines an olive disabled state, but the shipped script does not disable the button after copying.

### Checklist disclosure

Native `details` and `summary` provide expandable rows with a name, explanation and chevron. Hover adds the near black surface. Opening rotates the chevron and reveals an olive finish label with supporting text. Keyboard activation remains native.

### Guide register

Two ruled columns on desktop, one on phones. Each link has a medium weight title, muted supporting line and a small sand SVG arrow. Hover turns the title sand. These are linked rows, without separate card backgrounds.

### Navigation and article reading

The masthead pairs the bilingual mark and name with quiet text links. A logical inline rule separates the locale switch. The guide navigation link hides on phones; the locale and source links stay available. A skip link appears on keyboard focus. Article navigation is sticky on desktop and wraps above the article on narrower screens.

### Repository artwork

`assets/cover.png` and `assets/social-preview.png` carry the bilingual visual identity into the repository’s native rendering. `assets/README.md` records artwork provenance. Their embedded typography remains artwork; README text remains controlled by GitHub.

## Do's and Don'ts

### Do:
- **Do** use logical inline spacing and paired language links.
- **Do** keep finish criteria visible inside each expanded check.
- **Do** retain keyboard focus, native disclosure behavior and a manual copy fallback.
- **Do** keep font licenses and artwork provenance with redistributed assets.
- **Do** treat GitHub previews as approximate and publication as a separate approval.

### Don't:
- **Don't** apply Latin letter spacing to Arabic.
- **Don't** replace ruled reading registers with decorative card grids.
- **Don't** imply that the guide scans a device or automatically changes settings.
- **Don't** put private audit data or identifying material in public assets or documentation.
- **Don't** use the GitHub approximation’s system display font as the custom reading identity.
