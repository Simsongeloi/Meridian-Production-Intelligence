import pandas as pd

import pandas as pd
production_data = pd.read_csv("data/production_data.csv")
print(production_data)

production_data["Efficiency_Percent"] = (
    production_data["Actual_Units"]
    / production_data["Planned_Units"]
) * 100

production_data["Production_Shortfall"] = (
    production_data["Planned_Units"]
    - production_data["Actual_Units"]
)

shortfall_by_product = production_data.groupby("Product")["Production_Shortfall"].sum()

highest_shortfall_product = shortfall_by_product.idxmax()
highest_shortfall_product = "Chicken Breast"

total_downtime = production_data["Downtime_Minutes"].sum()
downtime_hours = total_downtime / 60

downtime_by_product = production_data.groupby("Product")["Downtime_Minutes"].sum()

highest_downtime_product = downtime_by_product.idxmax()

production_data["Waste_Cost"] = (
    production_data["Waste_Units"]
    * production_data["Cost_Per_Unit"]
)

total_waste_cost = production_data["Waste_Cost"].sum()

waste_cost_by_product = production_data.groupby("Product")["Waste_Cost"].sum()

highest_waste_product = "Chicken Breast"



print("\nMERIDIAN PRODUCTION EFFICIENCY REPORT")

print(
    production_data[
        ["Product", "Planned_Units", "Actual_Units", "Efficiency_Percent"]
    ].round(2).to_string(index=False)
)

total_planned = production_data["Planned_Units"].sum()

total_actual = production_data["Actual_Units"].sum()

overall_efficiency = (total_actual / total_planned) * 100

print("\nMERIDIAN PRODUCTION MANAGEMENT SUMMARY")
print("--------------------------------------")
print(f"Total Planned Units: {total_planned:,}")
print(f"Total Actual Units: {total_actual:,}")
print(f"Overall Production Efficiency: {overall_efficiency:.2f}%")

print("\nMERIDIAN PRODUCTION SHORTFALL REPORT")
print("------------------------------------")

print(
    production_data[
        ["Date", "Product", "Planned_Units", "Actual_Units", "Production_Shortfall"]
    ].to_string(index=False)
)

print("\nMERIDIAN SHORTFALL BY PRODUCT")
print("-----------------------------")
print(shortfall_by_product)

print("\nMERIDIAN PRODUCTION PERFORMANCE ALERT")
print("-------------------------------------")

print(f"Product With Highest Shortfall: {highest_shortfall_product}")

print(
    f"Total Shortfall: "
    f"{shortfall_by_product[highest_shortfall_product]:,} units"
)

print("\nMERIDIAN MACHINE DOWNTIME REPORT")
print("--------------------------------")
print(f"Total Downtime: {total_downtime} minutes")
print(f"Total Downtime in Hours: {downtime_hours:.2f} hours")


print("\nMERIDIAN MACHINE DOWNTIME ALERT")
print("--------------------------------")

print(f"Product With Highest Downtime: {highest_downtime_product}")

print(
    f"Total Downtime: "
    f"{downtime_by_product[highest_downtime_product]} minutes"
)

print("\nMERIDIAN PRODUCTION WASTE COST REPORT")
print("--------------------------------------")

print(
    production_data[
        ["Date", "Product", "Waste_Units", "Cost_Per_Unit", "Waste_Cost"]
    ].to_string(index=False)
)

print("\nMERIDIAN TOTAL MANUFACTURING WASTE COST")
print("---------------------------------------")
print(f"Total Waste Cost: ${total_waste_cost:,.2f}")

print("\nMERIDIAN WASTE COST BY PRODUCT")
print("------------------------------")

print(waste_cost_by_product)

print("\nMERIDIAN WASTE COST MANAGEMENT ALERT")
print("------------------------------------")

print(f"Product With Highest Waste Cost: {highest_waste_product}")

print(
    f"Total Waste Cost: "
    f"${waste_cost_by_product[highest_waste_product]:,.2f}"
)

