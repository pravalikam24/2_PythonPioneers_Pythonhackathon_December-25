import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Page Config ---
st.set_page_config(
    page_title="COVID Dashboard",
    layout="wide"
)

st.title("Flatten: COVID-19 Survey Data on Symptoms, Demographics and Mental Health in Canada")

# --- Load Data ---
df = pd.read_csv("covid_python_Dec25.csv")

# =========================
# Prepare Data
# =========================

# --- Sex Distribution ---
sex_df = df[df['sex'] != 'NR']
sex_counts = sex_df['sex'].value_counts()

# --- Positive Cases by Province ---
positive_df = df[df['covid_positive'] == 'positively']
positive_counts = positive_df['province'].value_counts()

# --- Age Category: COVID Probable Percentage ---
age_df = df[df['age_category'] != 'NR']
probable_df = age_df[age_df['probable'] == 'y']
age_total_counts = age_df['age_category'].value_counts().sort_index()
age_probable_counts = probable_df['age_category'].value_counts().sort_index()
age_percent = (age_probable_counts / age_total_counts * 100).fillna(0)

# --- Financial Obligations vs Mental Health Correlation ---
impact_map = {
    "positively": 1,
    "negatively": -1,
    "NoImpact": 0,
    "NR": None
}
df["mental_health_num"] = df["mental_health_impact"].map(impact_map)

# Split multi-select values into lists
df["financial_list"] = (
    df["financial_obligations_impact"]
    .replace("NR", "")
    .fillna("")
    .apply(lambda x: x.split(";"))
)

# Get unique financial obligation types
all_financial_cols = set(f for sublist in df["financial_list"] for f in sublist if f)

# Create binary columns
for col in all_financial_cols:
    df[col] = df["financial_list"].apply(lambda x: 1 if col in x else 0)

financial_cols = list(all_financial_cols)
correlations = {}

for col in financial_cols:
    corr = df[[col, "mental_health_num"]].dropna().corr().loc[col, "mental_health_num"]
    correlations[col] = corr

correlation_df = pd.DataFrame.from_dict(
    correlations, orient="index", columns=["Correlation_with_mental_health"]
).sort_values(by="Correlation_with_mental_health", ascending=False)

# =========================
# Display Charts in 3 Columns (Aligned & Smaller)
# =========================

col1, col2, col3 = st.columns(3)

# --- Pie Chart: Sex Distribution ---
with col1:
    fig1, ax1 = plt.subplots(figsize=(3, 3))
    ax1.pie(
        sex_counts,
        labels=sex_counts.index,
        autopct='%1.1f%%',
        startangle=90
    )
    ax1.set_title("Sex Distribution")
    ax1.axis('equal')
    st.pyplot(fig1)

# --- Bar Chart: Positive Cases by Province ---
with col2:
    st.subheader("COVID-Positive Cases by Province")
    fig2, ax2 = plt.subplots(figsize=(4, 3))
    positive_counts.sort_values().plot(
        kind="bar",
        ax=ax2,
        color='skyblue'
    )
    ax2.set_xlabel("Province")
    ax2.set_ylabel("Number of Positive Cases")
    ax2.set_title("Positive Cases by Province")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig2)

# --- Bar Chart: Age Category Probable Cases Percentage ---
with col3:
    st.subheader("COVID Probable Cases by Age Category (%)")
    fig3, ax3 = plt.subplots(figsize=(4, 3))
    age_percent.plot(
        kind='bar',
        ax=ax3,
        color='salmon'
    )
    ax3.set_ylabel("Percentage (%)")
    ax3.set_xlabel("Age Category")
    ax3.set_title("Probable Cases (%) by Age")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig3)

# =========================
# Financial Obligations vs Mental Health Chart
# =========================

#st.subheader("Financial Obligations vs Mental Health Impact (Correlation)")

# Horizontal bar chart (smaller)
fig4, ax4 = plt.subplots(figsize=(8, 4))
colors = correlation_df['Correlation_with_mental_health'].apply(lambda x: 'green' if x > 0 else 'red')
correlation_df.plot(kind='barh', y='Correlation_with_mental_health', ax=ax4, color=colors)
ax4.set_xlabel("Correlation with Mental Health Impact")
ax4.set_ylabel("Financial Obligation")
ax4.set_title("Impact of Financial Obligations on Mental Health")
plt.tight_layout()
st.pyplot(fig4)
