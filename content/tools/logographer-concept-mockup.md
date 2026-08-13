# Logographer Concept Mockup

## Intent
Reduce distress from agent-generated writing by learning and enforcing your personal readability preferences.

## Interaction flow
```mermaid
sequenceDiagram
    participant U as You
    participant A as AI Assistant
    participant L as Logographer
    U->>A: Request draft
    A-->>L: Raw draft
    L->>L: Apply personal style profile
    L-->>U: Refined draft + change rationale
    U->>L: Feedback (accept/reject notes)
    L->>L: Update preference profile
```

## MVP panels (UI mockup outline)
1. Preference profile summary
2. Raw vs refined side-by-side
3. Rule activations with confidence
4. Quick feedback controls
5. Export refined text

## Quality targets
- lower rejection rate over time
- reduced reading friction
- stable voice and structure consistency
