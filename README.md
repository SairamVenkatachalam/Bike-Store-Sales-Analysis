# 🚲 European Bike Store Sales Analysis

## 📈 Project Overview
This project focuses on analyzing and visualizing sales data from a European Bike Store to extract valuable insights for business decision-making. The dataset contains transactional-level information, including sales figures and location details such as Country and State, offering a rich foundation for uncovering key sales trends and patterns.

---

## 🎯 Objectives
- **Data Exploration**: Provide an overview of the sales dataset, identifying key variables and their relationships.
- **Outlier Treatment**: Ensure data quality by handling outliers effectively.
- **Normality Tests**: Assess the distribution of numerical variables through statistical tests.
- **Dimensionality Reduction**: Use Principal Component Analysis (PCA) to identify important features and reduce dataset complexity.
- **Data Visualization**: Generate univariate and multivariate plots to uncover hidden patterns in the sales data.
- **Statistical Testing**: Conduct t-tests to explore significant relationships between variables.
- **Interactive Dashboard**: Develop a user-friendly dashboard for dynamic data exploration and insight generation.

---

## 🔬 Methodology

### Phase 1: Data Analysis and Visualization
1. **Data Overview**: 
   - Explored key attributes, including sales amount, order quantities, and location-based data.
2. **Outlier Treatment**: 
   - Identified and treated outliers to ensure robust analysis.
3. **Normality Tests**: 
   - Conducted Shapiro-Wilk, KS, and D’Agostino tests on numerical variables to check for normal distribution.
4. **PCA**: 
   - Reduced the dataset's dimensionality, selecting features that explain 95% of variance.
5. **Static Plots**: 
   - Created univariate and multivariate visualizations to detect sales patterns and correlations.
6. **t-tests**: 
   - Tested hypotheses about relationships between key variables (e.g., sales vs. location).

### Phase 2: Interactive Dashboard
- Built an interactive **Dash** dashboard to allow end-users to:
  - Filter data dynamically by Country, State, and Product category.
  - Visualize trends through bar charts, pie charts, and time series plots.
  - Download processed data for further offline analysis.

---

## 🚀 Tech Stack
- **Python**: Data manipulation and analysis
- **Pandas & NumPy**: Data cleaning and statistical analysis
- **Matplotlib & Seaborn**: Static data visualizations
- **Dash (by Plotly)**: Interactive dashboard development
- **Scikit-learn**: PCA and statistical tests
- **Jupyter Notebooks**: Exploratory data analysis (EDA) and prototyping

---

## 📊 Visualizations
Key visualizations produced include:
- **Sales Trends Over Time**: Time series plots for revenue, profit, and order quantity.
- **Geographical Sales Patterns**: Heatmaps highlighting high-revenue countries and states.
- **Product Analysis**: Bar charts comparing sales across product categories.
- **PCA Explained Variance Plot**: Showcasing feature importance and variance contribution.
- **Interactive Charts**: Filterable and responsive visuals in the dashboard.

---

## 🏁 Running the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/European-Bike-Store-Analysis.git
