print("=== STRING METHODS - DAY 2 ===")
print()

# LinkedIn example applied to MY context
my_goal = "  i will become an automation tester  "

print("Original goal:", my_goal)
print()

# Clean and format
clean_goal = my_goal.strip()
proper_goal = clean_goal.title()
print("Cleaned and proper:", proper_goal)
print()

# Check what I want
if "automation" in clean_goal.lower():
    print("Yes! Automation is my goal!")
print()

# Replace to make it present tense
current_statement = proper_goal.replace("Will Become", "Am Becoming")
print("Mindset shift:", current_statement)
print()

# Find position
auto_position = clean_goal.find("automation")
print("Length of my goal:", len(clean_goal))
print("First word:", clean_goal.split()[0])
print("Last word:", clean_goal.split()[-1])