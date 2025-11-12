#!/usr/bin/env python3
"""
Generate SVG diagrams programmatically using Python
Model Used: Claude Sonnet 4.5 (claude-sonnet-4-5-20250929)

This script demonstrates how to generate SVG diagrams directly
without external dependencies.
"""

class SVGDiagram:
    """Helper class to build SVG diagrams programmatically"""

    def __init__(self, width=800, height=600, title="Architecture Diagram"):
        self.width = width
        self.height = height
        self.title = title
        self.elements = []
        self.styles = []
        self.markers = []

    def add_style(self, selector, properties):
        """Add a CSS style"""
        props = "; ".join([f"{k}: {v}" for k, v in properties.items()])
        self.styles.append(f"      .{selector} {{ {props}; }}")

    def add_arrow_marker(self, marker_id="arrowhead", color="#333"):
        """Add an arrow marker definition"""
        marker = f'''    <marker id="{marker_id}" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="{color}" />
    </marker>'''
        self.markers.append(marker)

    def add_rect(self, x, y, width, height, text, css_class="box", rx=5):
        """Add a rectangle with text"""
        rect = f'  <rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{rx}" class="{css_class}"/>'
        text_elem = f'  <text x="{x + width/2}" y="{y + height/2 + 5}" class="text">{text}</text>'
        self.elements.append(rect)
        self.elements.append(text_elem)

    def add_ellipse(self, cx, cy, rx, ry, text, css_class="db"):
        """Add an ellipse with text (for databases)"""
        ellipse = f'  <ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" class="{css_class}"/>'
        text_elem = f'  <text x="{cx}" y="{cy + 5}" class="text">{text}</text>'
        self.elements.append(ellipse)
        self.elements.append(text_elem)

    def add_arrow(self, x1, y1, x2, y2, css_class="arrow"):
        """Add an arrow line"""
        arrow = f'  <path d="M {x1} {y1} L {x2} {y2}" class="{css_class}"/>'
        self.elements.append(arrow)

    def add_text(self, x, y, text, css_class="text", font_size=None):
        """Add text element"""
        size_attr = f' font-size="{font_size}"' if font_size else ''
        text_elem = f'  <text x="{x}" y="{y}" class="{css_class}"{size_attr}>{text}</text>'
        self.elements.append(text_elem)

    def generate(self):
        """Generate the complete SVG"""
        svg = [f'<?xml version="1.0" encoding="UTF-8"?>']
        svg.append(f'<!-- {self.title} -->')
        svg.append(f'<!-- Model Used: Claude Sonnet 4.5 (claude-sonnet-4-5-20250929) -->')
        svg.append(f'<svg width="{self.width}" height="{self.height}" xmlns="http://www.w3.org/2000/svg">')

        # Add defs (styles and markers)
        if self.styles or self.markers:
            svg.append('  <defs>')

            if self.styles:
                svg.append('    <style>')
                svg.extend(self.styles)
                svg.append('    </style>')

            if self.markers:
                svg.extend(self.markers)

            svg.append('  </defs>')

        # Add title
        svg.append('')
        svg.append('  <!-- Title -->')
        svg.append(f'  <text x="{self.width/2}" y="30" class="text" font-size="18" font-weight="bold" text-anchor="middle">{self.title}</text>')
        svg.append('')

        # Add all elements
        svg.extend(self.elements)

        svg.append('</svg>')
        return '\n'.join(svg)


