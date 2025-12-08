---
marp: true
theme: corp-theme
paginate: true
footer: "Product Docs · Page $[page] / $[total]"
math: mathjax
---

<style>
/* ================================
   Custom Marp Theme: corp-theme
   ================================ */
/* @theme corp-theme */

section {
  font-family: "Segoe UI", sans-serif;
  background-color: #f8fafc;
  color: #0f172a;
  padding: 2rem;
}

h1, h2 {
  color: #0f172a;
}

.accent {
  color: #2563eb;
  font-weight: bold;
}

pre code {
  font-size: 0.85rem;
  border-radius: 8px;
  padding: 10px;
  background: #0f172a;
  color: #f8fafc;
}

footer {
  color: #6b7280;
  font-size: 0.7rem;
}
</style>

---

<!-- _class: lead -->

# Product Documentation Presentation  
### Software Engineering Division  

Contact: **23f2004089@ds.study.iitm.ac.in**

---

## Documentation Goals

- Version-controlled **Markdown** source  
- Exportable to **PDF, HTML, PPTX**  
- Developer-friendly contribution workflow  
- Easy CI/CD integration

---

## System Architecture

- Distributed microservices  
- Central API Gateway  
- Auth, Billing, Monitoring services  
- Versioned public SDKs

---

## Algorithmic Complexity Example

We highlight algorithmic complexity for core data-processing steps.

Time Complexity:

\[
T(n) = O(n \log n)
\]

Space Complexity:

\[
S(n) = O(1)
\]

---

## Example API Usage

```js
import { Client } from "@company/sdk";

const client = new Client({
  apiKey: process.env.DOCS_API_KEY
});

async function load() {
  const data = await client.usage.summary();
  console.log("Usage:", data);
}

load();
