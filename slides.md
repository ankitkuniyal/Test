---
marp: true
theme: corp-theme
paginate: true
footer: "Product Docs · Page $[page] / $[total]"
math: mathjax
---

<style>
/* ---------------------------------------
 * Custom Marp Theme: corp-theme
 * ------------------------------------- */
/* @theme corp-theme */

section {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI",
    sans-serif;
  color: #0f172a;
  background-color: #f9fafb;
}

section.lead h1 {
  font-size: 2.8rem;
  font-weight: 800;
  color: #0b1120;
}

section h2 {
  color: #111827;
}

section p,
section li {
  font-size: 1rem;
}

/* Accent elements */
.accent {
  color: #2563eb;
  font-weight: 600;
}

/* Code styling */
pre code {
  font-size: 0.85rem;
  line-height: 1.4;
  border-radius: 0.5rem;
}

/* Table styling */
table {
  border-collapse: collapse;
  width: 100%;
}

th,
td {
  border: 1px solid #e5e7eb;
  padding: 0.4rem 0.6rem;
}

th {
  background-color: #e5e7eb;
}

/* Footer styling for page numbers */
footer {
  color: #6b7280;
  font-size: 0.7rem;
}
</style>

---

<!-- _class: lead -->

# Product Documentation:  
Interactive Developer Platform

**Technical Writer – Software Division**

Contact: **23f2004089@ds.study.iitm.ac.in**

---

## Goals of This Documentation

- Provide clear onboarding for new developers  
- Make documentation **version-controlled**, reviewable, and testable  
- Ensure easy export to:
  - HTML slides
  - PDF manuals
  - Static website documentation

> Maintained as a single `slides.md` file in Git, rendered with **Marp**.

---

## Architecture Overview

- Monolithic core refactored into **microservices**
- Public API gateway for external integrations
- Internal services:
  - Authentication & Authorization
  - Billing & Usage Tracking
  - Analytics & Reporting

```mermaid
flowchart LR
    client[Client Apps] --> gateway[API Gateway]
    gateway --> auth[Auth Service]
    gateway --> billing[Billing Service]
    gateway --> analytics[Analytics Service]
