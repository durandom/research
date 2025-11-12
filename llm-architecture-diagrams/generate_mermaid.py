#!/usr/bin/env python3
"""
Generate Mermaid diagrams programmatically using Python
Model Used: Claude Sonnet 4.5 (claude-sonnet-4-5-20250929)

This script demonstrates how to generate Mermaid diagram syntax
that can be rendered by Mermaid.js or saved to markdown files.
"""

def generate_simple_mermaid():
    """Generate a simple three-tier architecture diagram"""
    diagram = """```mermaid
graph TD
    A[User Browser] --> B[Web Server]
    B --> C[Database]

    style A fill:#e1f5ff
    style B fill:#fff4e1
    style C fill:#ffe1f5
```"""
    return diagram


def generate_microservices_mermaid():
    """Generate a medium complexity microservices diagram"""
    diagram = """```mermaid
graph TB
    subgraph "Client Layer"
        A[Web App]
        B[Mobile App]
    end

    subgraph "API Layer"
        C[API Gateway]
        D[Load Balancer]
    end

    subgraph "Service Layer"
        E[User Service]
        F[Product Service]
        G[Order Service]
        H[Payment Service]
    end

    subgraph "Data Layer"
        I[(User DB)]
        J[(Product DB)]
        K[(Order DB)]
    end

    subgraph "Infrastructure"
        L[Message Queue]
        M[Cache Redis]
    end

    A --> C
    B --> C
    C --> D
    D --> E
    D --> F
    D --> G
    D --> H

    E --> I
    F --> J
    G --> K
    H --> L
    G --> L

    E --> M
    F --> M

    style A fill:#e3f2fd
    style B fill:#e3f2fd
    style C fill:#fff3e0
    style D fill:#fff3e0
    style E fill:#f3e5f5
    style F fill:#f3e5f5
    style G fill:#f3e5f5
    style H fill:#f3e5f5
    style L fill:#e8f5e9
    style M fill:#e8f5e9
```"""
    return diagram


def generate_custom_diagram(nodes, edges, title="Custom Architecture"):
    """
    Generate a custom Mermaid diagram from nodes and edges

    Args:
        nodes: List of tuples (id, label, color)
        edges: List of tuples (from_id, to_id, label)
        title: Diagram title

    Returns:
        Mermaid diagram string
    """
    lines = ["```mermaid", "graph TB"]

    # Add title as a comment
    lines.append(f"    %% {title}")
    lines.append("")

    # Add edges
    for from_id, to_id, label in edges:
        if label:
            lines.append(f"    {from_id}[{label}] --> {to_id}")
        else:
            lines.append(f"    {from_id} --> {to_id}")

    lines.append("")

    # Add styling
    for node_id, label, color in nodes:
        if color:
            lines.append(f"    style {node_id} fill:{color}")

    lines.append("```")
    return "\n".join(lines)


def save_diagram_to_file(diagram, filename):
    """Save a Mermaid diagram to a markdown file"""
    with open(filename, 'w') as f:
        f.write(f"# Architecture Diagram\n\n")
        f.write(f"Generated with Python\n\n")
        f.write(diagram)
    print(f"Diagram saved to {filename}")


def main():
    """Main function to demonstrate diagram generation"""

    # Generate simple diagram
    simple = generate_simple_mermaid()
    print("Simple Diagram:")
    print(simple)
    print("\n" + "="*50 + "\n")

    # Generate microservices diagram
    microservices = generate_microservices_mermaid()
    print("Microservices Diagram:")
    print(microservices)
    print("\n" + "="*50 + "\n")

    # Generate custom diagram
    nodes = [
        ("A", "Frontend", "#e1f5ff"),
        ("B", "Backend API", "#fff4e1"),
        ("C", "Database", "#ffe1f5"),
        ("D", "Cache", "#e8f5e9"),
    ]

    edges = [
        ("A", "B", "Frontend"),
        ("B", "C", "Backend API"),
        ("B", "D", ""),
    ]

    custom = generate_custom_diagram(nodes, edges, "Custom Web Application")
    print("Custom Diagram:")
    print(custom)

    # Optionally save to files
    # save_diagram_to_file(simple, "simple_diagram.md")
    # save_diagram_to_file(microservices, "microservices_diagram.md")


if __name__ == "__main__":
    main()
