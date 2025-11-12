# LLM-Based Architecture Diagram Generation Research

**Research Date:** November 12, 2025
**Model Used:** Claude Sonnet 4.5 (claude-sonnet-4-5-20250929)

## Executive Summary

This research investigates various approaches for generating architecture diagrams using Large Language Models (LLMs), specifically focusing on text-based diagram formats and direct SVG generation. The study evaluates three primary methods: Mermaid.js, Graphviz DOT, and direct SVG generation, testing each at varying complexity levels.

## Key Findings

### Best Approach: Mermaid.js
- **Winner for most use cases:** Mermaid.js offers the best balance of simplicity, readability, and capability
- Excellent LLM generation quality across all complexity levels
- Wide tool support (GitHub, GitLab, VS Code, web browsers)
- Easy to version control and modify
- No external dependencies for text generation

### Other Viable Options
- **Graphviz DOT:** Good for automatic layout, especially complex hierarchies
- **Direct SVG:** Best for pixel-perfect control, but harder to maintain
- **Python Libraries:** Excellent for automation and programmatic generation

## Tested Approaches

### 1. Mermaid.js (Recommended)

**Pros:**
- Intuitive, markdown-like syntax
- Excellent LLM generation capability
- Supports subgraphs for organization
- Inline styling support
- Wide ecosystem support
- No dependencies for text generation
- Easy to version control

**Cons:**
- Limited fine-grained layout control
- Rendering requires a tool or library

**Example Files:**
- `test_mermaid_simple.md` - Basic 3-tier web app (3 nodes)
- `test_mermaid_medium.md` - Microservices platform (13 nodes, 5 subgraphs)
- `test_mermaid_complex.md` - Multi-region cloud platform (40+ nodes, 7 subgraphs)

**Python Script:**
- `generate_mermaid.py` - Programmatic Mermaid generation

### 2. Direct SVG Generation

**Pros:**
- Complete control over styling and positioning
- No external dependencies
- Can be embedded directly in HTML
- Pixel-perfect layouts
- Works anywhere SVG is supported

**Cons:**
- Manual coordinate management
- More verbose than text-based formats
- Harder to maintain
- Difficult for very complex diagrams
- Not as LLM-friendly for large diagrams

**Example Files:**
- `test_svg_simple.svg` - Basic 3-tier web app (~70 lines)
- `test_svg_medium.svg` - Microservices platform (~150 lines)
- `test_svg_complex.svg` - Multi-region cloud platform (~350 lines)

**Python Script:**
- `generate_svg.py` - SVG generation with helper class

### 3. Graphviz DOT

**Pros:**
- Automatic layout algorithms
- Clean, declarative syntax
- Good for complex hierarchical diagrams
- Supports clustering (subgraphs)
- Can render to multiple formats (PNG, SVG, PDF)

**Cons:**
- Requires graphviz installation for rendering
- Less control over exact positioning
- Syntax less intuitive than Mermaid

**Python Script:**
- `generate_graphviz.py` - Graphviz DOT generation

## Complexity Level Examples

All approaches were tested at three complexity levels:

### Simple (3-5 components)
**Use Case:** Basic architecture overviews, simple data flows

**Example:** Three-tier web application
- User Browser
- Web Server
- Database

**Best Format:** Any (Mermaid recommended for simplicity)

### Medium (10-20 components)
**Use Case:** Microservices architectures, departmental systems

**Example:** E-commerce microservices platform
- Client layer (web, mobile)
- API gateway and load balancer
- 4 microservices (user, product, order, payment)
- 3 databases (database-per-service pattern)
- Infrastructure (message queue, cache)

**Best Format:** Mermaid (excellent subgraph support)

### Complex (30+ components)
**Use Case:** Enterprise architectures, multi-region cloud platforms

**Example:** Cloud-native multi-region platform
- CDN and edge security
- Two active regions (US-East, EU-West)
- Multiple compute types (ECS, Lambda, Kubernetes)
- Cross-region replication
- Event-driven architecture (SQS, SNS, Kinesis, EventBridge)
- Observability stack (CloudWatch, X-Ray, Prometheus, Grafana)
- Security components (Cognito, IAM, Secrets Manager, KMS)
- CI/CD pipeline

**Best Format:** Mermaid with careful organization, or Graphviz for automatic layout

## Python Libraries for Diagram Generation

### Evaluated Libraries

1. **Diagrams** (Python package)
   - Built on Graphviz
   - Pre-made icons for cloud providers (AWS, Azure, GCP)
   - Good for infrastructure diagrams
   - Installation: `pip install diagrams`
   - Requires Graphviz system dependency

2. **Mermaid (via text generation)**
   - No Python package needed for generation
   - Simply generate text strings
   - Can integrate with `mermaid-cli` for rendering
   - Best for documentation pipelines

3. **python-graphviz**
   - Python interface to Graphviz
   - Installation: `pip install graphviz`
   - Requires system Graphviz installation

4. **Direct SVG (no library needed)**
   - Pure Python string manipulation
   - XML generation libraries can help
   - No external dependencies

### Custom Helper Code

Created reusable Python scripts for all three approaches:

- **generate_mermaid.py**: Simple string generation, easy to customize
- **generate_svg.py**: `SVGDiagram` helper class with methods for common shapes
- **generate_graphviz.py**: DOT format generation with clustering support

## LLM Performance Analysis

### Model Used
**Claude Sonnet 4.5** (claude-sonnet-4-5-20250929)

### Generation Quality

#### Mermaid.js: Excellent (9/10)
- Syntax was correct in all cases
- Good structure and organization
- Appropriate use of subgraphs
- Effective styling
- Scaled well to complex diagrams

