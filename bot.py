import datetime
import random
import json
import os

print("="*50)
print("🤖 AUTO MONEY BOT STARTED")
print("="*50)

# Simulate earning money
earning_types = [
    "YouTube Ad Revenue",
    "Amazon Affiliate",
    "Sponsorship Deal",
    "Product Sales",
    "Course Revenue"
]

today_earnings = {}

for source in earning_types:
    amount = round(random.uniform(1.50, 25.00), 2)
    today_earnings[source] = amount
    print(f"💰 {source}: ${amount:.2f}")

# Calculate total
total = sum(today_earnings.values())
print(f"\n📊 TODAY'S TOTAL: ${total:.2f}")
print(f"📈 MONTH PROJECTION: ${total * 30:.2f}")
print(f"📅 YEAR PROJECTION: ${total * 365:.2f}")

# Save to file
data = {
    "date": str(datetime.date.today()),
    "earnings": today_earnings,
    "total": total,
    "system_status": "ACTIVE"
}

os.makedirs("data", exist_ok=True)
with open(f"data/earnings_{datetime.date.today()}.json", "w") as f:
    json.dump(data, f)

print("\n✅ Earnings saved!")
print("🔄 Next run in 6 hours automatically")
print("="*50)
