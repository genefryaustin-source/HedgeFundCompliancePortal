# Encryption Policy (SOC 2 Security & Confidentiality)

**Requirements**:
- Data at rest: AES-256 or stronger.
- Data in transit: TLS 1.2 or higher (1.3 preferred).
- Key management: Centralized KMS or HSM with rotation every 90 days for high-risk keys.
- Full-disk encryption on all laptops and mobile devices.
- Prohibition on storing unencrypted sensitive data in email or cloud storage without controls.

**Exceptions**: Must be documented and approved by CCO with compensating controls.