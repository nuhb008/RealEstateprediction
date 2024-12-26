# Real Estate Price Prediction

## Overview

This is a Python Flask application that predicts real estate prices based on user input such as location, square footage, number of bedrooms, and number of bathrooms. The model is trained using a CSV dataset of real estate transactions. It leverages machine learning to provide an estimated price based on historical data.

---

## Features

- **Location-Based Price Prediction**: Supports multiple locations.
- **User Input Handling**: Accepts square footage, BHK (bedrooms), bathrooms, and location.
- **Machine Learning Model Integration**: Uses a pre-trained model for prediction.
- **API Endpoints**: Provides RESTful APIs to fetch location names and predict prices.
- **CORS Enabled**: Supports cross-origin requests.

---

## Installation

### Prerequisites

- Python 3.x installed.
- Required Python libraries (`Flask`, `pandas`, `numpy`, `sklearn`).

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/real-estate-prediction.git
   cd real-estate-prediction
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Prepare the dataset:
   - Place your CSV file (e.g., `real_estate_data.csv`) in the project directory.
   - Ensure the dataset contains columns like `location`, `total_sqft`, `bhk`, `bath`, and `price`.

4. Train the model:
   - Use the `utils.py` file to preprocess the data and train the machine learning model.
   - Save the trained model and location data for use in the Flask app.

5. Start the Flask server:

   ```bash
   python app.py
   ```

6. Access the application:
   - Open `http://127.0.0.1:5000` in your browser or use a tool like Postman to test the APIs.

---

## API Endpoints

### 1. **Get Locations**
   - **URL**: `/getlocationnames`
   - **Method**: GET
   - **Response**:
     ```json
     {
       "locations": ["Location1", "Location2", "Location3"]
     }
     ```

### 2. **Predict Price**
   - **URL**: `/predict`
   - **Method**: POST
   - **Request Parameters**:
     - `total_sqft` (float): Total square footage of the property.
     - `location` (string): Location name.
     - `bhk` (int): Number of bedrooms.
     - `bath` (int): Number of bathrooms.
   - **Response**:
     ```json
     {
       "estimatedprice": 1200000.0
     }
     ```

---

## Code Structure

- **`app.py`**: Main Flask application with API routes.
- **`utils.py`**:
  - Contains utility functions for:
    - Loading the trained model.
    - Fetching location names.
    - Predicting property prices.
- **`real_estate_data.csv`**: Dataset used for training the model.
- **Trained Model**: The saved machine learning model (e.g., `.pkl` file).

---

## Machine Learning Workflow

1. **Preprocessing**:
   - Cleaned the dataset (handled missing values, outliers, etc.).
   - Encoded categorical variables like location.

2. **Feature Engineering**:
   - Used features such as `total_sqft`, `location`, `bhk`, and `bath`.

3. **Model Training**:
   - Trained a regression model (e.g., Linear Regression, Decision Tree) to predict property prices.

4. **Model Saving**:
   - Saved the trained model using `pickle` or `joblib` for use in the Flask app.

---

## Example Usage

### Predict Price (POST Request)
```bash
curl -X POST http://127.0.0.1:5000/predict \
  -d "total_sqft=1500" \
  -d "location=Indiranagar" \
  -d "bhk=3" \
  -d "bath=2"
```

**Response**:
```json
{
  "estimatedprice": 2500000.0
}
```

---

## Dependencies

- **Flask**: Web framework for building APIs.
- **pandas**: Data manipulation and analysis.
- **numpy**: Numerical computations.
- **scikit-learn**: Machine learning library.

---

## Customization

- **Dataset**:
  Replace `real_estate_data.csv` with your dataset and update the preprocessing logic in `utils.py` accordingly.

- **Model**:
  Experiment with different machine learning algorithms or hyperparameters to improve accuracy.

---

## Future Enhancements

- **Frontend Integration**: Add a web interface for user-friendly interactions.
- **Additional Features**: Include more variables like property age, amenities, etc.
- **Deployment**: Host the application on platforms like AWS, Heroku, or Azure.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributions

Contributions are welcome! Fork the repository, make your changes, and create a pull request.

---

Get started and make your real estate predictions smarter! 🏠