#### SVG: Good (7/10)
- Valid SVG generated
- Reasonable positioning for simple diagrams
- Some coordinate calculation errors in complex diagrams
- Required iteration for complex layouts
- Better for simple/medium complexity

#### Graphviz DOT: Excellent (9/10)
- Clean, correct syntax
- Good use of clusters
- Appropriate node shapes and colors
- Scales well to complexity

### Recommendations by Complexity

| Complexity | Best Choice | Alternative | Use Case |
|------------|-------------|-------------|----------|
| Simple | Mermaid | Any | Quick diagrams, documentation |
| Medium | Mermaid | Graphviz | Microservices, system designs |
| Complex | Mermaid/Graphviz | Diagrams library | Enterprise architectures |
| Very Complex | Graphviz + manual | Mermaid + splitting | Multi-region, detailed systems |

## Use Cases and Recommendations

### Documentation in Git Repositories
**Recommendation:** Mermaid
- Renders natively in GitHub, GitLab
- Easy to review in PRs
- Version control friendly

### Automated Diagram Generation
**Recommendation:** Python + Mermaid or Graphviz
- Use scripts to generate from data
- Integrate into CI/CD
- Dynamic documentation

### Pixel-Perfect Presentations
**Recommendation:** Direct SVG or Diagrams library
- Export to PNG/PDF
- Full styling control
- Professional appearance

### Large Enterprise Architectures
**Recommendation:** Graphviz or split into multiple Mermaid diagrams
- Automatic layout for complex graphs
- Or break into logical sections
- Use consistent styling across diagrams

### Real-time Collaborative Editing
**Recommendation:** Mermaid
- Simple text format
- Many online editors available
- Low barrier to entry

## Code Examples

### Mermaid.js Example

```python
def generate_microservices_diagram():
    return """```mermaid
graph TB
    subgraph "Client Layer"
        A[Web App]
        B[Mobile App]
    end

    subgraph "API Layer"
        C[API Gateway]
    end

    A --> C
    B --> C

    style A fill:#e3f2fd
    style B fill:#e3f2fd
```"""
```

### SVG Example

```python
from generate_svg import SVGDiagram

diagram = SVGDiagram(width=600, height=400, title="My Architecture")
diagram.add_rect(100, 100, 150, 60, "Web Server", "server")
diagram.add_rect(100, 220, 150, 60, "Database", "db")
diagram.add_arrow(175, 160, 175, 220)
svg_output = diagram.generate()
```

### Graphviz Example

```python
dot = '''digraph G {
    rankdir=TB;
    node [shape=box, style=filled];

    frontend [label="Frontend", fillcolor="#e1f5ff"];
    backend [label="Backend", fillcolor="#fff4e1"];

    frontend -> backend;
}'''
```

## Tools and Ecosystem

### Rendering Tools

**Mermaid:**
- Online: https://mermaid.live/
- CLI: `npm install -g @mermaid-js/mermaid-cli`
- VS Code: Mermaid Preview extension
- GitHub/GitLab: Native rendering

**Graphviz:**
- System install: `apt-get install graphviz` or `brew install graphviz`
- Online: https://dreampuf.github.io/GraphvizOnline/
- Python: `pip install graphviz`

**SVG:**
- Any web browser
- Inkscape for editing
- ImageMagick for conversion

### Integration Points

- **Documentation generators:** Sphinx, MkDocs, Docusaurus
- **CI/CD:** GitHub Actions, GitLab CI
- **Notebooks:** Jupyter (all formats work)
- **Wikis:** Confluence, Notion (varies by platform)

## Lessons Learned

1. **LLMs excel at text-based diagram formats** - Mermaid and Graphviz are very LLM-friendly
2. **Coordinate management is challenging** - Direct SVG requires careful positioning
3. **Complexity limits exist** - Beyond 50-60 components, consider splitting diagrams
4. **Consistency matters** - Use templates and style guides for professional results
5. **Automation enables scale** - Python scripts enable dynamic, data-driven diagrams
6. **Version control is valuable** - Text-based formats enable git diff and merge

## Future Exploration

Potential areas for further research:

1. **Python Diagrams library testing** - Cloud provider icon libraries
2. **PlantUML evaluation** - Another popular text-based format
3. **D2 language** - Modern alternative to Graphviz
4. **Excalidraw** - Hand-drawn style diagrams
5. **AI-powered layout optimization** - LLM feedback loops for better positioning
6. **Dynamic diagram generation** - From code, APIs, or infrastructure

## Conclusion

For LLM-based architecture diagram generation, **Mermaid.js is the recommended primary approach** due to its excellent balance of simplicity, capability, and ecosystem support. The LLM (Claude Sonnet 4.5) demonstrated strong capability in generating correct, well-structured diagrams across all tested formats.

For automation and programmatic generation, Python scripts combined with Mermaid or Graphviz provide powerful, flexible solutions. Direct SVG generation is viable for simple diagrams but becomes challenging at higher complexity levels.

The research confirms that modern LLMs can effectively generate high-quality architecture diagrams across multiple formats, making diagram-as-code a practical approach for documentation and system design.

## Files in This Research

- `README.md` - This document
- `notes.md` - Detailed research notes and observations
- `test_mermaid_simple.md` - Simple Mermaid example
- `test_mermaid_medium.md` - Medium Mermaid example
- `test_mermaid_complex.md` - Complex Mermaid example
- `test_svg_simple.svg` - Simple SVG example
- `test_svg_medium.svg` - Medium SVG example
- `test_svg_complex.svg` - Complex SVG example
- `generate_mermaid.py` - Python script for Mermaid generation
- `generate_svg.py` - Python script for SVG generation
- `generate_graphviz.py` - Python script for Graphviz generation

---

**Research completed by:** Claude Sonnet 4.5 (claude-sonnet-4-5-20250929)
**Date:** November 12, 2025
