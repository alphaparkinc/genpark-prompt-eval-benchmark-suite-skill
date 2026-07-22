from client import PromptEvalBenchmarkSuiteClient
client = PromptEvalBenchmarkSuiteClient()
res = client.evaluate(
    prompt_variants=["Summarize in 3 bullet points", "Provide a concise executive summary"],
    test_cases=[{"input": "Article text..."}]
)
print(f"Best Variant: {res['best_variant']}")
for s in res["scores"]:
    print(f"  [{s['variant_id']}] Score: {s['accuracy_score']} | Latency: {s['latency_ms']}ms")