def generate_simple_svg():
    """Generate a simple three-tier architecture SVG"""
    diagram = SVGDiagram(width=600, height=400, title="Basic Three-Tier Web Application")

    # Add styles
    diagram.add_style("box", {
        "fill": "#e1f5ff",
        "stroke": "#0277bd",
        "stroke-width": "2"
    })
    diagram.add_style("server", {
        "fill": "#fff4e1",
        "stroke": "#f57c00",
        "stroke-width": "2"
    })
    diagram.add_style("db", {
        "fill": "#ffe1f5",
        "stroke": "#c2185b",
        "stroke-width": "2"
    })
    diagram.add_style("text", {
        "font-family": "Arial, sans-serif",
        "font-size": "14px",
        "text-anchor": "middle"
    })
    diagram.add_style("arrow", {
        "stroke": "#333",
        "stroke-width": "2",
        "fill": "none",
        "marker-end": "url(#arrowhead)"
    })

    # Add arrow marker
    diagram.add_arrow_marker()

    # Add components
    diagram.add_rect(225, 80, 150, 60, "User Browser", "box")
    diagram.add_rect(225, 200, 150, 60, "Web Server", "server")
    diagram.add_rect(225, 320, 150, 60, "Database", "db")

    # Add arrows
    diagram.add_arrow(300, 140, 300, 200)
    diagram.add_arrow(300, 260, 300, 320)

    return diagram.generate()


def generate_microservices_svg():
    """Generate a microservices architecture SVG"""
    diagram = SVGDiagram(width=1000, height=600, title="Microservices E-Commerce Platform")

    # Add styles
    diagram.add_style("client", {"fill": "#e3f2fd", "stroke": "#1976d2", "stroke-width": "2"})
    diagram.add_style("api", {"fill": "#fff3e0", "stroke": "#f57c00", "stroke-width": "2"})
    diagram.add_style("service", {"fill": "#f3e5f5", "stroke": "#7b1fa2", "stroke-width": "2"})
    diagram.add_style("db", {"fill": "#c8e6c9", "stroke": "#388e3c", "stroke-width": "2"})
    diagram.add_style("text", {
        "font-family": "Arial, sans-serif",
        "font-size": "12px",
        "text-anchor": "middle"
    })
    diagram.add_style("arrow", {
        "stroke": "#333",
        "stroke-width": "2",
        "fill": "none",
        "marker-end": "url(#arrowhead)"
    })

    diagram.add_arrow_marker()

    # Client layer
    diagram.add_rect(50, 80, 120, 50, "Web App", "client")
    diagram.add_rect(190, 80, 120, 50, "Mobile App", "client")

    # API layer
    diagram.add_rect(420, 80, 160, 50, "API Gateway", "api")
    diagram.add_rect(420, 160, 160, 50, "Load Balancer", "api")

    # Service layer
    diagram.add_rect(200, 280, 120, 50, "User Service", "service")
    diagram.add_rect(340, 280, 120, 50, "Product Service", "service")
    diagram.add_rect(480, 280, 120, 50, "Order Service", "service")
    diagram.add_rect(620, 280, 120, 50, "Payment Service", "service")

    # Data layer
    diagram.add_ellipse(260, 420, 70, 30, "User DB", "db")
    diagram.add_ellipse(400, 420, 70, 30, "Product DB", "db")
    diagram.add_ellipse(540, 420, 70, 30, "Order DB", "db")

    # Add connections
    diagram.add_arrow(170, 105, 420, 105)
    diagram.add_arrow(500, 130, 500, 160)
    diagram.add_arrow(460, 210, 260, 280)
    diagram.add_arrow(500, 210, 400, 280)
    diagram.add_arrow(260, 330, 260, 390)
    diagram.add_arrow(400, 330, 400, 390)
    diagram.add_arrow(540, 330, 540, 390)

    return diagram.generate()


def save_svg(svg_content, filename):
    """Save SVG content to a file"""
    with open(filename, 'w') as f:
        f.write(svg_content)
    print(f"SVG saved to {filename}")


def main():
    """Main function to demonstrate SVG generation"""

    # Generate simple SVG
    print("Generating simple SVG diagram...")
    simple = generate_simple_svg()
    print("Simple SVG generated successfully")
    print(f"Size: {len(simple)} characters\n")

    # Generate microservices SVG
    print("Generating microservices SVG diagram...")
    microservices = generate_microservices_svg()
    print("Microservices SVG generated successfully")
    print(f"Size: {len(microservices)} characters\n")

    # Optionally save to files
    # save_svg(simple, "simple_architecture.svg")
    # save_svg(microservices, "microservices_architecture.svg")

    # Print a sample
    print("Sample SVG output (first 500 characters):")
    print(simple[:500] + "...")


if __name__ == "__main__":
    main()
