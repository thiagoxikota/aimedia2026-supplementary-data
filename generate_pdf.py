#!/usr/bin/env python3
"""Generate supplementary_visual_dataset.pdf from cropped assets."""

import json
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Image, KeepTogether, PageBreak, Table, TableStyle,
)
from reportlab.lib import colors
from PIL import Image as PILImage

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets", "cropped")
MANIFEST = os.path.join(BASE_DIR, "manifest.json")
OUTPUT = os.path.join(BASE_DIR, "supplementary_visual_dataset.pdf")

PAGE_W, PAGE_H = A4
MARGIN = 18 * mm
CONTENT_W = PAGE_W - 2 * MARGIN

# Section name translations (PT -> EN)
SECTION_EN = {
    "Dashboard": "Dashboard",
    "Motoristas": "Drivers",
    "Detalhes do Motorista": "Driver Details",
    "Entregas": "Deliveries",
    "Alertas": "Alerts",
    "Painel": "Control Panel",
    "Mapa": "Map",
    "Conflitos": "Conflicts",
    "Monitoramento": "Monitoring",
}

# Page descriptions in English (keyed by filename without extension)
DESCRIPTIONS = {
    "fig_01_ai_dashboard_page1": "Top-bar navigation, 4 KPI cards, alerts list, priority deliveries",
    "fig_02_ai_dashboard_page2": "Sidebar navigation, KPI cards, driver status pie chart",
    "fig_03_ai_dashboard_page3": "Sidebar navigation, KPI cards with progress bars, driver status icons",
    "fig_04_ai_dashboard_page4": "Top-bar navigation, KPI cards, active drivers list with ETA",
    "fig_05_designer_dashboard_page1": "Map-based overview, driver cards, route details",
    "fig_06_designer_dashboard_page2": "Tabbed interface, scheduling view, driver assignments",
    "fig_07_designer_dashboard_page3": "Multi-table dashboard with driver and delivery data",
    "fig_08_ai_motoristas_page1": "Full driver listing with status, route, delivery count",
    "fig_09_ai_motoristas_page2": "Compact driver list with search and filters",
    "fig_10_ai_motoristas_page3": "Driver cards with route and delivery info",
    "fig_11_ai_motoristas_page4": "Driver table view with sortable columns",
    "fig_12_ai_motoristas_page5": "Full-page driver listing with additional detail columns",
    "fig_13_designer_motoristas_page1": "Driver listing with status badges, vehicle info, alert indicators",
    "fig_14_designer_detalhes_page1": "Driver profile with current route, delivery status, contact info",
    "fig_15_designer_detalhes_page2": "Driver detail with performance history and delivery log",
    "fig_16_ai_entregas_page1": "Delivery listing with status, driver, address, time",
    "fig_17_ai_entregas_page2": "Delivery summary with filters and status categories",
    "fig_18_ai_entregas_page3": "Delivery cards with route details and progress",
    "fig_19_ai_entregas_page4": "Compact delivery table with sortable columns",
    "fig_20_ai_entregas_page5": "Full-page delivery listing with additional detail columns",
    "fig_21_ai_alertas_page1": "Alert center with severity filters and summary statistics",
    "fig_22_ai_alertas_page2": "Alert listing with system and driver alerts",
    "fig_23_ai_alertas_page3": "Alert detail view with severity badges and timestamps",
    "fig_24_ai_alertas_page4": "Alert dashboard with severity counters and priority view",
    "fig_25_designer_alertas_page1": "Alert center with color-coded severity, filter tabs, action buttons",
    "fig_26_ai_painel_page1": "Control panel with operational metrics and system status",
    "fig_27_ai_mapa_page1": "Map interface with driver locations and route paths",
    "fig_28_ai_conflitos_page1": "Conflict listing with scheduling overlaps and resolution actions",
    "fig_29_designer_monitoramento_page1": "3-panel layout: driver list (left), geographic driver cards (center), critical alerts (right)",
    "fig_30_designer_monitoramento_page1_card": "Same layout with driver selected: detail panel replaces alerts on right",
}


