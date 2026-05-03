from django.shortcuts import render

def index(request):
    result_support = []
    result_alpha = []

    if request.method == "POST":
        data = request.POST.get("data")
        alpha = float(request.POST.get("alpha"))

        # Parse input
        pairs = data.split(",")

        fuzzy_set = []
        for pair in pairs:
            x, mu = pair.split(":")
            fuzzy_set.append((int(x), float(mu)))

        # Support set (μ > 0)
        result_support = [x for x, mu in fuzzy_set if mu > 0]

        # Alpha-cut (μ >= alpha)
        result_alpha = [x for x, mu in fuzzy_set if mu >= alpha]

    return render(request, "index.html", {
        "support": result_support,
        "alpha_set": result_alpha
    })