import sqlite3
from datetime import datetime
import os

# Ensure data directory exists
os.makedirs('data', exist_ok=True)

def init_db():
    conn = sqlite3.connect('data/compliance.db')
    c = conn.cursor()
    # ... your existing table creation code ...
    conn.commit()
    conn.close()

def init_db():
    """Initialize all database tables"""
    conn = sqlite3.connect('data/compliance.db')
    c = conn.cursor()
    
    # Users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 username TEXT PRIMARY KEY,
                 name TEXT,
                 role TEXT,
                 email TEXT)''')
    
    # Audit Trail (logs every action)
    c.execute('''CREATE TABLE IF NOT EXISTS audit_trail (
                 id INTEGER PRIMARY KEY,
                 timestamp TEXT,
                 username TEXT,
                 action TEXT,
                 details TEXT,
                 ip TEXT)''')
    
    # Policy Attestations
    c.execute('''CREATE TABLE IF NOT EXISTS attestations (
                 id INTEGER PRIMARY KEY,
                 username TEXT,
                 policy_title TEXT,
                 date TEXT,
                 drive_file_id TEXT,
                 envelope_id TEXT,
                 status TEXT)''')
    
    # Training Records
    c.execute('''CREATE TABLE IF NOT EXISTS training_records (
                 id INTEGER PRIMARY KEY,
                 username TEXT,
                 module TEXT,
                 score INTEGER,
                 passed BOOLEAN,
                 date TEXT,
                 certificate_path TEXT,
                 envelope_id TEXT)''')
    
    # Incident Reports
    c.execute('''CREATE TABLE IF NOT EXISTS incidents (
                 id INTEGER PRIMARY KEY,
                 username TEXT,
                 incident_type TEXT,
                 severity TEXT,
                 description TEXT,
                 date TEXT,
                 status TEXT DEFAULT 'Open',
                 drive_file_id TEXT,
                 envelope_id TEXT)''')
    
    # AI Risk Testing Records
    c.execute('''CREATE TABLE IF NOT EXISTS ai_risk_testing (
                 id INTEGER PRIMARY KEY,
                 username TEXT,
                 model_name TEXT,
                 overall_score REAL,
                 date TEXT,
                 drive_file_id TEXT,
                 envelope_id TEXT)''')
    
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully")

def log_audit_trail(username, action, details, ip="Unknown"):
    """Log every action for full audit trail (SEC books & records)"""
    conn = sqlite3.connect('data/compliance.db')
    c = conn.cursor()
    c.execute("""INSERT INTO audit_trail 
                 (timestamp, username, action, details, ip) 
                 VALUES (?, ?, ?, ?, ?)""",
              (datetime.now().isoformat(), username, action, details, ip))
    conn.commit()
    conn.close()



def log_attestation(username, policy_title, drive_file_id=None, envelope_id=None, status="Sent"):
    """Log policy attestations"""
    conn = sqlite3.connect('data/compliance.db')
    c = conn.cursor()
    c.execute("""INSERT INTO attestations 
                 (username, policy_title, date, drive_file_id, envelope_id, status) 
                 VALUES (?, ?, ?, ?, ?, ?)""",
              (username, policy_title, datetime.now().isoformat(), drive_file_id, envelope_id, status))
    conn.commit()
    conn.close()

def log_training_record(username, module, score, passed, certificate_path=None, envelope_id=None):
    """Log training completion (used by all training modules)"""
    conn = sqlite3.connect('data/compliance.db')
    c = conn.cursor()
    c.execute("""INSERT INTO training_records 
                 (username, module, score, passed, date, certificate_path, envelope_id) 
                 VALUES (?, ?, ?, ?, ?, ?, ?)""",
              (username, module, score, passed, datetime.now().isoformat(), certificate_path, envelope_id))
    conn.commit()
    conn.close()

def log_incident(username, incident_type, severity, description, drive_file_id=None, envelope_id=None):
    """Log incidents (including phishing, Reg S-P, AI, AML, etc.)"""
    conn = sqlite3.connect('data/compliance.db')
    c = conn.cursor()
    c.execute("""INSERT INTO incidents 
                 (username, incident_type, severity, description, date, drive_file_id, envelope_id) 
                 VALUES (?, ?, ?, ?, ?, ?, ?)""",
              (username, incident_type, severity, description, datetime.now().isoformat(), drive_file_id, envelope_id))
    conn.commit()
    conn.close()

def log_ai_risk_test(username, model_name, overall_score, drive_file_id=None, envelope_id=None):
    """Log AI risk testing results"""
    conn = sqlite3.connect('data/compliance.db')
    c = conn.cursor()
    c.execute("""INSERT INTO ai_risk_testing 
                 (username, model_name, overall_score, date, drive_file_id, envelope_id) 
                 VALUES (?, ?, ?, ?, ?, ?)""",
              (username, model_name, overall_score, datetime.now().isoformat(), drive_file_id, envelope_id))
    conn.commit()
    conn.close()

# Optional helper to get recent records (useful for Report Center)
def get_recent_audit_trail(limit=50):
    conn = sqlite3.connect('data/compliance.db')
    df = pd.read_sql_query(f"SELECT * FROM audit_trail ORDER BY timestamp DESC LIMIT {limit}", conn)
    conn.close()
    return df

print("Database module loaded with all logging functions")