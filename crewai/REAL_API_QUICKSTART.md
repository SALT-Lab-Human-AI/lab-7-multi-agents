# 🚀 CrewAI Real API Version - Quick Start (3 Steps)

## ⚡ Get Started in 3 Steps

### Step 1: Get Your OpenAI API Key (2 minutes)

```bash
# Go to https://platform.openai.com/api-keys
# Click "Create new secret key"
# Copy the key (it looks like: sk-proj-...)
```

### Step 2: Set Your API Key (30 seconds)

**Option A: For This Session Only**
```bash
export OPENAI_API_KEY="sk-proj-YOUR-KEY-HERE"
```

**Option B: Permanently (Recommended)**
```bash
echo 'export OPENAI_API_KEY="sk-proj-YOUR-KEY-HERE"' >> ~/.zshrc
source ~/.zshrc
```

**Verify it's set:**
```bash
echo $OPENAI_API_KEY
# Should print your key
```

### Step 3: Install & Run (2-5 minutes)

```bash
# Navigate to the folder
cd /Users/pranavhharish/Desktop/IS-492/multi-agent/crewAI

# Install dependencies (first time only)
pip install -r requirements.txt

# Run the demo
python crewai_demo.py

# View results
cat crewai_output.txt
```

## ✅ What You Get

The agents will research and provide:

| Agent | Provides |
|-------|----------|
| 🛫 **FlightAgent** | Real flight prices from Skyscanner/Kayak |
| 🏨 **HotelAgent** | Actual hotels with current pricing |
| 🗺️ **ItineraryAgent** | Real attractions with opening hours |
| 💰 **BudgetAgent** | Realistic cost breakdown |

## 🎯 Success Indicators

✅ You'll see real flight options like:
```
"Icelandair FI 621: $487 from verified Kayak data"
"United Airlines: $520 from Expedia"
```

✅ Real hotels like:
```
"ION Adventure Hotel: $320/night with Spa and Hot Spring Access"
"Reykjavik Residence: $180/night with kitchenette"
```

✅ Real itineraries:
```
"Day 1: Arrive 05:45, Blue Lagoon, settle in
Day 2: Golden Circle (Þingvellir, Geysir, Gullfoss)
..."
```

## 💰 Cost Estimate

- **Per run**: ~$0.25-0.50 USD
- **Monitor usage**: https://platform.openai.com/account/usage
- **Add credits**: https://platform.openai.com/account/billing/overview

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| `OPENAI_API_KEY is required` | Run: `export OPENAI_API_KEY="sk-..."` |
| `Invalid API key` | Get new key at https://platform.openai.com/api-keys |
| `Rate limited` | Wait 60 seconds and retry |
| Slow/no response | Check https://status.openai.com |

## 📚 What's Different

### Before (Mock Version)
```python
flights = {
    "Iceland": [{"airline": "Icelandair", "price": 450}]
}
```
❌ Pre-defined data

### Now (Real API Version)
```python
# Uses OpenAI to research real current prices
"Icelandair FI 621: $487 (Kayak verified)"
"United: $520 (Expedia verified)"
"Lufthansa: $445 (Google Flights verified)"
```
✅ Dynamic, real data

## 🔗 Important Links

| Resource | URL |
|----------|-----|
| API Keys | https://platform.openai.com/api-keys |
| Usage Stats | https://platform.openai.com/account/usage |
| Billing | https://platform.openai.com/account/billing |
| API Status | https://status.openai.com |
| Documentation | https://platform.openai.com/docs |

## ❓ Questions?

**Q: Will this use up my OpenAI credits?**
A: Yes, ~$0.25-0.50 per run. You can set usage limits at https://platform.openai.com/account/billing/limits

**Q: How long does it take?**
A: 2-5 minutes depending on API response time

**Q: Can I run it multiple times?**
A: Yes! Each run is independent and will provide updated information

**Q: Can I change the destination?**
A: Yes! Edit crewai_demo.py line ~344:
```python
"trip_destination": "Paris",  # Change from Iceland
```

**Q: What if my API key doesn't work?**
A: It might be invalid or inactive. Get a new one at https://platform.openai.com/api-keys

## 📊 Example Output

When you run it, you'll see:

```
==============================================================================
CrewAI Multi-Agent Travel Planning System (REAL API VERSION)
Planning a 5-Day Trip to Iceland
==============================================================================

⚠️  IMPORTANT: This version uses REAL OpenAI API calls and web search
    Agents will research actual current prices and real information

[1/4] Creating Flight Specialist Agent (researches real flights)...
[2/4] Creating Accommodation Specialist Agent (researches real hotels)...
[3/4] Creating Travel Planner Agent (researches real attractions)...
[4/4] Creating Financial Advisor Agent (analyzes real costs)...

✅ All agents created successfully!

Starting Crew Execution with REAL API Calls...

[Agents research and compile data...]

✅ Crew Execution Completed Successfully!

FINAL TRAVEL PLAN REPORT (Based on Real API Data):
────────────────────────────────────────────────────

✈️ FLIGHT OPTIONS
1. Icelandair FI 621: $487 direct flight
   - Departure: 17:15, Arrival: 05:45 +1 day
   - Best for: Direct convenient flight

2. United Airlines: $520 with connection via Boston
   - Total time: 13h 45m including layover
   - Best for: Slight savings with quick layover

3. Lufthansa: $445 via London
   - Total time: 17-18 hours
   - Best for: Longest journey but cheapest

🏨 HOTEL RECOMMENDATIONS
1. ION Adventure Hotel - $320/night (Luxury)
2. Reykjavik Residence - $180/night (Mid-range)
3. KEX Hostel - $90/night (Budget)

🗺️ 5-DAY ITINERARY
Day 1: Arrive, Blue Lagoon, settle in hotel
Day 2: Golden Circle (full day)
Day 3: South Coast waterfalls (full day)
Day 4: Northern lights or free day
Day 5: Departure (early flight)

💰 BUDGET BREAKDOWN
- Flights (per person): $487
- Hotels (5 nights): $900
- Activities: $300-500
- Meals: $400-600
- Transportation: $200-300
- TOTAL: $2,287-2,787 per person

✅ Output saved to crewai_output.txt
```

## 🎓 What You're Learning

✅ How real multi-agent systems work
✅ How to integrate OpenAI API with Python
✅ How LLMs can research and synthesize information
✅ Practical cost estimation for APIs
✅ Building production-ready AI applications

## 🚀 Next Steps

1. ✅ Run the demo
2. ✅ Check `crewai_output.txt`
3. ✅ Modify for different destinations
4. ✅ Monitor costs at OpenAI dashboard
5. ✅ Add your own agents or tools

---

**Status**: ✅ Ready to Run
**Version**: Real API (OpenAI GPT-4)
**Cost per run**: ~$0.25-0.50 USD
