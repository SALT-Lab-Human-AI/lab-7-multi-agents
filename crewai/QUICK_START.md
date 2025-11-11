# CrewAI Multi-Agent Demo - Quick Start Guide

## 🚀 What's Inside

This folder contains a complete implementation of the **CrewAI Multi-Agent Travel Planning System** that demonstrates how to build collaborative AI agents using the CrewAI framework.

## 📁 Project Structure

```
crewAI/
├── crewai_demo.py              ← Main implementation (run this!)
├── requirements.txt             ← Dependencies
├── README.md                    ← Comprehensive overview
├── IMPLEMENTATION_GUIDE.md      ← Detailed explanation
├── QUICK_START.md              ← This file
└── crewai_output.txt           ← Output (generated after running)
```

## 🎯 What It Does

Creates a "crew" of 4 specialized agents that collaboratively plan a 5-day trip to Iceland:

1. **FlightAgent** 🛫 - Researches flight options
2. **HotelAgent** 🏨 - Finds accommodation recommendations
3. **ItineraryAgent** 🗺️ - Plans daily activities
4. **BudgetAgent** 💰 - Calculates total costs and savings

## ⚡ Quick Start (5 minutes)

### Step 1: Install Dependencies
```bash
cd /Users/pranavhharish/Desktop/IS-492/multi-agent/crewAI
pip install -r requirements.txt
```

### Step 2: Set Your OpenAI API Key
```bash
export OPENAI_API_KEY="sk-proj-YOUR-KEY-HERE"
```

### Step 3: Run the Demo
```bash
python crewai_demo.py
```

### Step 4: Check Results
```bash
cat crewai_output.txt
```

## 🧠 Key Concepts

### Sequential Execution
```
Flight Research → Hotel Selection → Itinerary Planning → Budget Calculation
```
Each agent receives output from previous agent, enabling information flow.

### Agent Structure
```python
Agent(
    role="[What they do]",
    goal="[What they achieve]",
    backstory="[Their context/expertise]",
    tools=[tool1, tool2],
    verbose=True
)
```

### Task Definition
```python
Task(
    description="[What to do]",
    agent=responsible_agent,
    expected_output="[What to produce]"
)
```

## 📊 Expected Output

The system generates a comprehensive travel plan with:

```
1. FLIGHT OPTIONS
   - 3 options with pricing ($380-$520)
   - Airline, times, duration
   - Best value recommendation

2. HOTEL RECOMMENDATIONS
   - 4 hotels with ratings (4.2-4.8 stars)
   - Price per night ($150-$320)
   - Amenities list

3. 5-DAY ITINERARY
   - Day-by-day activity plan
   - Golden Circle, Blue Lagoon, South Coast
   - Travel times and durations

4. BUDGET REPORT
   - Itemized costs
   - Budget/Mid-range/Luxury options
   - Cost-saving recommendations
```

## 💡 How CrewAI Works

1. **Agent Creation** - Define specialized agents with roles and goals
2. **Tool Assignment** - Give agents tools to research and gather data
3. **Task Definition** - Create explicit tasks with expected outputs
4. **Crew Formation** - Combine agents and tasks with execution strategy
5. **Execution** - Run kickoff() with input parameters
6. **Results** - Aggregate outputs from all agents

## 🔧 Code Organization

### crewai_demo.py (255 lines)

**Lines 14-78: Tools**
- `search_flights()` - Mock flight search
- `search_hotels()` - Mock hotel search
- `get_iceland_attractions()` - Attractions data

**Lines 82-123: Agent Definitions**
- `create_flight_agent()`
- `create_hotel_agent()`
- `create_itinerary_agent()`
- `create_budget_agent()`

**Lines 127-179: Task Definitions**
- Flight research task
- Hotel selection task
- Itinerary planning task
- Budget calculation task

**Lines 183-255: Crew Orchestration**
- Agent instantiation
- Task creation
- Crew formation
- Execution and output handling

## 🎓 Learning Objectives

After running this demo, you'll understand:

✅ How CrewAI orchestrates multi-agent workflows
✅ Difference between agents, tasks, and tools
✅ Sequential execution patterns
✅ How agents communicate through tasks
✅ Tool integration with agents
✅ Output aggregation from multiple agents

## 🚨 Troubleshooting

| Problem | Solution |
|---------|----------|
| ImportError: OPENAI_API_KEY required | `export OPENAI_API_KEY="your-key"` |
| ModuleNotFoundError: crewai | `pip install crewai crewai-tools` |
| Agent output is empty | Check backstory is detailed |
| Connection timeout | Check OpenAI API status |

## 📚 What's Different from AutoGen

| Feature | CrewAI | AutoGen |
|---------|--------|---------|
| Style | Task-based | Conversational |
| Workflow | Sequential | Chat-based |
| Agent Roles | Predefined | Dynamic |
| Output | Task results | Conversation log |
| Best For | Structured tasks | Iterative discussion |

## 🔄 Modification Ideas

### Change Destination
```python
# In main(), modify:
inputs={"trip_destination": "Paris", ...}
```

### Add a New Agent
```python
def create_tour_agent():
    return Agent(
        role="Tour Guide",
        goal="Plan guided tours",
        backstory="...",
        tools=[...]
    )
# Add to crew agents list
```

### Parallel Execution
```python
crew = Crew(
    agents=[...],
    tasks=[...],
    process="hierarchical"  # Instead of "sequential"
)
```

### Real API Integration
```python
# Replace mock search_flights with:
def search_flights(destination, dates):
    response = skyscanner_api.search(destination, dates)
    return json.dumps(response)
```

## 📖 Documentation

- **README.md** - Comprehensive overview and features
- **IMPLEMENTATION_GUIDE.md** - Detailed technical explanation
- **QUICK_START.md** - This file
- **crewai_demo.py** - Fully commented source code

## 🌟 Key Features Demonstrated

✅ **Multi-Agent Collaboration** - 4 agents working together
✅ **Sequential Workflows** - Ordered task execution
✅ **Tool Integration** - Agents equipped with research tools
✅ **Information Flow** - Agent outputs feed into next agent
✅ **Autonomous Decision Making** - Agents analyze and recommend
✅ **Structured Output** - Professional travel plan report

## 📞 Next Steps

1. ✅ Run the demo: `python crewai_demo.py`
2. ✅ Review the output: `cat crewai_output.txt`
3. ✅ Read IMPLEMENTATION_GUIDE.md for details
4. ✅ Modify the code for different scenarios
5. ✅ Compare with AutoGen implementation (Part 1)

## 🎯 Project Status

✅ **Complete and Ready to Run**

- [x] Four specialized agents created
- [x] Tools for flight, hotel, and attraction research
- [x] Sequential task execution pipeline
- [x] Comprehensive crew orchestration
- [x] Output saving to file
- [x] Full documentation

---

**Framework**: CrewAI
**Lab**: Multi-Agent Systems (IS-492)
**Status**: 🟢 Ready for Execution
**Time to Run**: ~2-5 minutes (depending on API latency)
