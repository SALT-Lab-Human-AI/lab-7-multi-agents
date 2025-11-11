# CrewAI Multi-Agent Workflow - Implementation Guide

## Project Overview

This project implements **Part 2** of the Multi-Agent Systems Lab using **CrewAI** framework. It demonstrates a collaborative multi-agent system for planning a 5-day trip to Iceland.

## What Was Implemented

### 1. Four Specialized Agents

#### FlightAgent (Flight Specialist)
```python
- Role: Flight Specialist
- Goal: Research and recommend best flight options
- Backstory: Experienced flight specialist with airline knowledge
- Tools: search_flights()
- Expected Output: 2-3 flight options with pricing and recommendations
```

#### HotelAgent (Accommodation Specialist)
```python
- Role: Accommodation Specialist
- Goal: Suggest top-rated hotels in Reykjavik
- Backstory: Seasoned accommodation expert
- Tools: search_hotels()
- Expected Output: 3-4 hotel recommendations with amenities and ratings
```

#### ItineraryAgent (Travel Planner)
```python
- Role: Travel Planner
- Goal: Create detailed 5-day travel plan
- Backstory: Creative travel planner passionate about Iceland
- Tools: get_iceland_attractions()
- Expected Output: Day-by-day itinerary with activities and durations
```

#### BudgetAgent (Financial Advisor)
```python
- Role: Financial Advisor
- Goal: Calculate costs and identify savings
- Backstory: Meticulous financial advisor specializing in travel budgeting
- Tools: None (uses AI analysis from other agents' outputs)
- Expected Output: Comprehensive budget breakdown with savings tips
```

### 2. Specialized Tools

```python
@tool
def search_flights(destination: str, dates: str) -> str
    Purpose: Research flight options
    Mock Data: 3 flight options with pricing
    Returns: JSON formatted flight data

@tool
def search_hotels(location: str, check_in: str, nights: int) -> str
    Purpose: Find hotel options
    Mock Data: 4 Icelandic hotels with amenities
    Returns: JSON formatted hotel data

@tool
def get_iceland_attractions(region: str) -> str
    Purpose: Get attractions and activities
    Mock Data: Attractions in Golden Circle, Blue Lagoon, South Coast, North
    Returns: JSON formatted attractions data
```

### 3. Sequential Task Execution

```
Task 1: Flight Research
   ↓ (Output: Flight options)
Task 2: Hotel Selection
   ↓ (Output: Hotel recommendations)
Task 3: Itinerary Planning
   ↓ (Output: Day-by-day plan)
Task 4: Budget Calculation
   ↓ (Output: Cost breakdown)
Final: Comprehensive Travel Plan Report
```

## Project Structure

```
crewAI/
├── crewai_demo.py              # Main implementation (255 lines)
├── requirements.txt             # Dependencies
├── README.md                    # Quick reference guide
├── IMPLEMENTATION_GUIDE.md      # This file
└── crewai_output.txt           # Generated output (after running)
```

## File Breakdown

### crewai_demo.py (255 lines)

**Section 1: Tools Implementation (14-78 lines)**
- `search_flights()` - Mock flight data with 3 options
- `search_hotels()` - Mock hotel data with 4 options
- `get_iceland_attractions()` - Mock attractions data

**Section 2: Agent Definitions (82-123 lines)**
- `create_flight_agent()` - FlightAgent creation
- `create_hotel_agent()` - HotelAgent creation
- `create_itinerary_agent()` - ItineraryAgent creation
- `create_budget_agent()` - BudgetAgent creation

**Section 3: Task Definitions (127-179 lines)**
- `create_flight_task()` - Search flights task
- `create_hotel_task()` - Find hotels task
- `create_itinerary_task()` - Plan itinerary task
- `create_budget_task()` - Calculate budget task

**Section 4: Crew Orchestration (183-255 lines)**
- Agent instantiation
- Task creation
- Crew formation with sequential process
- Execution with input parameters
- Output handling and file saving

## Key Implementation Details

### 1. Agent Structure
Each agent follows the pattern:
```python
Agent(
    role="[Specialized Role]",
    goal="[Specific Goal]",
    backstory="[Detailed Context]",
    tools=[tool1, tool2, ...],
    verbose=True  # For debugging
)
```

### 2. Task Definition
Each task includes:
```python
Task(
    description="[Detailed task description]",
    agent=specific_agent,
    expected_output="[What the agent should produce]"
)
```

### 3. Crew Configuration
```python
Crew(
    agents=[agent1, agent2, agent3, agent4],
    tasks=[task1, task2, task3, task4],
    verbose=True,
    process="sequential"  # Sequential execution ensures order
)
```

### 4. Execution
```python
result = crew.kickoff(inputs={
    "trip_destination": "Iceland",
    "trip_duration": "5 days",
    "trip_dates": "January 15-20, 2025"
})
```

## CrewAI Concepts Demonstrated

### 1. Agent Autonomy
- Agents are autonomous in their decision-making
- Each agent analyzes its task independently
- Agents use tools to gather information

### 2. Sequential Workflow
- Tasks execute in defined order
- Information flows from one agent to next
- Each agent sees context from previous agents

### 3. Tool Integration
- Tools are Python functions decorated with `@tool`
- Can be mock implementations or real APIs
- Agents access tools to gather data

### 4. Output Aggregation
- Task outputs automatically passed to next agent
- Crew manages information flow
- Final result aggregates all outputs

## How to Use This Implementation

### Step 1: Installation
```bash
cd /Users/pranavhharish/Desktop/IS-492/multi-agent/crewAI
pip install -r requirements.txt
```

