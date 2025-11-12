#!/usr/bin/env python3
"""
Generate Graphviz DOT diagrams programmatically using Python
Model Used: Claude Sonnet 4.5 (claude-sonnet-4-5-20250929)

This script demonstrates how to generate Graphviz DOT language diagrams.
Note: Requires graphviz to be installed to render (not required to generate the DOT code)

Installation: pip install graphviz
System dependency: apt-get install graphviz (Linux) or brew install graphviz (Mac)
"""

def generate_simple_graphviz():
    """Generate a simple three-tier architecture in DOT format"""
    dot = '''digraph G {
    rankdir=TB;
    node [shape=box, style=filled];

    // Title
    labelloc="t";
    label="Basic Three-Tier Web Application";

    // Nodes
    browser [label="User Browser", fillcolor="#e1f5ff"];
    webserver [label="Web Server", fillcolor="#fff4e1"];
    database [label="Database", fillcolor="#ffe1f5", shape=cylinder];

    // Edges
    browser -> webserver;
    webserver -> database;
}'''
    return dot


def generate_microservices_graphviz():
    """Generate a microservices architecture in DOT format"""
    dot = '''digraph G {
    rankdir=TB;
    node [shape=box, style=filled];
    compound=true;

    labelloc="t";
    label="Microservices E-Commerce Platform";

    // Client Layer
    subgraph cluster_0 {
        label="Client Layer";
        style=filled;
        color=lightgrey;

        webapp [label="Web App", fillcolor="#e3f2fd"];
        mobile [label="Mobile App", fillcolor="#e3f2fd"];
    }

    // API Layer
    subgraph cluster_1 {
        label="API Layer";
        style=filled;
        color=lightgrey;

        gateway [label="API Gateway", fillcolor="#fff3e0"];
        lb [label="Load Balancer", fillcolor="#fff3e0"];

        gateway -> lb;
    }

    // Service Layer
    subgraph cluster_2 {
        label="Service Layer";
        style=filled;
        color=lightgrey;

        user_svc [label="User Service", fillcolor="#f3e5f5"];
        product_svc [label="Product Service", fillcolor="#f3e5f5"];
        order_svc [label="Order Service", fillcolor="#f3e5f5"];
        payment_svc [label="Payment Service", fillcolor="#f3e5f5"];
    }

    // Data Layer
    subgraph cluster_3 {
        label="Data Layer";
        style=filled;
        color=lightgrey;

        user_db [label="User DB", fillcolor="#c8e6c9", shape=cylinder];
        product_db [label="Product DB", fillcolor="#c8e6c9", shape=cylinder];
        order_db [label="Order DB", fillcolor="#c8e6c9", shape=cylinder];
    }

    // Infrastructure
    subgraph cluster_4 {
        label="Infrastructure";
        style=filled;
        color=lightgrey;

        mq [label="Message Queue", fillcolor="#e8f5e9"];
        cache [label="Redis Cache", fillcolor="#e8f5e9"];
    }

    // Connections between layers
    webapp -> gateway;
    mobile -> gateway;

    lb -> user_svc;
    lb -> product_svc;
    lb -> order_svc;
    lb -> payment_svc;

    user_svc -> user_db;
    product_svc -> product_db;
    order_svc -> order_db;

    payment_svc -> mq;
    order_svc -> mq;

    user_svc -> cache;
    product_svc -> cache;
}'''
    return dot


def generate_custom_graphviz(nodes, edges, clusters=None, title="Custom Architecture"):
    """
    Generate a custom Graphviz diagram

    Args:
        nodes: List of dicts with keys: id, label, color, shape
        edges: List of tuples (from_id, to_id)
        clusters: Optional list of dicts with keys: name, node_ids, label
        title: Diagram title

    Returns:
        DOT format string
    """
    lines = ["digraph G {"]
    lines.append("    rankdir=TB;")
    lines.append('    node [shape=box, style=filled];')
    lines.append("")
    lines.append(f'    labelloc="t";')
    lines.append(f'    label="{title}";')
    lines.append("")

    # Add clusters if provided
    if clusters:
        for i, cluster in enumerate(clusters):
            lines.append(f"    subgraph cluster_{i} {{")
            lines.append(f'        label="{cluster["label"]}";')
            lines.append('        style=filled;')
            lines.append('        color=lightgrey;')
            lines.append("")

            # Add nodes in this cluster
            for node in nodes:
                if node['id'] in cluster['node_ids']:
                    shape = node.get('shape', 'box')
                    color = node.get('color', '#ffffff')
                    lines.append(f'        {node["id"]} [label="{node["label"]}", fillcolor="{color}", shape={shape}];')

            lines.append("    }")
            lines.append("")
    else:
        # Add nodes without clusters
        for node in nodes:
            shape = node.get('shape', 'box')
            color = node.get('color', '#ffffff')
            lines.append(f'    {node["id"]} [label="{node["label"]}", fillcolor="{color}", shape={shape}];')
        lines.append("")

    # Add edges
    for from_id, to_id in edges:
        lines.append(f"    {from_id} -> {to_id};")

    lines.append("}")
    return "\n".join(lines)


def save_dot(dot_content, filename):
    """Save DOT content to a file"""
    with open(filename, 'w') as f:
        f.write(dot_content)
    print(f"DOT file saved to {filename}")


def render_graphviz(dot_content, output_file, format='png'):
    """
    Render Graphviz diagram to an image file
    Requires: pip install graphviz
    """
    try:
        import graphviz

        # Create a Source object
        src = graphviz.Source(dot_content)

        # Render to file
        src.render(output_file, format=format, cleanup=True)
        print(f"Rendered diagram to {output_file}.{format}")

    except ImportError:
        print("graphviz package not installed. Install with: pip install graphviz")
        print("Also requires system graphviz: apt-get install graphviz (or brew install graphviz)")


def main():
    """Main function to demonstrate Graphviz generation"""

    # Generate simple diagram
    simple = generate_simple_graphviz()
    print("Simple Graphviz DOT diagram:")
    print(simple)
    print("\n" + "="*50 + "\n")

    # Generate microservices diagram
    microservices = generate_microservices_graphviz()
    print("Microservices Graphviz DOT diagram:")
    print(microservices)
    print("\n" + "="*50 + "\n")

    # Generate custom diagram
    nodes = [
        {"id": "frontend", "label": "Frontend", "color": "#e1f5ff"},
        {"id": "backend", "label": "Backend API", "color": "#fff4e1"},
        {"id": "db", "label": "Database", "color": "#ffe1f5", "shape": "cylinder"},
        {"id": "cache", "label": "Cache", "color": "#e8f5e9"},
    ]

    edges = [
        ("frontend", "backend"),
        ("backend", "db"),
        ("backend", "cache"),
    ]

    custom = generate_custom_graphviz(nodes, edges, title="Custom Web Application")
    print("Custom Graphviz DOT diagram:")
    print(custom)

    # Optionally save to files
    # save_dot(simple, "simple_diagram.dot")
    # save_dot(microservices, "microservices_diagram.dot")

    # Optionally render (requires graphviz package)
    # render_graphviz(simple, "simple_diagram", format='png')


if __name__ == "__main__":
    main()
