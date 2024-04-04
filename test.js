// Example data for prediction
const inputData = {
  danceability: 0.75,
  energy: 0.65,
  acousticness: 0.2,
  instrumentalness: 0.1,
  tempo: 120
};

// Fetch API to send POST request
fetch('http://127.0.0.1:5000/predict_genre', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(inputData)
})
.then(response => response.json())
.then(data => {
  console.log('Predicted Genre:', data.predicted_genre);
})
.catch(error => {
  console.error('Error:', error);
});
