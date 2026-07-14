# Project ICE Publication Guide

## Official repository

This repository is the authoritative source of truth for the HANA-X Copilot Technical Publication and the founding document set for Project ICE.

The canonical repository must be private whenever restricted source evidence is present. Approved public outputs may be published separately or through a sanitized public mirror.

## Governed master artifacts

- **Master Authoring Guide - ICE-GOV-002**
  - `00_Governance/02_Master_Authoring_Guide/`
- **Source Register**
  - `01_Registers/ICE_Source_Register.csv`
- **Artifact Register**
  - `01_Registers/ICE_Artifact_Register.csv`
- **Original source materials**
  - `02_Source_Materials/`
- **Normalized knowledge and authoring context**
  - `03_Knowledge_Base/`
- **White-paper chapters and front matter**
  - `04_White_Paper/`
- **Architecture specifications**
  - `05_Architecture/`
- **Product and technical requirements**
  - `06_Requirements/`
- **Approved publication deliverables**
  - `11_Deliverables/`
- **Immutable release snapshots**
  - `12_Releases/`

## Authoring lifecycle

Research -> Source validation -> Outline -> Draft -> Editorial review -> Technical architecture review -> SAP integration review -> Source and citation review -> Claims and legal review -> Executive approval -> Publication -> Immutable release

## Repository rules

1. Original evidence is immutable.
2. Every source must have a permanent source ID, manifest, register entry, authority tier, and SHA-256 hash.
3. Every governed artifact must have a permanent artifact ID.
4. Drafts, approved artifacts, published outputs, and releases must remain clearly separated.
5. Published artifacts are never overwritten.
6. Changes to published material require a new version.
7. AI-generated research is exploratory until independently verified.
8. Only approved and traceable claims may appear in published materials, unless a formal risk-acceptance exception is recorded.
9. Publication artifacts use `DRAFT`, `IN-REVIEW`, `APPROVED`, `PUBLISHED`, `SUPERSEDED`, and `WITHDRAWN`. Planning records may use `PLANNED` and `SCAFFOLDED` before drafting begins.
10. Source-intake records use `Proposed`, `Accepted`, `Verified`, `Superseded`, and `Withdrawn`.
11. Do not use `FINAL` as a lifecycle status.

## Project purpose

Project ICE defines Intent-Centric Enterprise Computing and establishes HANA-X Copilot as the Enterprise Intent Layer for SAP S/4HANA.
