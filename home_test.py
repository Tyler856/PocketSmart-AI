from gemini_utils import get_home_recommendations

result = get_home_recommendations(
    budget=50000,
    room="Living Room",
    style="Modern",
    items="Ceiling fan, lights, dining table and wall decoration"
)

print("\n===== POCKETSMART AI HOME RECOMMENDATIONS =====\n")
print(result)