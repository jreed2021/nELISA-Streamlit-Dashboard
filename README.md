# 📊 nELISA Streamlit Dashboard

## 🔬 Overview
This project is an **interactive Streamlit dashboard** for analyzing **nELISA (Nanoparticle-Enhanced Enzyme-Linked Immunosorbent Assay) data**. The dashboard allows users to explore protein concentration distributions across different experimental groups, visualize trends, and filter data dynamically.

## 🚀 Features
- 📊 **Interactive Boxplots**: Compare protein concentrations across experimental groups.
- 🔍 **Filtering Options**: Filter data by treatment groups and time points.
- 📈 **Summary Statistics**: View mean, standard deviation, and other descriptive stats.
- 📂 **Data Table Display**: Toggle the raw dataset for transparency.
- 🌍 **Web-Based Interface**: Hosted on Streamlit Cloud for easy access.

## 📁 Project Structure
```
📂 nELISA-Streamlit-Dashboard/
 ├── 📄 nELISA_report.py  # Streamlit app
 ├── 📄 simulated_nELISA_data.csv  # Dataset (or real dataset)
 ├── 📄 requirements.txt  # Dependencies for Streamlit Cloud
 ├── 📄 README.md  # Project documentation
```

## 🛠️ Installation & Usage
### 1️⃣ **Clone the Repository** (or download manually)
```bash
git clone https://github.com/your-username/nELISA-Streamlit-Dashboard.git
cd nELISA-Streamlit-Dashboard
```

### 2️⃣ **Install Dependencies**
Ensure you have **Python 3.8+** installed. Then, install the required libraries:
```bash
pip install -r requirements.txt
```

### 3️⃣ **Run the Streamlit App**
Launch the interactive dashboard using:
```bash
streamlit run nELISA_report.py
```
This will open the app in your web browser.

## 🌍 Deployment on Streamlit Cloud
The app is publicly accessible at:
🔗 **[Live App Link](https://https://nelisareportpy-ntycjsyqxb6brsua7k6gek.streamlit.app/)**

## 📊 Example Screenshots

![image](https://github.com/user-attachments/assets/1fcb1baf-b977-404a-b7a9-ef3e0b1b763d)
![image](https://github.com/user-attachments/assets/93190766-e321-4a51-8768-222ca18bcb45)
![image](https://github.com/user-attachments/assets/60b7ac1e-013b-42be-b294-1c2254573cd9)


## 📌 About the Data
The dataset contains **protein concentration measurements** from an **nELISA experiment** with multiple treatment groups and time points.

### **Columns in the Dataset**
- **Sample_ID**: Unique identifier for each sample
- **Group**: Experimental condition (e.g., Control, Treatment_A, Treatment_B)
- **Time_Point**: Measurement time (e.g., Day 1, Day 7, Day 14)
- **Protein_X**: Protein concentration values (e.g., Protein_1, Protein_2, ...)

## 🛠️ Built With
- **Python** 🐍
- **Streamlit** 🌐 (for web-based interactivity)
- **Pandas** 🏭 (for data handling)
- **Plotly** 📊 (for visualization)

## 📓 Jupyter Notebook Analysis
For a step-by-step exploratory data analysis (EDA) and statistical insights, check out:
🔗 [nELISA_Data_Analysis.ipynb](./nELISA_Data_Analysis.ipynb)

This notebook provides:
- Data cleaning & preprocessing
- Summary statistics & visualizations
- Hypothesis testing (ANOVA, t-tests)


## 📜 License
This project is **open-source** under the MIT License.

## ✉️ Contact
For questions or suggestions, reach out via GitHub Issues or connect with me on [LinkedIn](https://www.linkedin.com/in/janessa-clark-reed-els-aab-413263111).

---

🚀 **Enjoy exploring the nELISA dataset!** 🔬

