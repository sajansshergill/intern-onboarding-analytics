# 🎯 Power BI DAX Measures

### ✅ Onboarding Completion %
```dax
Onboarding Completion % = 
DIVIDE(
    CALCULATE(COUNTROWS(intern_onboarding), intern_onboarding[onboarding_completed] = "Yes"),
    COUNTROWS(intern_onboarding)
)
