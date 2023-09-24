# django/myapp/import_data.py

import csv
import csv
import importlib.util
from django.apps import apps

# Import your models here
# from django.myapp.models.models_csv1 import Ganison_dataset_1
# from django.myapp.models.models_csv2 import Ganison_dataset_2
# from django.myapp.models.models_csv3 import ganison_dataset_3
# from django.myapp.models.models_csv4 import ganison_dataset_4
# from django.myapp.models.models_csv5 import ganison_dataset_5
# from django.myapp.models.models_csv6 import ganison_dataset_6

# Define a mapping of column names to model fields for each CSV file
column_mapping = {

    "Ganison_dataset_1.csv": {
        # Mapping for the first CSV file...
        "school_name": "name",
        "year": "year",
        "StudentID": "student_id",
        "First Name": "first_name",
        "Last Name": "last_name",
        "Year Level": "year_level",
        "Class Subject": "class_subject",
        "Answers": "answers",
        "Correct Answers": "correct_answers",
        "Question Number": "question_number",
        "Subject Contents": "subject_contents",
        "Assessment Areas": "assessment_areas",
        "sydney_correct_count_percentage": "sydney_correct_count_percentage",
        "sydney_average_score": "sydney_average_score",
        "sydney_participants": "sydney_participants",
        "student_score": "student_score",
        "student_total_assessed": "student_total_assessed",
        "student_area_assessed_score": "student_area_assessed_score",
        "total_area_assessed_score": "total_area_assessed_score",
        "participant": "participant",
        "correct_answer_percentage_per_class": "correct_answer_percentage_per_class",
        "average_score": "average_score",
        "school_percentile": "school_percentile",
        "sydney_percentile": "sydney_percentile",
        "strength_status": "strength_status",
        "high_distinct_count": "high_distinct_count",
        "distinct_count": "distinct_count",
        "credit_count": "credit_count",
        "participant_count": "participant_count",
        "award": "award",
    },

    "Ganison_dataset_2.csv": {
        # Mapping for the second CSV file...
        "school_name": "name",
        "year": "year",
        "StudentID": "student_id",
        "First Name": "first_name",
        "Last Name": "last_name",
        "Year Level": "year_level",
        "Class Subject": "class_subject",
        "Answers": "answers",
        "Correct Answers": "correct_answers",
        "Question Number": "question_number",
        "Subject Contents": "subject_contents",
        "Assessment Areas": "assessment_areas",
        "sydney_correct_count_percentage": "sydney_correct_count_percentage",
        "sydney_average_score": "sydney_average_score",
        "sydney_participants": "sydney_participants",
        "student_score": "student_score",
        "student_total_assessed": "student_total_assessed",
        "student_area_assessed_score": "student_area_assessed_score",
        "total_area_assessed_score": "total_area_assessed_score",
        "participant": "participant",
        "correct_answer_percentage_per_class": "correct_answer_percentage_per_class",
        "average_score": "average_score",
        "school_percentile": "school_percentile",
        "sydney_percentile": "sydney_percentile",
        "strength_status": "strength_status",
        "high_distinct_count": "high_distinct_count",
        "distinct_count": "distinct_count",
        "credit_count": "credit_count",
        "participant_count": "participant_count",
        "award": "award",

    },
    "Ganison_dataset_3.csv": {
        "school_name": "name",
        "year": "year",
        "StudentID": "student_id",
        "First Name": "first_name",
        "Last Name": "last_name",
        "Year Level": "year_level",
        "Class Subject": "class_subject",
        "Answers": "answers",
        "Correct Answers": "correct_answers",
        "Question Number": "question_number",
        "Subject Contents": "subject_contents",
        "Assessment Areas": "assessment_areas",
        "sydney_correct_count_percentage": "sydney_correct_count_percentage",
        "sydney_average_score": "sydney_average_score",
        "sydney_participants": "sydney_participants",
        "student_score": "student_score",
        "student_total_assessed": "student_total_assessed",
        "student_area_assessed_score": "student_area_assessed_score",
        "total_area_assessed_score": "total_area_assessed_score",
        "participant": "participant",
        "correct_answer_percentage_per_class": "correct_answer_percentage_per_class",
        "average_score": "average_score",
        "school_percentile": "school_percentile",
        "sydney_percentile": "sydney_percentile",
        "strength_status": "strength_status",
        "high_distinct_count": "high_distinct_count",
        "distinct_count": "distinct_count",
        "credit_count": "credit_count",
        "participant_count": "participant_count",
        "awarDistinction": "award",
    },

        "Ganison_dataset_4.csv": {
        # Mapping for the fourth CSV file...
        "school_name": "name",
        "year": "year",
        "StudentID": "student_id",
        "First Name": "first_name",
        "Last Name": "last_name",
        "Year Level": "year_level",
        "Class Subject": "class_subject",
        "Answers": "answers",
        "Correct Answers": "correct_answers",
        "Question Number": "question_number",
        "Subject Contents": "subject_contents",
        "Assessment Areas": "assessment_areas",
        "sydney_correct_count_percentage": "sydney_correct_count_percentage",
        "sydney_average_score": "sydney_average_score",
        "sydney_participants": "sydney_participants",
        "student_score": "student_score",
        "student_total_assessed": "student_total_assessed",
        "student_area_assessed_score": "student_area_assessed_score",
        "total_area_assessed_score": "total_area_assessed_score",
        "participant": "participant",
        "correct_answer_percentage_per_class": "correct_answer_percentage_per_class",
        "average_score": "average_score",
        "school_percentile": "school_percentile",
        "sydney_percentile": "sydney_percentile",
        "strength_status": "strength_status",
        "high_distinct_count": "high_distinct_count",
        "distinct_count": "distinct_count",
        "credit_count": "credit_count",
        "participant_count": "participant_count",
        "award": "award",
    },

    "Ganison_dataset_5.csv": {
        # Mapping for the fifth CSV file...
        "school_name": "name",
        "year": "year",
        "StudentID": "student_id",
        "First Name": "first_name",
        "Last Name": "last_name",
        "Year Level": "year_level",
        "Class Subject": "class_subject",
        "Answers": "answers",
        "Correct Answers": "correct_answers",
        "Question Number": "question_number",
        "Subject Contents": "subject_contents",
        "Assessment Areas": "assessment_areas",
        "sydney_correct_count_percentage": "sydney_correct_count_percentage",
        "sydney_average_score": "sydney_average_score",
        "sydney_participants": "sydney_participants",
        "student_score": "student_score",
        "student_total_assessed": "student_total_assessed",
        "student_area_assessed_score": "student_area_assessed_score",
        "total_area_assessed_score": "total_area_assessed_score",
        "participant": "participant",
        "correct_answer_percentage_per_class": "correct_answer_percentage_per_class",
        "average_score": "average_score",
        "school_percentile": "school_percentile",
        "sydney_percentile": "sydney_percentile",
        "strength_status": "strength_status",
        "high_distinct_count": "high_distinct_count",
        "distinct_count": "distinct_count",
        "credit_count": "credit_count",
        "participant_count": "participant_count",
        "award": "award",
    },

        "Ganison_dataset_6.csv": {
        # Mapping for the sixth CSV file...
        "school_name": "name",
        "year": "year",
        "StudentID": "student_id",
        "First Name": "first_name",
        "Last Name": "last_name",
        "Year Level": "year_level",
        "Class Subject": "class_subject",
        "Answers": "answers",
        "Correct Answers": "correct_answers",
        "Question Number": "question_number",
        "Subject Contents": "subject_contents",
        "Assessment Areas": "assessment_areas",
        "sydney_correct_count_percentage": "sydney_correct_count_percentage",
        "sydney_average_score": "sydney_average_score",
        "sydney_participants": "sydney_participants",
        "student_score": "student_score",
        "student_total_assessed": "student_total_assessed",
        "student_area_assessed_score": "student_area_assessed_score",
        "total_area_assessed_score": "total_area_assessed_score",
        "participant": "participant",
        "correct_answer_percentage_per_class": "correct_answer_percentage_per_class",
        "average_score": "average_score",
        "school_percentile": "school_percentile",
        "sydney_percentile": "sydney_percentile",
        "strength_status": "strength_status",
        "high_distinct_count": "high_distinct_count",
        "distinct_count": "distinct_count",
        "credit_count": "credit_count",
        "participant_count": "participant_count",
        "award": "award",
    },
}

