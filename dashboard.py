# Cloud Healthcare Data Dashboard

patients = [
    {"name": "John", "age": 45, "medication_adherence": 90},
    {"name": "Sarah", "age": 60, "medication_adherence": 75},
    {"name": "Michael", "age": 35, "medication_adherence": 85},
    {"name": "Emily", "age": 50, "medication_adherence": 95}
]

print("=== Cloud Healthcare Data Dashboard ===")

total_patients = len(patients)
average_adherence = sum(
    patient["medication_adherence"] for patient in patients
) / total_patients

print(f"Total Patients: {total_patients}")
print(f"Average Medication Adherence: {average_adherence:.2f}%")

print("\nPatient Summary:")
for patient in patients:
    print(
        f"{patient['name']} | Age: {patient['age']} | "
        f"Adherence: {patient['medication_adherence']}%"
    )
