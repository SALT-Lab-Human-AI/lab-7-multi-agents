"""
Simplified AutoGen Demo - Interview Platform Product Planning

This is a lightweight version for quick testing and understanding the workflow.
It demonstrates multi-agent collaboration using AutoGen's ConversableAgent,
where each agent generates responses via generate_reply().
"""

from datetime import datetime
from config import Config, WorkflowConfig

# Try to import AutoGen
try:
    import autogen
except ImportError:
    print("ERROR: AutoGen is not installed!")
    print("Please run: pip install -r ../requirements.txt")
    exit(1)


class SimpleInterviewPlatformWorkflow:
    """Simplified workflow for interview platform planning using AutoGen agents"""

    def __init__(self):
        """Initialize the workflow with AutoGen agents"""
        if not Config.validate_setup():
            print("ERROR: Configuration validation failed!")
            exit(1)

        self.config_list = Config.get_config_list()
        self.llm_config = {"config_list": self.config_list, "temperature": Config.AGENT_TEMPERATURE}
        self.outputs = {}

        # Create all four AutoGen agents
        self.research_agent = autogen.ConversableAgent(
            name="ResearchAgent",
            system_message="""You are a market research analyst. Provide a brief analysis of
3 competitors in AI interview platforms (HireVue, Pymetrics, Codility).
List their key features and identify market gaps in 150 words.""",
            llm_config=self.llm_config,
            human_input_mode="NEVER",
        )

        self.analysis_agent = autogen.ConversableAgent(
            name="AnalysisAgent",
            system_message="""You are a product analyst. Based on the market research provided,
identify 3 key market opportunities or gaps for a new AI interview platform.
Be concise in 150 words.""",
            llm_config=self.llm_config,
            human_input_mode="NEVER",
        )

        self.blueprint_agent = autogen.ConversableAgent(
            name="BlueprintAgent",
            system_message="""You are a product designer. Based on the market analysis and opportunities,
create a brief product blueprint including:
- Key features (3-5)
- User journey (2-3 steps)
Keep it concise - 150 words.""",
            llm_config=self.llm_config,
            human_input_mode="NEVER",
        )

        self.reviewer_agent = autogen.ConversableAgent(
            name="ReviewerAgent",
            system_message="""You are a product reviewer and strategist. Review the product blueprint
and provide 3 strategic recommendations for success.
Be concise - 150 words.""",
            llm_config=self.llm_config,
            human_input_mode="NEVER",
        )

        print("All AutoGen agents created successfully.")

    def run(self):
        """Execute the complete workflow"""
        print("\n" + "="*80)
        print("AUTOGEN INTERVIEW PLATFORM WORKFLOW - SIMPLIFIED DEMO")
        print("="*80)
        print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Model: {Config.OPENAI_MODEL}\n")

        # Phase 1: Research
        self.phase_research()

        # Phase 2: Analysis
        self.phase_analysis()

        # Phase 3: Blueprint
        self.phase_blueprint()

        # Phase 4: Review
        self.phase_review()

        # Summary
        self.print_summary()

    def phase_research(self):
        """Phase 1: Market Research"""
        print("\n" + "="*80)
        print("PHASE 1: MARKET RESEARCH")
        print("="*80)
        print("[ResearchAgent is analyzing the market...]")

        response = self.research_agent.generate_reply(
            messages=[{"content": "Analyze the current market for AI-powered interview platforms.", "role": "user"}]
        )

        self.outputs["research"] = response
        print("\n[ResearchAgent Output]")
        print(self.outputs["research"])

    def phase_analysis(self):
        """Phase 2: Opportunity Analysis"""
        print("\n" + "="*80)
        print("PHASE 2: OPPORTUNITY ANALYSIS")
        print("="*80)
        print("[AnalysisAgent is identifying opportunities...]")

        response = self.analysis_agent.generate_reply(
            messages=[{
                "content": f"Market research findings:\n{self.outputs['research']}\n\nNow identify market opportunities and gaps.",
                "role": "user",
            }]
        )

        self.outputs["analysis"] = response
        print("\n[AnalysisAgent Output]")
        print(self.outputs["analysis"])

    def phase_blueprint(self):
        """Phase 3: Product Blueprint"""
        print("\n" + "="*80)
        print("PHASE 3: PRODUCT BLUEPRINT")
        print("="*80)
        print("[BlueprintAgent is designing the product...]")

        response = self.blueprint_agent.generate_reply(
            messages=[{
                "content": f"Market Analysis:\n{self.outputs['analysis']}\n\nCreate a product blueprint for our platform.",
                "role": "user",
            }]
        )

        self.outputs["blueprint"] = response
        print("\n[BlueprintAgent Output]")
        print(self.outputs["blueprint"])

    def phase_review(self):
        """Phase 4: Strategic Review"""
        print("\n" + "="*80)
        print("PHASE 4: STRATEGIC REVIEW")
        print("="*80)
        print("[ReviewerAgent is providing recommendations...]")

        response = self.reviewer_agent.generate_reply(
            messages=[{
                "content": f"Product Blueprint:\n{self.outputs['blueprint']}\n\nProvide strategic review and recommendations.",
                "role": "user",
            }]
        )

        self.outputs["review"] = response
        print("\n[ReviewerAgent Output]")
        print(self.outputs["review"])

    def print_summary(self):
        """Print final summary"""
        print("\n" + "="*80)
        print("FINAL SUMMARY")
        print("="*80)

        print("""
This workflow demonstrated a 4-agent collaboration using AutoGen ConversableAgent:
1. ResearchAgent - Analyzed the market
2. AnalysisAgent - Identified opportunities
3. BlueprintAgent - Designed the product
4. ReviewerAgent - Provided strategic recommendations

Each agent received context from the previous agent's output,
demonstrating the sequential workflow pattern of AutoGen.
""")

        # Print full results
        print("\n" + "="*80)
        print("FULL RESULTS - ALL PHASES")
        print("="*80)

        for phase, label in WorkflowConfig.PHASE_DESCRIPTIONS.items():
            print("\n" + "-"*80)
            print(f"{label.upper()} (Full Output)")
            print("-"*80)
            print(self.outputs.get(phase, "N/A"))

        # Save to file
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f"workflow_outputs_{timestamp}.txt"
        with open(output_file, 'w') as f:
            f.write("="*80 + "\n")
            f.write("AUTOGEN INTERVIEW PLATFORM WORKFLOW - FULL RESULTS\n")
            f.write("="*80 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Model: {Config.OPENAI_MODEL}\n\n")

            for phase, label in WorkflowConfig.PHASE_DESCRIPTIONS.items():
                f.write("\n" + "-"*80 + "\n")
                f.write(f"{label.upper()}\n")
                f.write("-"*80 + "\n")
                f.write(str(self.outputs.get(phase, "N/A")) + "\n")

        print(f"\nFull results saved to: {output_file}")

        print(f"\nEnd Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80)


if __name__ == "__main__":
    try:
        workflow = SimpleInterviewPlatformWorkflow()
        workflow.run()
        print("\nWorkflow completed successfully!")
    except Exception as e:
        print(f"\nError during workflow execution: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Verify API key is set in parent directory .env (../.env)")
        print("2. Check your API key has sufficient credits")
        print("3. Ensure pyautogen is installed: pip install -r ../requirements.txt")
        print("4. Verify internet connection")
        import traceback
        traceback.print_exc()
