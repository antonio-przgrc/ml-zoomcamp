import pickle

filename = 'pipeline.bin'
with open(filename, 'rb') as f:
    model = pickle.load(f)

lead = {
  "lead_source": "paid_ads",
  "industry": "technology",
  "employment_status": "employed",
  "location": "north_america",
  "number_of_courses_viewed": 2,
  "annual_income": 79276.0,
  "interaction_count": 4,
  "lead_score": 0.41
}

pred = model.predict_proba(lead)[:, 1][0]

print(round(pred,3))