def load_manifest():
    with open(MANIFEST) as f:
        return json.load(f)


def cropped_path(filename):
    base = filename.replace(".png", "")
    return os.path.join(ASSETS_DIR, f"{base}_viewport.png")


def get_image_size(path):
    with PILImage.open(path) as img:
        return img.size


class NumberedDocTemplate(BaseDocTemplate):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page_count = 0

    def afterPage(self):
        self.page_count += 1
        canvas = self.canv
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(HexColor("#888888"))
        canvas.drawCentredString(PAGE_W / 2, 10 * mm, f"{self.page_count}")
        canvas.restoreState()


def build_pdf():
    manifest = load_manifest()

    doc = NumberedDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=14 * mm,
    )

    frame = Frame(MARGIN, 14 * mm, CONTENT_W, PAGE_H - MARGIN - 14 * mm, id="main")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame])])

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "Title", parent=styles["Title"], fontSize=20, spaceAfter=6 * mm, alignment=TA_CENTER
    )
    subtitle_style = ParagraphStyle(
        "Subtitle", parent=styles["Normal"], fontSize=11, textColor=HexColor("#555555"),
        alignment=TA_CENTER, spaceAfter=4 * mm,
    )
    section_style = ParagraphStyle(
        "Section", parent=styles["Heading1"], fontSize=16, spaceBefore=8 * mm,
        spaceAfter=4 * mm, textColor=HexColor("#1a1a1a"),
    )
    author_style = ParagraphStyle(
        "Author", parent=styles["Heading2"], fontSize=13, spaceBefore=4 * mm,
        spaceAfter=2 * mm, textColor=HexColor("#333333"),
    )
    caption_style = ParagraphStyle(
        "Caption", parent=styles["Normal"], fontSize=9, textColor=HexColor("#666666"),
        alignment=TA_CENTER, spaceAfter=2 * mm,
    )
    crop_label_style = ParagraphStyle(
        "CropLabel", parent=styles["Normal"], fontSize=7, textColor=HexColor("#999999"),
        alignment=TA_CENTER, spaceAfter=3 * mm,
    )
    toc_style = ParagraphStyle(
        "TOC", parent=styles["Normal"], fontSize=10, spaceBefore=1.5 * mm,
    )

    story = []

    # --- Cover ---
    story.append(Spacer(1, 40 * mm))
    story.append(Paragraph("Supplementary Visual Dataset", title_style))
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph(
        "Structural Convergence in AI-Generated Media:<br/>"
        "How Specification Literacy Moderates Homogenization<br/>"
        "in GenAI-Assisted Interface Design",
        subtitle_style,
    ))
    story.append(Spacer(1, 6 * mm))
    story.append(Paragraph("AIMEDIA 2026", ParagraphStyle(
        "Conf", parent=styles["Normal"], fontSize=12, alignment=TA_CENTER,
        textColor=HexColor("#777777"),
    )))
    story.append(Spacer(1, 10 * mm))
    story.append(Paragraph(
        "30 screens — 21 AI-generated (Figma Make) · 9 human-designed<br/>"
        "Viewport-cropped to 1426px height for standardized comparison",
        ParagraphStyle("CoverNote", parent=styles["Normal"], fontSize=9,
                       alignment=TA_CENTER, textColor=HexColor("#999999")),
    ))
    story.append(PageBreak())

    # --- Table of Contents ---
    story.append(Paragraph("Table of Contents", section_style))
    story.append(Spacer(1, 4 * mm))

    sections_order = []
    seen = set()
    for entry in manifest:
        sec = entry["section"]
        if sec not in seen:
            seen.add(sec)
            sections_order.append(sec)

    for sec in sections_order:
        en = SECTION_EN.get(sec, sec)
        entries = [e for e in manifest if e["section"] == sec]
        ai_count = sum(1 for e in entries if e["author"] == "AI")
        des_count = sum(1 for e in entries if e["author"] == "Designer")
        parts = []
        if ai_count:
            parts.append(f"AI: {ai_count}")
        if des_count:
            parts.append(f"Designer: {des_count}")
        story.append(Paragraph(f"<b>{en}</b> — {', '.join(parts)}", toc_style))

    story.append(PageBreak())

    # --- Comparative Examples (side by side) ---
    story.append(Paragraph("Comparative Examples", section_style))
    story.append(Paragraph(
        "Side-by-side pairs from functional areas produced under both conditions. "
        "AI condition listed on the left.",
        ParagraphStyle("CompNote", parent=styles["Normal"], fontSize=9,
                       textColor=HexColor("#666666"), spaceAfter=4 * mm),
    ))

    comparisons = [
        ("Dashboard", "fig_01_ai_dashboard_page1", "fig_05_designer_dashboard_page1"),
        ("Drivers", "fig_08_ai_motoristas_page1", "fig_13_designer_motoristas_page1"),
        ("Alerts", "fig_21_ai_alertas_page1", "fig_25_designer_alertas_page1"),
    ]

    col_w = (CONTENT_W - 4 * mm) / 2
    for label, ai_key, des_key in comparisons:
        ai_path = cropped_path(f"{ai_key}.png")
        des_path = cropped_path(f"{des_key}.png")

        ai_img = Image(ai_path, width=col_w, height=col_w * 0.75, kind="proportional")
        des_img = Image(des_path, width=col_w, height=col_w * 0.75, kind="proportional")

        header = Table(
            [[Paragraph(f"<b>{label} — AI (Figma Make)</b>", caption_style),
              Paragraph(f"<b>{label} — Designer</b>", caption_style)]],
            colWidths=[col_w, col_w],
        )
        header.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "BOTTOM")]))

        img_table = Table([[ai_img, des_img]], colWidths=[col_w, col_w])
        img_table.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ]))

        story.append(KeepTogether([header, Spacer(1, 1 * mm), img_table, Spacer(1, 6 * mm)]))

    story.append(PageBreak())

    # --- Complete Dataset ---
    story.append(Paragraph("Complete Visual Dataset", section_style))
    story.append(Spacer(1, 2 * mm))

    current_section = None
    current_author = None

    for entry in manifest:
        sec = entry["section"]
        author = entry["author"]
        filename = entry["filename"]
        base = filename.replace(".png", "")
        en_section = SECTION_EN.get(sec, sec)

        if sec != current_section:
            current_section = sec
            current_author = None
            story.append(Paragraph(en_section, section_style))

        if author != current_author:
            current_author = author
            label = "AI (Figma Make)" if author == "AI" else "Designer"
            story.append(Paragraph(label, author_style))

        img_path = cropped_path(filename)
        if not os.path.exists(img_path):
            continue

        iw, ih = get_image_size(img_path)
        aspect = ih / iw
        display_w = CONTENT_W
        display_h = display_w * aspect
        max_h = PAGE_H * 0.6
        if display_h > max_h:
            display_h = max_h
            display_w = display_h / aspect

        img = Image(img_path, width=display_w, height=display_h)

        desc = DESCRIPTIONS.get(base, "")
        page_num = base.split("page")[-1] if "page" in base else ""
        if "_card" in base:
            page_label = f"Page {page_num.replace('_card', '')} (Card Selected)"
        else:
            page_label = f"Page {page_num}" if page_num else ""

        caption_text = f"<b>{page_label}</b>"
        if desc:
            caption_text += f" — {desc}"

        # Crop label
        orig_res = entry.get("resolution", "")
        orig_h = int(orig_res.split("x")[1]) if "x" in orig_res else 0
        crop_note = ""
        if orig_h > 1426:
            crop_note = f"Viewport crop — original height: {orig_h}px"

        elements = [
            Paragraph(caption_text, caption_style),
            img,
        ]
        if crop_note:
            elements.append(Paragraph(crop_note, crop_label_style))
        elements.append(Spacer(1, 4 * mm))

        story.append(KeepTogether(elements))

    doc.build(story)
    print(f"Generated: {OUTPUT}")


if __name__ == "__main__":
    build_pdf()
