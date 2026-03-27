# utils.py - Improved version with proper PDF generation and error handling

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
import os
from datetime import datetime

def generate_pdf_from_markdown(title, content, output_path):
    """Improved PDF generator that handles longer content better"""
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Use Platypus for better text handling (multi-page, wrapping)
        doc = SimpleDocTemplate(output_path, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []
        
        # Title
        story.append(Paragraph(f"<b>{title}</b>", styles['Heading1']))
        story.append(Spacer(1, 0.5 * inch))
        
        # Content - split into paragraphs for better formatting
        paragraphs = content.split('\n\n')
        for para in paragraphs:
            if para.strip():
                story.append(Paragraph(para.replace('\n', '<br/>'), styles['Normal']))
                story.append(Spacer(1, 0.2 * inch))
        
        doc.build(story)
        return output_path
        
    except Exception as e:
        # Fallback to simple canvas method if Platypus fails
        print(f"Platypus failed, using fallback: {e}")
        return generate_pdf_fallback(title, content, output_path)

def generate_pdf_fallback(title, content, output_path):
    """Simple fallback PDF generator"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    c = canvas.Canvas(output_path, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, title)
    c.setFont("Helvetica", 11)
    y = 720
    for line in content.split('\n'):
        if y < 50:
            c.showPage()
            y = 750
        c.drawString(50, y, line[:95])  # Safe truncation
        y -= 14
    c.save()
    return output_path

def generate_and_sign_policy(title, content, username, email, folder_id):
    """Generate PDF, upload to Google Drive (placeholder), and prepare for DocuSign"""
    try:
        pdf_path = f"pdfs/{title.replace(' ', '_').replace('/', '_')}_{username}_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
        
        # Generate the PDF
        pdf_path = generate_pdf_from_markdown(title, content, pdf_path)
        
        # Placeholder for real integrations (Google Drive + DocuSign)
        # In production, call your integrations.py functions here
        drive_id = f"drive_{datetime.now().strftime('%Y%m%d')}"
        envelope_id = f"env_{datetime.now().strftime('%Y%m%d%H%M')}"
        
        print(f"✅ PDF generated successfully: {pdf_path}")
        return drive_id, envelope_id, pdf_path
        
    except Exception as e:
        print(f"Error generating PDF: {e}")
        # Return fallback values
        return "error_drive_id", "error_envelope_id", "error.pdf"