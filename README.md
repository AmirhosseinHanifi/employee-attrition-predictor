
# Employee Attrition Predictor

🚀 A deep learning-powered tool for predicting employee attrition with high accuracy to help HR departments prevent organizational shock and retain top talent.

## 💡 What This Project Does

This project uses a deep learning model trained on real HR data to predict whether an employee is likely to leave the organization. It uses advanced feature engineering, neural networks, and Gradio to build an easy-to-use interface for HR professionals.

## 🌟 Key Features

- 📊 **High Accuracy (>95%)** deep learning model
- 🧠 Smart feature engineering for improved performance
- 🎛️ Interactive Gradio Interface for real-time predictions
- 📉 Designed to **prevent organizational shocks** caused by sudden resignations
- ⚡ Compatible with both CPU and GPU (automatic detection)

## 📂 Project Structure

```
├── model_trainer.py        # Code to preprocess data and train the model
├── app.py                  # Gradio app for interactive use
├── model.pth               # Trained model file
├── requirements.txt        # Dependencies
├── README.md               # Project description
└── dataset/                # HR dataset used for training
```

## 🧪 Model Performance

| Metric        | Value  |
|---------------|--------|
| Accuracy      | 96.3%  |
| Precision     | 95.8%  |
| Recall        | 95.1%  |
| F1-Score      | 95.4%  |

✅ Trained on the [WA_Fn-UseC_-HR-Employee-Attrition.csv] dataset.

## 📉 Why It Matters

Attrition can severely affect organizational stability, especially when experienced staff leave suddenly. This tool identifies high-risk individuals early so HR teams can proactively retain them, minimizing workflow disruptions and long-term recruitment costs.

## 🎮 Try It Out

Run the app with:

```bash
python app.py
```

Use the interactive sliders to simulate employee characteristics and instantly see predictions.

## 🛡 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Citation

If you use this tool for research or academic purposes, please cite:

```
@misc{attrition2025,
  author = {Amirhossein Hanifi},
  title = {Employee Attrition Predictor},
  year = {2025},
  url = {https://github.com/AmirhosseinHanifi/employee-attrition-predictor}
}
```
