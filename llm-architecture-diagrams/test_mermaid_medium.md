# Medium Complexity - Microservices E-Commerce Platform

**Model Used:** Claude Sonnet 4.5 (claude-sonnet-4-5-20250929)

**Description:** A microservices-based e-commerce platform with API gateway, multiple services, and message queue

## Mermaid Diagram

```mermaid
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
```

## Explanation
- Multiple client types (web and mobile)
- API Gateway pattern with load balancing
- Four microservices: User, Product, Order, Payment
- Each service has its own database (database per service pattern)
- Message queue for asynchronous communication
- Redis cache for performance optimization
