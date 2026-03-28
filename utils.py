# utils.py - Full version with professional PDF generation + integration placeholders
import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def generate_pdf_from_markdown(title: str, content: str, output_path: str) -> str:
    """Generate a clean, professional multi-page PDF from policy markdown content."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    doc = SimpleDocTemplate(output_path, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
    styles = getSampleStyleSheet()
    
    # Custom styles
    styles['Title'].fontSize = 16
    styles['Title'].spaceAfter = 30
    styles['Normal'].fontSize = 11
    styles['Normal'].spaceAfter = 12
    styles['Heading2'].fontSize = 14
    styles['Heading2'].spaceAfter = 18
    
    story = []
    
    # Title
    story.append(Paragraph(f"<b>{title}</b>", styles['Title']))
    story.append(Spacer(1, 0.5 * inch))
    
    # Add date and firm info
    story.append(Paragraph(f"Date: {datetime.now().strftime('%Y-%m-%d')}", styles['Normal']))
    story.append(Paragraph("Firm: Your Hedge Fund Group – $1B AUM RIA", styles['Normal']))
    story.append(Spacer(1, 0.5 * inch))
    
    # Split content into paragraphs and add them
    paragraphs = content.split('\n\n')
    for para in paragraphs:
        if para.strip():
            # Handle bold/headers if present
            if para.strip().startswith('**') and para.strip().endswith('**'):
                cleaned = para.strip('**')
                story.append(Paragraph(f"<b>{cleaned}</b>", styles['Heading2']))
            else:
                # Replace simple markdown line breaks
                cleaned = para.replace('\n', '<br/>')
                story.append(Paragraph(cleaned, styles['Normal']))
            story.append(Spacer(1, 12))
    
    doc.build(story)
    return output_path

def generate_and_sign_policy(title: str, content: str, username: str, email: str, folder_id: str = "Compliance_Policies"):
    """
    Generate PDF + Placeholder for real Google Drive upload + DocuSign envelope.
    
    This is where the real integrations should happen.
    """
    safe_title = "".join(c if c.isalnum() or c in (' ', '_', '-') else '_' for c in title)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    pdf_path = f"pdfs/{safe_title}_{username}_{timestamp}.pdf"
    
    try:
        # Generate professional PDF
        pdf_path = generate_pdf_from_markdown(title, content, pdf_path)
        
        # TODO: Real Google Drive Upload (uncomment when you add google-api-python-client)
        # from integrations import upload_to_google_drive
        # drive_id = upload_to_google_drive(pdf_path, folder_id)
        drive_id = f"placeholder_drive_{timestamp}"
        
        # TODO: Real DocuSign Envelope Creation
        # from integrations import create_docusign_envelope
        # envelope_id = create_docusign_envelope(pdf_path, title, email)
        envelope_id = f"placeholder_envelope_{timestamp}"
        
        print(f"✅ PDF successfully generated: {pdf_path}")
        print(f"📤 Drive placeholder ID: {drive_id}")
        print(f"📧 DocuSign placeholder Envelope ID: {envelope_id}")
        
        return drive_id, envelope_id, pdf_path
        
    except Exception as e:
        print(f"❌ Error in generate_and_sign_policy: {str(e)}")
        raise

# Optional helper for future real integration
def create_placeholder_envelope(pdf_path: str, signer_email: str, document_name: str):
    """Placeholder for real DocuSign logic."""
    return f"env_{datetime.now().strftime('%Y%m%d%H%M')}"