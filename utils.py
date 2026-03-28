# utils.py - Clean version that calls real integrations
import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def generate_pdf_from_markdown(title: str, content: str, output_path: str) -> str:
    """Generate a clean professional PDF."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    doc = SimpleDocTemplate(output_path, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
    styles = getSampleStyleSheet()
    styles['Title'].fontSize = 16
    styles['Normal'].fontSize = 11
    styles['Normal'].spaceAfter = 12
    
    story = []
    story.append(Paragraph(f"<b>{title}</b>", styles['Title']))
    story.append(Spacer(1, 0.5 * inch))
    story.append(Paragraph(f"Date: {datetime.now().strftime('%Y-%m-%d')}", styles['Normal']))
    story.append(Spacer(1, 0.3 * inch))
    
    for para in content.split('\n\n'):
        if para.strip():
            cleaned = para.replace('\n', '<br/>')
            story.append(Paragraph(cleaned, styles['Normal']))
            story.append(Spacer(1, 12))
    
    doc.build(story)
    return output_path

# This function now properly calls the real integrations
def generate_and_sign_policy(title: str, content: str, username: str, email: str, folder_id: str = "Compliance_Policies"):
    """Main function - calls real Google Drive + DocuSign."""
    from integrations import generate_and_sign_policy as real_generate  # Import from integrations.py
    
    return real_generate(title, content, username, email, folder_id)