### Step 2: Set Environment Variable
```bash
export OPENAI_API_KEY="sk-proj-xxxxx"  # Your actual API key
```

### Step 3: Run the Demo
```bash
python crewai_demo.py
```

### Step 4: Review Output
```bash
cat crewai_output.txt
```

## What Makes CrewAI Effective

1. **Clear Agent Roles** - Each agent knows its expertise and responsibility
2. **Structured Tasks** - Tasks are explicit with clear inputs and outputs
3. **Sequential Flow** - Information naturally flows from one agent to next
4. **Tool Integration** - Agents can access specialized tools
5. **Autonomous Operation** - Agents make decisions based on available information

## Comparison with Requirements

✅ Created four specialized agents (Flight, Hotel, Itinerary, Budget)
✅ Each agent has specific role, goal, and backstory
✅ Implemented sequential task execution
✅ Created specialized tools for research
✅ Integrated tool outputs into agent workflows
✅ Crew orchestration with automatic task sequencing
✅ Generates comprehensive travel plan output
✅ Includes expected output structure (flights, hotels, itinerary, budget)

## Expected Output Format

When executed successfully, the demo generates:

```
FLIGHT OPTIONS
- Option 1: Icelandair, Jan 15-16, 6h 30m, $450
- Option 2: United Airlines, Jan 15-16, 7h 15m, $520
- Option 3: Lufthansa, Jan 15-17, 8h 45m, $380
Recommendation: Icelandair offers best balance

HOTEL RECOMMENDATIONS
- ION Adventure Hotel: 4.8★, $320/night, Luxury with Spa
- Golden Circle Hotel: 4.5★, $210/night, Mountain Views
- Reykjavik Dlux Hotel: 4.2★, $150/night, City Center
- Holt Reykjavik Hotel: 4.7★, $280/night, Art Gallery

5-DAY ITINERARY
Day 1: Arrival, Blue Lagoon
Day 2: Golden Circle Tour
Day 3: South Coast Waterfalls
Day 4: Free day or North Iceland (optional)
Day 5: Departure

BUDGET REPORT
Budget Option: $2,200 (flights + budget hotel + activities)
Mid-Range: $3,100 (flights + mid-range hotel + tours)
Luxury: $4,500+ (premium flights + luxury hotel + exclusive tours)
Savings Tips: Book 2+ weeks in advance, visit free attractions
```

## Architecture Advantages

### Modularity
- Easy to add/remove agents
- Agents can be tested independently
- Tools can be swapped for real implementations

### Maintainability
- Clear agent responsibilities
- Explicit task definitions
- Well-documented code structure

### Extensibility
- New tools can be added easily
- Agent roles can be extended
- Process can be changed (sequential → parallel)

### Scalability
- Framework handles agent coordination
- Information flow is automatic
- Can handle complex multi-step workflows

## Potential Enhancements

1. **Real API Integration**
   - Replace mock search_flights() with Skyscanner API
   - Replace search_hotels() with Booking.com API
   - Use real attraction data from travel APIs

2. **Parallel Execution**
   ```python
   process="hierarchical"  # Or parallel for independent tasks
   ```

3. **Error Handling**
   - Retry logic for failed tasks
   - Fallback strategies
   - Validation of outputs

4. **Feedback Loops**
   - Human review between agents
   - Agent refinement of outputs
   - Dynamic task adjustments

5. **Additional Agents**
   - WeatherAgent - Weather forecasting
   - TransportationAgent - Car rental planning
   - ActivityAgent - Event recommendations

## Learning Outcomes

After studying this implementation, you understand:

✅ How CrewAI framework orchestrates multi-agent workflows
✅ Structure and requirements for CrewAI agents
✅ Sequential task execution patterns
✅ Tool integration with agents
✅ Information flow in multi-agent systems
✅ Output aggregation from multiple agents
✅ When to choose CrewAI vs other frameworks

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ImportError: OPENAI_API_KEY is required` | Export API key: `export OPENAI_API_KEY="..."` |
| `ModuleNotFoundError: crewai` | Install: `pip install crewai crewai-tools` |
| `Agent output is empty` | Check agent backstory descriptiveness |
| `Tool not found` | Verify `@tool` decorator on function |
| `Task execution timeout` | Increase timeout or simplify agent goal |

## Next Steps

1. **Run the Demo**
   ```bash
   python crewai_demo.py
   ```

2. **Review Outputs**
   - Check crewai_output.txt for full results
   - Analyze agent decision-making process

3. **Modify Scenarios**
   - Change trip destination (Paris, Tokyo, etc.)
   - Adjust trip duration
   - Modify agent goals and backstories

4. **Compare with AutoGen**
   - Review AutoGen implementation (Part 1)
   - Compare output quality and workflow

5. **Extend the System**
   - Add new agents
   - Integrate real APIs
   - Implement error handling

## References

- [CrewAI Official Documentation](https://docs.crewai.com/)
- [CrewAI GitHub Repository](https://github.com/joaomdmoura/crewai)
- [Multi-Agent Systems Overview](https://lilianweng.github.io/posts/2023-06-23-agent/)
- [CrewAI Tools Documentation](https://github.com/joaomdmoura/crewai-tools)

## Summary

This implementation successfully demonstrates CrewAI's capabilities for:
- Multi-agent coordination
- Sequential workflow management
- Tool-augmented agents
- Complex task orchestration

It serves as a solid foundation for understanding how modern multi-agent systems can collaborate to solve complex, multi-step problems.

---

**Created**: January 11, 2025
**Framework**: CrewAI
**Lab**: Multi-Agent Systems (IS-492)
**Status**: ✅ Complete and Ready for Execution
