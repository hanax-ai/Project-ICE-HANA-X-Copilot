# Project ICE Security and Responsible Disclosure

## Repository classification

The canonical Project ICE repository contains governed publication work and may contain restricted internal source evidence. It must remain private whenever restricted sources are present.

## Do not commit

- SAP credentials, OAuth secrets, tokens, certificates, or connection strings;
- customer, supplier, employee, or personal data;
- export-controlled, licensed, or proprietary third-party material without rights;
- confidential conversation history or private prompts without review;
- restricted source evidence to a public mirror.

## Reporting

Report security or confidentiality concerns privately to the HANA-X repository owner. Do not open a public issue containing sensitive details.

## Source integrity

Files under an `Originals/` directory are immutable after intake. Corrections or replacements require a new version and updated manifest, register, and hash records.
