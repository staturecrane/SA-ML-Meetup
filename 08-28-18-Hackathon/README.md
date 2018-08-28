# Hackathon Instructions

The challenge for this hackathon is predicting the Wine Enthusiast score of a wine given:
- the country of origin
- description
- designation
- price
- province
- region_1
- region_2 
- the taster's name
- the taster's Twitter handle
- the title of the wine review
- varietal
- winery

You can find a full description of the dataset here: https://www.kaggle.com/zynicide/wine-reviews. 

## Registration

Once you have your team formed, please go to https://form.jotform.com/82394377793170 and fill out the registration template. Pick a team leader -- they will be responsible for submitting and explaining your solution, as well as be the one we contact to pick up prizes should the judging extend beyond tonight.

## Datasets

You will be provided with two datasets: train.csv and test.csv. Please use `train.csv` for training and validation, and only use `test.csv` to see how well your model does on unseen data. Judges will train and test your model from scratch, so resist the temptation to train on the test dataset ;). 

## Prediction

The prediction you will make are the number of points Wine Enthusiast gives the wine in question. These should all be between 80-100, as they claim to not publish reviews on wines that score lower than 80, but this is likely something you'd want to confirm with some data analysis. How the model predicts the score is up to you. The `requirements.txt` provided should be a good start, in terms of tools needed, but you are welcome to use any tool you wish, keeping in mind they should be easy to install and run on a Unix system. I would highly recommend using a Docker container to avoid environmental or dependency issues.

## Testing

Your testing script should take in the test dataset and output an accuracy metric. This will be tested and confirmed by judges.

## Scoring

Teams will be awared points for the following sections:

- data evaluation, preprocessing and feature engineering/selection
- model architecture and compilation
- training and validation
- final test score

If you do not complete all sections, you will still be awarded points. If no team completes all sections, the team with the highest number of points from completed section will win.

## Submission

Please create a folder in the root directory of the repository that includes your training and testing scripts, including instructions on how to run, train, and test. Then make a branch and submit a PR with the name of your team. Teams whose solution cannot be replicated will obviously have a harder time receiving points, so consider giving thought to documentation and reproduceability.
