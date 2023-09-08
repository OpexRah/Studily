# Studily
Studily is an AI tool that assists students to stay focussed while learning from online resources such as YouTube

## How it works
Studily uses an AI model which has been trained to recognise whether a given string has content that is Educational or not. Using selenium, the youtube video title is extracted and fed to the model. The model decides if the title is educational or not. If it determines that it is non-educational then it redirects the user back to YouTube homepage, thus not allowing them to watch the video.

## Details about the training process
The dataset was scraped using YouTube's API and a list of 3000 educational video titles and 3000 non-educational video titles were gathered. Using Term-Frequency-Inverse-Document-Frequency, vectors were made where the two groups educational and non-educational were placed by the model. This was its learning phase. 

For predicting, the model takes an input and finds a vector value for that input. The closest region(Educational / non-educational) to that vector is the final prediction

## Future scope
Currently only YouTube is supported. Support for other learning resources will be added in the near future. 
The model will be upgraded to cover more topics related to education.