def import_data_from_csv(file_path, file_name):
    # Determine which model to use based on the file_name
    # model_mapping = {
    #     "Ganison_dataset_1.csv": Ganison_dataset_1,
    #     "Ganison_dataset_2.csv": Ganison_dataset_2,
    #     "ganison_dataset_3.csv": ganison_dataset_3,
    #     "ganison_dataset_4.csv": ganison_dataset_4,
    #     "ganison_dataset_5.csv": ganison_dataset_5,
    #     "ganison_dataset_6.csv": ganison_dataset_6,
    # }

    # ModelClass = model_mapping.get(file_name)

     # Get the app's models module
    app_models_module = apps.get_app_config('myapp').models_module

    # Determine which model to use based on the file_name
    model_name = f"Ganison_dataset_{file_name.split('_')[2]}"
    ModelClass = getattr(app_models_module, model_name, None)


    if ModelClass is None:
        print(f"Model not found for file: {file_name}")
        return

    with open(file_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            # Use the appropriate column mapping for this file
            mapping = column_mapping.get(file_name, {})
            # Create an instance of the model and set its fields
            person = person(
                name=row.get(mapping.get("school_name", "default_column_name")),
                year=row.get(mapping.get("year", "default_column_name")),
                student_id=row.get(mapping.get("StudentID", "default_column_name")),
                first_name=row.get(mapping.get("First Name", "default_column_name")),
                last_name=row.get(mapping.get("Last Name", "default_column_name")),
                year_level=row.get(mapping.get("Year Level", "default_column_name")),
                class_subject=row.get(mapping.get("Class Subject", "default_column_name")),
                answers=row.get(mapping.get("Answers", "default_column_name")),
                correct_answers=row.get(mapping.get("Correct Answers", "default_column_name")),
                question_number=row.get(mapping.get("Question Number", "default_column_name")),
                subject_contents=row.get(mapping.get("Subject Contents", "default_column_name")),
                assessment_areas=row.get(mapping.get("Assessment Areas", "default_column_name")),
                sydney_correct_count_percentage=row.get(mapping.get("sydney_correct_count_percentage", "default_column_name")),
                sydney_average_score=row.get(mapping.get("sydney_average_score", "default_column_name")),
                sydney_participants=row.get(mapping.get("sydney_participants", "default_column_name")),
                student_score=row.get(mapping.get("student_score", "default_column_name")),
                student_total_assessed=row.get(mapping.get("student_total_assessed", "default_column_name")),
                student_area_assessed_score=row.get(mapping.get("student_area_assessed_score", "default_column_name")),
                total_area_assessed_score=row.get(mapping.get("total_area_assessed_score", "default_column_name")),
                participant=row.get(mapping.get("participant", "default_column_name")),
                correct_answer_percentage_per_class=row.get(mapping.get("correct_answer_percentage_per_class", "default_column_name")),
                average_score=row.get(mapping.get("average_score", "default_column_name")),
                school_percentile=row.get(mapping.get("school_percentile", "default_column_name")),
                sydney_percentile=row.get(mapping.get("sydney_percentile", "default_column_name")),
                strength_status=row.get(mapping.get("strength_status", "default_column_name")),
                high_distinct_count=row.get(mapping.get("high_distinct_count", "default_column_name")),
                distinct_count=row.get(mapping.get("distinct_count", "default_column_name")),
                credit_count=row.get(mapping.get("credit_count", "default_column_name")),
                participant_count=row.get(mapping.get("participant_count", "default_column_name")),
                award=row.get(mapping.get("award", "default_column_name")),
            )
            person.save()
            obj = ModelClass()
            for csv_column, model_field in mapping.items():
                setattr(obj, model_field, row.get(csv_column, None))
            obj.save()

if __name__ == "__main__":
    # Specify the CSV file name you want to import
    csv_file_name = "Ganison_dataset_1.csv"
    csv_file_path = f"django/myapp/csv/Ganison_dataset/Ganison_dataset_1.csv"
    import_data_from_csv(csv_file_path, csv_file_name)   

if __name__ == "__main__":
    # Specify the CSV file name you want to import
    csv_file_name = "Ganison_dataset_2.csv"
    csv_file_path = f"django/myapp/csv/Ganison_dataset/Ganison_dataset_2.csv"
    import_data_from_csv(csv_file_path, csv_file_name)   

if __name__ == "__main__":
    # Specify the CSV file name you want to import
    csv_file_name = "ganison_dataset_3.csv"
    csv_file_path = f"django/myapp/csv/Ganison_dataset/ganison_dataset_3.csv"
    import_data_from_csv(csv_file_path, csv_file_name)   

if __name__ == "__main__":
    # Specify the CSV file name you want to import
    csv_file_name = "ganison_dataset_4.csv"
    csv_file_path = f"django/myapp/csv/Ganison_dataset/ganison_dataset_4.csv"
    import_data_from_csv(csv_file_path, csv_file_name)   

if __name__ == "__main__":
    # Specify the CSV file name you want to import
    csv_file_name = "ganison_dataset_5.csv"
    csv_file_path = f"django/myapp/csv/Ganison_dataset/ganison_dataset_5.csv"
    import_data_from_csv(csv_file_path, csv_file_name)   

if __name__ == "__main__":
    # Specify the CSV file name you want to import
    csv_file_name = "ganison_dataset_6.csv"
    csv_file_path = f"django/myapp/csv/Ganison_dataset/ganison_dataset_6.csv"
    import_data_from_csv(csv_file_path, csv_file_name)   