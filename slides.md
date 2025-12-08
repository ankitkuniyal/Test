---
marp: true
theme: corp-theme
paginate: true
footer: "Product Documentation · Page $[page] / $[total]"
math: mathjax
---

<style>
/* ---------------------------------------
 * Custom Marp Theme: corp-theme
 * ------------------------------------- */
/* @theme corp-theme */

section {
  font-family: "Segoe UI", Arial, sans-serif;
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
  font-size: 0.9rem;
  border-radius: 8px;
  padding: 10px;
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
Email: **23f2004089@ds.study.iitm.ac.in**

---

# Overview

- Version-controlled documentation  
- Compatible with CI/CD pipelines  
- Export to **HTML, PDF, PPTX**  
- Uses **Marp Markdown** for maintainability  

---

# Architecture Summary

- Microservice-based backend  
- REST + GraphQL API layer  
- Authentication, Billing, Analytics modules  

---

# Mathematical Equation

Algorithmic Time Complexity:

\[
T(n) = O(n \log n)
\]

Space Complexity:

\[
S(n) = O(1)
\]

---

# Code Example (JS SDK)

```js
import { Client } from "@company/sdk";

const client = new Client({ key: process.env.API_KEY });

async function run() {
  const usage = await client.usage.get();
  console.log("Usage:", usage);
}

run();
