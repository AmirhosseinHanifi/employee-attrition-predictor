# Employee Attrition Predictor (Deep Learning + Gradio UI)

This project uses a deep learning model to predict employee attrition based on HR data. It also provides a user-friendly Gradio interface to explore attrition risk based on employee features.

## 📊 Dataset

We used the popular **IBM HR Analytics Employee Attrition & Performance** dataset (available as `WA_Fn-UseC_-HR-Employee-Attrition.csv`).  
This dataset includes 35 features such as age, job role, overtime, monthly income, work-life balance, and more.

## 🧠 Model

- Deep Neural Network (built with TensorFlow/Keras)
- Preprocessing:
  - Label encoding for categorical variables
  - Feature scaling for numeric data
- Evaluation Metrics:
  - Accuracy
  - Precision / Recall / F1-score
- Achieved **>92% accuracy** on test data

## 🖥️ Web Interface (Gradio)

- Enter custom employee data
- Get predicted attrition probability
- Display key risk factors if probability > 0.5

## 💡 How to Use

### 1. Clone the repository

```bash
git clone https://github.com/your-username/employee-attrition-predictor.git
cd employee-attrition-predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python gradio_app.py
```

Then open the link in your browser.

## 📁 Files

| File | Description |
|------|-------------|
| `model_trainer.py` | Builds, trains, and saves the deep learning model |
| `gradio_app.py` | Loads the model and launches Gradio interface |
| `WA_Fn-UseC_-HR-Employee-Attrition.csv` | HR dataset |
| `requirements.txt` | Required Python libraries |
| `README.md` | Project overview |

## 📌 Future Work

- Add SHAP for model interpretability
- Train with more diverse HR datasets
- Deploy with FastAPI or Streamlit

## 🔒 License

MIT License. Feel free to use and modify with attribution.
