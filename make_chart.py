import matplotlib.pyplot as plt
groups = ["Short sessions\n(≤5 turns)", "Long sessions\n(>10 turns)"]
avg_calls = [15.33, 239]

plt.figure(figsize=(7, 5))
plt.bar(groups, avg_calls)

plt.title("Average LLM Calls per Coding-Agent Session")
plt.ylabel("Average LLM Calls per Session")

for i, value in enumerate(avg_calls):
    plt.text(i, value + 5, f"{value:.2f}", ha="center")

plt.tight_layout()
plt.savefig("llm_calls_short_vs_long.png", dpi=200)
plt.show()