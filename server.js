const { exec } = require('child_process');

const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3000;

app.use(express.static('public')); // Serve static files from the 'public' directory

const filename = 'shopping_data.json'; // Use a fixed filename


app.post('/save-json', express.json(), (req, res) => {
  //saving user input data from html to json file
  const jsonData = req.body;

  // Create a unique filename (you can customize this logic)
  const filename = `shopping_data.json`;

  const filePath = path.join(__dirname, 'public', filename);

  fs.writeFile(filePath, JSON.stringify(jsonData, null, 2), (err) => {
    if (err) {
      console.error('Error writing JSON file:', err);
      res.status(500).send('Error writing JSON file');
    } else {
      console.log('JSON file written successfully');
      res.json({ success: true, filename });
    }
  });
});

app.post('/start-shopping', express.json(), (req, res) => {
  //logic for pressing button and starting listAlgo.yp

  const jsonData = req.body;

  fs.writeFile(path.join(__dirname, 'public', 'shopping_data.json'), JSON.stringify(jsonData, null, 2), (err) => {
    if (err) {
      console.error('Error writing JSON file:', err);
      return res.status(500).send('Error writing JSON file');
    } else {
      console.log("Shopping data sent to python")
    }

    // Run the Python script and wait for it to finish
    exec('python3 listAlgo.py', (error, stdout, stderr) => {
      if (error) {
        console.error('Error running listAlgo.py:', stderr);
        return res.status(500).send('Error running shopping list algorithm');
      }
      console.log('Received from Python script:', stdout);
      try {
        const results = JSON.parse(stdout);
        res.json({ success: true, results: results });
      } catch (parseError) {
        console.error('Error parsing the output from listAlgo.py:', parseError);
        return res.status(500).send('Error parsing shopping list algorithm output');
      }
    });
  });
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
