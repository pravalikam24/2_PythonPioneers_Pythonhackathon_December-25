**Dataset Description**
This project uses data derived from the Flatten the Curve COVID-19 Survey published on PhysioNet. The survey was designed to collect large-scale, self-reported information related to COVID-19 symptoms, exposure, testing, medical conditions, behavioral responses, and demographic factors. The dataset captures how individuals experienced symptoms, interacted with potential exposure sources, adhered to self-isolation guidance, and were affected socially and medically during the COVID-19 pandemic.
The cleaned dataset used in this project contains approximately 294,000 survey responses and includes variables such as:
•	COVID-19 symptom indicators (fever, cough, shortness of breath, etc.)
•	Exposure history (contact with illness, household exposure)
•	Testing status and results
•	Vulnerability and pre-existing medical conditions
•	Behavioral factors (self-isolation, travel, work/school exposure)
•	Geographic identifiers (FSA, province)
•	Demographic attributes (age category, sex, ethnicity)

**Data Availability Note**
Due to GitHub file size limitations, the cleaned dataset
`covid_python_Dec25.csv` is not stored in the repository.
To reproduce the analysis:
1. Use the raw CSV files in `data/raw/`
2. Run `Data_Cleaning_&_Preprocessing.ipynb`
3. This will regenerate the cleaned dataset in `data/cleaned/`

**Problem Statement**
During the COVID-19 pandemic, timely identification of high-risk individuals and behavioral gaps was critical for effective public health intervention. However, large survey datasets can be difficult to translate into actionable insights without structured analysis.
This project aims to answer key public health questions such as:
•	Which symptoms and conditions are most associated with probable COVID cases?
•	How do exposure and contact patterns influence infection likelihood?
•	Which vulnerable or high-risk groups may not be testing or self-isolating adequately?
•	Which geographic regions require prioritized intervention?
The ultimate goal is to move beyond descriptive statistics and provide prescriptive insights that can inform targeted testing, outreach, and prevention strategies.

**Methods and Analysis**
•	The analysis was conducted using Python, primarily leveraging:
•	pandas for data cleaning, transformation, and aggregation
•	matplotlib and seaborn for visual analytics
•	Statistical measures such as:
      	Symptom prevalence
      	Correlation analysis
      	Risk lift calculations
      	Exposure vs non-exposure comparisons
      	Behavioral gap analysis (self-isolation and testing gaps)
•	Key analytical steps include:
      	Cleaning and standardizing survey responses (handling y/n/NR values)
      	Creating derived features (province from FSA, symptom groups, exposure indicators)
      	Comparing groups using prescriptive visualizations (slope charts, lollipop charts, dot plots, heatmaps)
      	Identifying actionable risk patterns rather than simple counts

**Key Findings**
•	Fever, cough, and shortness of breath are the most strongly associated symptoms with probable COVID classification.
•	Contact with illness and household exposure significantly increase the probability of being a probable COVID case.
•	A substantial portion of respondents were classified as vulnerable, driven by age and pre-existing medical conditions.
•	Certain symptom and exposure markers are disproportionately present among non-isolating individuals, highlighting compliance gaps.
•	Some probable cases remain untested, indicating potential barriers to access or awareness.
•	Survey responses are concentrated in specific FSAs, suggesting areas where localized interventions may be most impactful.

**Team Name:** 		  Python Pioneers          		  **Team Members:**     Afshan Syed,
				                                                            Ajain Kolas,
				                                                            Pravalika Maram,
				                                                            Saranya Palanisamy,
			                                                            	Sneha Jacob.
  
