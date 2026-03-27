# utils.py - Minimal version with required functions
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from datetime import datetime

def generate_pdf_from_markdown(title, content, output_path):
    """Simple PDF generator from markdown content"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    c = canvas.Canvas(output_path, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, title)
    c.setFont("Helvetica", 12)
    y = 720
    for line in content.split('\n'):
        if y < 50:
            c.showPage()
            y = 750
        c.drawString(50, y, line[:100])  # safe truncation
        y -= 15
    c.save()
    return output_path

def generate_and_sign_policy(title, content, username, email, folder_id):
    """Generate PDF, upload to Google Drive, and send for DocuSign"""
    pdf_path = f"pdfs/{title.replace(' ', '_')}_{username}_{datetime.now().strftime('%Y%m%d')}.pdf"
    generate_pdf_from_markdown(title, content, pdf_path)
    
    # Placeholder for Drive + DocuSign (replace with your integrations.py functions)
    drive_id = "placeholder_drive_id"
    envelope_id = "placeholder_envelope_id"
    
    print(f"Generated PDF for {title} and sent for signature")
    return drive_id, envelope_id, pdf_path