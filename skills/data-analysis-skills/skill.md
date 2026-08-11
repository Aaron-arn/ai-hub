# Data Analysis

## When to use
Apply when working with datasets: cleaning, exploring, building models, or reporting numbers.

## Pipeline
1. **Understand the question**: what decision does this analysis inform? Define success metrics first.
2. **Profile the data**: shape, dtypes, missingness per column, value ranges, duplicates.
3. **Clean deliberately**: document every transformation. Drop vs impute vs flag - each with justification.
4. **Explore**: distributions, correlations, group breakdowns. Plot before modeling.
5. **Analyze**: choose methods that match the question (test vs estimate, regression vs comparison).
6. **Validate**: check assumptions, out-of-sample performance, sensitivity to choices.
7. **Communicate**: conclusions first, then evidence, then caveats.

## Clean-room rules
- Keep the raw data immutable; never overwrite the source.
- Track every cleaning step in code (not point-and-click) so it is reproducible.
- Version both data and code; record a hash of inputs in outputs.
- Handle missingness by pattern: random (impute) vs structural (drop or model).

## Statistical hygiene
- Correlation is not causation; say "associated with" unless you have an experiment.
- Report uncertainty: confidence intervals or effect sizes, not just p-values.
- Watch for multiple comparisons: adjust or pre-register hypotheses.
- Watch for selection bias: who/what is not in the dataset?
- Outliers: detect (IQR, z-score), investigate, decide with reason - never silently remove.

## Communication
- One chart per claim; label axes and units; state sample size in captions.
- Lead with the answer; put method details in an appendix.
- Be explicit about limitations before someone else finds them.
