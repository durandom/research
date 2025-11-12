# Research Notes: LLM-Based Architecture Diagram Generation

## Investigation Started
Date: 2025-11-12
Model: Claude Sonnet 4.5 (claude-sonnet-4-5-20250929)

## Goal
Research and test various approaches for generating architecture diagrams using LLMs:
- Text-based diagram formats (Mermaid.js, PlantUML, Graphviz)
- Direct SVG generation
- Python libraries that facilitate this
- Compare complexity levels and quality

## Research Log

### Initial Research - Existing Tools

Found several key Python libraries and diagram-as-code tools:

1. **Diagrams** (Python package)
   - Built on top of Graphviz
   - Supports AWS, Azure, GCP, and other cloud providers
   - Generates high-quality PNG/SVG images
   - Uses Python code to define diagrams

2. **Mermaid.js**
   - JavaScript library with markdown-like syntax
   - Supports flowcharts, sequence diagrams, Gantt charts, class diagrams
   - Can be generated as text and rendered in browsers or via CLI
   - Growing popularity (company raised capital in 2024)

3. **PlantUML**
   - Versatile, simple language for various diagram types
   - Well-established tool

4. **Graphviz**
   - Uses DOT language
   - Good for complex network diagrams and hierarchical layouts

5. **Kroki**
   - Unified API supporting multiple diagram formats
   - Can act as a service to render many diagram types

### Testing Approach
Will test:
1. Mermaid.js generation (text-based)
2. Direct SVG generation
3. Python Diagrams library if time permits

### Mermaid.js Testing Results

Created three complexity levels of architecture diagrams:

1. **Simple** (test_mermaid_simple.md)
   - Basic three-tier web application
   - 3 nodes, 2 connections
   - Clear and easy to understand

2. **Medium** (test_mermaid_medium.md)
   - Microservices e-commerce platform
   - ~13 nodes organized in 5 subgraphs
   - Shows API gateway pattern, multiple services, message queue, caching

3. **Complex** (test_mermaid_complex.md)
   - Cloud-native multi-region platform
   - ~40+ nodes organized in 7 subgraphs
   - Includes: multi-region deployment, event-driven architecture, observability, security, CI/CD
   - Shows cross-region replication with dotted lines

**Observations:**
- Mermaid syntax is intuitive and readable
- Subgraphs help organize complex diagrams
- Styling (colors) can be applied inline
- Good for both simple and complex architectures
- Text-based format is easy to version control
- Can be rendered in many tools (GitHub, GitLab, VS Code, web browsers)

### Direct SVG Generation Testing Results

Created three SVG files with increasing complexity:

1. **Simple** (test_svg_simple.svg)
   - Basic three-tier web application
   - Hand-coded SVG with boxes and arrows
   - ~70 lines of SVG code
   - Clean, precise positioning

2. **Medium** (test_svg_medium.svg)
   - Microservices e-commerce platform
   - Multiple layers with different colors
   - ~150 lines of SVG code
   - More complex positioning and connections

3. **Complex** (test_svg_complex.svg)
   - Multi-region cloud platform
   - 40+ components with regions, dashed lines for replication
   - ~350 lines of SVG code
   - Includes legend, grouped sections

**Observations:**
- LLM can generate valid, well-structured SVG
- Manual positioning required (x, y coordinates)
- More verbose than Mermaid
- Full control over styling and layout
- No external dependencies - pure SVG
- Can be embedded directly in HTML
- Harder to maintain and modify than text-based formats
- Better for static, pixel-perfect diagrams
- Difficult for very complex diagrams (coordinate management becomes challenging)

### Python Code Generation Testing Results

Created three Python scripts to demonstrate programmatic diagram generation:

1. **generate_mermaid.py**
   - Generates Mermaid diagrams as text strings
   - Simple, medium, and custom diagram examples
   - Easy to integrate into documentation pipelines
   - No external dependencies for generation
   - Output can be embedded in markdown files

2. **generate_svg.py**
   - Generates SVG directly using Python
   - Helper class `SVGDiagram` for building diagrams
   - Methods for rectangles, ellipses, arrows, text
   - No external dependencies
   - Full control over layout and styling
   - More complex than Mermaid generation

3. **generate_graphviz.py**
   - Generates Graphviz DOT format
   - Supports clusters (subgraphs) for organization
   - Can be rendered with graphviz library (optional)
   - Clean, declarative syntax
   - Good for automatic layout

**Observations:**
- All scripts executed successfully
- Mermaid generation is simplest and most readable
- SVG generation gives most control but requires coordinate management
- Graphviz DOT is good middle ground with automatic layout
- LLM can generate all formats effectively
- Python integration enables automation and dynamic generation
